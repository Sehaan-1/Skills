# Scoring rubric

Score each candidate **0–5** on four axes, then compute a weighted total (also 0–5). Scores are judgments, not measurements — the goal is a defensible ordering, not false precision. Always be able to say *why* a candidate got its score in one sentence.

## Weights

Default: **25% each**. Shift weights when the user states priorities, and state the weights in the report:

| User says | Suggested weights (Perf / Maint / License / DX) |
|---|---|
| nothing | 25 / 25 / 25 / 25 |
| "performance matters most" | 40 / 20 / 20 / 20 |
| "this is a long-lived product, stability matters" | 20 / 40 / 20 / 20 |
| "we're a company / legal cares" | 20 / 20 / 40 / 20 |
| "we're beginners / want smooth onboarding" | 20 / 20 / 20 / 40 |

License compatibility also acts as a **hard gate** (see `licensing.md`): a hard incompatibility with the user's project disqualifies a candidate regardless of score, though it can be listed as a flagged runner-up.

## Axis 1: Performance

What the SDK costs at runtime: throughput, latency, memory, cold-start time, binary/payload size, and whether its design fits the workload (async vs blocking, pooling, streaming vs buffering).

- **5** — Best-in-class for the workload; architected for it (e.g., zero-copy, native bindings to a proven engine, async where needed).
- **3–4** — Good enough for typical workloads; no known hot-path problems.
- **1–2** — Known bottlenecks for this use case (e.g., blocking I/O in a high-throughput path, huge dependency tree on a cold-start-sensitive runtime).

Evidence hierarchy: published benchmarks > architectural reasoning > vibes. Never invent numbers. If you have no direct evidence, score from architecture ("pure-Python serialization will trail native bindings at high throughput") and say that's what you're doing. When the user's workload is small (a CRUD app calling an API a few times/sec), say performance is a non-differentiator and score tightly — don't manufacture a gap.

## Axis 2: Active maintenance

Will this library still be alive and safe in 12–24 months? Signals: release recency and cadence, issue/PR responsiveness, history of timely security patches, backing (large company, foundation, funded team vs one volunteer), breaking-change discipline, deprecation notices.

The facts script gives release dates; calibrate:

- **5** — Regular releases within the last ~3 months, responsive maintainers, institutional backing or a large healthy contributor base.
- **4** — Release within ~6 months, responsive issues, clear ongoing activity.
- **3** — Release within ~13 months; slow but alive. Fine for stable, mature libraries.
- **2** — 1–2+ years since a release, unanswered issues piling up.
- **1** — Effectively abandoned or officially deprecated; only recommendable if there is truly no alternative and the risk is spelled out.

Note: *old and stable* (e.g., a finished, battle-tested spec implementation) is not the same as *abandoned*. A library that rarely changes because it's done can still be a 4–5 if issues get triaged and it tracks the standards it implements. For official vendor SDKs, maintenance usually tracks the vendor's own business interest — usually strong, but watch for the vendor sunsetting the product.

## Axis 3: License compatibility

Two layers:

1. **Hard gate** — is the license compatible with the user's project? See `licensing.md`. Incompatible → disqualified (mention as flagged runner-up only).
2. **Soft score** — among compatible candidates:
   - **5** — Maximally permissive for the context (MIT/BSD/ISC/Apache-2.0 for commercial work), clearly declared SPDX identifier, no CLA gotchas.
   - **4** — Permissive with minor friction (e.g., Apache-2.0 NOTICE obligations, dual-license where the free side is fine).
   - **3** — Weak copyleft (LGPL/MPL/EPL) usable with care under the user's setup.
   - **≤2** — Copyleft that technically fits but creates real compliance work, or license is **unknown/ambiguous** (treat unknown as a risk to resolve, not a default-pass).

## Axis 4: Developer experience

How fast can the user go from `install` to working code, and how painful is maintenance after? Signals: docs quality and quickstart, official-vs-community status (official SDKs usually track API changes), typed interfaces/IDE support, clear error messages, runnable examples, community size for googling errors (Stack Overflow, GitHub stars as a rough proxy), semver discipline, migration guides between major versions.

- **5** — Official or flagship-quality: excellent docs, quickstart that works, types, active community.
- **3–4** — Good docs, some rough edges; community answers findable.
- **1–2** — Sparse docs, trial-and-error setup, error messages that don't help, or frequent breaking changes without guides.

## Reporting scores

Show per-axis scores and the weighted total in the comparison table. Round totals to one decimal. If two candidates land within ~0.3 of each other, call it a near-tie, pick one anyway (users need a decision), and state what would tip the balance the other way.
