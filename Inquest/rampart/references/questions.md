# Interview question catalog

Use this to pick practice questions, find worked solutions in this repo, and extend practice beyond the solved set.

> **Standalone note:** if this package is used outside the system-design-primer repo, the `solutions/…` paths below won't resolve — still use the "core techniques" column as a study checklist, and run each question with the 4-step method from `SKILL.md`. The additional-questions table is fully standalone (reference links are external URLs).

## Solved system design questions (worked solutions in this repo)

Each solution follows the 4-step format with diagrams. Read the linked `README.md` and mirror its structure when the user asks one of these.

| Question | Solution | Core techniques exercised |
|---|---|---|
| Design Pastebin.com (or Bit.ly) | `solutions/system_design/pastebin/README.md` (+ runnable `pastebin.py`) | key generation (MD5 + base62), SQL schema + indexes, REST API, object store, MapReduce analytics, expiration jobs |
| Design the Twitter timeline and search (or Facebook feed and search) | `solutions/system_design/twitter/README.md` | fanout on write vs pull, timelines at scale, search indexing |
| Design a web crawler | `solutions/system_design/web_crawler/README.md` | BFS frontier, politeness/robots, URL normalization, distributed crawl, dedup (bloom filters) |
| Design Mint.com | `solutions/system_design/mint/README.md` | aggregating financial data, scraping vs API, data modeling |
| Design the data structures for a social network | `solutions/system_design/social_graph/README.md` | graph storage, adjacency lists, friend/feed queries, OOD of the data layer |
| Design a key-value store for a search engine | `solutions/system_design/query_cache/README.md` | cache hierarchy, TTL/LRU, consistency under load |
| Design Amazon's sales ranking by category | `solutions/system_design/sales_rank/README.md` | aggregation pipelines, sorted structures, precomputation |
| Design a system that scales to millions of users on AWS | `solutions/system_design/scaling_aws/README.md` | full AWS stack: ELB, EC2 autoscaling, RDS/replicas, ElastiCache, CloudFront, S3 |

Empty starter: `solutions/system_design/template/` (diagram template for new solutions).

## Solved object-oriented design questions

Notebooks + Python in `solutions/object_oriented_design/<name>/`:

| Question | Solution |
|---|---|
| Design a hash map | `hash_table/` |
| Design a least recently used cache | `lru_cache/` |
| Design a call center | `call_center/` |
| Design a deck of cards | `deck_of_cards/` |
| Design a parking lot | `parking_lot/` |
| Design a chat server | `online_chat/` |

OOD method: identify classes/interfaces and relationships first (inheritance, composition), cover concurrency and persistence, then write the core methods — validate with the primer's linked notebooks.

## Additional system design questions (not solved in-repo — run the 4 steps yourself)

| Question | Reference in primer appendix |
|---|---|
| File sync service (Dropbox) | youtube walkthrough linked in README |
| Search engine (Google) | queue.acm.org, Stanford PageRank paper |
| Scalable web crawler | quora.com |
| Google Docs (realtime collab) | mobwrite / neil.fraser.name sync essays |
| Key-value store (Redis) | codecapsule.com, Dynamo paper |
| Cache system (Memcached) | slideshare intro |
| Recommendation system (Amazon) | hulu.com, IJCAI tutorial |
| TinyURL (Bitly) | n00tc0d3r blog |
| Chat app (WhatsApp) | highscalability WhatsApp architecture |
| Picture sharing (Instagram) | highscalability Instagram architecture |
| Facebook news feed | quora + slideshare activity feeds |
| Facebook timeline | facebook.com notes (denormalization) |
| Facebook chat | Erlang at Facebook papers |
| Graph search (Facebook) | facebook.com notes series |
| CDN (CloudFlare) | figshare |
| Trending topics (Twitter) | michael-noll, snikolov |
| Random ID generation (Snowflake) | blog.twitter.com, github/twitter/snowflake |
| Top-k requests in a time window | cs.ucsb.edu, wpi.edu papers |
| Multi-datacenter serving | highscalability Google multi-DC |
| Online multiplayer card game | indieflashblog, buildnewgames |
| Garbage collection system | stuffwithstuff, washington.edu |
| API rate limiter | stripe.com/blog/rate-limiters |
| Stock exchange (NASDAQ/Binance) | Jane Street video, Go limit-order implementations |

Full link list: `README.md` → "Additional system design interview questions".

## Real-world architectures to study (pattern-spotting, not trivia)

Per the primer: identify **shared principles, common technologies, and patterns**; note what problem each component solves, where it works and fails; review lessons learned.

- **Data processing:** MapReduce, Spark, Storm
- **Data stores:** Bigtable, HBase, Cassandra, DynamoDB, MongoDB, Spanner, Memcached, Redis
- **File systems:** GFS, HDFS
- **Misc:** Chubby (locks), Dapper (tracing), Kafka (pub/sub), Zookeeper (coordination)

Company architecture write-ups (Amazon, Google, Twitter, Uber, Netflix, WhatsApp, …) and engineering blogs: see `README.md` appendix sections "Company architectures" and "Company engineering blogs". Recommend reading a few for the target company before an interview.

## Study plan (from the primer's Study guide)

| Activity | Short | Medium | Long |
|---|---|---|---|
| Read system design topics for breadth | ✓ | ✓ | ✓ |
| Read target-company engineering blogs | ✓ | ✓ | ✓ |
| Read real-world architectures | ✓ | ✓ | ✓ |
| Review the 4-step interview method | ✓ | ✓ | ✓ |
| Work system design solutions | some | many | most |
| Work OOD solutions | some | many | most |
| Review additional questions | some | many | most |

Short timeline → breadth. Medium → breadth + some depth. Long → breadth + more depth. Nobody needs *everything*; start broad, then go deep in a few areas.
