---
name: keystone
description: System architecture, aggregate boundaries, context mapping, fitness functions, and structural stress tests.
disable-model-invocation: true
---

# Keystone

Keystone sets architectural boundaries, context maps, domain aggregates, dependency rules, and fitness functions for systems.

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
13. **This skill does not own product questions and does not own taste.** A new product fork is a cuecards card. How it looks is heraldry. Whether the math works is siegecraft. Whether the wall stands at ten times the load — capacity, latency, the scale verdict on a proposed design — is rampart (Inquest).

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


## Core Lifecycle

`
[Survey & Map: architecture.md] -> [Distill & Aggregate] -> [Enforce: Fitness Functions] -> [Stress Test: stress.md]
`

1. **Survey & Context Mapping**: Read existing code, identify axes of change, and map bounded contexts.
2. **Distillation & Aggregates**: Define the core domain model and transactional consistency boundaries.
3. **Boundary & Port Enforcement**: Fix the dependency rule (inward dependencies only) and define ports owned by core.
4. **Stress Testing & Review**: Apply perturbations across axes of change and record in docs/architecture/<system>-stress.md.

## Artifact Contracts

### Architecture Record (docs/architecture/<system>.md)
`markdown
# Architecture: <system or subsystem name>
## Provenance
## Destination and forcing constraints
## Context map
### Context: <name>
## Distillation
## Aggregate boundaries
### Aggregate: <root name>
## Dependency rule
## Component structure
## Ports the core owns
## Deferred decisions
## Fitness functions
## Stress test
## Open structural questions
`

### Stress Test Record (docs/architecture/<system>-stress.md)
`markdown
# Stress Test: <system or subsystem name>
Tested against Architecture commit: <sha>

## Scenario 1: <Axis of Change>
- **Perturbation**: <What changes 10x or shifts fundamentally>
- **Blast Radius**: <Which contexts/modules are touched>
- **Result**: PASS | WARN | FAIL
`

## Reference Index

- [reference/architectural-moves.md](reference/architectural-moves.md) - The 12 Architectural Moves from Survey to Hold.
- [reference/survey-and-metrics.md](reference/survey-and-metrics.md) - Survey inputs and Robert C. Martin package metrics ($, $, $).
- [reference/boundary-enforcement.md](reference/boundary-enforcement.md) - Boundary enforcement, ports, and architectural fitness functions.
- [reference/stress-testing.md](reference/stress-testing.md) - 3-violation protocol, stress test questions, and template.
- [reference/smells-and-flags.md](reference/smells-and-flags.md) - Architectural smell catalog, bad vs good comparisons, and red flags.
- [reference/operations-and-tone.md](reference/operations-and-tone.md) - Board operations, stopping rules, tone, and approval bar.
- [reference/component-principles.md](reference/component-principles.md) - Component cohesion and coupling principles (REP, CRP, CCP, ADP, SDP, SAP).
- [reference/context-maps.md](reference/context-maps.md) - DDD context mapping patterns (Shared Kernel, Customer/Supplier, Anti-Corruption Layer).
- [reference/tactical-patterns.md](reference/tactical-patterns.md) - Tactical DDD patterns (Entities, Value Objects, Aggregates, Domain Events).
