---
name: siegecraft
description: "Use when a decided ticket, card, or handoff slice is genuinely algorithm-hard and the math is the risk: optimization, search, scheduling, parsing, geometry, matching, compression, simulation, statistics, cryptography, constraint solving. Use when a task needs a researched or novel algorithm designed before anyone builds, when a builder would otherwise invent math mid-slice, when tickets must be rewritten or split into highly technical sub-tickets, or when the user asks for siegecraft, an engine, or algorithm research. Does not implement (oneslice), ship (lanes), decide product (cuecards), or design interfaces (heraldry)."
disable-model-invocation: true
---

# Siegecraft

The wall is too high for ladders. Sending the same riders at the same gate is not a plan. A siege is won before the first stone moves: someone walks the ground, reads the wall, and designs the engine that makes the assault takeable. The engine is not the assault. It is what makes the assault possible.

This skill is that idea, applied to the hardest tickets on the board. Take a decided task whose difficulty is genuinely algorithmic. **Scout it first**: investigate the question against **primary sources** (official docs, source code, specs, papers, first-party APIs), not a secondary write-up of them — follow every claim back to the source that owns it. Then derive the **engine**: a precise algorithm with a formal contract, a correctness argument, and a cost model at the real input sizes, mathematical where the math is real. Rewrite the ticket so it carries the engine, and split it into more tickets when the engine has parts. Commit the spec, update the board, and stop.

**No implementation leaves this skill.** Oneslice cuts code; siegecraft designs the machines.

Cuecards decides *what* to build. Oneslice builds one slice. Lanes ships the destination. Keystone decides the shape everything must not break. Siegecraft exists for the tickets in that pipeline that would otherwise force whoever builds them to invent mathematics mid-slice — from memory, unsupervised, and wrong in ways the tests will not catch until production.

Announce at start: `Using siegecraft to [aim | scout | aim again | design the engine | break the wall | stop].`

## Hard gates

1. **No decided task, no engine.** A ticket, a closed card, a cited ADR, a handoff slice, or an explicit human ask names the wall. A product question still open is a cuecards card, not an engine. If you catch yourself choosing *what the product should do*, you have left the skill.
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

## Sort

Say the path out loud so they can override.

- **Still fuzzy or undecided** — cuecards. Siegecraft does not decide product, and it does not aim at a moving target.
- **Decided, but the risk is volume, not math** — oneslice. "Algorithm-hard" means the risk is *wrong math*: search, optimization, scheduling, parsing, geometry, matching, compression, simulation, statistics, cryptography, planning, constraint solving. Not "lots of code."
- **Shape of the system is the question** — keystone. If the wall is "where does this live" or "which way do dependencies point", that is architecture, not an algorithm. Keystone first, then siegecraft if a component turns out to have a hard engine inside it.
- **Decided and genuinely hard** — here. One engine spec per sitting. A wall too big for one spec is several walls: split the tickets first, aim again.
- **Sent here mid-build** — oneslice handed back a slice that turned out to be a wall. Read what oneslice already did and what it did not claim, then aim.

When someone says "just implement it": that is oneslice, working from your spec. If no spec exists and the ticket is algorithm-hard, they asked for the wrong skill first. This is the right one.

---

# Aim

Read the ticket, every ADR it cites, the board's Notes and standing rules, the handoff slice if one exists, and any look-card proof it depends on. Then name the wall in one line:

> The wall: <what is too hard> under <the constraint that makes it hard>.

Fill in the shape of the problem before you scout:

- **What is decided** — ADRs by name, the destination, the slice Check.
- **The real n** — data sizes, rates, latencies, dimensions. From the ticket, the codebase, or measurement. Not from vibes.
- **The tolerance** — exact, or approximate within a stated bound? "Fast enough" is not a tolerance; a number is.
- **The environment** — memory, single machine or distributed, latency budget, determinism requirements, what language the builder will cut.
- **What "solved" looks like** — the walk and proof this engine must eventually survive.

If you cannot name the wall, the ticket is still fuzzy. Back to cuecards — say so out loud.

---

# Scout (research first, always first)

The engine is only as good as its sources. Spin up a **background agent** (or parallel subagents) for the reading so you can keep aiming and structuring in parallel. If this harness has no background tool, do the research yourself first, write the dossier, then design — do not skip the artifact.

