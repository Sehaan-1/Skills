# Repo map — everything in system-design-primer and where the skill uses it

Coverage map of the upstream repo (`github.com/donnemartin/system-design-primer`) so nothing is learned in isolation. Paths under `repo/` exist only when the primer is checked out; the right column shows what already ships **inside this package** for standalone use.

## Primer README.md

| README section | Learned into (this package) |
|---|---|
| Motivation (learn large-scale design · open source community · interview prep) | This skill's purpose: coach/architect grounded in the primer (`SKILL.md` intro). The primer is free, community-maintained, and organized for interview prep — treat it as the source of truth. |
| Anki flashcards | Extracted → `data/anki_cards.json` (56 cards) via `scripts/gen_flashcards.py --deck anki*`; originals at `resources/flash_cards/*.apkg` when repo present (see `study-extras.md`) |
| Coding Resource: Interactive Coding Challenges | Sister repo: `github.com/donnemartin/interactive-coding-challenges` (algo/coding practice + another Anki deck) — recommend alongside `study` mode when the user also preps coding rounds |
| Index of system design topics | → `topic-playbook.md` (+ `quick-reference.md` for appendix numbers) |
| Study guide (short/medium/long timeline table) | → `questions.md` §Study plan |
| How to approach a system design interview (Steps 1–4 + back-of-envelope) | → `SKILL.md` §Core method + `worked-exemplar.md` + `estimate.py` |
| System design interview questions with solutions (8) | → `solutions-index.md` (all 8 distilled) + `worked-exemplar.md` (pastebin full) + `questions.md` |
| Object-oriented design questions (6) | → `ood-solutions.md` + `questions.md` §OOD |
| **System design topics: start here** | Beginner path (below) |
| Performance vs scalability · Latency vs throughput · CAP · Consistency patterns · Availability patterns (failover, replication, 9s) | → `topic-playbook.md` §Foundations + `quick-reference.md` §Availability |
| DNS · CDN (push/pull) · Load balancer (L4/L7, horizontal) · Reverse proxy · Application layer (microservices, service discovery) | → `topic-playbook.md` §Edge + §Application + `diagrams.md` |
| Database (RDBMS: master-slave/master-master/federation/sharding/denormalization/SQL tuning · NoSQL: KV/document/wide-column/graph · SQL or NoSQL) | → `topic-playbook.md` §Data layer + `solutions-index.md` technique cribs |
| Cache (levels, query vs object, cache-aside/write-through/write-behind/refresh-ahead) | → `topic-playbook.md` §Caching + `ood-solutions.md` §LRU + `query_cache` entry |
| Asynchronism (message queues, task queues, back pressure) | → `topic-playbook.md` §Asynchronism + `diagrams.md` §6 |
| Communication (HTTP verbs, TCP, UDP, RPC, REST, RPC-vs-REST table) | → `topic-playbook.md` §Communication + RPC vs REST table |
| Security basics | → `topic-playbook.md` §Security |
| Appendix: powers of two · latency numbers · additional questions · real-world architectures · company architectures · company engineering blogs | → `quick-reference.md` · `questions.md` (additional Qs + real-world architectures) · `study-extras.md` (blogs, company architectures) |
| Under development (MapReduce · consistent hashing · scatter gather) | → `study-extras.md` §stretch + playbook notes + `solutions-index.md` (MapReduce in sales_rank/crawler/mint/pastebin) |

### System design topics: start here (beginner resources — external)

1. **Scalability video lecture** — [Harvard CS265 Scalability](https://www.youtube.com/watch?v=-W9F__D3oY4): vertical/horizontal scaling, caching, load balancing, DB replication & partitioning.
2. **Scalability article series** (lecloud "Scalability for Dummies"): Clones · Databases · Caches · Asynchronism.
3. Then high-level trade-offs (performance vs scalability, latency vs throughput, availability vs consistency) — *"everything is a trade-off"* — then DNS/CDN/LB deep dives.

Offer this path in `study` mode when the user is new to system design.

## solutions/ tree

| Path | Package counterpart |
|---|---|
| `solutions/system_design/{pastebin,twitter,web_crawler,mint,social_graph,query_cache,sales_rank,scaling_aws}/README.md` | `worked-exemplar.md` + `solutions-index.md` |
| Runnable code: `pastebin.py`, `*_snippets.py`, `*_mapreduce.py` | Techniques captured as pseudocode in exemplar/index; run originals when repo present |
| `solutions/system_design/template/` | Blank diagram template — use `diagrams.md` instead |
| `solutions/object_oriented_design/{hash_table,lru_cache,call_center,deck_of_cards,parking_lot,online_chat}/` (.py + .ipynb) | `ood-solutions.md` (class designs from the .py sources) |

## resources/ · meta

| Path | Notes |
|---|---|
| `resources/flash_cards/{System Design, System Design Exercises, OO Design}.apkg` | Extracted → `data/anki_cards.json` (56 notes). Import originals into Anki when repo present. |
| `images/` | Primer diagrams (imgur mirrors) — package uses mermaid equivalents in `diagrams.md` |
| `README-ja.md`, `README-zh-Hans.md`, `README-zh-TW.md`, `TRANSLATIONS.md` | Translations of the primer — cite if the user prefers JA/ZH |
| `CONTRIBUTING.md`, `.github/PULL_REQUEST_TEMPLATE.md` | Contribution workflow for improving the primer itself |
| `generate-epub.sh`, `epub-metadata.yaml` | Build an offline EPUB of the README |
| `LICENSE.txt` (MIT, © Donne Martin) | Skill metadata carries `license: MIT` |

## What is intentionally not re-hosted in the package

- Full prose of every solution (condensed instead — avoid duplicating 300+ KB)
- Company-architecture deep-dive URLs beyond names (see primer README appendix when repo present)
- Binary `.apkg` scheduling data (notes extracted; Anki owns the scheduling)
- Sister coding-challenges repo content (different skill — point users there)

If a request needs any of the above and the repo is present, open the original; otherwise degrade per `SKILL.md` §Standalone mode.
