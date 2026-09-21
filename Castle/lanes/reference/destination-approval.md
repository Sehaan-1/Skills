# Destination Approval Bar and Tone

# Build loop (this sitting)

1. **Load.** Handoff, ADRs, Notes, How we'll know, tree layout — plus `DESIGN.md` and the `docs/architecture/` record when they exist (gate 20). If any of those is missing, cuecards.
2. **Map.** Cut lanes and shared contracts. Depth-review. Commit `docs/lanes/map-<slug>.md`. File/claim tickets.
3. **Lock.** Freeze the destination Check. Record time/spend constraints. Status = Locked.
4. **Round:** profile → brief → shared contracts that blockers need → dispatch takeable lanes (oneslice bar, parallel if independent) → merge → walk before/after → rebalance.
5. Repeat 4 until an exit criterion.
6. **Destination Check** (if claiming shipped). Walk. Proof. Enforced. Break it on purpose and watch enforcement fail, then restore.
7. **Report** on the board issue and the map, in spoken English. What landed, what you didn't touch, which ADRs, where the proof lives, how many rounds, what the bottleneck was.
8. **Stop.** The destination shipped, or a named human block or budget is on the map. Not "slice 1 of n."

## Approval bar (do not call the destination shipped without this)

- Map exists, committed, and matches what actually ran (ownership, shared contracts, Now/Next, round, profile)
- Target was locked before round 1 and not quietly moved
- Every landed lane passed the oneslice approval bar — not "good enough because we were looping"
- Destination **walk** works end to end without you in the room
- **Proof** is in the repo
- **Enforced:** CI (or the named pin) fails if that walk regresses
- Cited ADRs still true
- If `DESIGN.md` exists: every landed lane's user-visible work matches DESIGN.md
- If a keystone record exists: no lane crossed a boundary or weakened a fitness function
- Nothing from **Not this effort** landed
- shared contracts that were shared were written before both sides cut
- Tickets and map are readable by a person who missed the sitting
- No long-lived lane branches left open as the real integration strategy
- No secrets in any lane's diff
- You did not reopen product decisions to make the map nicer
- Independent lanes were briefed thinly and dispatched together, not serialized for fear
- Each round recorded walk before → after; idle agents were not started
- A time/spend budget, if named, did not buy a messy finish

Any line above that fails is a blocker unless you can justify it in one sentence to the human. The classics: lanes parallel on the map but coupled in the tree, a seam invented twice, integration saved for the end, a lane shipped below the oneslice bar, the walk never run, or a map that is stale because chat knows more.

If the bar is not met, do not stop with "we'll tidy after launch." Fix it, or explicitly hand back a blocked destination with the map telling the truth.

## Tone

Be direct about collisions, fake parallelism, idle agents, and quality — including toward your own first map.
Do not be rude. Do not soften "these two lanes will fight in `src/db.ts`" into a note for later.
Do not confuse speed with shipping: six messy lanes is slower than two clean ones.
Do not confuse looping with thrashing: a round that does not move the walk is a failed round.

Useful self-talk (and useful things to tell the human):

- `no handoff. cuecards sitting, not a fake map.`
- `this is one ticket. oneslice, not lanes.`
- `these two lanes share a file. merging them / extracting a seam.`
- `honest map is one lane. writing that; still looping through the destination Check.`
- `target locked. round 1.`
- `this brief includes three other lanes. cutting it to Owns + shared contracts + ADRs.`
- `agent would sit idle on an unwritten seam. not dispatching.`
- `contract isn't written. seam first, then the consumers.`
- `lane Check passed. merging; walking as far as the destination allows; not stopping.`
- `lane B died. map blocked; A and C still running.`
- `round had no before/after on the walk. measuring before dispatching more.`
- `time budget in 20 minutes. not starting a new lane; finishing in-flight at full bar.`
- `this contradicts ADR-NNNN. stopping. cuecards sitting.`
- `new auth/PII/upload/CORS. asking the human before that lane cuts.`
- `map was a slide. rewriting so a new teammate could claim a Now lane.`
- `destination walk still wouldn't catch a break. fixing proof before calling shipped.`

## It's working if

- The whole destination shipped this sitting, or the map honestly names the human block or budget and every takeable Now lane has landed at the oneslice bar — the exit was real, not a pile of slices with no loop.
- A teammate who missed the sitting can open `docs/lanes/map-<slug>.md`, claim an unclaimed Now lane, and not need yesterday's thread.
- You did not use this skill to decide product, match a picture, or leave the destination half-built.
, or the map honestly names the human block or budget and every takeable Now lane has landed at the oneslice bar — the exit was real, not a pile of slices with no loop.
- A teammate who missed the sitting can open `docs/lanes/map-<slug>.md`, claim an unclaimed Now lane, and not need yesterday's thread.
- You did not use this skill to decide product, match a picture, or leave the destination half-built.
