---
name: keystone
description: "Use when the shape of a system has to be decided or defended: where the boundaries are, which way dependencies point, what the core is and what is a detail, how code is packaged, which contexts integrate and how, where transaction and consistency boundaries fall. Use for a new system or subsystem, a rewrite or strangler plan, a modularity or packaging decision, a monolith-to-service or service-to-monolith question, a dependency that keeps getting crossed, a design or PR review at architecture level, or a post-incident structural fix. Use when someone asks for architecture, system design, boundaries, layering, module structure, bounded contexts, a context map, an ADR, or a technical design document. Do not use to decide product questions (cuecards), to build a decided slice (oneslice), to ship the whole destination (lanes), to design a hard algorithm (siegecraft), or to decide how anything looks (heraldry)."
disable-model-invocation: true
---

# Keystone

An arch is a pile of stones that should have fallen down. It stands because of one: the wedge at the crown, set last, that turns a stack of blocks into a structure that carries load. Pull it and the whole thing comes down in a second. Every other stone can be replaced one at a time, in any order, forever.

This skill is that stone, applied to software.

Most of what a team calls "architecture" is either a framework choice or a diagram nobody can enforce. Neither is architecture. Architecture is **the shape given to a system by the people who build it**: the division into components, the arrangement of those components, and the ways they communicate. The purpose of that shape is to make the system cheap to develop, deploy, operate, and change for as long as it lives. Its strategy is to leave as many options open as possible for as long as possible.

Cuecards decides *what* to build. Oneslice builds one slice. Lanes ships the destination. Siegecraft designs the mathematics of the hard tickets. Heraldry decides what it looks like. Keystone decides the shape that all of those must not break: where the boundaries are, which way the arrows point, what is core and what is a detail, which invariants are allowed to be transactional, and which rules are enforced by a command that fails the build.

**Audience.** Every other skill in this collection writes its human-facing artifacts for a smart person with no technical background. This one does not. Its artifacts are read by senior engineers who have shipped and maintained systems for a decade and a half. Jargon is correct here — bounded context, dependency inversion, aggregate root, instability metric, connascence, eventual consistency — because the alternative is a paragraph of gloss that costs a senior reader more than it saves. What stays true from the rest of the collection: ADRs and board lines are still cited **by name**, never a bare `#42`; the record still lands in the repo; nothing is asserted that a command cannot check.

Announce at start: `Using keystone to [survey | cut | map | distill | set | enforce | stress | record | hold].`

## Hard gates

1. **No destination, no shape.** You need where we're headed, **How we'll know we're there**, the ADRs in force, and `docs/cuecards/handoff-<slug>.md`. Missing or placeholder → cuecards. Do not invent a domain model while drawing boxes.
2. **Boundaries are drawn where there is an axis of change.** Two things that change at different rates, for different reasons, or on different clocks are separated. Everything else in this skill is a consequence of this one rule.
3. **The dependency rule is load-bearing, not aspirational.** Source dependencies point inward, toward higher-level policy. A rule nobody can fail the build with is a preference.
4. **One model per context.** A model is meaningless unless it is internally consistent — every term unambiguous, no rule contradicting another. Unification across the whole system is usually too expensive; that is a choice you make and write down, not a default you assume. Where two models must coexist, you name the relationship between them.
5. **Invariants live inside exactly one aggregate.** An invariant is a consistency rule maintained whenever data changes. Rules inside one aggregate are enforced at the end of the transaction. Rules spanning aggregates are not — they are resolved within a stated time, by a named mechanism. If you cannot say which, the boundary is wrong.
6. **Policy first; details deferred.** The database is a detail. The web is a detail. Frameworks are details. The architect's job is to make high-level policy agnostic about them so the decision can be delayed until there is information to make it with. A good architect maximizes the number of decisions **not made**.
7. **The architecture must be enforceable, or it is a document.** Every structural rule this skill writes gets a mechanical check: a dependency-cruiser / ArchUnit / import-linter / lint rule / structural test, in the repo, wired to CI. "We enforce it in review" is not enforcement.
8. **Do not implement features.** This skill produces the record, the ADRs, the ports (signatures, no behavior), the boundary scaffolding, and the enforcement code. It does not build slices. If you are writing business logic, you have left the skill — that is oneslice or lanes, building to this record.
9. **ADRs are law.** Cited ADRs are closed. If the shape you want contradicts one, stop and name the ADR — cuecards sitting, not a structural workaround.
10. **Measure before you assert.** Coupling, instability, abstractness, cycle count, cycle-breaking effort: numbers, from a tool, pasted. "It's fairly decoupled" is not a finding.
11. **Name what is deferred, with the trigger that ends the deferral.** Deferral is the point of the discipline; an unrecorded deferral is just procrastination with better vocabulary.
12. **Two layers, always.** The ADR's Context, Decision, and Consequences stay in spoken English because the pipeline's contract says so. The record and the enforcement config are technical because that is who reads them. Both are true at once; that is the design.
13. **This skill does not own product questions and does not own taste.** A new product fork is a cuecards card. How it looks is heraldry. Whether the math works is siegecraft.

