# The Twelve Architectural Moves

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
costs, and how it breaks, live in [context-maps.md](context-maps.md).
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
[component-principles.md](component-principles.md).

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
[component-principles.md](component-principles.md).

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

