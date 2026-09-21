# Research Scout and Dossier Protocol

# Scout (research first, always first)

The engine is only as good as its sources. Spin up a **background agent** (or parallel subagents) for the reading so you can keep aiming and structuring in parallel. If this harness has no background tool, do the research yourself first, write the dossier, then design — do not skip the artifact.

One question per dossier. Two independent unknowns, two dossiers. Reuse an existing dossier instead of investigating the same primary source twice.

## What counts as primary

A source is primary for the claims *it owns*. Match the claim to its owner:

| The claim is about | Its owner | Primary form |
| --- | --- | --- |
| What an API or library does | Its first party | Official docs, the library's own source code, its tests, its changelog and issue tracker |
| What a format, protocol, or primitive means | The spec that defines it | RFC, ISO, ECMA, IEEE, W3C, NIST FIPS, the language reference |
| What an algorithm guarantees | The source that proved it | The original paper, the textbook proof, the reference implementation's code and its tests |
| How fast something really is | Your measurement | A benchmark you ran at your real n, on the reference implementation, output pasted |
| What you derived yourself | You | The derivation, in the spec, marked DERIVED |

A vendor's speed claim is a claim by the vendor until you reproduce it. A README is marketing next to the code that ships. A tutorial, a summary site, a blog post, an AI answer, a wiki: **signposts** — use them to find the primary, never as the citation.

## Rules

- **Follow every claim back to the source that owns it.** Not to someone's write-up of that source. If the chain stops at a summary, keep walking or mark it.
- **Read the reference implementation's source, not just its docs.** The behavior lives in the code and its tests. Where docs and code disagree, say which wins and why — usually the code, until the docs' version is confirmed by the maintainer or a test.
- **Unreachable primary → `UNVERIFIED`, and de-loaded.** If the paper is paywalled, hunt the author's copy, the arXiv version, the conference site, the reference code. If the primary still cannot be reached this sitting, the claim is marked UNVERIFIED in the dossier and **cannot be load-bearing**: the engine is redesigned around the hole, or the sitting stops and says what is missing.
- **Measure as research.** Where cost matters, run the reference implementation on real-scale inputs and paste the real numbers into the dossier: command, machine, date, input sizes. This is an estimate fed with data, not a guess. The recorded output is the artifact; the scratch script is not committed.
- **Never code a foreign shape from memory.** If the engine depends on an API, a format, or a constant, the dossier anchors it to its owner before any ticket assumes it.
- **A finding that contradicts an ADR, the ticket's premise, or the slice Check is a stop** — aim again, or a cuecards sitting. Not a silent product change.

## The dossier

`docs/research/<engine-slug>.md` — the same species as oneslice's research files, heavier. Committed before anything that depends on it.

```markdown
# Dossier: <the question, in one sentence>

- **For engine:** docs/siegecraft/<slug>.md
- **Date:** YYYY-MM-DD · **Researched by:** <agent name>

## Sources consulted
| # | Source | Kind | What it owns | Link / path |
| --- | --- | --- | --- | --- |
| 1 | <RFC 9110 §5.1> | primary spec | <semantic of the field> | <url> |
| 2 | <Author, "Title", venue year, §4> | primary paper | <the guarantee> | <url or local copy path> |
| 3 | <org/repo @ commit, src/thing.ts L120-180> | reference code | <actual behavior> | <permalink> |

## Findings
### F1. <claim>
- **CITED** — <owner, exact anchor>: <what it actually says — quote or tight paraphrase, not a summary of a summary>
- **So what:** <consequence for the engine>

## Measured
<command, machine, date, input size — output pasted>

## Unverified
<claims with no owner reached yet, and why the engine does not rest on them>

## Contradictions
<any two owners disagree; which wins and why>
```

Findings are rewritten so the next reader — the spec, the builder, the next siegecraft sitting — can use them without re-opening the paper. Facts are the scout's job; choices are not.

---

