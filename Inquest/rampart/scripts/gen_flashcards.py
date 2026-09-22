#!/usr/bin/env python3
"""Generate spaced-repetition flashcards for the rampart skill (system design).

Stdlib only. Emits a built-in deck covering core primer concepts.

Outputs:
  markdown  - Q/A cards for reading or importing
  tsv       - Anki-importable TSV (front<TAB>back[TAB>tags)
  json      - machine-readable cards

Usage:
  gen_flashcards.py --format markdown [--deck core|numbers|scaling|all] [--out FILE]
  gen_flashcards.py --format tsv --deck all --out cards.tsv
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CORE = [
    ("What does CAP theorem say about a distributed system?",
     "Under network partitions you can only strongly support 2 of 3: Consistency, Availability, Partition tolerance. Networks fail, so choose CP or AP.",
     "fundamentals cap"),
    ("Weak vs eventual vs strong consistency?",
     "Weak: reads may miss writes (VoIP, games). Eventual: reads see writes after a delay (DNS, email). Strong: reads immediately see writes, sync replication (RDBMS, transactions).",
     "fundamentals consistency"),
    ("Performance problem vs scalability problem?",
     "Performance: slow for a single user. Scalability: fine alone, slow under load — grows with added resources.",
     "fundamentals"),
    ("Latency vs throughput?",
     "Latency = time for one action; throughput = actions per unit time. Aim for max throughput at acceptable latency.",
     "fundamentals"),
    ("When does availability multiply vs combine?",
     "Components in sequence multiply (0.999×0.999=0.998). Components in parallel/redundant combine: 1−(1−a)(1−b) — two 99.9% → 99.9999%.",
     "fundamentals availability"),
    ("SQL or NoSQL — quick decision?",
     "SQL: structured data, strict schema, joins, transactions, clear scaling. NoSQL: flexible schema, no joins, TB–PB, very high IOPS (clickstream, leaderboards, carts).",
     "data sql nosql"),
    ("What is BASE?",
     "NoSQL alternative to ACID: Basically available, Soft state, Eventual consistency — availability over strong consistency.",
     "data nosql"),
    ("Name the four NoSQL types with their abstractions.",
     "Key-value (hash table), Document (KV with documents as values), Wide column (nested map column families), Graph (nodes + arcs).",
     "data nosql"),
    ("Cache-aside in one sentence?",
     "App checks cache, on miss loads DB and populates cache (lazy loading). Cost: 3 trips per miss, staleness until TTL.",
     "cache"),
    ("Write-through vs write-behind?",
     "Write-through: cache sync-writes DB — fresh reads, slower writes. Write-behind: cache async-writes DB — fast writes, risk of data loss if cache dies first.",
     "cache"),
    ("What is refresh-ahead?",
     "Cache auto-refreshes entries before expiry — lower latency if prediction of future reads is accurate; worse if not.",
     "cache"),
    ("Why is horizontal scaling harder with state?",
     "App servers must be stateless to clone: move sessions to a centralized store (DB or Redis/Memcached).",
     "scaling lb"),
    ("L4 vs L7 load balancing?",
     "L4 routes on transport headers (faster, less flexible). L7 routes on content/cookies (smarter, terminates connections, more work).",
     "scaling lb"),
    ("Reverse proxy vs load balancer?",
     "LB spreads traffic across many equivalent servers (needs ≥2). Reverse proxy is the single public face: SSL, caching, static content — useful even with one backend.",
     "scaling lb"),
    ("Master-slave vs master-master replication?",
     "Slave setup: slaves serve reads, promote on master failure (promotion logic, lag). Master-master: both R/W — conflict resolution, routing, lag or looser consistency.",
     "scaling data replication"),
    ("What is federation?",
     "Functional partitioning: split monolithic DB by function (users, forums, products) — less traffic per DB, parallel writes; cross-federation joins get hard.",
     "scaling data"),
    ("Sharding trade-offs?",
     "Rows split across DBs (consistent hashing for rebalance): scales storage/throughput; costs complex joins, hot-shard skew, app routing complexity.",
     "scaling data"),
    ("Why denormalize?",
     "Redundant copies avoid expensive joins — wins when reads ≫ writes (100:1+). Cost: duplication, harder write-path consistency.",
     "scaling data sql"),
    ("Message queue vs task queue?",
     "MQ: deliver messages (decouple producers/consumers). Task queue: carry job payloads + scheduling for background/compute work (Celery).",
     "async"),
    ("What is back pressure?",
     "Bound queue size; when full return 503 and clients retry with exponential backoff — protects throughput of already-queued work.",
     "async"),
    ("When UDP over TCP?",
     "Lowest latency matters, late data worse than loss, or you implement your own error correction (VoIP, games, streaming). TCP when all data must arrive intact.",
     "network"),
    ("REST vs RPC rule of thumb?",
     "REST exposes data — public APIs, loosely coupled. RPC exposes behavior — internal hot paths, hand-tuned, but tighter coupling and harder debugging.",
     "network api"),
    ("Pick a key strategy for a URL shortener.",
     "base62(md5(ip+timestamp))[:7]: uniform, URL-safe alphabet (unlike base64's +/), 62^7 ≈ 3.5T keys; check PK uniqueness, regenerate on collision.",
     "design hashing"),
    ("Fanout-on-write vs fanout-on-read (feeds)?",
     "On-write: precompute follower timelines — fast reads, storage cost, hard for celebrities. On-read: merge at read time — cheap writes, expensive reads. Hybrid for big accounts.",
     "design feed"),
    ("What should you do BEFORE jumping to a final scaled design?",
     "Iterate: benchmark/load-test → profile bottlenecks → fix while evaluating trade-offs → repeat. Justify each component against Step 1 numbers.",
     "method"),
]

NUMBERS = [
    ("L1 / L2 / main memory reference latencies?",
     "L1 ≈ 0.5 ns · L2 ≈ 7 ns · main memory ≈ 100 ns.",
     "numbers latency"),
    ("Round trip within same datacenter?",
     "≈ 500 µs (0.5 ms) — about 2,000 RTTs/s.",
     "numbers latency"),
    ("HDD seek vs SSD random 4KB read?",
     "HDD seek ≈ 10 ms · SSD random 4KB ≈ 150 µs (~1 GB/s SSD).",
     "numbers latency"),
    ("Cross-continent packet (CA→NL→CA)?",
     "≈ 150 ms — only ~6–7 worldwide RTTs per second.",
     "numbers latency"),
    ("Sequential throughput: HDD / 1Gbps / SSD / memory?",
     "≈ 30 MB/s · ≈ 100 MB/s · ≈ 1 GB/s · ≈ 4 GB/s.",
     "numbers latency"),
    ("Requests/month ↔ QPS conversion?",
     "1 rps ≈ 2.5M requests/month · 40 rps ≈ 100M/month · 400 rps ≈ 1B/month.",
     "numbers estimation"),
    ("2^10, 2^20, 2^30, 2^40?",
     "1 KB · 1 MB · 1 GB · 1 TB.",
     "numbers"),
    ("Downtime budgets: three 9s and four 9s per year?",
     "99.9% → 8h 45m 57s/year · 99.99% → 52m 35.7s/year.",
     "numbers availability"),
]

SCALING = [
    ("Order of SQL scaling levers from least to most invasive?",
     "Master-slave replication → federation → sharding → denormalization → SQL tuning.",
     "scaling data sql"),
    ("How do you absorb uneven read spikes?",
     "Cache (cache-aside) in front of the DB + read replicas for misses; CDN for cacheable content. Watch replication lag and invalidation.",
     "scaling cache"),
    ("Hot shard / power-user skew mitigation?",
     "Consistent hashing for rebalance, split hot keys, cache the hot entity, rate-limit or shed load.",
     "scaling data"),
    ("Cache stampede mitigation?",
     "TTL jitter, refresh-ahead, request coalescing — stop many misses rebuilding the same key.",
     "cache"),
    ("Stateless app server requirements?",
     "No user data on the box: sessions in Redis/DB; config externalized — enables clone-and-scale behind an LB.",
     "scaling lb"),
    ("What breaks first: single primary DB?",
     "Write ceiling + SPOF. Fix order: read replicas → cache → federation → denormalization → shard; each adds cost (lag, complexity, skew).",
     "scaling data"),
    ("Active-passive failover mechanism?",
     "Heartbeats to standby; on failure standby takes the VIP. Hot standby = faster, cold = slower; risk losing unreplicated writes.",
     "availability"),
    ("When to put a CDN in front?",
     "Cacheable static or popular content with geo-distributed users; cost = invalidation (push vs pull CDN choice).",
     "cdn edge"),
]

DECKS = {"core": CORE, "numbers": NUMBERS, "scaling": SCALING}
ANKI_PATH = Path(__file__).resolve().parent.parent / "data" / "anki_cards.json"


def anki_cards(subdeck: str | None = None):
    """Load primer-extracted Anki notes. subdeck: system|exercises|oo|None=all."""
    if not ANKI_PATH.exists():
        return []
    data = json.loads(ANKI_PATH.read_text(encoding="utf-8")).get("decks", {})
    keys = [subdeck] if subdeck else list(data.keys())
    out = []
    for k in keys:
        for c in data.get(k, []):
            front = " ".join(c["front"].replace("\xa0", " ").split())[:400]  # TSV-safe
            back = " ".join(c["back"].replace("\xa0", " ").split())[:800]
            out.append((front, back, f"primer-anki {k}"))
    return [c for c in out if c[0]]


def cards_for(deck: str):
    if deck == "all":
        return CORE + NUMBERS + SCALING + anki_cards()
    if deck == "anki":
        return anki_cards()
    if deck.startswith("anki-"):
        return anki_cards(deck.split("-", 1)[1])
    if deck not in DECKS:
        raise SystemExit(
            f"unknown deck: {deck} (choose from {', '.join(DECKS)}, anki, "
            f"anki-system, anki-exercises, anki-oo, or all)"
        )
    return DECKS[deck]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--format", choices=("markdown", "tsv", "json"), default="markdown")
    p.add_argument("--deck", default="all",
                   help="core|numbers|scaling|anki|anki-system|anki-exercises|anki-oo|all")
    p.add_argument("--out", default=None, help="output file (default: stdout)")
    args = p.parse_args()

    cards = cards_for(args.deck)
    if args.format == "markdown":
        lines = [f"# Flashcards — deck: {args.deck} ({len(cards)} cards)\n"]
        for i, (q, a, tags) in enumerate(cards, 1):
            lines += [f"## {i}. {q}", "", f"**A:** {a}", "", f"`{tags}`", ""]
        text = "\n".join(lines)
    elif args.format == "tsv":
        # Anki: front \t back \t tags
        text = "\n".join(f"{q}\t{a}\t{tags}" for q, a, tags in cards) + "\n"
    else:
        text = json.dumps(
            [{"front": q, "back": a, "tags": tags.split()} for q, a, tags in cards],
            indent=2,
        ) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{len(cards)} cards → {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