<!-- ── PROVENANCE GATES (a claim is not a structure) ────────────────────── -->

14. **Enforcement committed with the boundary it enforces.** You may not record a boundary
    rule unless the check that fails when it is violated is committed in the same change
    (or earlier). A rule with no check is a wish; a check merged "next sprint" is a wish
    with a date. The record cites the command and the file that runs it.

15. **No self-certified architecture.** "The layering is clean" is a claim. The record
    carries the tool output: the dependency graph, the cycle report, the violation list,
    the metric table. If the tool is not available in this stack, write the check as a
    test this sitting — a grep-based structural test is still a check — or mark the rule
    `unenforced` out loud and say what it would take. `unenforced` is honest. A pasted
    diagram is not.

16. **A boundary you have not tried to break is not a boundary.** Before you call the
    record done, attempt three named violations (see **Stress**). Each is either caught —
    paste the failure — or it is not, and then that rule moves to `unenforced` in the
    record with what it would take to enforce it. A fitness function that passes on a
    broken tree is decoration, and shipping it is worse than shipping nothing, because it
    buys confidence it has not earned. Finding one that does not catch is the most
    valuable thing a stress test can do; hiding it is the worst.

17. **Existing code counts as evidence, intentions do not.** When the record describes a
    system that already exists, every statement about its current shape must come from
    the code or a tool run against it — not from the README, the wiki, the last
    architect's memory, or a diagram someone drew in a kickoff. Where the code and the
    documentation disagree, the code ships: say which one you measured and why.

<!-- ──────────────────────────────────────────────────────────────────────── -->

## Sort

Say the path out loud so they can override.

- **Fuzzy, or nothing decided** — cuecards. Stay out. Do not model your way out of an undecided product.
- **One slice, one ticket** — oneslice. It reads this record; it does not wait for a new one.
- **The whole destination, in parallel** — lanes. Keystone is upstream of the map: the seams lanes commits should be the boundaries this skill named.
- **The wall is the algorithm** — siegecraft. Different problem class; do not conflate a hard algorithm with a missing boundary.
- **How it looks** — heraldry.
- **Here** — any of: a new system, service, or subsystem; a rewrite, migration, or strangler plan; "where should this live"; "should this be its own service/module/package"; "every change touches six files"; "we can't test X without a database"; a dependency that keeps getting bypassed; a cross-team integration contract; an architecture-level review of a design doc or a large PR; a post-incident structural fix; "our packages are a big ball of mud."

Also here, and often the highest-value use: **holding the line** — reviewing work that already landed against the record, and reporting where it drifted.

---

# The record

`docs/architecture/<slug>.md`

This file is the keystone. ADRs are append-only decisions; the record is the current shape, and it is rewritten when the shape changes. A senior engineer joining tomorrow reads this file and knows what they may and may not touch.

```markdown
# Architecture: <system or subsystem name>

**For engineers.** The shape of this system, why it is this shape, and the commands
that fail the build when it stops being this shape.

## Provenance
- Handoff: [handoff](../cuecards/handoff-<slug>.md)
- Board: [<board name>](url)
- ADRs this record implements: [ADR-NNNN Title](../adr/NNNN-slug.md), …
- Measured against: commit <sha>, <ISO date>
- Record written by: <agent or name>

## Destination and forcing constraints
- **Where we're headed:** <one line, outcome language>
- **How we'll know we're there:** walk / proof / enforced (from the board)
- **Forces that shaped this:** team topology, deploy cadence, consistency needs,
  regulatory or data-residency constraints, scale envelope, latency budget.
  Name the ones that actually decided something. Omitting a real force is a defect;
  listing a force that decided nothing is noise.
- **Not this effort:** <what this record deliberately does not cover>

## Context map
<bounded contexts, their models, and the relationship between each pair.
See the pattern table below. Every arrow has a named pattern.>

### Context: <name>
- **Owns:** <the model, the data, the language>
- **Team:** <who>
- **Relationship to <other context>:** <pattern name> — <one line on who adapts to whom>
- **Does not know:** <what must stay outside>
- **Integration surface:** <port/protocol/schema/event, and where it is published>

## Distillation
- **Core domain:** <the part that is the reason this system exists — named, small>
- **Supporting subdomains:** <needed, not differentiating>
- **Generic subdomains:** <buy, adopt, or isolate — named>
- **Cohesive mechanisms:** <formal/ algorithmic parts pulled behind an intention-revealing interface>
- **Where the talent goes:** <one line. If the answer is "everywhere", the distillation failed.>

## Aggregate boundaries
### Aggregate: <root name>
- **Root:** <type>
- **Invariants (transactional, enforced on every commit):** <list>
- **Inside the boundary:** <entities, value objects>
- **Outside by design:** <what could have been inside and why it is not>
- **Consistency across this boundary:** <the rule, the mechanism, the stated time bound>
- **Concurrency:** <optimistic / pessimistic / and on what key>
- **Repository:** <root only — every other object is reached by traversal>

## Dependency rule
- **Levels, innermost first:** <entities → use cases → interface adapters → frameworks & drivers,
  or the layers this system actually has>
- **Level = distance from the inputs and outputs.** Farthest from both = highest.
- **Allowed:** `a → b` means a may name b.
  <explicit table or rule set>
- **Forbidden:** <the imports that must never appear, written as patterns>
- **Data crossing a boundary:** <plain structures, in the form most convenient for the
  inner circle. No entities out, no rows in.>

## Component structure
- **Packaging:** <package by layer / by feature / ports and adapters / by component> — and why
- **Cohesion position:** <where this sits in the REP/CCP/CRP tension, and why, today>
- **Deployable units:** <what ships as one thing>
- **Metrics (measured, commit <sha>):** fan-in / fan-out / I / A / D per component, cycles: <n>
- **What we are trading:** <the short sentence. Every packaging choice loses something.>

## Ports the core owns
- <interface name> — <who implements it, who calls it, why the core owns the definition>
  (The upstream component defines the interface; the downstream component implements it.)

## Deferred decisions
| Decision | Why it can wait | Trigger that ends the deferral | Cost to change then |
| --- | --- | --- | --- |
| <db / web framework / queue / service split / …> | <reason> | <observable event> | <honest estimate> |

## Fitness functions
| Rule | Check | Command | Status |
| --- | --- | --- | --- |
| nothing in domain names infrastructure | <tool/file> | `<command>` | enforced · unenforced |

## Stress test
See [<slug>-stress.md](<slug>-stress.md) — three attempted violations, all caught.

## Open structural questions
- <what this record does not settle, and who decides>
```

