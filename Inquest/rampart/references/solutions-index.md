# Solutions index — all 8 system design answers (distilled from `solutions/system_design/`)

Depth bar and technique crib for `interview`/`design` modes. **Pastebin** has a full walkthrough in `worked-exemplar.md`; the rest are distilled here. With the repo present, open each `README.md` for diagrams and full code. Every solution follows the same 4-step frame and ends with the same "Additional talking points" menu (SQL scaling · caching · async/microservices · comms · security · latency numbers) — offer those when time remains.

## 1. Pastebin / Bit.ly — `pastebin/`

→ Full model answer: `worked-exemplar.md`. Techniques: base62(MD5) keys, PK uniqueness, object store payloads, MapReduce analytics, indexed expiry scans.

## 2. Twitter timeline & search (≈ FB feed) — `twitter/`

**Scope:** post tweet + fanout to followers/push; user timeline; home timeline; keyword search. Out: firehose, visibility rules, analytics.

**Numbers (primer's):** 100M active users · 500M tweets/day (15B/mo) · avg fanout 10 → 150B deliveries/mo · 250B reads/mo · 10B searches/mo · ~10 KB/tweet → **150 TB/month, 5.4 PB/3yr** · ≈100k reads/s · 6k tweets/s · 60k fanout deliveries/s · 4k searches/s.

**Core:**
- User timeline: SQL is fine. **Home timeline fanout (60k deliveries/s) overloads RDBMS** → NoSQL/memory cache for fast writes.
- **Fan Out Service:** User Graph Service → followers from memory cache → insert tweet into each follower's home-timeline Redis **list** (packed `tweet_id+user_id+meta` tuples) · enqueue notifications · index for search · media → object store.
- **Timeline Service (read):** O(1) fetch of ids from cache → multiget Tweet Info + User Info services to hydrate (O(n) multiget, not O(n) round trips).
- **User timeline:** read from SQL directly.
- **Search:** tokenize/normalize query → scatter-gather across Lucene-style Search Cluster → merge/rank/sort.
- Public REST, internal RPC. Celebrity problem = hybrid fanout (pull for huge accounts).

**Scale pass:** cache absorbs hot reads + spikes; master-slave for SQL; LB + stateless web/app; CDN for media; queue for async notifications.

## 3. Web crawler — `web_crawler/`

**Scope:** crawl URL list → reverse index + titles/snippets; user search over that. Out: analytics, personalization, PageRank. Constraint: must not loop forever (cycles); exercise traditional systems (no Solr/Nutch).

**Numbers:** 1B links to crawl, ~weekly refresh → 4B crawls/mo · 500 KB/page → **2 PB/month, 72 PB/3yr** · 100B searches/mo → **1,600 crawl writes/s · 40,000 search QPS**.

**Core:**
- Frontier: `links_to_crawl` as **Redis sorted set** (priority by site popularity); `crawled_links` holds URL → page **signature**.
- Loop: pop max priority → if similar signature already crawled, *reduce priority* (cycle guard) → else crawl, enqueue Reverse-Index + Document jobs, store signature, move link.
- Classes: `PagesDataStore` (frontier ops), `Page` (url/contents/children/signature), `Crawler` (create_signature, crawl_page, crawl).
- **Dedup:** URLs via `sort | unique` or MapReduce frequency=1; content via signature similarity (Jaccard / cosine).
- **Freshness:** `timestamp` per crawl; default weekly refresh; popular/changed sites sooner; mine mean-time-to-update; honor `robots.txt`.
- Query path: parse → reverse index ranks → document service returns title/snippet.

**Scale pass:** popular queries → memory cache; reverse-index + document services **shard/federation**; crawler-local DNS cache; connection pooling (or UDP); provision bandwidth (crawl is bandwidth-heavy).

## 4. Mint.com — `mint/`

**Scope:** link financial account · extract transactions daily (active in last 30d) · categorize (manual override, no auto re-cat) · monthly spend by category · budget + notifications. Out: extra analytics.

**Numbers:** 10M users · 10 categories each → 100M budget items · 30M accounts · 50k sellers · **5B tx/mo write-heavy (10:1 write:read!)** · 500M reads/mo · ~50 B/tx → 250 GB/mo, 9 TB/3yr · **2,000 tx/s · 200 reads/s**.

**Core:**
- `accounts` table (indexes on id, user_id, created_at) — password **hashed** (char(64)).
- Extraction is slow → Accounts API enqueues job (**SQS/RabbitMQ**) → Transaction Extraction Service pulls from institution → raw logs → Object Store → Category Service → Budget Service → SQL (`transactions`, `monthly_spending`) → Notification Service (async via queue).
- **Category Service:** seed seller→category dict for top sellers (50k × 255 B ≈ **12 MB RAM**); uncategorized sellers learn from user manual overrides via **heap of top override per seller** (O(1) peek_min); `Categorizer.categorize` checks seed map then crowd map.
- Budget notifications needn't be realtime → queue-friendly.

**Scale:** classic ladder from `scaling_aws`; write-heavy may need federation/sharding later; object store for raw logs.

## 5. Social graph shortest path — `social_graph/`

**Scope:** search person → shortest path (unweighted). Constraints: no graph DB/GraphQL (use traditional systems); graph won't fit one machine; 100M users · 50 friends avg → **5B edges** · 1B searches/mo → **400 QPS**.

**Core:**
- Small scale: **BFS** with `prev_node_keys` map → reconstruct path (deque, visit states).
- Large scale: **Lookup Service** (person_id → Person Server) + sharded **Person Servers** (person_id → Person{id,name,friend_ids}) + **User Graph Service** running BFS across shards (lookup per hop — optimization talking point: cache adjacency / colocate high-affinity nodes).
- Classes: `Person`, `LookupService`, `PersonServer`, `UserGraphService`, `Graph.shortest_path`.

**Scale:** shard person servers; cache hot subgraphs; discuss why Neo4j was excluded but when a graph DB *would* win.

## 6. Query cache (KV for search results) — `query_cache/`

**Scope:** cache hit path + miss path for search results. 10M users · 10B queries/mo → **4,000 QPS** · entry (query 50 B + title 20 + snippet 200) ≈ **270 B → 2.7 TB if all cached** → must evict.

**Core:**
- Memory cache (Redis/Memcached) in front of Reverse Index + Document services.
- **LRU:** doubly-linked list (head = newest, tail = evict) + **hash lookup** to nodes for O(1) get/set; on `set` full → pop tail. (Same design as OOD `lru_cache`.)
- `QueryApi.process_query`: parse (markup, terms, typos, case, boolean) → cache get → miss → reverse index → cache set.
- **Update policy:** TTL = cache-aside; invalidate on content change/removal/rank change (page-rank hook).

**Scale:** expand cache across machines (consistent hashing); uneven traffic → cache absorbs spikes.

## 7. Sales rank by category — `sales_rank/`

**Scope:** compute + serve past-week top products per category. Out: the rest of e-commerce. Assumptions: items in multiple categories, no category changes, no subcategories, **hourly refresh** · 10M products · 1000 categories · 1B tx/mo · 100B reads/mo (100:1) · ~40 B/tx → 40 GB/mo · **400 tx/s · 40,000 reads/s**.

**Core:**
- Sales API logs → Object Store → **multi-step MapReduce**: (1) emit `(category, product), sum(qty)` over past week; (2) re-key `(category, quantity), product` so shuffle/sort does a **distributed sort** → identity reducer → insert sorted results into `sales_rank` table (indexes on category_id, product_id).
- Read path: Read API → indexed `sales_rank` rows.

**Scale:** warehouse/MapReduce for aggregation; cache hot category boards; recompute more often for hot products.

## 8. Scale to millions of users on AWS — `scaling_aws/`

The **canonical iterative ladder** — cite this whenever someone jumps to a final design. Loop: **benchmark → profile → fix with trade-offs → repeat.**

| Stage | Bottleneck found | Moves | Costs noted |
|---|---|---|---|
| Start | none (1–2 users) | Single EC2 box, MySQL, static Elastic IP, DNS (Route 53), lock ports (80/443/22-whitelist), vertical scaling + monitor (CloudWatch/top/nagios/statsd/graphite) | Vertical scaling gets expensive; no redundancy |
| **Users+** | DB CPU/mem, disk filling; can't scale tiers independently | Static → **S3**; MySQL → **RDS** separate box; VPC public/private subnets; encrypt transit+rest | More complexity, more security surface, AWS cost vs self-host |
| **Users++** | Web server peaks/downtime; want HA | **ELB/HAProxy**, multi-AZ web servers, **master-slave MySQL failover** multi-AZ, split web (reverse proxy) vs app tier (read/write API split), **CDN (CloudFront)** | LB/reverse-proxy redundancy complexity; SSL termination trade |
| **Users+++** | Read-heavy 100:1 crushing MySQL | **ElastiCache** (first tune MySQL's own cache!) for hot rows + **sessions → stateless autoscalable web**; **read replicas** with read/write split; more app servers | Replica lag; cache invalidation |
| **Users++++** | US business-hours spikes; small team | **Autoscaling** groups per tier multi-AZ, min/max, CloudWatch triggers (time/CPU/latency/network); config mgmt (Chef/Puppet/Ansible); monitoring stack: host/aggregate/log (CloudWatch, CloudTrail, Loggly, Splunk)/external (Pingdom, New Relic)/PagerDuty/Sentry | Scale-up delay; autoscaling complexity |
| **Users+++++** | Growth toward 1B writes + 100B reads/mo | Hot reads → scale cache; old data → **Redshift** (1 TB/mo fine); 400 writes/s stressing single master → federation/sharding/denormalize/tuning; consider **NoSQL (DynamoDB)**; async non-realtime work → **SQS + workers** (photo upload → queue → thumbnail worker) | Each lever's standard trade-offs |

**Numbers anchor:** 10M users · 1B writes + 100B reads/mo (100:1) · 1 KB/write → 1 TB/mo, 36 TB/3yr · **400 writes/s · 40,000 reads/s**.

## Cross-solution patterns (what interviewers are really checking)

1. Read:write ratio picks the first scaling lever (100:1 → cache + replicas before sharding).
2. Write-heavy fanout (Twitter/Mint) → queue + fast-write store; never fanout through a synchronous SQL transaction path at 60k/s.
3. Precompute offline (MapReduce sales rank, crawl reverse-index jobs, Mint aggregates) → read path stays a simple indexed lookup.
4. Shard only when single-box math (from Step 1 estimates) says you must — social graph 5B edges, crawler 72 PB.
5. Same building blocks recur: reverse proxy, LB, cache-aside, master-slave, object store, queue+worker, REST outside / RPC inside.
