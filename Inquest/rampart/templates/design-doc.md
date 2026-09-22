# Design: {SYSTEM NAME}

> Fill-in template mirroring the System Design Primer's 4-step method and its worked solutions under `solutions/system_design/`. Delete the `{…}` placeholders and guidance as you go.

## 1. Requirements, constraints, assumptions

### 1.1 Use cases (in scope)

- **User:** {primary action → result}
- **User:** {secondary action}
- **Service:** {background behavior: analytics, cleanup, notifications…}

### 1.2 Out of scope

- {explicitly excluded feature} — reason: {why deferred}

### 1.3 Constraints and assumptions

- {N} users; {N} writes/month; {N} reads/month; read:write ≈ {10:1}
- {latency / availability / consistency targets, e.g. p99 < 200 ms, 99.99%}
- {data shape: text only? media? geo-distributed?}
- Traffic assumptions: {even/uneven distribution, hot keys}

### 1.4 Back-of-the-envelope estimates

| Metric | Estimate |
|---|---|
| Record size | {e.g. 1.27 KB} |
| New data / month | {GB} — over 3 years: {GB} |
| Average writes/s | {QPS_w} (peak ≈ {2–3×}) |
| Average reads/s | {QPS_r} (peak ≈ {2–3×}) |
| Bandwidth (read path) | {QPS_r × size} |
| Hot working set (cache RAM) | {GB} |

Conversion: 1 rps ≈ 2.5M requests/month. Latency table → `references/quick-reference.md`.

## 2. High-level design

```
[Client] → [DNS/CDN] → [L7 Load Balancer]
   → [Web server (reverse proxy)]
   → [API servers: Read API | Write API]   (stateless, horizontally scaled)
        → [Cache (Redis/Memcached, cache-aside)]
        → [Primary DB] → [Read replicas]
        → [Object store / blob store]
        → [Message queue] → [Workers] (async jobs)
```

{Replace with a mermaid diagram. Justify each box in one line: problem solved + cost.}

### 2.1 API

```
POST /api/v1/{resource}      {body fields}
GET  /api/v1/{resource}/{id}
```

{Note REST for public surface, RPC for internal hot paths if relevant.}

### 2.2 Data model

```
table {name}(
  {key}          char(7) NOT NULL,   -- PK, uniqueness via index
  {field}        type NOT NULL,
  created_at     datetime NOT NULL
)
PRIMARY KEY({key})  -- index on {filter column}
{Secondary store: {NoSQL type} because {flexible schema / scale / relationships}}
```

{Justify SQL vs NoSQL explicitly (see references/topic-playbook.md).}

## 3. Core component deep dive

### 3.1 Write path ({use case})

1. Client → web server → **Write API**
2. {key generation: hash / snowflake / sequence — collision handling}
3. {uniqueness check, validation}
4. Persist {metadata → DB, payload → object store}
5. {enqueue async work: fanout, analytics, cleanup}
6. Return {response}

{Pseudocode only as deep as requested — "Clarify how much code you are expected to write."}

### 3.2 Read path ({use case})

1. Client → web server → **Read API**
2. Cache lookup (cache-aside): miss → DB/replica → populate → serve
3. {fallback, error shape}

### 3.3 Background jobs

- {expiration/cleanup}: schedule via {task queue + workers}, scan by {indexed created_at}
- {fanout/aggregation}: message queue → workers → {timeline/index/rank store}

## 4. Scale the design

| Bottleneck | Fix | Trade-off accepted |
|---|---|---|
| Read QPS on primary | read replicas + cache-aside | replication lag / stale reads (TTL) |
| Single DB growth | {federation → sharding} | cross-shard joins, rebalancing skew |
| App SPOF | LB + stateless horizontal scale | session state moved to {Redis/DB} |
| Slow/expensive inline work | message queue + workers | eventual completion, duplicate delivery (idempotency) |
| Large payload bandwidth | CDN / object store | cache invalidation |
| Skewed hot keys | {consistent hashing, hot-key split, rate limit} | added routing complexity |

## 5. Failure modes & open questions

- **Node failure:** {who fails over, promotion path, data-loss window}
- **Replication lag:** {read-your-writes story}
- **Cache down / stampede:** {TTL jitter, rebuild from DB, protect DB with request coalescing}
- **Queue backlog:** back pressure → 503 + exponential backoff on clients
- **SPOF audit:** {list remaining SPOFs and why acceptable or how removed}
- **Open questions:** {things needing interviewer input or future phase}

## 6. Further reading

- Primer topics: this skill's `references/topic-playbook.md` → {e.g. Caching, SQL scaling, CAP} (or `README.md` → {section} if the primer repo is present)
- Worked solution to compare against: `solutions/system_design/{matching question}/README.md` *(only if repo present; otherwise cite github.com/donnemartin/system-design-primer)*
- OOD counterpart if relevant: `solutions/object_oriented_design/` *(only if repo present)*
