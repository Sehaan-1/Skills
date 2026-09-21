# Destination Map and Lane Ticket Specification

# The map

The map is the shared engineering picture. Chat is not. Standup is not. Closed cuecards issues are not.

`docs/lanes/map-<handoff-slug>.md`

Living file. Commit it before anyone cuts. Update it as lanes land and when ownership or shared contracts change. Git versions it next to the code.

A non-technical person should understand **where we're headed** and **what's in flight**. An engineer who joined this morning should be able to claim a lane without a hallway conversation.

```markdown
# Map: <destination spoken name>

**For the team.** Cuecards decided. This file is how we ship it without colliding.

- **Handoff:** [handoff](../cuecards/handoff-<slug>.md)
- **Board:** [<board name>](url)
- **Arms:** `DESIGN.md` at the repo root — law for user-visible lanes when present · **Shape:** `docs/architecture/<slug>.md` — law for every lane when present
- **Integration owner:** <HUMAN NAME — not an agent>
- **Status:** Mapping · Locked · Round N · Blocked: <plain reason> · Destination Check passed
- **Time budget:** none · until <local time> (clock started <time>)
- **Spend ceiling:** none · <what they named>
- **Round:** 0
- **Agents in flight:** none

## Where we're headed
<from the board, one or two lines, outcome language>

## How we'll know we're there
- **Walk:**
- **Proof:**
- **Enforced:**

This is the locked target. Rounds do not rewrite it.

## Decisions we honor
- [ADR-NNNN Title](../adr/NNNN-….md)

## Not this effort
- [ADR-00NN …](…) — <gist>
- <anything else from the board that must not land>

## shared contracts (shared contracts)
A seam is anything two lanes both touch: API, schema, event, package, fixture, env.

### Seam: <spoken name>
- **Contract:** <path to types / schema / proto — exists before both sides cut>
- **Owned by:** <lane that writes it>
- **Consumed by:** <lanes>
- **Status:** not written · written · both sides on it

## Lanes

### Lane A — <spoken name>
- **Check:** <user-visible or integration; must be able to fail>
- **Does:** <what exists when this lane is done>
- **Handoff slices:** Slice 2, Slice 3
- **Owns (files/packages):** `src/billing/`
- **Does not touch:** `src/auth/`
- **Needs shared contracts:** Seam: payments API
- **Parallel with:** Lane B
- **Waits on:** none | Lane C merge
- **Claimed by:** unclaimed | <name>
- **Ticket:** [<spoken name>](url)
- **Brief:** <path or "inline below — only this lane's packet">
- **Status:** unclaimed · in progress · Check passed · blocked: <plain>

## Now / Next / Then
- **Now, in parallel:** A, B
- **Next:** C (needs A and B merged)
- **Then:** destination walk

## Integration
- Merge to the default branch after every lane Check, not only at the end
- After each merge, walk as far as the destination currently allows
- Final: full walk + proof + enforced

## Sitting profile (this round)
- **Takeable now:**
- **Idle / waiting on:**
- **Bottleneck:** <seam, file, merge, or none>
- **Duplicate work or duplicate context:**
- **Walk before → after this round:**

## What landed
- <lane / seam, in spoken English>

## Blocked
nothing
```

Do not skip sections. Shorten them; do not omit them. If you cannot fill shared contracts and Owns, you are not ready to parallelize — you have a queue, and the map should say so.


---

# Tracker (team)

Live status is the map plus GitHub issues. The map is the picture. The issue is the lane's ticket.

Lane ticket — same voice as oneslice, extra lines for the team:

```markdown
## Lane <letter>: <spoken name>

**For you to read.** On the map: [Map: <destination>](docs/lanes/map-<slug>.md)

### What this lane does
### How we'll know
### Owns / does not touch
### Parallel with / waits on
### Decisions this honors
- [ADR-NNNN Title](path)

### Status
In progress — claimed by <name>.

### What landed
### What I didn't touch (on purpose)
### Blocked
nothing
```

After every increment and when a lane Check passes, update **both** the issue and the map (Status, What landed, Now/Next, Sitting profile). Refer to lanes, slices, and ADRs **by name**.

Lanes run in parallel sessions, so expect the map and issues to be edited concurrently. Re-read the map before you write to it.

A teammate reads the map, not the integration owner's head.

If `gh` cannot see this repo: say so, keep the map in `docs/lanes/` anyway, and fall back the same way oneslice/cuecards do. The map is not optional.

---

