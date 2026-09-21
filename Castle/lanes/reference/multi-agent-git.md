# Multi-Agent Git Topology and Rebase Discipline

# Run

## One agent, one sitting

Lock, then loop the rounds above until an exit. If two independent Now lanes exist and you can only run one body: still finish both before you stop, unless a human gate or the clock says otherwise. Slice-one-and-stop is the wrong ending.

## Team / many agents

- The map is the assignment board. People claim an unclaimed **Now** lane, write their name, assign the ticket.
- Each claimed lane is an oneslice sitting for that owner, from a **thin brief**, not from the whole thread.
- They do not take a second lane until their Check passed and merged, unless the integration owner says the first is blocked on a seam they cannot write.
- Integration owner (named on the map) is the only one who changes Now/Next/Then, Owns, and shared contracts, and the only one who dispatches extra agents. If ownership is wrong, stop the colliding lanes, fix the map, restart. Do not "just resolve" a merge that means the map was a lie.
- Sync through the map and tickets. Chat lore that is not on the map does not exist.
- Do not wait for a meeting to unstick a seam. Stop the two lanes, write the contract, continue.
- New people: read the map, claim a Now lane, read the ADRs it cites. They should not need yesterday's thread.
- One failed owner does not rewind the team.

## Git (across lanes)

Oneslice git rules hold inside a lane. Across lanes:

- Default branch stays deployable.
- **No long-lived lane branches.** Short-lived `feature/<lane-spoken-slug>` (or per-slice), merge in days. A flag beats a long-lived branch.
- File ownership on the map is the lock. Touch another lane's files → you found a missing seam or a map bug. Stop. Fix the map.
- Worktrees when two agents must not share a working tree. One lane per worktree.
- Do not force-push shared branches. Never commit secrets. If a secret hits a remote: rotate first, then purge.
- After each lane merge, the integration owner runs the destination walk as far as it can go — not only at the end.

---

