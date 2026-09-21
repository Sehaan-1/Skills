# Architecture: Invoices

**For engineers.** The shape of this system, why it is this shape, and the commands that fail the build when it stops being this shape.

> Worked example for the [invoicing effort](../invoicing/board.md). The commit hash and metric numbers are illustrative; the shape is the point.

## Provenance
- Handoff: [handoff](../invoicing/handoff.md)
- Board: [Invoices for customers](../invoicing/board.md)
- ADRs this record implements: [ADR-0001 Who owes us?](../invoicing/adr/0001-who-owes-us.md), [ADR-0002 Where does the invoice go?](../invoicing/adr/0002-where-the-invoice-goes.md), [ADR-0003 Money moves outside the app](../invoicing/adr/0003-money-moves-outside-the-app.md)
- Measured against: commit 4f9c2e1, 2026-09-21
- Record written by: keystone sitting, 2026-09-21

## Destination and forcing constraints
- **Where we're headed:** a customer can be invoiced, and the owner can watch an invoice go from sent to paid, without doing any of it by hand.
- **How we'll know we're there:** the invoice-flow walk (create → send → paid, end to end), the `invoice-flow` proof, CI failing on regression.
- **Forces that shaped this:** two people build and operate it — no on-call rotation, no deploy train, so every boundary must pay for itself in days. One write path: the owner. Money never moves in the app (ADR-0003), so there is no payment integrity to defend — the integrity that matters is the invoice's state history. Email is how invoices travel (ADR-0002), so deliverability is outsourced and editable templates are a standing rule.
- **Not this effort:** online payment capture, customer onboarding, recurring invoices.

## Context map

Two contexts. The seam between them is one port, and it exists because email changes for reasons invoices never do (providers, templates, deliverability), and invoices change for reasons email never does (numbering, line items, state).

### Context: Invoicing (core)
- **Owns:** the invoice model — the customer owes the owner (ADR-0001); invoice numbering; the draft → sent → paid / void state machine; the live invoice page the email links to.
- **Team:** both people.
- **Relationship to Delivery:** customer/supplier, Invoicing upstream. Invoicing hands Delivery a rendered email as plain data; Delivery's acceptance tests run in Invoicing's CI.
- **Does not know:** SMTP, providers, template syntax, how email physically travels.
- **Integration surface:** the `Outbox` port, and the public invoice URL.

### Context: Delivery (generic subdomain — adopt, don't build)
- **Owns:** email rendering from owner-editable templates, provider adaptation, bounce notices.
- **Team:** both people, but nobody is proud of it.
- **Relationship to Invoicing:** downstream conformist to the `Outbox` contract; the mail library sits behind one anti-corruption adapter so its shape never leaks inward.
- **Does not know:** what an invoice is. It renders a subject, a body, and a link.
- **Integration surface:** the `Outbox` port; template files a person can edit (standing rule).

The big-ball-of-mud warning, named so it can be watched for: the live invoice page is Invoicing's, not Delivery's. The moment "the email needs a button that mutates invoice state" is solved by letting Delivery import Invoicing internals, the seam is gone.

## Distillation
- **Core domain:** the invoice lifecycle — numbering, state history, who owes whom. That is the product; the rest is plumbing.
- **Supporting subdomains:** the live invoice page (needed, not differentiating — plain server-rendered HTML).
- **Generic subdomains:** email delivery. Adopt; isolate behind `Outbox`; leave no trace of our specialties in it.
- **Cohesive mechanisms:** none yet. Money math is exact-decimal and lives inside the aggregate, not behind a framework.
- **Where the talent goes:** the state machine and its history. If the answer is "everywhere," the distillation failed.

## Aggregate boundaries

### Aggregate: Invoice
- **Root:** `Invoice`.
- **Invariants (transactional, enforced on every commit):**
  - I1: `total == sum(lineItems.amount)`, in exact minor units.
  - I2: status moves only along draft → sent → paid | void; every transition records who and when.
  - I3: a sent invoice is immutable except for its status — an edited invoice is a new revision, not a quiet mutation.
