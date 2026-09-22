---
name: siegecraft
description: Deep-problem algorithmic specification, primary source research dossiers, impossibility passes, and two-layer ticket decomposition.
disable-model-invocation: true
---

# Siegecraft

Siegecraft tackles hard, novel, or algorithmic problems: conducts primary source research, runs impossibility checks, authors rigorous algorithm specifications, and decomposes implementations into verifiable tickets.

## Hard gates

1. **No decided task, no engine.** A ticket, a closed card, a cited ADR, a handoff slice, or an explicit human ask names the wall. A product question still open is a cuecards card, not an engine. If you catch yourself choosing *what the product should do*, you have left the skill. Order-of-magnitude sizing is rampart's (Inquest); when a number must be provably right, it is an engine, and engines are this skill's.
2. **Scout before you design.** The dossier exists before the spec; the spec is committed before any ticket is rewritten. No engine from memory. No algorithm because a blog, a summary site, or a training recollection said so.
3. **Primary sources own their facts.** Official docs, specs and standards, the original paper, the reference implementation's code and tests, first-party APIs. A secondary write-up is a signpost to the primary, never a citation. Follow every claim back to the source that owns it.
4. **No product code.** Output is the dossier, the engine spec, and tickets. Measurement you run as research is recorded in the dossier; scratch scripts stay out of the tree. If you are opening a source file to add a feature, you have left the skill.
5. **ADRs are law.** Cited ADRs for this task are closed decisions. If the best engine contradicts one, stop and name the ADR — that is a cuecards sitting, not a clever approximation.
6. **The engine carries its own proof.** Every load-bearing step is CITED to its owner or DERIVED with the derivation written down: loop invariant plus induction, reduction to a cited-correct primitive, or an exhaustive small-case argument. "It is a well-known algorithm" with no citation is programming by coincidence, and a spec that does it is a defect.
7. **Cost is a number, not a vibe.** Complexity in the table, then the same complexity at the *real* n with real constants. Best is not always best; an O(2^n) engine is fine at n = 12 and catastrophic at n = 2M. No estimate without data: a cited benchmark, a measurement this sitting, or honest arithmetic from both.
8. **Novelty is earned, then proven.** Cited where the sources fit; invented only where they run out; the invention carries the heavier proof burden. Novel is a cost you justify, not a feature you decorate with.
9. **Hard math says so out loud.** When numbers are load-bearing — floats, conditioning, accumulation, overflow, exactness — the spec has a numerics section. An engine whose correctness dies at IEEE-754 boundaries is not done.
10. **Every ticket can fail.** Each ticket the split produces carries a Check that would catch a wrong implementation: known-answer vectors from the sources, differential against a naive baseline, property tests on the invariants, measured thresholds with numbers. A Check that cannot fail is decoration.
11. **Two-layer tickets.** One spoken line for the board, rigorous technical body for the builder. Jargon is correct where the audience is technical — that is the point of this skill — but the board line stays plain and never a bare `#42`.
12. **Splits keep the parent honest.** When one ticket becomes many, the parent becomes an index of the children with native blocked-by edges and a pointer into the spec per child. A parent still describing the old monolithic work is a lie on the board.
13. **Stop at the spec.** No branch, no slice, no "while I'm here." The engine spec, the dossier, and the tickets are the whole output. The next sitting is oneslice's.

<!-- ── PROVENANCE GATES (a claim is not a derivation) ────────────────────── -->

14. **Dossier committed before tickets change.** You may not rewrite a ticket body to
    assume a fact unless the dossier citing that fact's owner is already committed —
    same commit or earlier. The order is strict: dossier commit → spec commit → issue
    edits. A commit message that says "research TBD" or "will verify later" is a defect.
    The comment that records the ticket update links the dossier path and the spec path.

15. **Mark every load-bearing claim CITED or DERIVED.** CITED → the owner, at an exact
    anchor: doc section, paper section, spec clause, or the reference implementation's
    file and line. DERIVED → the derivation, in the spec, worked — not asserted. An
    engine whose key steps are neither is a fabricated design. Do not file it.

16. **No self-certified correctness.** "Verified correct" is a claim, not a check. The
    spec's correctness section names the argument *and* the counterexample hunt: the
    inputs you tried to break the engine with, and why they do not. If the engine cannot
    be fully checked this sitting, the tickets say `Engine: spec only — check unbuilt`
    out loud. An admitted gap is honest; a claimed proof is fabrication.

17. **Split provenance.** When a ticket is split, the new parent body links every child,
    the spec section each child implements, and the check each child inherits. The
    original ticket is rewritten into that index or closed as superseded by it — never
    left as a second live description of the same work.

<!-- ──────────────────────────────────────────────────────────────────────── -->


## Core Lifecycle

`
[Aim & Research: dossier.md] -> [Impossibility Pass] -> [Algorithm Spec: spec.md] -> [Ticket Decomposition]
`

1. **Aim & Primary Source Research**: Anchor on primary literature and reference implementations. Record in docs/siegecraft/<slug>-dossier.md.
2. **Impossibility Pass**: Stress-test assumptions and establish bounds before designing algorithms.
3. **Algorithm Specification**: Write the 11-section engine spec with formal contracts, invariant proofs, and cost bounds (docs/siegecraft/<slug>-spec.md).
4. **Ticket Decomposition**: Decompose the spec into two-layer implementation tickets with explicit check steps.

## Artifact Contracts

### Research Dossier
`markdown
# Dossier: <the question, in one sentence>
## Sources consulted
## Findings
### F1. <claim>
## Measured
## Unverified
## Contradictions
`

### Algorithm Specification
`markdown
# Engine: <spoken name>
## 1. Problem, formally
## 2. Contracts
## 3. The engine
## 4. Why it is correct
## 5. Cost
## 6. Numbers (if the math is real)
## 7. Edges and failures
## 8. Alternatives the sources offer
## 9. Novelty
## 10. Check (for the builder)
## 11. Open risks
`

## Reference Index

- [reference/aim-and-impossibility.md](reference/aim-and-impossibility.md) - Aiming criteria, hard problem boundaries, and the impossibility pass.
- [reference/scout-and-dossier.md](reference/scout-and-dossier.md) - Primary source research rules, findings documentation, and dossier template.
- [reference/spec-template.md](reference/spec-template.md) - Full 11-section algorithm engine specification template and rules.
- [reference/splitting-tickets.md](reference/splitting-tickets.md) - Ticket splitting discipline, two-layer tickets, sequencing, and quality flags.
- [reference/operations-and-tone.md](reference/operations-and-tone.md) - GitHub board operations, stopping rules, tone, and approval bar.