One question per dossier. Two independent unknowns, two dossiers. Reuse an existing dossier instead of investigating the same primary source twice.

## What counts as primary

A source is primary for the claims *it owns*. Match the claim to its owner:

| The claim is about | Its owner | Primary form |
| --- | --- | --- |
| What an API or library does | Its first party | Official docs, the library's own source code, its tests, its changelog and issue tracker |
| What a format, protocol, or primitive means | The spec that defines it | RFC, ISO, ECMA, IEEE, W3C, NIST FIPS, the language reference |
| What an algorithm guarantees | The source that proved it | The original paper, the textbook proof, the reference implementation's code and its tests |
| How fast something really is | Your measurement | A benchmark you ran at your real n, on the reference implementation, output pasted |
| What you derived yourself | You | The derivation, in the spec, marked DERIVED |

A vendor's speed claim is a claim by the vendor until you reproduce it. A README is marketing next to the code that ships. A tutorial, a summary site, a blog post, an AI answer, a wiki: **signposts** — use them to find the primary, never as the citation.

## Rules

- **Follow every claim back to the source that owns it.** Not to someone's write-up of that source. If the chain stops at a summary, keep walking or mark it.
- **Read the reference implementation's source, not just its docs.** The behavior lives in the code and its tests. Where docs and code disagree, say which wins and why — usually the code, until the docs' version is confirmed by the maintainer or a test.
- **Unreachable primary → `UNVERIFIED`, and de-loaded.** If the paper is paywalled, hunt the author's copy, the arXiv version, the conference site, the reference code. If the primary still cannot be reached this sitting, the claim is marked UNVERIFIED in the dossier and **cannot be load-bearing**: the engine is redesigned around the hole, or the sitting stops and says what is missing.
- **Measure as research.** Where cost matters, run the reference implementation on real-scale inputs and paste the real numbers into the dossier: command, machine, date, input sizes. This is an estimate fed with data, not a guess. The recorded output is the artifact; the scratch script is not committed.
- **Never code a foreign shape from memory.** If the engine depends on an API, a format, or a constant, the dossier anchors it to its owner before any ticket assumes it.
- **A finding that contradicts an ADR, the ticket's premise, or the slice Check is a stop** — aim again, or a cuecards sitting. Not a silent product change.

## The dossier

`docs/research/<engine-slug>.md` — the same species as oneslice's research files, heavier. Committed before anything that depends on it.

```markdown
# Dossier: <the question, in one sentence>

- **For engine:** docs/siegecraft/<slug>.md
- **Date:** YYYY-MM-DD · **Researched by:** <agent name>

## Sources consulted
| # | Source | Kind | What it owns | Link / path |
| --- | --- | --- | --- | --- |
| 1 | <RFC 9110 §5.1> | primary spec | <semantic of the field> | <url> |
| 2 | <Author, "Title", venue year, §4> | primary paper | <the guarantee> | <url or local copy path> |
| 3 | <org/repo @ commit, src/thing.ts L120-180> | reference code | <actual behavior> | <permalink> |

## Findings
### F1. <claim>
- **CITED** — <owner, exact anchor>: <what it actually says — quote or tight paraphrase, not a summary of a summary>
- **So what:** <consequence for the engine>

## Measured
<command, machine, date, input size — output pasted>

## Unverified
<claims with no owner reached yet, and why the engine does not rest on them>

## Contradictions
<any two owners disagree; which wins and why>
```

Findings are rewritten so the next reader — the spec, the builder, the next siegecraft sitting — can use them without re-opening the paper. Facts are the scout's job; choices are not.

---

# Aim again (the impossibility pass)

Before designing anything, spend five minutes trying to dissolve the wall. The hardest-engineered solution to a mis-stated problem is still the wrong answer.

1. **Is there an easier way?** Does the task secretly not need this? Is a dumber engine, run at a different time, indistinguishable at the real n?
2. **Question the premise.** Try each constraint on for size. Is n really 10^7 — measured, or assumed? Is exactness really required, or is a stated error bound acceptable? Is the deadline real? Is the data actually adversarial, or just big?
3. **Dig under the ticket.** The stated method is often one dig too shallow. What is the ticket *for*? Would a reformulation — different coordinates, precompute once and amortize, stream instead of batch, trade memory for time — serve the same need for a tenth of the engine?
4. **Renegotiate the shape, not the destination.** If one line changed in the ticket collapses the wall — a tolerance, a precompute step, a weaker guarantee that nobody would notice — that is a *decision*. Take it back to the board as a cuecards card with your recommendation. Do not silently weaken what was decided.

