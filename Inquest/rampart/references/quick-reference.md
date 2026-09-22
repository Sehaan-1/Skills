# Quick reference: numbers for back-of-the-envelope estimation

Source: appendix of `README.md` (System Design Primer). Use these while doing Step 1 / Step 4 math.

## Powers of two

```
Power           Exact Value         Approx Value        Bytes
---------------------------------------------------------------
7                             128
8                             256
10                           1024   1 thousand           1 KB
16                         65,536                       64 KB
20                      1,048,576   1 million            1 MB
30                  1,073,741,824   1 billion            1 GB
32                  4,294,967,296                        4 GB
40              1,099,511,627,776   1 trillion           1 TB
```

## Latency numbers every programmer should know

```
Latency Comparison Numbers
--------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 us
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
HDD seek                            10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from HDD     30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns
```

Handy throughput metrics:

- HDD sequential read: ~30 MB/s
- 1 Gbps Ethernet sequential read: ~100 MB/s
- SSD sequential read: ~1 GB/s
- Main memory sequential read: ~4 GB/s
- ~6–7 worldwide round trips per second
- ~2,000 round trips per second within a data center

## Requests-per-month conversion guide

- ~2.5 million seconds per month
- 1 request/second = 2.5 million requests/month
- 40 requests/second = 100 million requests/month
- 400 requests/second = 1 billion requests/month

## Estimation recipe (Step 1 / Step 4)

For a given constraint set, compute in this order — round aggressively:

1. **QPS** — monthly/daily requests ÷ seconds in period; separate peak (assume 2–3× average) from average.
2. **Storage** — size per record × records written per period → GB/TB per month and over the product lifetime.
3. **Bandwidth** — QPS × response size (and upload QPS × payload).
4. **Memory/cache** — working set of hot data that must fit in RAM.
5. **Shard/cluster count** — per-node capacity headroom ÷ required capacity; keep ~2× headroom for peaks.

Example (from the Pastebin solution): 10M writes + 100M reads per month, 1.27 KB per paste → ~12.7 GB/month, ~450 GB over 3 years; 10:1 read:write → ~40 reads/s and ~4 writes/s average (≈100–120 reads/s peak).

## Availability in numbers

Availability = uptime as a percentage; “nines” of availability:

| Level | Downtime/year | Downtime/month | Downtime/day |
|---|---|---|---|
| 99.9% (three 9s) | 8h 45m 57s | 43m 49.7s | 1m 26.4s |
| 99.99% (four 9s) | 52m 35.7s | 4m 23s | 8.6s |

Composition math:

- Components **in sequence** multiply: `A_total = A_foo × A_bar` (two 99.9% services → 99.8%)
- Components **in parallel** (redundancy) combine: `A_total = 1 − (1−A_foo)(1−A_bar)` (two 99.9% → 99.9999%)

## Quick rules of thumb

- Reads usually outnumber writes 10:1 to 1000:1 — design the read path first.
- Memory reads are ~1000× faster than HDD seeks — cache hot data, index everything you filter on.
- In-datacenter RTT ~0.5 ms; cross-continent RTT ~150 ms — count network hops on the critical path.
- 62^7 ≈ 3.5 trillion 7-char base62 tokens — enough short IDs for hundreds of millions of records with margin.