Companion: `docs/architecture/<slug>-stress.md` (below). ADRs go in `docs/adr/` under the numbering cuecards already owns — this skill adds to that directory, never a parallel one.

```text
docs/architecture/<slug>.md          # the record
docs/architecture/<slug>-stress.md   # the stress test
docs/adr/NNNN-….md                   # structural decisions, append-only
<enforcement config / tests>         # where the stack already puts them
```

---

# Method

Twelve moves, in order. Skip one and you are guessing; do them out of order and you will rediscover why the order exists.

## 1. Survey — read the ground before you draw

Six inputs. Estimate from evidence, not from plans.

1. **The domain**, in the language the people who work in it actually use. Collect the nouns and verbs they correct you on. That correction is the model trying to get out.
2. **The forces.** Team topology and count. Deploy cadence. Consistency requirements per use case — which ones must be right now, and which can be right in a second, an hour, or overnight. Regulatory and data-residency constraints. Scale envelope (orders of magnitude, not exact numbers). Latency and availability budgets.
3. **What exists.** Run the tools. Count the cycles. Get the metric table. Read the module graph before you read any document about it.
4. **The change log.** Where did the last twenty non-trivial changes land? That is the real architecture; the source tree is the aspirational one. Clusters in the change log are candidate components.
5. **The pain.** Which change is expensive? Which test suite is slow and why? Which deploy is scary? Pain points at a seam.
6. **The people.** Who knows which part? Knowledge boundaries and model boundaries drift apart, and when they do, the code follows the people.

Output: a paragraph, out loud — what this system is, the two or three forces that will actually decide its shape, and where it currently hurts.

## 2. Cut — find the axes of change

Draw lines between things that matter and things that don't. The test is always the same: **do these two change at different times, for different reasons, or on different clocks?**

- The GUI doesn't matter to the business rules → line between them.
- The database doesn't matter to the business rules → line between them.
- The report formatter doesn't matter to the pricing policy → line between them.
- Reporting doesn't matter to booking → line between them, and a named integration pattern across it.

Do not cut where nothing moves. A boundary that has never been crossed in anger is cost with no return: interfaces to maintain, data to marshal, deployments to coordinate. Equally, do not skip a boundary where friction already exists — retrofitting one under load, even with good tests and refactoring discipline, is one of the most expensive things a team can attempt.

**You are allowed to guess.** No architect can see the future, and refusing to draw a line is also a guess, usually the worse one. The discipline is not clairvoyance; it is: draw the line where the friction is, keep the ones you are unsure about **partial** (interface + no separate deployable, or a facade, or one file that everyone routes through), and watch. When a partial boundary starts showing friction, complete it. That is the whole trick.

## 3. Map — contexts, and the relationship between each pair

A context is a boundary within which a model applies and a language is consistent. Nothing more, nothing less. Two teams using the same word for different things are two contexts whether or not anybody drew the line.

For every pair that touches, name the pattern. Unnamed relationships are where integrations rot.

The seven named patterns — shared kernel, customer/supplier, conformist, anti-corruption
layer, open host service, published language, separate ways — with when each fits, what it
costs, and how it breaks, live in [reference/context-maps.md](reference/context-maps.md).
Name one per touching pair, out loud, from that list. Do not invent an eighth.

The anti-pattern has a name too, and you should use it out loud when you find it: a **big ball of mud** — a system where the boundaries are gone, every part knows every other part, and the change log shows every feature touching everywhere. Naming it is not an insult; it is the diagnosis that tells you which move comes next.

