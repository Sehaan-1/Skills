# Interview scoring rubric & closing checklist

Use at the end of `interview` or `ood` mode when the user wants feedback, or self-score a practice run. Scores are formative — pair every deduction with what to say next time.

## System design rubric (100 points)

| Dimension | Pts | What full credit looks like | Typical deductions |
|---|---|---|---|
| Requirements & scoping | 20 | Asks who/how-many/read-write/latency-availability; splits in vs out of scope; states assumptions explicitly | Jumping to components; unexamined magic numbers; scope creep |
| Estimation | 15 | Round-number QPS → storage → bandwidth setup; uses 2–3× peak factor; cites orders of magnitude from `quick-reference` | Missing peak; false precision; no unit conversions (1 rps ≈ 2.5M/mo) |
| High-level design | 20 | Sketches client → LB → app → cache → store (+ queue/worker when async fits); justifies each box with problem *and* cost | Component laundry list; boxes without justification; missing API/data model |
| Core components | 20 | Walks read path and write path end-to-end; concrete schema/key generation; right level of code (checks how much is wanted) | Hand-waving hotspots; no schema; code dump when discussion wanted |
| Scaling & trade-offs | 20 | Names bottleneck → fix → *new cost* for each (replicas→lag, cache→invalidation, shards→skew, queues→duplicates) | Fixes without trade-offs; scaling before identifying bottleneck |
| Communication | 5 | Leads the conversation, checks in, timeboxes depth, closes with failure modes + open questions | Monologue; never surfaces what could go wrong |

**Bands:** 90+ offer-ready · 75–89 solid with polish · 60–74 passable, tighten estimation + trade-off language · <60 redo with the 4 steps until automatic.

## Object-oriented design rubric (100 points)

| Dimension | Pts | Full credit |
|---|---|---|
| Requirements (actors, core operations, constraints) | 20 | Clarifies use cases before classes |
| Class/interface design | 30 | Clear nouns → classes; sensible boundaries; inheritance vs composition chosen deliberately |
| Relationships & data flows | 20 | Sequences for core operations; who owns state |
| Edge cases & concurrency | 20 | Persistence, thread-safety, failure of collaborators |
| Code clarity | 10 | Core methods correct and readable; tests or invariants stated |

## Closing checklist (run before saying "done")

Interviewer-style probe list — answer each in one line or flag as open:

1. **SPOF audit** — any single component whose death takes the system down? What is the failover?
2. **Bottleneck** — what saturates first at 10× traffic? How do you see it (metrics)?
3. **Hotspots / shard skew** — hot key, power user, viral item? Mitigation (split, cache, consistent hash)?
4. **Cache invalidation** — which strategy (cache-aside/write-through/write-behind/refresh-ahead)? What happens on miss and on expiry?
5. **Replication lag** — read-your-writes story for the critical flow?
6. **Data loss window** — what is lost if the primary/cache/queue dies right now?
7. **Node or datacenter death** — degraded mode? Can the system serve reads while writes are down?
8. **Queue health** — if backlog grows: back pressure (503 + exponential backoff), scale workers, shed load?
9. **Security pass** — TLS, parameterized queries, least privilege, rate limiting on abuse-prone endpoints?
10. **What would you revisit** — with real metrics, which assumption here is shakiest?

## Feedback format

When scoring a practice run:

```
Score: NN/100  (band: …)
Strengths: 2–3 specific things to keep
Fix first: top 2 deductions → exact phrases/moves to use instead
Re-run suggestion: same question cold, or one from references/questions.md with same technique tags
```
