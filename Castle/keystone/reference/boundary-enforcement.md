# Boundary Enforcement, Ports, and Fitness Functions

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

