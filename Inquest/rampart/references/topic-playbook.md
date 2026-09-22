# Topic playbook: building blocks and their trade-offs

Condensed from the primer's Index of system design topics (`github.com/donnemartin/system-design-primer` → README). Self-contained for standalone use; every recommendation pairs with its disadvantage — that is the point of an interview.

## Foundations

- **Performance vs scalability** — slow for one user = performance problem; fast for one user but slow under load = scalability problem. Scalable = performance grows proportionally with resources added.
- **Latency vs throughput** — aim for maximal throughput at acceptable latency.
- **CAP theorem** — with network partitions (unavoidable), choose **CP** (atomic reads/writes, e.g. transactions) or **AP** (eventual consistency, keep serving).
- **Consistency patterns**:
  - *Weak* — best effort; VoIP, video chat, realtime games (memcached-style).
  - *Eventual* — async replication; DNS, email, highly available systems.
  - *Strong* — sync replication; file systems, RDBMS, anything needing transactions.
- **Availability patterns** — *fail-over* (active-passive via heartbeats; active-active load-shared) and *replication*. Failover costs hardware + complexity and risks losing unreplicated writes.

## Edge / delivery layer

- **DNS** — hierarchical name→IP; records: NS, MX, A, CNAME; caching via TTL; routing options: weighted round robin, latency-based, geolocation. Cost: lookup delay, management complexity, DDoS exposure.
- **CDN** — cache content close to users. *Push* CDNs (you upload, good for infrequent large updates) vs *Pull* CDNs (CDN fetches on miss, good for frequent updates). Cost: cache invalidation and pay-for-storage.
- **Load balancer** — distributes traffic; stops requests hitting unhealthy servers; removes single points of failure; supports SSL termination and session persistence. L4 (transport header, faster/cheaper) vs L7 (content/cookies, smarter routing, more work). Route by round robin, least loaded, session, etc. Cost: can itself become a bottleneck/SPOF; needs redundant pairs; adds complexity. Pair with **horizontal scaling** — app servers must be **stateless**; keep sessions in a centralized DB or persistent cache (Redis/Memcached).
- **Reverse proxy** — single public face in front of servers: security (hide backends), SSL termination, compression, caching, static content. Useful even with one server. L7 LBs and reverse proxies overlap (NGINX, HAProxy do both).

## Application layer

- Split **web layer** from **application (platform) layer** to scale each independently; single responsibility; small autonomous services.
- **Microservices** — independently deployable, modular services communicating via lightweight mechanisms (e.g. Pinterest: profile, follower, feed, search, photo upload). Cost: deployment/ops complexity, different org processes.
- **Service discovery** — Consul / Etcd / Zookeeper register names, addresses, ports; HTTP health checks; built-in KV store for config.

## Data layer

### SQL (RDBMS) — ACID

Scale techniques, in increasing order of pain:

1. **Master-slave replication** — master takes reads+writes, replicates to read-only slaves (tree allowed). Reads scale; fail → promote a slave (needs promotion logic). Risk: lost writes if master dies pre-replication; replication lag; replay burden on slaves.
2. **Master-master replication** — both masters read/write, coordinate. Survives either node dying; cost: routing/load balancing, conflict resolution, eventual consistency or higher write latency.
3. **Federation** (functional partitioning) — DBs split by function (forums, users, products): less traffic per DB, more cache locality, parallel writes. Cost: cross-federation joins, app routing logic; doesn't help if one function is huge.
4. **Sharding** — split rows across DBs (by geography, user key); consistent hashing limits rebalancing data movement. Benefits: like federation + smaller indexes. Cost: complex queries/joins, hot-shard skew, rebalancing, added hardware.
5. **Denormalization** — redundant copies to avoid expensive joins; read-heavy systems (100:1–1000:1 reads) benefit; materialized views help. Cost: duplication, write overhead, sync complexity.
6. **SQL tuning** — benchmark (`ab`) + profile (slow query log). Schema: `CHAR` vs `VARCHAR`, `TEXT` for big blobs (store pointer not BLOB), `DECIMAL` for currency, `NOT NULL`; index filter columns (B-tree, but slows writes); partition hot tables; beware query-cache pitfalls.

### NoSQL — BASE (basically available, soft state, eventual consistency)

| Type | Abstraction | Best for | Examples |
|---|---|---|---|
| Key-value | hash table | O(1) reads/writes, caches, rapidly-changing simple data; lexicographic key ranges | Redis, Memcached, DynamoDB |
| Document | KV with documents as values | flexible/evolving schema, JSON-ish objects | MongoDB, CouchDB, DynamoDB |
| Wide column | nested map `ColumnFamily<RowKey, Columns<ColKey, Value, Timestamp>>` | very large datasets, high availability/scalability | Bigtable, HBase, Cassandra |
| Graph | graph | complex relationships, many FKs / many-to-many (social networks) | Neo4j, FlockDB |