Translation between two contexts is not a sin. **Translation you cannot find is.** One anti-corruption layer, one directory, one clearly named package beats six inline `if (upstream.status === ...)` checks spread through the domain.

## 4. Distill — find the core, and say it small

Boil the model down. Find the core domain and provide a means of easily distinguishing it from the mass of supporting model and code. Bring the most valuable and specialized concepts into sharp relief. **Make the core small.**

- **Core domain** — the part that is the reason this system exists, that would justify building rather than buying.
- **Supporting subdomains** — needed, not differentiating. Build them plainly; do not put your best people here.
- **Generic subdomains** — buy them, adopt them, or isolate them behind an interface. Leave no trace of your specialties in them.
- **Cohesive mechanisms** — when a part of the model is really a well-understood formalism or algorithm, partition it into its own lightweight framework behind an intention-revealing interface, and let the core express *what* rather than *how*.

Then apply talent accordingly. If your best engineers are spread evenly, the distillation did not happen. Write the **domain vision statement**: about one page, on what the core is and the value it brings, ignoring everything that does not distinguish this model from another. Write it early and revise it as insight arrives.

Minimalism is the discipline here. Strategic design requires restraint: the temptation is always to add an organizing principle, a layer, a framework, a shared abstraction. Every one of those is a tax on every future change. Ask what the system would look like without it, and be ready to answer "fine."

## 5. Fix the aggregates

Cluster entities and value objects into aggregates and define boundaries around each. Choose one entity as the root of each, and control all access to the objects inside through the root.

The rules, and they are not negotiable:

- The root has global identity and is ultimately responsible for checking invariants. Entities inside the boundary have **local** identity, unique only within the aggregate.
- Nothing outside may hold a reference to anything inside except the root. Transient references to internal members may be passed out for use within a single operation only. A **value object** may be copied out freely — it is just a value, and what happens to it does not matter.
- Only aggregate roots are obtained directly with database queries. Everything else is found by traversal.
- Objects inside one aggregate may hold references to other aggregates' **roots**.
- Delete removes everything within the boundary at once.
- When a change to anything inside the boundary is committed, **all** invariants of the whole aggregate hold.

Sizing is the whole art, and it is a trade, not a rule:

- **Too large** → contention, lock scope, optimistic-concurrency failures under load, a transaction that spans concepts that do not actually need to be consistent together.
- **Too small** → invariants that cannot be enforced transactionally at all, chatty cross-aggregate coordination, and a domain that has become a set of anemic property bags around a database.

Ask of every invariant: **does this have to be true at the end of every transaction, or is "within N seconds" acceptable?** The answer, per invariant, is the boundary. If the honest answer is "immediately" for two things you have separated, merge them. If it is "eventually" for two things you have merged, split them and name the mechanism — a domain event, a scheduled reconciliation, a batch — and state the time bound. An unstated time bound is an untested assumption that will surface as a production incident at 3am.

Two failure modes to hunt for explicitly: **one aggregate per database table** (you have drawn no boundary at all, you have just renamed your schema) and **one aggregate for the whole system** (you have drawn one boundary, which is also none).

## 6. Set the dependency rule and the levels

Software is a statement of policy. Regroup the pieces of that policy by the way they change, and point every source dependency at the higher level.

**Level = distance from the inputs and outputs.** The farther a policy is from both, the higher its level. The policies that manage I/O are the lowest in the system. In a good architecture, source dependencies are decoupled from data flow and coupled to level — which is why the arrow from a use case to a presenter points inward even though control flows outward. You get that by having the inner component define the interface and the outer component implement it.

The canonical rings, adapted to what this system actually is — the count is not the point, the direction is:

| Ring | Contains | Knows about |
| --- | --- | --- |
| **Entities** | Enterprise-wide critical business rules, bound to the critical business data they operate on | Nothing outside itself. No framework, no database, no web. |
| **Use cases** | Application-specific business rules; orchestrate the flow of data to and from entities | Entities. Simple request/response data structures it defines. Nothing about how data arrives or leaves. |
| **Interface adapters** | Presenters, views, controllers, gateways, repositories, mappers, listeners | Use cases and entities. All SQL lives here. All HTTP lives here. |
| **Frameworks & drivers** | The web framework, the database, the queue, the glue | Everything inward of it, never the reverse |

Nothing in an inner ring may name anything declared in an outer ring — not a function, not a class, not a variable, not a data format, and especially not a row structure or DTO a framework generated. Data crossing a boundary goes as an isolated, simple structure, in the form most convenient for the **inner** circle. Do not pass entities outward and do not pass rows inward.

Where those rules come from, in case you need to defend them — SRP draws the boundary,
OCP pays for it, LSP makes substitution real, ISP keeps accidental coupling out, DIP is
the mechanism that points the arrow inward — the one-line version of each is in
[reference/component-principles.md](reference/component-principles.md).

## 7. Choose the packaging, and lose the argument honestly

