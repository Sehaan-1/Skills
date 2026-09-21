---
name: keystone
description: "Use when the shape of a system has to be decided or defended: where boundaries are, which way dependencies point, what is core and what is detail, how code is packaged, which contexts integrate and how, and where transaction boundaries fall. Do not use to decide product questions (cuecards) or build features (oneslice)."
disable-model-invocation: true
---

# Keystone

Define and enforce the structural shape of a software system.

Architecture is the division of a system into components, the arrangement of those components, and the ways they communicate. Its purpose is to keep systems cheap to develop, deploy, operate, and change. Keystone produces the structural boundaries that all implementation skills must respect.

Announce at start: `Using keystone to [survey | cut | map | distill | set | enforce | stress | record | hold].`

## Hard gates

1. **No handoff, no shape.** Requires clear destination goals, handoff document, and ADRs from cuecards before drawing boundaries.
2. **Boundaries follow axes of change.** Separate components that change at different rates or for different reasons.
3. **The dependency rule is absolute.** Source code dependencies point strictly inward toward higher-level domain policies.
4. **One model per bounded context.** Terminology and rules must be consistent within each context. Where contexts touch, explicitly define the integration pattern (see [reference/context-maps.md](reference/context-maps.md)).
5. **Invariants live inside one aggregate.** Enforce business invariants synchronously inside aggregate roots. Across aggregates, use eventual consistency (see [reference/tactical-patterns.md](reference/tactical-patterns.md)).
6. **Policy first, details deferred.** Databases, web frameworks, and messaging transports are implementation details. Keep domain policies agnostic of them.
7. **Every structural rule must be mechanically checked.** Automated fitness functions in CI must fail the build when boundaries are violated (see [reference/boundary-enforcement.md](reference/boundary-enforcement.md)).
8. **Do not implement feature logic.** Keystone creates boundary scaffolding, port interfaces, and fitness tests — not business feature code.
9. **ADRs are law.** Honor existing decisions. Changing a structural decision requires superseding ADRs via cuecards.
10. **Measure before asserting.** Calculate real coupling metrics ($I$, $A$, $D$) and count dependency cycles (see [reference/survey-and-metrics.md](reference/survey-and-metrics.md)).
11. **Document deferred decisions.** State why a technical choice can wait, the trigger that ends deferral, and the cost to change later.
12. **Deliberate stress testing required.** Attempt three deliberate structural violations and verify that the fitness functions fail (see [reference/stress-testing.md](reference/stress-testing.md)).

## Workflow

1. **Survey:** Gather real forces, change-log clusters, coupling metrics ($I$, $A$, $D$), and cycle counts.
2. **Cut:** Identify axes of change and separate domain policy from infrastructure details.
3. **Map:** Define bounded contexts and assign explicit integration patterns (Shared Kernel, ACL, Customer/Supplier).
4. **Distill:** Separate core differentiating domain from supporting and generic subdomains.
5. **Aggregates & Ports:** Establish aggregate roots and transactional consistency boundaries. Define port interfaces owned by the core.
6. **Enforce:** Write fitness functions (`dependency-cruiser`, `ArchUnit`, import linters) wired to CI.
7. **Stress:** Execute three deliberate violations to confirm automated checks catch them.
8. **Record:** Save architecture record to `docs/architecture/<slug>.md` and record structural ADRs.

## Architecture Record Template

Record the structural contract at `docs/architecture/<slug>.md`:

```markdown
# Architecture: <System / Subsystem>

## Destination & Forcing Constraints
- **Goal:** <from cuecards handoff>
- **Forces:** Deploy cadence, team topology, latency envelope, data consistency

## Context Map
- Contexts, boundaries, and relationship patterns (ACL, Open Host, etc.)

## Distillation
- **Core Domain:** <differentiating value>
- **Supporting / Generic Subdomains:** <buy, adopt, or isolate>

## Aggregate Boundaries
- Aggregate roots, internal entities, transactional invariants, repository ports

## Dependency Rule & Ports
- Dependency levels (Domain -> Use Cases -> Adapters -> Infrastructure)
- Ports owned by the core: Persistence, Presenters, External Services

## Deferred Decisions
| Decision | Why Deferred | Trigger to Resolve | Cost to Change Later |

## Fitness Functions
| Rule | Check Tool | CI Command | Status |
| --- | --- | --- | --- |
| No infrastructure in core | linter/arch-test | `npm run test:arch` | enforced |
```

## Reference guides

- [reference/survey-and-metrics.md](reference/survey-and-metrics.md) — Six survey inputs, coupling metrics ($I, A, D$), and code smells.
- [reference/boundary-enforcement.md](reference/boundary-enforcement.md) — Fitness functions, ports and adapters, and humble objects.
- [reference/stress-testing.md](reference/stress-testing.md) — Protocol for verifying architectural checks with deliberate violations.
- [reference/context-maps.md](reference/context-maps.md) — The 7 bounded context integration patterns.
- [reference/tactical-patterns.md](reference/tactical-patterns.md) — Aggregates, value objects, entities, and repositories.
- [reference/component-principles.md](reference/component-principles.md) — SOLID, component cohesion (REP, CCP, CRP), and coupling (ADP, SDP, SAP).
