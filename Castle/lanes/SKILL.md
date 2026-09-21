---
name: lanes
description: Parallel slice execution, destination mapping, shared contracts, round loops, and multi-agent coordination.
disable-model-invocation: true
---

# Lanes

Lanes orchestrates multi-agent or multi-round execution across parallel work streams toward a single integrated destination.

## Hard gates

1. **No destination, no ship.** You need where we're headed, **How we'll know we're there** (walk / proof / enforced), ADRs in force, and `docs/cuecards/handoff-<slug>.md` with real slices. Missing, placeholder, or "the closed issues are the plan" â†’ cuecards. Do not invent a destination while coding.
2. **Do not reopen product.** The map is engineering: order, ownership, shared contracts, parallelism. A new product question is a cuecards card, not a clever extra lane.
3. **ADRs are law.** Cited ADRs are closed. If the destination cannot honor one, stop and name it â€” cuecards sitting, not a workaround spread across lanes.
4. **Map before parallel.** If two people or two agents would cut without a committed map, they will collide. Write the map. Commit it. Then run.
5. **The destination Check is done.** Slice Checks are waypoints. You are not done until the board's walk works, the proof exists, and enforcement would fail if it regressed.
6. **Not this effort still binds.** Shipping the destination is not permission to ship the backlog, the nice-to-haves, or uncited ADRs.
7. **Each lane holds the oneslice bar.** Many lanes is not a license for spaghetti. Read the sibling skill `oneslice/SKILL.md` and apply it inside every lane: Check, quality bar, thin increments, save-point git, contract-first interfaces, threat-model security, primary-source research, spoken-English tickets, no secrets. This skill does not lower that bar.
8. **Fake parallelism is a defect.** Two lanes that must edit the same files, or that only look parallel on a slide, are one lane. Say so. One honest lane beats five that thrash `main`.
9. **shared contracts before both sides.** If two lanes share an API, schema, event, package, or fixture, the contract is written and committed **before** both implement. Consuming lanes do not start the part that needs an unwritten seam.
10. **Tickets and the map are for people.** A teammate who was not in the room must be able to open the map, pick an unclaimed Now lane, and know what to touch. Agent jargon as the live status is a defect. Never a bare `#42`.
11. **Claim a lane.** One owner per lane. Do not have two writers on the same files. Assign the ticket. Put the name on the map.
12. **This sitting is the destination.** Do not stop merely because Slice 1's Check passed. Stop when the destination Check passes, or when you are blocked on a human (ADR, auth/PII/upload/CORS/integration, access, a missing decision). If the work cannot fit one sitting without dropping the oneslice bar, **do not drop the bar** â€” commit an honest map, ship every Now lane that still fits at that bar, and leave Next/Then visible. Never "finish" by shipping a mess.
13. **Lock, then loop.** Freeze the destination Check and commit the map before round 1. Rounds change the tree, not the target. Do not move the walk to make a round look done.
14. **Thin briefs.** A lane agent or teammate gets only what their Check needs: their lane, Owns / Does not touch, the shared contracts they consume, the ADRs they honor. Dumping the whole handoff, every other lane, and the chat into every agent is a coordination failure â€” cost, latency, and drift.
15. **Idle waiting is a bottleneck.** Do not start an agent that cannot cut yet. Profile the sitting, write the blocking seam, then dispatch. An agent sitting on an unwritten contract is wasted spend.
16. **The clock does not lower the bar.** A time or spend budget stops you *starting* more work. It does not buy shortcuts, a weaker Check, or "good enough because we were looping." Better to hit the limit with meaningful landed lanes than with everything roughly present and messy.

<!-- â”€â”€ PROVENANCE GATES (added to prevent self-adjudication) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ -->

17. **Integration owner must be a human name.** The `Integration owner` field in the map
    header is the person who merges, runs the destination walk, and briefs agents. An agent
    cannot be the integration owner. If no human has taken this role, write
    `Integration owner: unassigned â€” needs a person` and stop until a human claims it.
    Shipping without a named human integration owner is shipping without accountability.

18. **"Destination Check passed" requires a CI run URL, not a claim.** The map status may
    only be set to `Destination Check passed` when you can link a passing CI run (or a
    recorded terminal session with timestamped output) that executed the walk described in
    **How we'll know we're there**. The link must appear in the map under `## What landed`
    and in the commit message. A passing vibe, a passing slice Check, or "I ran it and it
    worked" with no artifact are not sufficient. If the destination Check is not yet in CI,
    the status is `Round N` until it is.

19. **A same-session round-trip is a red flag, not done.** If the map was written and
    committed in this session **and** you are about to claim `Destination Check passed` in
    this same session without referencing a CI run from a *prior* session or commit, stop.
    State out loud: "The map and the done claim are both from this sitting. That is
    provenance collapse. I need a passing CI run from a committed state before I can close
    this." Either link the run or leave the map status as `Round N` and stop.

<!-- â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ -->

20. **Existing arms and shape are law when present.** If `DESIGN.md` exists at the repo
    root, every user-visible lane matches DESIGN.md; the lane's brief carries the design system pointer,
    and an arm change is deliberate, same-commit, and stated (heraldry owns the file).
    If `docs/architecture/` holds a record, lanes cut along its boundaries and do not
    weaken its fitness functions â€” the map's Owns lines should already follow that
    shape. A lane that cannot honor either stops and names it; that is a heraldry or
    keystone sitting, not an adaptation inside the lane.


## Core Lifecycle

`
[Destination Map] -> [Lane Cutting & Contracts] -> [Round Lock & Loop] -> [Integration Verification]
`

1. **Destination Map (docs/lanes/<destination>-map.md)**: Define target end-state, acceptance criteria, and non-goals.
2. **Lane Cutting & Shared Contracts**: Divide work into 2-4 parallel streams with explicit typed contracts at boundaries.
3. **Round Lock & Execution**: Lock branch state before round begins; execute slices in isolated lane branches.
4. **Integration Verification**: Rebase, run integration test suite, verify integrated whole, and update map.

## Artifact Contracts

### Destination Map
`markdown
# Map: <destination spoken name>
## Where we're headed
## How we'll know we're there
## Decisions we honor
## Not this effort
## Shared contracts
### Contract: <name>
## Lanes
### Lane A — <name>
## Now / Next / Then
## Integration
## Sitting profile (this round)
## What landed
## Blocked
`

### Lane Ticket
`markdown
## Lane <letter>: <spoken name>
### What this lane does
### How we'll know
### Owns / does not touch
### Parallel with / waits on
### Decisions this honors
### Status
### What landed
### What I didn't touch (on purpose)
### Blocked
`

## Reference Index

- [reference/map-specification.md](reference/map-specification.md) - Full Destination Map schema, section requirements, and lane ticket format.
- [reference/cutting-lanes.md](reference/cutting-lanes.md) - Lane cutting principles, maximum concurrency, and isolation boundaries.
- [reference/shared-contracts.md](reference/shared-contracts.md) - Shared contracts, interface definitions, types, and cross-lane decoupling.
- [reference/round-mechanics.md](reference/round-mechanics.md) - Pre-round lock protocol, execution loop, exit conditions, and time/spend limits.
- [reference/multi-agent-git.md](reference/multi-agent-git.md) - Git branch topology, rebase discipline, and integration order.
- [reference/map-quality.md](reference/map-quality.md) - Offstage map quality review, red flags, and bad vs good examples.
- [reference/destination-approval.md](reference/destination-approval.md) - Destination approval bar, integrated build loop, and completion criteria.
