# Architectural Survey and Package Metrics

## 1. Survey â€” read the ground before you draw

Six inputs. Estimate from evidence, not from plans.

1. **The domain**, in the language the people who work in it actually use. Collect the nouns and verbs they correct you on. That correction is the model trying to get out.
2. **The forces.** Team topology and count. Deploy cadence. Consistency requirements per use case â€” which ones must be right now, and which can be right in a second, an hour, or overnight. Regulatory and data-residency constraints. Scale envelope (orders of magnitude, not exact numbers). Latency and availability budgets.
3. **What exists.** Run the tools. Count the cycles. Get the metric table. Read the module graph before you read any document about it.
4. **The change log.** Where did the last twenty non-trivial changes land? That is the real architecture; the source tree is the aspirational one. Clusters in the change log are candidate components.
5. **The pain.** Which change is expensive? Which test suite is slow and why? Which deploy is scary? Pain points at a seam.
6. **The people.** Who knows which part? Knowledge boundaries and model boundaries drift apart, and when they do, the code follows the people.

Output: a paragraph, out loud â€” what this system is, the two or three forces that will actually decide its shape, and where it currently hurts.


---

## 7. Choose the packaging, and lose the argument honestly

Four ways to organize code, and the differences between them evaporate if you get the access modifiers wrong. If everything is public, packages are folders â€” decoration. Encapsulation is what makes a boundary real, and access control is what makes encapsulation real.

| Style | Shape | Buys you | Costs you |
| --- | --- | --- | --- |
| **Package by layer** | Horizontal: `web`, `service`, `repository` | Fast to start, familiar to everyone | Screams nothing about the domain; every cross-cutting change touches three packages; easy to cheat by skipping a layer and still have an acyclic graph |
| **Package by feature** | Vertical slices by feature, concept, or aggregate root | The top level screams the domain; one place to go for one change | Still no enforced boundary â€” the controller is the only truly public thing, or nothing is |
| **Ports and adapters** | Inside (domain) / outside (infrastructure); outside depends on inside | Domain code with no framework in it; testable without I/O; language named after the domain, not the persistence | Marshalling across boundaries; more files; easy to leak a detail through a poorly drawn port |
| **Package by component** | All responsibilities for one coarse-grained component behind one interface, in one package | One place to go, **and** the compiler enforces the boundary â€” internals are not public | Coarser than you'd like for very large components; a stepping stone to services, not a substitute |

Choose with the cohesion principles â€” REP, CCP, CRP â€” and say which one you are
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

- **(0, 0) Zone of Pain** â€” stable and concrete: rigid, hard to extend, hard to change. A database schema lives here, which is exactly why schema changes hurt. Volatile concrete components here are the painful ones.
- **(1, 1) Zone of Uselessness** â€” maximally abstract with no dependents: leftover abstractions nobody implemented.
- **The Main Sequence** â€” the line from (1, 0) to (0, 1). Most components should sit near it; the very best sit at its endpoints.

A table of six components with I, A, and D, plus a cycle count, is worth more than four diagrams. If you cannot produce it, install the tool first â€” that is a legitimate first move.