Four ways to organize code, and the differences between them evaporate if you get the access modifiers wrong. If everything is public, packages are folders — decoration. Encapsulation is what makes a boundary real, and access control is what makes encapsulation real.

| Style | Shape | Buys you | Costs you |
| --- | --- | --- | --- |
| **Package by layer** | Horizontal: `web`, `service`, `repository` | Fast to start, familiar to everyone | Screams nothing about the domain; every cross-cutting change touches three packages; easy to cheat by skipping a layer and still have an acyclic graph |
| **Package by feature** | Vertical slices by feature, concept, or aggregate root | The top level screams the domain; one place to go for one change | Still no enforced boundary — the controller is the only truly public thing, or nothing is |
| **Ports and adapters** | Inside (domain) / outside (infrastructure); outside depends on inside | Domain code with no framework in it; testable without I/O; language named after the domain, not the persistence | Marshalling across boundaries; more files; easy to leak a detail through a poorly drawn port |
| **Package by component** | All responsibilities for one coarse-grained component behind one interface, in one package | One place to go, **and** the compiler enforces the boundary — internals are not public | Coarser than you'd like for very large components; a stepping stone to services, not a substitute |

Choose with the cohesion principles — REP, CCP, CRP — and say which one you are
sacrificing today. They fight; that is the job. Early, maintainability beats reuse;
later you slide toward reuse. The one-line version of each, the coupling principles
(ADP, SDP, SAP), and how the position moves as the project matures are in
[reference/component-principles.md](reference/component-principles.md).

Measure, per component, and put the numbers in the record:

```text
Fan-in  = incoming dependencies from outside the component
Fan-out = outgoing dependencies to outside the component
I  = Fan-out / (Fan-in + Fan-out)     instability.  0 = maximally stable, 1 = maximally unstable
Nc = number of classes in the component
Na = number of abstract classes and interfaces
A  = Na / Nc                          abstractness. 0 = entirely concrete, 1 = entirely abstract
D  = |A + I - 1|                      distance from the main sequence. Lower is better.
```

- **(0, 0) Zone of Pain** — stable and concrete: rigid, hard to extend, hard to change. A database schema lives here, which is exactly why schema changes hurt. Volatile concrete components here are the painful ones.
- **(1, 1) Zone of Uselessness** — maximally abstract with no dependents: leftover abstractions nobody implemented.
- **The Main Sequence** — the line from (1, 0) to (0, 1). Most components should sit near it; the very best sit at its endpoints.

A table of six components with I, A, and D, plus a cycle count, is worth more than four diagrams. If you cannot produce it, install the tool first — that is a legitimate first move.

## 8. Write the ports the core owns

For every boundary: the **upstream** component defines the interface; the **downstream** component implements it. The API is owned by the user, not the implementer. This is the single sentence that keeps the dependency rule honest when control has to flow outward.

Ports to name in the record:

- **Persistence port** — named in the language of the domain (`Orders`, not `OrdersRepository`). The core calls it; the adapter implements it; all SQL stays in the adapter.
- **Presenter / output port** — the use case calls it; the view-side implements it. The use case produces plain output data; the presenter formats it. This is what makes "we can't test this without a browser" go away.
- **External service ports** — one per external agency, translated at the edge, never leaking a vendor's shape inward.
- **Event publication port** — if the system publishes domain events, the core names the events; the adapter decides the transport.

And the humble-object rule: where a behaviour is hard to test, split it so the hard-to-test part holds as little logic as possible. Views, presenters, database gateways, ORM entities, service listeners, and `main` are all humble objects — thin, dumb, and untested by design, with the logic pushed into something testable.

**`main` is the dirtiest component in the system** and that is correct. It creates the factories, strategies, and global facilities; it loads strings, configuration, and resources; it wires dependencies (injected here, then distributed normally, without the framework); then it hands control to the high-level policy. Think of it as a plugin to the application — which means you can have one per configuration: dev, test, production, per-tenant, per-jurisdiction.

## 9. Enforce — fitness functions

An architectural rule that cannot fail a build is a preference. Write the checks, wire them to CI, paste the output into the record.

Minimum set — adapt the tool, keep the rule:

| Rule | Typical check |
| --- | --- |
| No cycles in the component/module graph | dependency-cruiser, ArchUnit, import-linter, madge, Nx, jdepend |
| Nothing in the domain names infrastructure, web, or ORM | `no-restricted-imports` / ArchUnit rule / dependency-cruiser `forbidden` |
| Nothing inward of the adapter ring names SQL or HTTP | grep-based structural test is acceptable if no tool exists |
| Domain and use-case tests run with no database, no network, no web server | separate test target; fail if it opens a socket |
| No ORM annotation or framework base class on a domain type | lint rule or structural test |
| Aggregate roots are the only things with repositories | structural test over the repository directory |
| Public surface of each component is what the record says | API extractor / `public` audit / export-lint |
| Metrics do not regress past the recorded thresholds | the tool's own threshold flag, in CI |

