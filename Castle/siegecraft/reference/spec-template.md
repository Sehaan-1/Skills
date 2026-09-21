# Algorithm Specification Template

# Design the engine (the spec)

The spec is the artifact: `docs/siegecraft/<slug>.md`. Precise enough that the builder of any ticket it produces never has to invent math. Short enough that the builder actually reads all of it. No implementation language — pseudo-code and exact statements are welcome; a code dump is not the deliverable.

```markdown
# Engine: <spoken name>

- **Status:** proposed | accepted | implemented
- **Date:** YYYY-MM-DD
- **Wall:** <one line — what was too hard, under what constraint>
- **Tickets:** [<parent>](url) → <children>
- **Dossier:** [docs/research/<slug>.md](../research/<slug>.md)
- **ADRs honored:** [ADR-NNNN Title](../adr/NNNN-slug.md), …

## 1. Problem, formally
Inputs (types, sizes, distributions), outputs, and the exact success condition.
If approximate: the tolerance as a number, and the metric it is measured in.

## 2. Contracts
Preconditions, postconditions, invariants. What the engine refuses loudly.
No silent fallbacks: a precondition failure is a crash with a message, not a guess.

## 3. The engine
The algorithm, step by step: data structures, the loop, the update rule,
the termination condition, tie-breaking, determinism guarantees.
Exact where exactness is the point; named primitives where one is used.

## 4. Why it is correct
CITED steps: the owner, at an anchor, and what it guarantees.
DERIVED steps: the argument — loop invariant + induction, reduction to a
cited-correct primitive, or exhaustive small cases.
The counterexample hunt: what you tried to break it with, and why it holds.

## 5. Cost
Time and space: best / typical / worst, amortized where it matters — in the table,
then at the real n with real constants. Where the constants come from: cited
benchmark, measured this sitting (dossier link), or arithmetic from those.

## 6. Numbers (if the math is real)
Representation (integer / float / fixed / rational), IEEE-754 realities,
conditioning, error accumulation and summation order, comparison epsilons,
overflow and its trigger. If exactness is required: the exact method.
Known-answer vectors lifted from the sources.

## 7. Edges and failures
Empty, one, many, huge, adversarial. Untrusted input at the boundary.
What happens when each precondition fails — loud, per the contract.

## 8. Alternatives the sources offer
2–4 real candidates with owner citations, why each was rejected, and at what
cost. The naive baseline is always on this list — it is the differential
oracle for the Check.

## 9. Novelty
What is cited, what is composed, what is genuinely new. For each new piece:
why the cited ones fail (with the citation), and the proof burden it carries.
If nothing is new, say so: fitting a known engine well is a fine outcome.

## 10. Check (for the builder)
How each claim becomes a failing test: known-answer vectors from the sources,
differential vs the naive baseline at small n, property tests on the
invariants, measured thresholds with numbers. Tickets point into this section.

## 11. Open risks
What could still sink this, and what would signal it early.
```

### Rules for the spec

- **CITE and DERIVE inline.** Every load-bearing line is one or the other. UNVERIFIED carries nothing.
- **Naive baseline always.** The simplest correct engine is on the alternatives list even when rejected — it is what the implementation gets differentially tested against.
- **Determinism is decided here.** Tie-breaking, ordering, iteration order — specified, not left to the builder's mood.
- **Numbers are honest.** Measured numbers carry their machine and date; estimates say they are estimates.
- **Engines are not ADRs.** The spec is the citable record for engineering. When an engine decision closes a *card* other cards must honor, cuecards writes the ADR and the ADR cites the spec by name and path.

---