The pass ends one of two ways: **the wall stands** (proceed to design), or **the wall moves** (back to the board, with a card). Say which, out loud.

---

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

# Break the wall (rewrite and split the tickets)

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

# Board operations (GitHub)

Use `gh` in the current repo; `{owner}/{repo}` from `gh repo view --json nameWithOwner -q .nameWithOwner`. The create / sub-issue / blocked-by calls are the same ones cuecards' Board operations uses — reuse that skill's exact `gh api` incantations rather than inventing variants.

- Labels to create if missing: `siegecraft`, `engine` (plus the shared `now` / `next` / `later`).
- Split: `gh issue create` per child → sub-issue under the parent → native `blocked_by` edges.
- Report: comment on the original ticket — wall, engine name, spec path, dossier path, children by name — then rewrite it as the index.
- Frontier query: open, label `engine`, blockers closed, `now` before `next` before `later`.

Say out loud when falling back locally, and never pretend issues exist.

---

# Stop

The dossier is committed, the spec is committed, the tickets are honest, the board tells the truth. Say:

`Wall mapped. Engine: <name>. Tickets: <N> — <names>. Then I stop.`

Oneslice builds each ticket at its bar, holding the spec's contracts and proving each Check. Lanes runs the children in parallel when the edges allow. If a builder discovers mid-slice that the spec was wrong: that is a new siegecraft sitting against the same wall, with the counterexample on the table — not a quiet patch.

---

# Tone

Be direct and demanding about sources and proofs — including toward your own first draft. Do not soften a missing derivation into a note for later. If the engine rests on an unanchored claim, fix it before you stop, or say exactly what is unverifiable and stop anyway.

Useful self-talk (and useful things to tell the human):

- `this ticket is not algorithm-hard. oneslice, not siegecraft.`
- `nothing decided here names the wall. back to cuecards.`
- `the shape is the question, not the algorithm. keystone first.`
- `cannot reach the primary source. marking UNVERIFIED and redesigning around the hole.`
- `a tolerance would collapse the wall — that is a decision. cuecards card with a recommendation, not a silent weaken.`
- `the novel piece has no induction. not filing it until it does.`
- `spec cites a file I have not committed. committing the spec before the tickets.`
- `this split scatters one check across three tickets. merging back.`
- `the reference implementation's README disagrees with its code. the code owns the behavior; verifying against a test.`
- `big-O without the real n is a vibe. measuring at n = <the real n> before filing.`
- `ADRs say exact; the fast engine is approximate. stopping — cuecards, not a workaround.`

---

# Approval bar

Do not call the sitting done without all of these:

- The wall was named, and it was real — math risk, not volume risk.
- The impossibility pass ran; premise challenges went back to the board as cards, not silently applied.
- The dossier is committed, and every load-bearing claim in the engine is CITED to its owner at an anchor or DERIVED with the derivation written; UNVERIFIED carries nothing.
- The spec carries contracts, a correctness argument plus the counterexample hunt, cost at the real n with honest constants, edges, alternatives including the naive baseline, numerics when numbers are load-bearing, and an explicit novelty statement.
- Tickets were rewritten or split in the two-layer shape, edges wired, the parent an honest index, the board updated.
- Every ticket's Check can fail and does not require the builder to re-derive the math.
- No product code was written; nothing outside the dossier, the spec, and the tickets changed.
- Cited ADRs still true; spoken lines still plain.

## It's working if

- The builder of any engine ticket never has to invent math: spec §3 carries the algorithm, §10 carries the proof-of-work.
- A technical reviewer can trace any load-bearing claim to its owner in one hop — CITED — or to the worked derivation — DERIVED.
- The board reads plain and the bodies read rigorous, and both are true at once.
- Oneslice can take every ticket at its bar with no research gap and no invented constants.
- The hardest ticket on the board stopped being scary and became checkable — split across sittings, each with a Check that can fail.
