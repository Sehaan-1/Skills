# Primary-Source Research & Investigation Dossier

When an algorithm is complex or risks mathematical failure, research primary sources before designing specifications.

## What Counts as Primary

A source is primary for the claims it directly owns:

| Claim Domain | Owner | Primary Form |
| --- | --- | --- |
| Library or API behavior | First-party maintainer | Official reference documentation, source repository, test suites |
| Protocol, data format, primitive | Standards body | RFC, ISO, W3C, IEEE, NIST specification |
| Algorithmic guarantees & proofs | Originating authors | Original peer-reviewed paper, mathematical textbook proof, reference implementation |
| Real-world performance / latency | Empirical measurement | Benchmark run against reference implementation with environment and numbers pasted |

Blog posts, community tutorials, AI answers, and wikis are **signposts** to locate primary sources, never valid citations themselves.

---

## Investigation Rules

1. **Follow claims to the origin:** Trace every assumption back to the authoritative specification or paper.
2. **Inspect source code:** Behavior lives in reference implementations and test suites. Where documentation and code disagree, benchmark the code.
3. **Handle unreachable sources:** If a source is paywalled or unavailable, label the claim `UNVERIFIED` and do not allow the algorithm's correctness to depend on it.
4. **Benchmark real scales:** Measure reference implementations at production input sizes ($N$) and paste the raw commands and outputs.

---

## Dossier Template

Save research findings at `docs/research/<slug>-dossier.md`:

```markdown
# Research Dossier: <Question or Algorithmic Problem>

- **Target Spec:** docs/siegecraft/<slug>-spec.md
- **Date:** YYYY-MM-DD
- **Researched by:** <agent name>

## Sources Consulted
| # | Citation | Type | What It Proves | Link / DOI |
| --- | --- | --- | --- | --- |
| 1 | <RFC / Paper title> | primary spec | Formal invariant definition | <URL> |

## Verified Findings
### F1. <Claim>
- **Citation:** <Exact section / line reference>
- **Fact:** <Verbatim text or precise formula>
- **Impact on Algorithm:** <How this shapes the implementation>

## Empirical Measurements
- Command: `<benchmark command>`
- Machine & Date: `<hardware details, date>`
- Output: `<pasted console output>`

## Unverified Claims & Contradictions
- <List of assumptions not backed by primary citations>
```