**SQL when:** structured data, strict schema, relations, complex joins, transactions, clear scaling patterns, index lookups.
**NoSQL when:** semi-structured/flexible schema, no joins, TB–PB scale, data-intensive, very high IOPS; clickstreams, leaderboards, carts, hot tables, metadata.

## Caching

Cache levels: client, CDN, web server (Varnish/reverse proxy), DB built-in, application (Redis/Memcached in RAM; Redis adds persistence + sorted sets/lists). Cache **database queries** (hard to invalidate on complex queries) or **objects** (invalidate object on change; async workers). Good candidates: sessions, rendered pages, activity streams, user graphs. Avoid file-based caching (hurts cloning/auto-scaling).

Update strategies:

| Strategy | How | Pros | Cons |
|---|---|---|---|
| **Cache-aside** (lazy loading) | app reads cache → miss → load DB → populate cache | only hot data cached; simple; Memcached-style | miss = 3 trips; stale until TTL; new node starts cold |
| **Write-through** | app → cache → sync write to DB | reads of fresh writes fast; never stale | slow writes; new nodes empty until writes; unread writes waste space (TTL) |
| **Write-behind** | app → cache → async write to DB | fast writes | data loss risk if cache dies pre-flush; more complex |
| **Refresh-ahead** | auto-refresh entries before expiry | lower latency if prediction is good | bad prediction can be worse than no prefetch |

General costs: cache invalidation difficulty, consistency between cache and source of truth, app changes to introduce Redis/Memcached.

## Asynchronism

- **Message queues** — publish job → worker consumes → signal completion; user not blocked (e.g. tweet appears instantly, fans out in background).
  - Redis: simple broker, messages can be lost.
  - RabbitMQ: popular, AMQP, self-managed.
  - Amazon SQS: hosted, higher latency, at-least-once (duplicates possible).
- **Task queues** — carry task data + scheduling for background/compute-heavy jobs (Celery).
- **Back pressure** — cap queue size; when full return 503 and clients retry with exponential backoff; protects throughput for queued work.
- Cost: queues add delay and complexity; cheap synchronous calcs / realtime flows may not want them.

## Communication

- **HTTP** — request/response verbs: GET (idempotent/safe/cacheable), POST (create), PUT (idempotent replace), PATCH (partial), DELETE (idempotent).
- **TCP** — connection-oriented, ordered, reliable, flow/congestion control; use when data must arrive intact (web, DB, SMTP, FTP, SSH); connection pooling to limit open-connection memory cost.
- **UDP** — connectionless, unordered/lossy, no congestion control, can broadcast; use when lowest latency matters, late data worse than loss, or you do your own error correction (VoIP, video, streaming, realtime games).
- **RPC** — client calls remote procedure like local (Protobuf, Thrift, Avro); great for internal performance-critical calls; exposes **behaviors**. Cons: tight coupling, new API per operation, harder to debug/cache.
- **REST** — resource-oriented, stateless, cacheable HTTP; exposes **data**; ideal for public APIs; scales horizontally. Cons: awkward for non-hierarchical/query-heavy operations, N+1 round trips for nested views, payload bloat for old clients.
- Rule of thumb: **REST for public APIs, RPC for internal hot paths.**

## Security (always mention in Step 4/5)

Primer's basics — enough unless interviewing for a security role:

- Encrypt in transit and at rest
- Sanitize all user inputs / parameters (anti XSS, anti SQL injection)
- Parameterized queries
- Principle of least privilege
- Further: API security checklist · OWASP top ten (external links in primer README)

## RPC vs REST (condensed from primer comparison)

| | RPC | REST |
|---|---|---|
| Exposes | behavior (verbs) | data (resources + HTTP verbs) |
| Signup | POST /signup | POST /persons |
| Delete | POST /removeItem {id} | DELETE /persons/1234 |
| Update | POST /modifyItem {id, kv} | PUT /items/456 {kv} |
| Best for | internal hot paths, hand-tuned SDKs | public APIs, loose coupling, cacheability |
| Cost | tight coupling, new API per op, harder to debug/cache | awkward for non-hierarchical ops, N+1 fetches, payload bloat |

## Primer "under development" topics (stretch goals to mention)

MapReduce (distilled in solutions-index: sales_rank, crawler dedup, mint, pastebin analytics) · consistent hashing (see sharding note) · scatter gather (twitter/crawler search).

## Standard bottleneck → fix map (Step 4 checklist)

| Bottleneck | First moves | Then |
|---|---|---|
| Too much read traffic | cache hot reads (cache-aside), read replicas | denormalize, CDN |
| Too much write traffic | queue + async workers (write-behind) | shard / partition |
| Single DB too big | federation, then sharding (consistent hashing) | multi-region |
| Single server SPOF | LB + stateless app servers + failover | active-active |
| Slow responses on critical path | add cache, remove hops, connection pooling | async non-critical work |
| Hot shard / skewed load | better hash key, splitting hot keys | rate limit / shed load |
| Cache stampede on expiry | refresh-ahead, TTL jitter | request coalescing |
| Queue growth unbounded | back pressure (503 + retry/backoff) | scale workers, shed |
