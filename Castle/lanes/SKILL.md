---
name: lanes
description: "Use when shipping an entire multi-slice destination, coordinating parallel workstreams, managing multi-agent development, or executing under a defined time/spend budget. Do not use to decide product questions (cuecards) or build a single isolated slice (oneslice)."
disable-model-invocation: true
---

# Lanes

Coordinate parallel workstreams to ship a complete destination without file collisions or merge conflicts.

Lanes takes a decided handoff from cuecards and sequences it into isolated parallel workstreams. It enforces shared interface contracts before coding, synchronizes work in measured rounds, and loops until the full end-to-end destination test passes.

Announce at start: `Using lanes to [map | lock | round | integrate | verify | stop].`

## Hard gates

1. **No handoff, no map.** Requires a finished cuecards handoff (`docs/cuecards/handoff-<slug>.md`) and ADRs before cutting workstreams.
2. **Disjoint file boundaries.** Parallel workstreams must own disjoint sets of files. Never dispatch two parallel agents to edit the same file (see [reference/boundary-isolation.md](reference/boundary-isolation.md)).
3. **Contracts committed before code.** Shared interfaces between workstreams must be defined as types/schemas in the repo before implementation begins.
4. **Destination check is locked.** The end-to-end user scenario and automated verification cannot be weakened during rounds (see [reference/destination-check.md](reference/destination-check.md)).
5. **ADRs are law.** Workstreams cannot quietly contradict or reopen accepted ADRs.
6. **Existing DESIGN.md and architecture are law.** If `DESIGN.md` or `docs/architecture/` exists, all workstreams must follow them.
7. **Execution in synchronized rounds.** Dispatch parallel tasks, monitor progress, integrate cleanly, and update the map before starting the next round (see [reference/round-mechanics.md](reference/round-mechanics.md)).
8. **Enforce git branch topology.** Isolate workstreams on `lane/<name>` branches and merge into a coordinated `lanes/<slug>` integration branch (see [reference/merge-discipline.md](reference/merge-discipline.md)).
9. **Budget limits are absolute.** When time or token caps are reached, stop starting new work and commit working state.
10. **A single workstream is an honest map.** If tasks cannot run in parallel without colliding, serialize them in one lane. Do not invent fake parallelism.
11. **Human blockers pause execution.** Escalate product conflicts or missing credentials immediately rather than guessing.
12. **Destination done requires proof.** Prove completion through an automated end-to-end test and committed run transcript.

## Workflow

1. **Partition Workstreams:** Group handoff slices into independent workstreams based on file ownership.
2. **Commit Shared Contracts:** Write and commit schemas, types, and mock fixtures for interfaces shared between workstreams.
3. **Commit Map:** Save coordination plan to `docs/lanes/map-<slug>.md`.
4. **Round Loop:**
   - **Plan:** Select independent workstreams marked `Now`.
   - **Dispatch:** Run parallel agents with strict file ownership.
   - **Merge:** Rebase and integrate completed workstream branches into `lanes/<slug>`.
   - **Reconcile:** Update map with completed slices and open blockers.
5. **Final Destination Check:** Run end-to-end integration tests. Confirm all workstreams integrate seamlessly.
6. **Conclude:** Open pull request to default branch and stop.

## Workstream Map Template

Save coordination map at `docs/lanes/map-<slug>.md`:

```markdown
# Map: <Destination Name>

## Destination & Target Check
- **End-to-end scenario:** <user workflow traversing all workstreams>
- **Automated Check:** `npm run test:e2e`

## Shared Interface Contracts
- **Contract 1:** `src/contracts/billing.ts` (Owned by Lane A, consumed by Lane B)

## Workstreams
### Lane A: <Name>
- **Owns:** `src/billing/**`, `tests/billing/**`
- **Does not touch:** `src/frontend/**`
- **Status:** In progress (Round 1)

### Lane B: <Name>
- **Owns:** `src/frontend/**`
- **Depends on:** Contract 1
- **Status:** In progress (Round 1)

## Round Progress
- Round 1: Dispatched Lane A and Lane B.
- Round 2: Integrated Lane A; running Lane B verification.
```

## Reference guides

- [reference/boundary-isolation.md](reference/boundary-isolation.md) — Partitioning workstreams and establishing shared contracts.
- [reference/round-mechanics.md](reference/round-mechanics.md) — Pre-flight locking, round lifecycle, and budget constraints.
- [reference/merge-discipline.md](reference/merge-discipline.md) — Git branch hierarchy, rebase workflows, and integration testing.
- [reference/destination-check.md](reference/destination-check.md) — End-to-end verification and destination approval bar.
