# Ticket Splitting and Sequencing

# Decompose tickets (rewrite and split the tickets)

The spec is committed. Now the board learns about it. The live tracker is GitHub issues on the current repo, same as cuecards and oneslice. If `gh` cannot see this repo, say so, use the local fallback, and never pretend issues exist.

## When to split

Split when the engine has parts that are **independently checkable** — each child can pass or fail on its own named Check:

- the parts land in different sittings (oneslice builds one ticket per sitting);
- the parts can move in parallel later (lanes can run them as lanes);
- a part is reusable by other tickets (a parser, a distance oracle, a solver core);
- the whole would force one sitting to swallow the entire wall.

Do **not** split to look busy. One Check scattered across three tickets is one ticket badly written — merge it back. Every split must survive the question: *can a builder prove this child alone, without re-deriving the math?*

## Ticket shape

Every ticket the split produces — two layers, in this order:

```markdown
## Engine ticket N of M: <spoken name>

**For the board:** <one plain sentence anyone can read.>

**Builds:** [Engine: <name>](docs/siegecraft/<slug>.md) §3 step 2–4
**Researched in:** [Dossier](docs/research/<slug>.md)
**Honors:** [ADR-NNNN Title](docs/adr/NNNN-slug.md)

### What this ticket does
<precise and technical. The audience is the builder; jargon is correct here —
it is the point. The spec section carries the math; this body carries what
the builder must do with it and what must not drift.>

### Contract inherited
<preconditions / postconditions / invariants this ticket must preserve, from spec §2>

### Check
<from spec §10 — concrete and runnable: known-answer vectors (source, anchor),
differential vs the naive baseline at n ≤ 12 plus 10k random cases, property
test on a named invariant, or a measured threshold with the number>

### Blocked by / Blocks
<names, plus native edges>
```

The board line stays spoken English — Castle voice, the same as cuecards. The body is where the rigor lives. Both are true at once; that is the design.

## The split, in order

1. **Commit the dossier.** Then **commit the spec.** Then touch the issues. A ticket citing an uncommitted spec is the defect oneslice's gate 14 names, one layer up.
2. **Create the child tickets** with the shape above. Labels: `siegecraft`, `engine`, plus priority (`now` / `next` / `later`). Sub-issue them to the parent.
3. **Wire the edges** — native blocked-by plus the Blocked by / Blocks lines — so the frontier is visible where the code and CI are.
4. **Rewrite the parent into an index**: the wall in one line, the spec, the dossier, every child with the spec section it implements, the frontier. Close it as superseded-by-index or keep it as the index — never two live descriptions of the same work.
5. **Update the board** (if a cuecards board exists): the affected Ready now / Waiting lines, and Notes → Consult gains the spec path. The engine is context for every later card in this area.
6. **Comment on each touched ticket** in the same voice, linking spec and dossier paths, and say what changed and why. Then **stop**.

`docs/` layout this skill owns:

```text
docs/research/<engine-slug>.md     # the dossier — primary-source evidence
docs/siegecraft/<slug>.md          # the engine spec
```

Only if GitHub is impossible: `.siegecraft/<slug>/BOARD.md` as local fallback for the issue state. The spec and dossier are repo files either way — they are not issues.

---

# Bad vs good

Bad ticket body: "Implement the recommendation engine. Should be fast."
Good body: "Rank candidates by score S(u,i) = Σ w_k · sim_k, per spec §3 step 2; ties broken by lower id (§3 determinism note). Contract: no candidate set may be mutated (§2 invariant I2). Check: differential vs the naive full-scan baseline on all n ≤ 12 inputs, 10k random cases, exact match; plus the known-answer vector from the dossier F3."

Bad cost claim: "It's O(n log n), so it's fine."
Good cost claim: "O(n log n) comparisons — CITED (Bentley & McIlroy 1993, §4). At the measured 180 ns/item on the reference (dossier F3, measured this sitting at n = 2M events/day): ~0.36 s/day against a 5 s budget. The rejected O(n²) alternative costs 4.6 hours/day at the same n."

Bad novelty: "We invented a new algorithm!"
Good novelty: "Cited engines fail at our n: A needs O(n²) memory (n = 2M ⇒ ~4 TB), B is approximate with error up to 5% (contract §1 demands exact). So the engine is a composition: their streaming core (CITED, paper §3.2) under an exact reconciliation pass (DERIVED — induction over the merge invariant, spec §4)."

Bad Check: "Tests pass."
Good Check: "Differential: engine vs naive baseline, exact match on all n ≤ 12 inputs and 10k random cases. Known-answer vector from the spec's own test suite (dossier F1, file+line). Property: output is always a permutation of the eligible set (property test pinned in spec §10)."

Bad scout: "I know this algorithm, everyone uses it."
Good scout: "The guarantee is CITED from the original paper §2 (author copy linked), and the reference implementation's actual behavior at the edges is CITED from its tests (repo @ commit, path). The blog I found first is a signpost, not in the dossier."

---

# Red flags

| Thought | Reality |
| --- | --- |
| "I know this algorithm" | From memory is from a blog. Cite the owner, or mark UNVERIFIED and de-load it. |
| "The paper is paywalled, the summary will do" | The summary is a signpost. Find the author copy, the reference code, or redesign around the hole. |
| "It's obviously correct" | Then the one-paragraph induction writes itself. Write it. |
| "Big-O is enough" | Constants at the real n decide. Estimate from data or measure. |
| "Novel sounds better" | Novel is a cost. Cited where it fits, invented where the cited ones provably fail, proven either way. |
| "I'll add the derivation after filing the tickets" | Dossier → spec → tickets, in commit order. Every other order is a defect. |
| "The ticket got too technical" | The body's audience is the builder. Keep the board line plain instead. |
| "Nine tickets shows rigor" | Each child needs its own checkable Check. Scatter is not rigor. |
| "The Check can't really fail" | Then it is decoration. Vector, differential, property, or threshold — pick one that breaks. |
| "The fast engine contradicts the ADR, but only slightly" | Stop. Name the ADR. Cuecards sitting, not a workaround. |
| "I'll just build it, the engine is clear in my head" | Clear in your head is worth zero to the next builder. Spec it or you have left the skill. |
| "The README and the code disagree; I'll cite the README" | The code ships. Say which wins and why, and verify against a test. |

---