- **Inside the boundary:** `LineItem` (local identity), the status type, the state-history entries.
- **Outside by design:** `Customer` (referenced by id — names and addresses change on their own clock and carry none of the invariants).
- **Consistency across this boundary:** none required this effort. When "remind me if unpaid after N days" arrives, it is eventual via a named scheduled job, and the job and its time bound get named then.
- **Concurrency:** optimistic on the invoice's `revision`. The owner is the only writer today (ADR-0003), so conflicts are rare, and loud is fine.
- **Repository:** `Invoices` — root only. There is no `LineItemRepository`, ever.

## Dependency rule
- **Levels, innermost first:** invoice model and its invariants → send / mark-paid use cases → live-page controller, email rendering, repositories → framework and driver glue.
- **Level = distance from the inputs and outputs.** The state machine is farthest from both; `main` is touching them.
- **Allowed:** `invoicing/core` imports nothing outward. Use cases import core. `adapters/*` import app and core. `main` imports everything once, at wiring.
- **Forbidden:** anything in `invoicing/core` importing from `adapters/`, the web framework, or the mail library; SQL outside `adapters/store/`; template syntax outside Delivery.
- **Data crossing a boundary:** plain structures, in the form most convenient for the inner ring. No ORM rows into core; no entities out to templates.

## Component structure
- **Packaging:** by component — `core/`, `app/`, `adapters/{store,mail,web}`, `main/`. With two people, package-by-feature buys nothing this small; the compiler-enforced component boundary is the thing we actually need.
- **Cohesion position:** CCP over REP — early project, maintainability beats reuse, and we say so. We sacrifice reuse on purpose.
- **Deployable units:** one. A service split here would be a distributed monolith with a staff of two.
- **Metrics (measured, illustrative commit 4f9c2e1):** `core` I=0.11 A=0.55 D=0.34; `app` I=0.45 A=0.40 D=0.05; `adapters.mail` I=0.80 A=0.10 D=0.30; `adapters.store` I=0.72 A=0.18 D=0.10. Cycles: 0. `core` sits near stable-abstract by design; the adapters sit volatile-concrete, which is where adapters belong.
- **What we are trading:** a little ceremony per boundary for a team of two. If the ceremony ever costs more than the invoice, collapse `app` into `core` and keep the forbidden-import rule — that is the part that pays.

## Ports the core owns
- **`Invoices`** — the persistence port, named in the domain's language, not `InvoiceRepository`. Core calls it; the store adapter implements it; all SQL lives in the adapter.
- **`Outbox`** — `send(invoiceEmail)`. Core defines the email as plain data (subject, body parts, reply-to); Delivery renders and transmits. The provider's types never appear upstream.
- **`Clock`** — injected, so state-history tests can pin time.

## Deferred decisions
| Decision | Why it can wait | Trigger that ends the deferral | Cost to change then |
| --- | --- | --- | --- |
| Persistence engine (SQLite today) | One writer; `Invoices` is the only thing core needs | A second concurrent writer, or the first reporting query that needs a join | Swap the adapter: ~2 days. No core change. |
| Mail provider | Behind `Outbox`; deliverability outsourced | Bounce rates we can see, or the first customer domain we must send from | New adapter: ~1 day. |
| Customer as its own context | One owner, low churn, no invariants | A second effort (quotes, receipts) needs the same customer data | Extract the context: ~1 week. |

## Fitness functions
| Rule | Check | Command | Status |
| --- | --- | --- | --- |
| `core` imports nothing from adapters, web, or mail | dependency-cruiser | `npx depcruise --config .dependency-cruiser.cjs src` | enforced |
| SQL appears only under `adapters/store/` | grep structural test | `npm run check:sql` | enforced |
| Invoice status mutates only through root methods | structural test — no `.status =` outside core | `npm run check:status` | enforced |
| Email bodies are built only from Delivery templates | grep structural test | `npm run check:templates` | enforced |
| The board's walk (create → send → paid) stays true | e2e | `e2e:invoice-flow` in CI | enforced |

## Stress test
See [stress.md](stress.md) — three attempted violations, all caught.

## Open structural questions
- Whether the live invoice page earns its own context once customers can act on it (disputes, comments). Today it is a read model; revisit when it takes its first write from a customer.
