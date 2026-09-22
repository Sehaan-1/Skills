# Worked invocation examples (few-shot routing)

Use these as calibration when resolving mode + depth. Match the *shape* of the response, not the wording.

## Example 1 — `interview` mode (default for greenfield drills)

**User:** "Design a URL shortener."

**Routing:** design drill → `interview`. Load nothing extra yet.

**First response shape:**

1. Confirm scope in one breath: *"I'll lead us through requirements → high-level design → core components → scaling."*
2. Step 1 questions (or state assumptions if they say "just answer it"): users? read:write? custom aliases? expiry? QPS/storage targets?
3. Estimate teaser only if constraints land (10M writes + 100M reads/mo → ~4/40 QPS; point at `quick-reference` if doing full math).
4. Stop and wait — do **not** dump the full architecture in turn one.

**Deeper turns:** high-level diagram (mermaid), API + schema, key generation (MD5 + base62), read/write paths, then scale pass (cache-aside, replicas, sharding) each with its trade-off. Cite `solutions/system_design/pastebin/` if the repo is present.

## Example 2 — `estimate` mode (narrow numeric ask)

**User:** "How much storage do we need for 10 million new pastes a month at 1 KB each, over 3 years?"

**Routing:** pure numbers → `estimate`. Load `references/quick-reference.md`; optionally run `scripts/estimate.py`.

**Response shape:**

```
10M × 1.27 KB ≈ 12.7 GB/month → ~450 GB over 3 years
1 rps ≈ 2.5M req/month, so with 10:1 read:write:
  writes ≈ 4/s, reads ≈ 40/s (peak ~100/s at 2.5×)
```

No architecture diagram, no component deep dive. If asked "how many servers?" follow with node-count logic (headroom × peak), not a full design.

## Example 3 — `decide` mode (trade-off question)

**User:** "Should I use SQL or Postgres— wait, SQL or NoSQL for this feed service?"

**Routing:** technology choice → `decide`. Load `references/topic-playbook.md`.

**Response shape:** recommendation + counter-trade-off matrix, e.g.

| | SQL | NoSQL |
|---|---|---|
| Fits | strict schema, transactions, complex joins | flexible schema, TB scale, hot read throughput |
| Cost here | write throughput ceiling, vertical scaling | eventual consistency, app-level joins |

Pick one, defend it against the stated constraints (Step 1 facts if known; state assumptions if not). No full design unless asked.

## Example 4 — `review` mode (existing system critique)

**User:** "Here's our design: single Postgres primary, app servers with in-memory session maps, no cache. 50k DAU. What breaks first?"

**Routing:** existing architecture → `review`. Load `references/topic-playbook.md`.

**Response shape:** ordered audit, not a redesign —

1. SPOFs (single primary; sticky/unshared sessions break on horizontal scale)
2. Bottlenecks (read QPS on primary, no cache absorption for hot rows)
3. Failure modes (primary dies → writes halt; app server dies → sessions lost)
4. Minimal fix ladder: read replicas → cache-aside → stateless sessions in Redis — each with its cost

Use the Step 4 checklist at the end of the body (SPOF, hotspot, invalidation, replication lag, node/datacenter death).

## Example 5 — `study` mode

**User:** "I have a system design interview in 2 weeks. What should I study?"

**Routing:** prep plan → `study`. Load `references/questions.md`.

**Response shape:** short-timeline plan from the primer's Study guide — breadth over depth; pick ~4–6 questions skewed to the target company's domain; point at Anki decks if repo present; give a day-by-day sketch. No design doc.

## Example 6 — correct non-invocation

**User:** "Why is my pytest fixture failing with a teardown error?"

**Routing:** plain debugging, no design/scale dimension → **do not invoke this skill**. Answer normally. (Also do not invoke for CI/ops questions, refactors, or product questions.)

## Example 7 — mode precedence conflict

**User:** "We have this architecture diagram — also, how many shards would it need?"

**Routing:** `estimate` (narrow numeric) answers the shard math first via `quick-reference`/`estimate.py`; offer a `review` of the diagram as a follow-up. Precedence: `estimate`/`decide` → `review` → `interview`/`design`.
