---
name: armory
description: "Recommends the best SDK, client library, driver, or API wrapper for a given programming language, framework, and use case: scores candidates on performance, active maintenance, license compatibility, and developer experience, then returns a single top pick with honest trade-offs, a scored comparison of alternatives, and a ready-to-run initialization snippet. Use this skill whenever someone must choose between integration libraries — which SDK or package to use, which of several gems/crates/packages is actually maintained, whether to adopt an SDK at all or call a REST API directly, or standardizing a library choice across a team — even if they never say 'SDK' or 'recommend'. Do NOT use for writing, using, debugging, migrating, or configuring a library that was already chosen; general licensing or legal questions with no library decision involved; conceptual SDK-vs-API questions; dependency audits or CVE checks; or picking services or models (e.g., which LLM)."
---

# Armory

The castle's armory is where you pick the right weapon before the campaign. This skill does that for SDKs: it helps the user commit to ONE library with confidence. The deliverable is a short Markdown report: a top choice, a scored comparison, honest trade-offs, and an initialization snippet they can paste straight into their project.

Armory picks the weapon after the architecture has decided a slot exists. Whether the wall must stand at ten times the load — the architecture itself, capacity verdicts, design trade-offs — is rampart's sitting (Inquest), not this one.

Users come to this skill because choosing an SDK is expensive to get wrong — swapping one later means rewriting glue code — and because the signals that matter (is it still maintained? will legal sign off on the license?) are scattered across registries, GitHub, and docs. Your job is to gather those signals and do the weighing for them.

## Inputs

The request is framed by three inputs, possibly incomplete:

| Input | Examples | If missing |
|---|---|---|
| Language (and version if given) | Python 3.12, Rust, Kotlin | infer from the framework |
| Framework / runtime | FastAPI, Android, Actix, Lambda | assume general-purpose |
| Use case | "Stripe checkout", "high-throughput Kafka consumer" | ask — this one is not guessable |

Optional modifiers that change the analysis: stated priorities ("performance matters most"), the user's own project license ("we're closed source"), deployment constraints (serverless cold starts, embedded, mobile binary size, offline builds).

Do not stall on intake. Fill gaps with sensible defaults and list every assumption in the report's **Assumptions** section so the user can correct it. Ask a clarifying question only when the missing input could flip the recommendation — the classic case is an unknown project license when the strongest candidate is copyleft.

## Workflow

### 1. Frame the request
Restate the need in one sentence: *language + framework + what the integration must do + any stated constraints.* This sentence anchors candidate discovery; a misframed request produces plausible-but-wrong candidates.

### 2. Build the candidate set
List 3–5 candidates. A good set usually spans:
- the **official SDK** (if the service vendor publishes one),
- **community alternatives** with real adoption,
- the **generic fallback** (raw HTTP/REST client, language stdlib) when it is genuinely competitive.

Drop candidates that obviously fail a hard constraint (wrong language, archived/unmaintained, license the user already ruled out). Prefer candidates you have real knowledge of over exotic ones — a recommendation the user can't verify is worse than a boring one. A well-known candidate you excluded (e.g., a wrapper for a different framework) is worth one line in the report — "considered X, dropped because Y" preempts the user's most likely follow-up question.

### 3. Gather live facts
If network/tool access is available, run the bundled facts script for every candidate — it pulls latest version, release date, license, repository, and downloads straight from the registry, which beats memory for maintenance and license questions:

```bash
python scripts/fetch_package_facts.py pypi:stripe npm:@stripe/stripe-js crates:rdkafka maven:org.apache.kafka:kafka-clients go:github.com/aws/aws-sdk-go-v2
```

Spec format is `ecosystem:package-name`; supported ecosystems: `pypi`, `npm`, `crates`, `rubygems`, `nuget`, `maven` (needs `group:artifact`), `go` (module path). Individual failures don't abort the run — a package that can't be resolved comes back with `"found": false` and an error message.

