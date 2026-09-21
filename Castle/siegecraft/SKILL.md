---
name: siegecraft
description: "Use when an implementation ticket is algorithm-heavy, mathematically complex, or prone to edge-case bugs. Use to research primary sources, establish formal correctness arguments, write algorithm specifications, and split complex logic into checkable tickets. Do not use to decide product scope (cuecards) or write application feature glue (oneslice)."
disable-model-invocation: true
---

# Siegecraft

Design algorithm specifications with formal correctness arguments and primary-source research before implementing code.

When an engineering task is mathematically complex or algorithm-heavy, guessing during implementation leads to subtle bugs. Siegecraft scouts primary sources, writes formal specifications (`docs/siegecraft/<slug>-spec.md`), and decomposes complex tasks into smaller tickets each with a verifiable test.

Announce at start: `Using siegecraft to [scout | verify-problem | design-spec | split-tickets | verify | stop].`

## Hard gates

1. **No decided ticket, no spec.** Requires an established handoff slice or ticket from cuecards before formulating algorithms.
2. **Scout primary sources first.** Never implement complex algorithms from memory. Cite official specifications, textbook proofs, or reference code (see [reference/investigation-dossier.md](reference/investigation-dossier.md)).
3. **Question the premise first.** Verify if the algorithmic challenge can be eliminated by reframing data shapes, caching, or loosening unnecessary constraints.
4. **Formal correctness argument mandatory.** The algorithm specification must include explicit invariants and a termination proof (see [reference/formal-contract.md](reference/formal-contract.md)).
5. **State computational complexity.** Document exact Big-O time and space complexity bounds.
6. **Address numerical precision.** Document floating-point tolerances, rounding modes, and overflow guards when numerical calculations are involved.
7. **Checks must be capable of failing.** Verification tests must catch naive or incorrect implementations (see [reference/check-design.md](reference/check-design.md)).
8. **Do not write product feature code.** Siegecraft produces research dossiers, algorithm specs, and split tickets — not application code.
9. **ADRs are law.** Specifications must respect decisions in force. Changes to product behavior require cuecards.
10. **Unverified sources cannot be load-bearing.** If a source cannot be verified, the algorithm cannot depend on it.

## Workflow

1. **Scout Primary Sources:** Search official RFCs, papers, and reference implementations. Compile findings in `docs/research/<slug>-dossier.md`.
2. **Evaluate Problem Premise:** Check if algorithmic complexity can be simplified by reframing data structures.
3. **Formulate Algorithm Specification:** Write contracts, pseudo-code, correctness proofs, and complexity bounds in `docs/siegecraft/<slug>-spec.md`.
4. **Split into Child Tickets:** Decompose large algorithms into discrete, sequentially checkable units.
5. **Verify Check Criteria:** Ensure every child ticket includes test cases with known mathematical solutions.
6. **Hand off to Implementation:** Pass split tickets to oneslice or lanes for coding.

## Split Ticket Template

Format child tickets for complex algorithmic components:

```markdown
## Algorithm Ticket N of M: <Spoken Name>

### What this ticket does
<One clear paragraph describing this algorithmic phase>

### Contract Inherited
- **Specification:** [docs/siegecraft/<slug>-spec.md](docs/siegecraft/<slug>-spec.md)
- **Invariants:** <Guaranteed pre- and post-conditions>

### Check
- **Verification test:** `npm test tests/algo-part-N.test.ts`
- **Pass criteria:** Confirms mathematical invariants against known analytical solutions.

### Tracking
- **Parent ticket:** #<number>
- **Depends on:** Ticket N-1
```

## Reference guides

- [reference/investigation-dossier.md](reference/investigation-dossier.md) — Primary source standards, citation methods, and dossier format.
- [reference/formal-contract.md](reference/formal-contract.md) — 11-section algorithm specification template.
- [reference/check-design.md](reference/check-design.md) — Test case design, analytical solutions, and ticket splitting.