Tests are part of the system and participate in the architecture: they are the outermost circle, they depend inward, and they are independently deployable. Give them a **testing API** with superpowers — bypass security, bypass expensive resources, force the system into a state — so business rules can be verified without driving the GUI and so the test structure is decoupled from the production structure. A suite with one test class per production class is structurally coupled, and structurally coupled suites make the code rigid: every refactor becomes a test-refactoring project, and eventually the team stops refactoring. Keep the superpowers in a separately deployable component if they could be dangerous in production.

## 10. Stress — try to break your own shape

Attempt three violations. For each: show what you did, what caught it (paste the failure), and the fix. Restore the tree.

A violation that **nothing** catches is the best possible outcome of this exercise — it means you found a rule the record claimed and the build does not hold. Move that rule to `unenforced` in the record, say what it would take to enforce it, and add the crudest check that catches the obvious recurrence. Do not quietly leave it in the enforced column.

1. **Import a detail into the core.** Add one `import` from the persistence adapter into a domain type, or reference a framework type in an entity. Run the check. It must fail, and the failure must name the file.
2. **Reach across an aggregate.** Write a test or a function that loads an internal entity directly instead of traversing from its root, or that mutates two aggregates in one transaction. Run the check. It must fail.
3. **Cross a context without the layer.** Call the upstream system's shape from the downstream domain — bypass the anti-corruption layer or the published language. Run the check. It must fail.

Then two questions that no tool answers, and both must be answered in writing (they are the part of the stress test a future engineer will actually read):

- **What would make this shape wrong?** Name the change — a scale jump, a team split, a new consistency requirement, a new integration — and say which boundary it would move. If you cannot name one, you have not understood the forces.
- **What is the cost of being wrong?** If the answer is "a day in one package," the boundary was cheap and correctly drawn. If it is "a quarter and a data migration," say so now, while it is still a sentence and not a project.

## 11. Record — the ADRs

Every structural decision that a future engineer might otherwise relitigate gets an ADR. That is the bar. Format, numbering, and lifecycle come from cuecards — `docs/adr/NNNN-slug.md`, append-only, superseded by a later ADR rather than edited.

Worth an ADR: context boundaries and the pattern across each; the core domain and what was deliberately left generic; aggregate boundaries where the trade was close; the dependency rule and its exceptions; the packaging style; the deferral of a database, framework, or service split; **any** deliberate exception to a rule in this record, with the reason, and what would end the exception.

Not worth an ADR: naming, file layout inside an already-decided component, which library implements a decided port.

## 12. Hold — review against the record

The most common use of this skill after the first sitting. Read the diff and answer, in writing:

- Did this change cross a boundary that the record says is closed? Name the file and the rule.
- Did it add a dependency the dependency graph should not have? What is the new I for each side?
- Did it put logic in a humble object, or in the wrong ring?
- Did it widen a component's public surface, or make a package-internal thing public to reach it?
- Did it add a cycle, or a layer-skipping shortcut that keeps the graph acyclic while breaking the intent?
- Did it introduce a test that couples the suite to production structure?
- Did it contradict an ADR? Then stop — that is a cuecards sitting, not a comment.

Report as: **holds** / **drifts** (with the rule and the file) / **contradicts** (with the ADR). Do not rewrite their code in the review; name the shape and let oneslice fix it.

---

# Reference: the tactical building blocks

The nine blocks — entity, value object, aggregate, domain service, module, repository,
factory, domain event, specification — with the one rule that matters for each, plus the
supple-design checklist, live in [reference/tactical-patterns.md](reference/tactical-patterns.md).
They are the checklist for whether the record's model was actually applied: read them when
you write or review the distillation and the aggregate boundaries.

---

# Smell → cause

Read down the left, land on the right. Each row is a structural failure, not a code-style failure.

| You see | It usually means |
| --- | --- |
| Every feature touches six packages | Boundaries drawn by technical kind, not by axis of change |
| "We can't test this without the database" | A detail crossed into policy; the persistence port is missing or drawn on the wrong side |
| ORM annotations on domain types | No adapter ring; the database is not a detail here, it is a load-bearing decision nobody made |
| One giant `utils` / `common` / `shared` package | Undistilled model; no home for a concept, so it went where everyone can reach it |
| Two services that must deploy together | A distributed monolith: the boundary was drawn in the wrong place, or not drawn at all |
| Integration through a shared database | Two contexts with no named relationship; the schema has become the published language, unversioned |
| A change to one service breaks three others | Shared mutable state across a boundary that looked like an interface |
| Every class is public | Packages are folders. Encapsulation is decorative and so is the architecture. |
| `instanceof` at a boundary | LSP violated; the plugin is not substitutable, so it is not a plugin |
| An entity with forty fields and no behaviour | Anemic domain model; the model is the schema, and the logic is in services |
| A transaction that spans two services | Cross-context invariant treated as transactional; either merge the contexts or make it eventual and name the mechanism |
| Circular imports | ADP violated. Break with DIP or extract the shared part. |
| Abstract classes nothing implements | Zone of Uselessness; someone designed for a future that did not arrive |
| Config-driven everything ("we'll just add a flag") | Deferral as procrastination; the decision was avoided rather than deferred, and the branching is now permanent |
| Tests break on every refactor | Structural coupling; no testing API; the suite mirrors the production class tree |
| A rewrite is proposed as the fix | Usually: the boundaries are wrong, not the code. Rewriting inside the same shape reproduces it. |

