# Round Execution Loop and Mechanics

# The loop

Lock the target. Then round until an exit. Implementation *is* the loop. The map is the scoreboard.

This is not a visual loop. There is no target screenshot, no pixel match, no fidelity-to-a-picture. The target is the destination **walk / proof / enforced**.

## Lock (before round 1)

1. Map committed and depth-reviewed.
2. Destination Check written on the map in the same words as the board. **That is the target.** Do not move it later to make a round look done.
3. If they gave a **time budget**, record the clock on the map now (after lock, not before). Check it between rounds.
4. If they named a **spend ceiling**, performance goal, or "Now lanes only," write it on the map. Constraints do not rewrite ADRs or the oneslice bar.
5. If they gave **no** time budget, warn once that this sitting may run until the destination Check — then run until an exit.
6. Map Status = Locked. Say out loud: `Target locked: <walk in one line>. Then I loop.`

## A round

Every round, in order:

1. **Profile the sitting** (five minutes, on the map — not a product APM tour unless a lane Check says so).
   - Which Now lanes are actually takeable?
   - Where would an agent sit idle (unwritten seam, unmerged wait, missing claim)?
   - Which seam or file is the bottleneck?
   - Duplicate work, or the same context about to be pasted into two agents?
   - Is `main` green?
2. **Brief, don't dump.** For each takeable lane, a thin packet: lane block, Owns / Does not touch, seam contract paths, ADRs, the DESIGN.md pointer for user-visible lanes, Check. Not the whole handoff. Not every other lane's diff. Not the chat. If it isn't needed to pass that Check, it isn't in the brief.
3. **Dispatch independent work together.** One owner per lane. No second agent on a claimed lane. Do not start a blocked lane "to look busy." If this harness has subagents or worktrees, independent Now lanes in parallel (one worktree per lane). If not, run them in sequence with `main` green after each — still finish the takeable set before you stop.
4. **Implement** at the oneslice bar. Research foreign facts in the background per lane; reuse an existing research file instead of investigating the same primary source twice.
5. **Fault isolation.** One lane failing (tests, merge, human gate) does not cancel the others. Mark it blocked on the map. Keep A and C moving.
6. **Merge + measure.** Integration owner merges. Run tests. Walk as far as the destination currently allows. Write **Walk before → after this round** on the map. A round with no before/after is just typing.
7. **Rebalance.** Unlock Next whose waits landed. Split a lane that is the bottleneck. Merge lanes that turned out coupled. Check the clock and spend. Update the map. Next round, or exit.

Main stays green after every merge. A round that leaves the tree broken is a failed round: revert to last green, then investigate. Changes stay gradual and reversible (oneslice increments).

## Exit (only these)

- Destination Check passed (walk + proof + enforced), or
- Named human block on the map, or
- Time or spend budget hit — stop with meaningful landed lanes at full bar, map honest about Next.

Do not exit because a slice Check passed. Do not exit by lowering the implementation bar. Do not exit by rewriting the walk.

## Time and spend

- **Time budget given:** lock, note the time, check between rounds. When the remainder cannot fit another lane at full bar, do not start one. Finish in-flight well.
- **Don't degrade to hit the clock.** Don't take shortcuts. It is better to hit the limit with two lanes that would pass a hard review than with every slice roughly present and messy.
- **Spend:** don't spawn two agents on one lane; don't paste the repo into every brief; reuse research notes and committed shared contracts (those are the cache; chat is not); prefer one round-trip of parallel Now lanes over a chatty "you wait, then you."
- If a spend ceiling is in sight, stop *starting* agents. Finish in-flight at full bar.

Do not pick models, prices, or dashboards this skill does not have. Track what you can see: rounds, agents in flight, idle waits, whether the walk advanced.

---