If a web search tool is also available, use it to fill gaps the script can't see: recent announcements, deprecations, known issues, benchmark comparisons, maintainer responsiveness. Cite anything important you learn this way.

Two failure modes to watch for:
- **Partial egress.** Sandboxed environments sometimes block some registries at the network level while others work, or while a browser-style fetch tool still gets through. If the script fails for a host, retry that package through whatever fetch/search tool is available before falling back to knowledge — a partial live picture beats a fully stale one.
- **Stale search indexes.** Registry *search* APIs lag behind canonical records (e.g., Maven search has reported versions months behind the true latest). When a release date or version drives the recommendation, prefer the canonical source (registry JSON endpoint, `maven-metadata.xml`) and say which one you used.

If you have NO network access at all, say so in the report, proceed from knowledge, date every maintenance claim ("as of early 2025"), and tell the user to re-check release recency before committing.

### 4. Score the candidates
Read `references/scoring.md` for the full rubric. In short: score each candidate 0–5 on four axes — **performance**, **active maintenance**, **license compatibility**, **developer experience** — then compute a weighted total. Default weights are equal (25% each); shift them when the user states priorities (e.g. "performance is the top concern" → ~40% performance, 20% each other). Show the weights you used.

Never fabricate benchmark numbers, download counts, or star counts. Use script/search output when you have it; otherwise use qualitative language ("widely benchmarked as the fastest option", "low adoption") and mark it as such.

### 5. Apply the license gate
License incompatibility with the user's project is a hard constraint, not a scoring penalty — a brilliant GPL library is the wrong answer for a closed-source product. Read `references/licensing.md` when a candidate's license is anything other than the obviously-safe permissive set (MIT/BSD/ISC/Apache-2.0) or when the user's project is copyleft itself. Unknown license = flag as a risk, don't assume it's fine.

### 6. Write the report
Use this template exactly — the fixed shape is what makes the output skimmable and comparable across recommendations:

```markdown
# SDK Recommendation: <use case> — <language>/<framework>

**Top pick: `<package>` (license, vX.Y.Z)** — one-sentence rationale.

## Why it wins
2–4 bullets tied to the four axes and the user's stated priorities.

## Comparison
| Candidate | Performance | Maintenance | License | DX | Weighted |
|---|---|---|---|---|---|
| `winner` | 4/5 | 5/5 | ✅ MIT | 5/5 | **4.6/5** |
| `runner-up` | ... | ... | ... | ... | ... |

Weights used: <state them>. Facts verified live on <date> / from knowledge as of <date>.

## Trade-offs
- Honest downsides of the top pick (be specific — dependency weight, maturity gaps, vendor lock-in...).
- What you give up by not choosing the runner-up, and when the runner-up would be the better call.

## Getting started
Install command, then a minimal snippet: client initialization + the smallest example
matching the user's actual use case (not a generic hello-world).

## Assumptions & caveats
- Every default you assumed (priorities, project license, runtime...).
- Data freshness: which facts are live-verified vs. from knowledge.
- Anything the user should verify before committing (e.g. license text, latest breaking changes).
```

## Ground rules

- **Snippet fidelity matters.** The initialization snippet is the part users run blind. If you are not certain the top pick's current API matches your snippet, verify it against the official docs (fetch the quickstart page) before writing it. Include the install command, client initialization with placeholder credentials, and a minimal example of the user's actual use case.
- **Keep it tight.** Target ~400–600 words plus the snippet. The comparison table does the heavy lifting; don't narrate what it already shows.
- **Recommend "none of these" when true.** If no SDK is genuinely good — tiny ecosystem, everything abandoned — say so, recommend the fallback (usually a raw REST/HTTP client), and explain why. A forced weak pick erodes trust in all your other recommendations.
- **Disclose uncertainty.** Stale knowledge, unverified claims, or a close call between two candidates should be visible in the report, not papered over. Close calls are fine — pick one anyway (users need a decision, not a shrug) and say what would tip it the other way.