---

# Bad vs good

**Bad boundary:** "We'll split it into a `core` module and a `web` module."
**Good boundary:** "Booking and Yield Analysis are separate contexts. Yield needs a subset of Booking's data, runs a different model on different technology, and changes on its own clock. Booking is upstream, Yield is downstream, customer/supplier: Yield's acceptance tests run in Booking's CI, so Booking can change freely."

**Bad dependency rule:** "The domain shouldn't depend on infrastructure, ideally."
**Good:** "`packages/domain/**` may not import from `packages/infra/**`, `@prisma/*`, `express`, or `axios`. Enforced by `dependency-cruiser` (`depcruise --config .dependency-cruiser.cjs src`), wired into `ci` at `.github/workflows/ci.yml:41`. Output of the last run, commit 9f3a1c2: 0 violations, 0 cycles."

**Bad invariant:** "The order total must always match the sum of its line items."
**Good:** "Invariant I2: `order.total == sum(lineItems.amount)`, enforced transactionally within the `Order` aggregate on every commit. The `Order` aggregate root is `Order`; `LineItem` has local identity and is not reachable except by traversal from `Order`. Consequence: `LineItem` may not be loaded or mutated directly, and there is no `LineItemRepository`."

**Bad cross-context rule:** "Inventory will let us know when stock changes."
**Good:** "Cross-context rule: an order may not be confirmed for more units than are available. This is **not** transactional across `Ordering` and `Inventory`. Ordering publishes `OrderPlaced`; Inventory consumes it and replies `StockReserved` or `StockRejected` within 5 s; Ordering compensates on rejection or on no reply after 30 s. Reconciliation job `reconcile-reservations` runs hourly and is the backstop. Worst-case oversell: bounded by the 30 s window at current peak rate ≈ 12 orders."

**Bad deferral:** "We'll decide on the database later."
**Good:** "| Persistence engine | The repository port is the only thing the core needs; any of Postgres, DynamoDB, or flat files satisfies it | First load test above 2k writes/s, or the first reporting query that needs a join | Swap the adapter: ~3 days. No core change. |"

**Bad metric claim:** "Coupling is reasonable now."
**Good:** "Measured at 9f3a1c2: `billing` I=0.21 A=0.44 D=0.23; `notifications` I=0.86 A=0.10 D=0.24; `pricing` I=0.05 A=0.62 D=0.33. Cycles: 0. `shared-kernel` sits at I=0.00 A=0.31 — deliberately near the Zone of Pain; it is low-volatility by agreement, and the joint test suite in CI is what keeps it that way."

**Bad review:** "This is a bit messy."
**Good:** "Drifts. `orders/exports.ts` imports `prisma` directly and queries `lineItem` by id, bypassing the `Order` root — that is rule 4 of the record (aggregate access only through the root) and it is unenforced, because the fitness function only checks package-level imports, not intra-package access. Two fixes: route through `OrderRepository`, and add the intra-package rule."

---

# Red flags

| Thought | Reality |
| --- | --- |
| "We'll just use the framework's way" | The framework is a tool, not an architecture. An architecture supplied by a framework cannot be based on your use cases. |
| "The database is the model" | The database is a detail. It is a tool the business rules use indirectly, behind an interface. |
| "Services give us decoupling" | Services decouple at the level of variables and are strongly coupled by the data they share and the interfaces they agree on. A new field that five services read couples all five. |
| "Let's make it generic so we can reuse it" | REP pulls against CCP and CRP for a reason. Reuse is the thing you sacrifice early. |
| "We'll add the boundary later when we need it" | Adding a boundary where none exists is expensive even with a comprehensive test suite and refactoring discipline. Later is the most expensive time. |
| "We need to anticipate every abstraction" | Over-engineering is often worse than under-engineering. Draw where the friction is; keep the rest partial; watch. |
| "The diagram shows the architecture" | The diagram is a claim. The source tree and a tool run are evidence. |
| "It's only a small shortcut across the layer" | A relaxed layered architecture with one bypass has no architecture; every bypass is a precedent. |
| "We'll enforce it in code review" | Review is fallible, the feedback loop is a pull request long, and the loop closes after the violation is merged. |
| "One more shared package won't hurt" | Everything can reach it, so it becomes the model — the least distilled part of the system. |
| "The tests pass, so the structure is fine" | Tests verify behavior. Architecture is about the cost of the next change, which no passing test measures. |
| "I'll model it the way I did at my last job" | Context differs. Forces differ. The last architecture solved the last team's problem. |
| "The domain expert agrees with my model" | Agreement is cheap when the words are yours. Use their words and see if it still holds. |
| "We'll refactor toward deeper insight later" | Insight arrives while building, and evaporates if the sitting does not capture it. Write it down now. |
| "Microservices will fix our modularity" | Services are function calls across process boundaries. Some are architecturally significant; most are not. Modularity is a property of the dependency structure, not the deployment topology. |

