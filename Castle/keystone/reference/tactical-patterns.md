# Tactical building blocks

> Reference for [keystone](../SKILL.md). The short version of each DDD block, with the
> rule that actually matters, and the supple-design checklist that separates a working
> domain model from a good one.

| Block | The rule |
| --- | --- |
| **Entity** | Distinguished by identity, not attributes. Keep the definition focused on life-cycle continuity and identity. Beware requirements that match objects by attributes — that is usually a value object or a specification. |
| **Value object** | Care only about attributes → immutable, no identity, conceptually whole. Whole Value: `street, city, postalCode` is one `Address`, not three fields. Immutability is what makes sharing safe and combination cheap. |
| **Aggregate** | See gate 5 and move 5. Root controls access; invariants hold at commit. |
| **Domain service** | A significant process or transformation that is not a natural responsibility of an entity or value object. Stateless. Named after an activity from the domain language, not `XHelper`. If you need one for every other operation, your entities are anemic. |
| **Module** | Choose modules that tell the story of the system and contain a cohesive set of concepts. Names become part of the ubiquitous language. Low coupling is the goal; if you cannot get it, the model is wrong — look for the overlooked concept. |
| **Repository** | Provide the illusion of an in-memory collection of aggregate roots. Reconstitution, not querying convenience. Only for roots that genuinely need direct access. Encapsulate the storage and query technology completely. |
| **Factory** | Shift complex assembly — especially whole aggregates — to a separate object that enforces the invariants on creation and does not require the client to name concrete classes. |
| **Domain event** | A record of something that happened, in domain language, published because another part of the system or another context must react. Not a message queue; the queue is an adapter. |
| **Specification** | An explicit predicate value object: "does this object satisfy the criteria." Combine with logical operators when the rules get complex. Keeps rule knowledge out of the caller and out of the repository. |

**Supple design** — the checklist that separates a working domain model from a good one:

- **Intention-revealing interfaces** — name classes and operations to describe effect and purpose, not mechanism. Write the test first; it forces client-developer mode.
- **Side-effect-free functions** — push logic into functions that return results with no observable side effects. Segregate commands into simple operations that return no domain information. Complex logic belongs in value objects, where it is safe to combine.
- **Assertions** — state post-conditions and invariants explicitly. Where the language cannot express them, they become unit tests; where they cannot be tested, they become documentation. Either way, write them down.
- **Conceptual contours** — decompose along the axes of change and stability the domain actually has. Stable, coherent units; no irrelevant options. This emerges from refactoring toward insight, not from a technically-motivated cleanup.
- **Standalone classes** — minimise dependencies on other concepts. Low coupling is a design goal in itself, not a side effect.
- **Closure of operations** — where it fits, an operation whose return type is the type of its arguments. A high-level interface with no dependency on other concepts.
- **Declarative design** — a style where the specification of *what* drives the system and the *how* is delegated to a mechanism behind an intention-revealing interface. Feasible only where the mechanism is genuinely well understood; otherwise it is a trap of indirection.

---

