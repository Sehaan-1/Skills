# Operations, Stopping Rules, Tone, and Approval Bar

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