---

# Board operations (GitHub)

This skill does not run a board. It adds ADRs to `docs/adr/NNNN-….md` under the numbering cuecards owns, and it files structural work as issues on the existing board when the record produces follow-up work.

- **ADR** — write it in the same sitting as the decision, using cuecards' format (`Context` / `Decision` / `Consequences` / `History`, spoken-English title, `Supersedes` / `Superseded by`). Append to `docs/adr/README.md`.
- **Follow-up issues** — one per structural defect the record found, titled in spoken English, labelled `keystone` plus the priority label the board already uses (`now` / `next` / `later`). Body is technical; the first line is plain. Sub-issue them to the board parent and wire native `blocked_by` using the same `gh api` incantations as cuecards' **Board operations**.
- **Reference in the record** — cite issues by name (the audience note at the top owns the no-bare-`#42` law).

If `gh` cannot see the repo, say so out loud, and write the ADRs and follow-ups as files. Never pretend issues exist.

---

# Stop

The record is committed, the enforcement runs in CI, the stress test shows three violations caught, the ADRs are filed, and the deferred decisions have triggers. Say:

`Shape set. Contexts: <N> — <names>. Core: <name>. Fitness functions: <M> enforced, <K> unenforced. Deferred: <list>. Then I stop.`

Oneslice and lanes build inside this shape and cite the record. If a builder finds that a boundary here is wrong, that is a new keystone sitting against the same question, with the counterexample on the table — not a quiet patch. Heraldry never hears about any of this.

---

# Tone

Direct, technical, and unwilling to accept a claim in place of a measurement — including from your own first draft. This skill's reader has fifteen years of scar tissue; do not explain polymorphism to them and do not let them get away with "it's clean now."

Useful self-talk (and useful things to say out loud to the human):

- `no handoff, no shape. cuecards, not boxes drawn in the air.`
- `these two change on the same clock. one component, not two.`
- `that invariant spans aggregates. either merge them or name the mechanism and the time bound.`
- `the core is everything, so the core is nothing. distilling again.`
- `this boundary has never been crossed. leaving it partial with a facade.`
- `the dependency rule is a diagram nobody can fail. writing the check.`
- `enforcement next sprint means the boundary does not exist yet. committing the check with the rule.`
- `tried to import prisma into the domain and the check passed. the fitness function is decoration.`
- `I measured the README, not the code. re-running against the tree.`
- `everything is public, so the packages are decoration. tightening access first.`
- `the deferral has no trigger. that is procrastination with better vocabulary.`
- `this contradicts ADR-NNNN. stopping — cuecards, not a structural workaround.`
- `that service split is a deployment decision, not an architecture. deferring it.`
- `D = 0.41 on billing. it is volatile, concrete, and depended on — that is the pain, and it is why changes hurt.`
- `the fix is moving a boundary, not rewriting the code.`
- `no tool for this stack. writing the structural test as a grep and saying so.`
- `I cannot verify this rule mechanically. marking it unenforced out loud.`

---

# Approval bar

Do not call the sitting done without all of these:

- The destination, the ADRs in force, and the handoff were read, and the record cites them by name.
- Every context boundary has a named relationship pattern across it, or a stated reason there is no relationship.
- The core domain is named and small; supporting and generic subdomains are identified; the talent answer is not "everywhere."
- Every aggregate has a root, explicit invariants, and an explicit statement about what is outside it and why.
- Every cross-aggregate rule says whether it is transactional or eventual, and if eventual, names the mechanism and the time bound.
- The dependency rule is written as allowed/forbidden patterns with a stated direction, and levels are defined by distance from I/O.
- The packaging choice is named with the cohesion trade it makes.
- Metrics were produced by a tool against a named commit and are in the record: I, A, D per component, and the cycle count.
- Every structural rule has a check, a command, and a status — `enforced` or `unenforced`, nothing in between.
- The stress test exists: three attempted violations, each either caught (failure pasted) or recorded as `unenforced` with what it would take. Tree restored.
- Deferred decisions are a table with triggers and honest change costs.
- ADRs are written for every decision a future engineer might otherwise relitigate, in the existing `docs/adr/` numbering.
- No feature code was written; no ADR was contradicted; no product question was decided.
- What could not be verified mechanically is listed as unverified, not asserted as done.

## It's working if

- A new engineer reads `docs/architecture/<slug>.md` and can say what they may and may not touch, without asking anyone.
- A builder who wants to do the wrong thing is stopped by CI in under a minute, not by a reviewer in two days.
- The change that used to touch six packages now touches one, because the boundary followed the axis of change.
- The core got smaller this sitting, and something moved out of it.
- Someone proposes deferring a database, framework, or service decision, and the record already has it deferred with a trigger.
- The domain tests run with no database and no web server, and they are fast.
- Two teams can ship in a week without a joint release, because the seam between them was committed before both sides cut.
- A year from now, the shape is still recognisable in the code — and where it is not, the drift is visible in a failing build rather than in someone's memory.
