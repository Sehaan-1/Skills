# Round Mechanics & Budget Management

Lanes organizes execution into measured rounds. A round is a synchronized cycle of planning, parallel dispatch, progress monitoring, and map reconciliation.

## Pre-Flight Lock (Before Round 1)

Before launching parallel workstreams, verify and lock:

- **Destination Check:** The end-to-end user verification scenario and automated test are clearly stated and locked.
- **Accepted ADRs:** Decisions in force cannot be reopened during the round.
- **Budget Limits:** Explicit time limit (hours) or token/cost spend cap recorded on the map.
- **Workstream Map:** Committed to `docs/lanes/map-<slug>.md`.

---

## Round Execution Lifecycle

```text
Lock ──▶ Round N [Dispatch ──▶ Monitor ──▶ Merge ──▶ Reconcile] ──▶ Destination Check?
           ▲                                                                 │
           └────────────────────────── Not Done ─────────────────────────────┘
```

1. **Plan:** Identify independent workstreams marked `Now` whose blockers have cleared.
2. **Dispatch:** Launch parallel agents or threads, assigning explicit file boundaries.
3. **Monitor:** Ensure agents stay within assigned scope and commit atomic increments.
4. **Reconcile:** Update `docs/lanes/map-<slug>.md` with completed slices, what landed, and current blockers.

---

## Exit Conditions

A Lanes session terminates **only** when one of three explicit conditions is reached:

1. **Destination Check passes:** The end-to-end verification succeeds and automated tests pass.
2. **Blocked by human:** A critical architectural or product ambiguity arises requiring user resolution.
3. **Budget cap reached:** The predefined time or spend limit is exhausted. Work stops cleanly; unmerged code is committed to feature branches.
