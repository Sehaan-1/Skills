# Formal Algorithm Specification

The algorithm specification is the bridge between theoretical mathematics and production code. It must be precise enough that implementing engineers do not need to invent mathematical formulas mid-task.

Location: `docs/siegecraft/<slug>-spec.md`

## Specification Structure (11 Sections)

```markdown
# Algorithm Specification: <Problem Name>

- **Status:** proposed | accepted | implemented
- **Date:** YYYY-MM-DD
- **Problem Statement:** <one-sentence summary of algorithmic challenge>

## 1. Problem Definition (Formal)
- Inputs, outputs, data domain, and formal types.

## 2. Invariants & Contracts
- Pre-conditions: what must hold before execution.
- Post-conditions: guaranteed guarantees on return.
- Loop/State invariants: properties maintained across each step.

## 3. Core Algorithm
- Step-by-step logic in precise pseudo-code.
- Deterministic behavior and state transition definitions.

## 4. Correctness Argument
- Induction base case and inductive step.
- Termination proof: bounded monotonic variant function ensuring termination.

## 5. Computational Complexity
- Time complexity: best, average, and worst-case Big-O notation.
- Space complexity: auxiliary heap and stack allocations.

## 6. Numerical Precision & Error Bounds
- Floating-point tolerances, rounding modes, overflow prevention, and stability.

## 7. Edge Cases & Known Failure Modes
- Degenerate inputs (empty sets, zeroes, collinearity, duplicate values).

## 8. Prior Art & Alternatives
- Established standard algorithms evaluated and reasons for rejection.

## 9. Novel Derivations
- Explicitly mark any non-standard mathematical formulation as `DERIVED`.

## 10. Check Criteria
- Concrete verification test cases with known mathematical solutions.

## 11. Open Risks
- Remaining performance limits or hardware assumptions.
```
