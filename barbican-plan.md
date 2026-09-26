# barbican — decision log (planning artifact, v0.1 draft)

> Purpose: single source of truth for how the `barbican` README skill behaves.
> Every row below was decided in the planning interview. "Rejected" columns exist so
> nobody "fixes" a deliberate choice later. Nothing has been built yet.

## 0. One-paragraph intent

`barbican` is an Agent Skill (portable `SKILL.md` format) that, when asked to create,
update, refresh or audit a repository's README, inspects the repo **read-only**, builds on the
**existing README** (verbatim-first), and writes **two draft files only** —
`README.draft.md` and `README.draft.review.md`. It never asks questions, never runs project
commands, never edits `README.md`. Every claim in the draft is tiered by evidence; anything it
could not verify is a visible `TODO(maintainer)` marker. It must pass a self-review gate
(including a ledger proving every original section was accounted for) before writing.

---

## A. Foundation

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| A1 | Portable Agent Skills format (`SKILL.md` + frontmatter `name`, `description`; optional `license`, `metadata`, `compatibility`) | Claude-Code-only features, Cursor `.mdc`, plain prompt | Runs in Claude Code, Codex, Cursor, etc. No `allowed-tools` reliance. |
| A2 | `SKILL.md` + `references/` + `assets/`; **no `scripts/`** | Executable scanners | No runtime dependency; determinism comes from catalogs/checklists, not code. |
| A3 | **One-shot, never asks** | Interview-first; hybrid | Gaps become markers, not questions. Drives G4 and B2. |
| A4 | **Draft file** output; `README.md` untouched | In-place edit; in-place + summary | The draft *is* the human review step, which is what makes one-shot acceptable. |

## B. Honesty policy

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| B1 | **Three evidence tiers**, phrasing differs per tier: T1 code/config/CI → stated as fact; T2 docs/comments/commits/issues → attributed ("the design notes say…"); T3 none → marker, never invented | Two-tier; judgment-only | Commit/PR messages are usually the only place "why" lives; T2 keeps them without laundering them into facts. |
| B2 | Unverifiable → **visible inline marker** `> ⚠️ TODO(maintainer): …` **plus a checklist block at the top of the draft** listing every marker | Hidden HTML comments; silent omission; end-section only | A draft must look unfinished where it is unfinished. Block is deleted on promotion. |
| B3 | **Hard ban list** (`references/language-policy.md`) **+ "evidence or delete"** for any performance/scale/security adjective; **applies to inherited text too** | Soft rule; new-text-only | Otherwise the skill knowingly ships inherited puffery. |
| B4 | **Always** a one-line **Status** (inferred; basis stated in a marker) **and** a **Known limitations** section (mined from TODO/FIXME, open bug issues, existing caveats; if none found it says so explicitly) | Only-when-confident; badges-only | Absence of a limitations section reads as "no limitations". |

## C. Badges

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| C1 | **Artifact-backed only**, via `references/badge-catalog.md` mapping repo artifacts → badges | Always-on meta badges; "everything plausible" | No artifact, no badge. |
| C2 | **Static, offline rule**: registry/coverage/docs badges require a **publish/upload step in CI** (npm publish, twine/uv publish, cargo publish, codecov-action…) | Network verification; config-is-enough | Deterministic and offline. **Accepted cost:** manually-published packages get no registry badge (mitigated by C2×C4). |
| C2×C4 | An **inherited** registry badge with no CI publish step is **Tier-2 evidence → kept + marker** ("confirm package is published under this name") | Strict removal; manifest-name heuristic | Don't delete something that probably works. |
| C3 | shields.io **`flat`**, **max 8**, fixed order: CI status → coverage → version/release → downloads → license → docs → community/code-style. Overflow is **dropped**, not hidden. One line, no table. | flat-square/no cap; for-the-badge; match-existing | Predictable header; loud styles read as marketing. |
| C4 | Inherited badges are **re-verified under the same rules**, style-normalised, removals listed in the change summary | Keep verbatim; keep+flag | Consistent with B3. |
| C5 | **Detect visibility** (`gh repo view --json isPrivate` if authed; else remote/API); **private or unknown → GitHub-native workflow badge + static label badges only**, with a checklist note | Assume public; static-everywhere | shields.io can't read private repos; broken badges are dishonest badges. |

## D. Architecture section

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| D1 | **Mermaid by default; registry-aware**: if a manifest routes the README to PyPI/npm/crates, also emit an ASCII version in `<details>` | Mermaid-only; ASCII-only; committed image | Mermaid doesn't render on registry pages; images need a renderer (conflicts with A2). |
| D2 | **One component/data-flow diagram + annotated directory tree** (≤12 lines, 3–6-word purpose each) | Diagram-only; tree-only; C4 two-level | Engineer gets the flow, intern gets "where things live". |
| D3 | **Every node/edge maps to an artifact; inferred ones drawn dashed + flagged** (`classDef inferred`, `-.->`) | Free inference (initially chosen, then reverted); artifact-only | Keeps the diagram inside the B1 contract. |
| D4 | **≤ ~10 nodes**; over cap → collapse leaves into parent subgraph. **Tiny repos** (single module/script) → "Single-module project — no diagram needed" + 2–3 sentence How-it-works + tree | Always-diagram; omit section | No filler flowcharts; index stays stable. |

## E. Index

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| E1 | **H2-only flat list, always present**, placed after header (title/logo, badges, one-liner, Status). GitHub slug anchors; **no emoji in headings** | Nested H2+H3; conditional | Stable anchors, short index. |

## F. Setup

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| F1 | **CI-first priority chain**: CI steps → Makefile/justfile/package scripts → Dockerfile/compose → manifests/lockfiles → existing README → docs/. **Discrepancies flagged inline** | README-first; manifest-first | CI is the only source that provably runs. |
| F2 | **Never execute anything.** Checklist item: "Setup commands derived from `<source>`, NOT executed — run once before promoting" | Safe probes; full verify | Portable, no side effects, no permission prompt possible in one-shot. |
| F3 | Prerequisites as a table **Requirement | Version | Where it's pinned** | Table without source; bullets | Source column doubles as evidence. |
| F4 | **Primary path expanded** (the one CI uses), **alternates in `<details>`**, ends with a **"Check it works"** step from CI's test/health command | All-equal; primary-only | Intern gets one obvious path and a pass/fail signal. |

## G. Design decisions & trade-offs

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| G1 | **Full source chain**: ADRs → design docs → old README rationale → CHANGELOG → git log (capped ~200 commits, merge bodies first, bots excluded) → `gh` PRs/issues **only if already authenticated, never fails the run** → code comments. Found rationale is quoted/attributed (T2) | Artifacts-only; local-only | Most "why" lives in commits/PRs. |
| G2 | **Structured bullets, 3–6 items, ≤2 lines each**: `**Chose X over Y** — because … (source). *Cost:* …` | Table; prose | Each item is forced to have a *because* and a *cost*. |
| G3 | **One section** "Design decisions & trade-offs": 2–3 sentence "why this shape" intro, then bullets | Two sections; why-in-overview | Short index; brief "why" lives with the trade-offs. |
| G4 | If no rationale is documented: **state the observed choice (T1) + its well-known consequence; mark the missing "why" as TODO** | Documented-only; free motive inference | Section stays useful in one-shot mode without inventing motives. |

## H. Existing README

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| H1 | **Verbatim-first.** Restructure into canonical order; sentence-level edits **only** for (a) contradicted by code, (b) language-policy violation, (c) command differs from CI. Every edit listed | +clarity edits; free rewrite | Author's voice survives; edits are auditable. |
| H2 | Contradicted claim → **replaced with evidenced version; noted in change summary only (no inline marker)** | Replace+inline marker; keep+marker | Verified corrections don't need a marker (markers are for the *unverifiable*, per B2). |
| H3 | Orphan sections **folded into the nearest canonical section** via the fold map (see I4). Header art/logos/GIFs stay verbatim at top | Preserve-near-end; details block | Tighter structure; fold map removes the "nearest" ambiguity. |
| H4 | New content **links** to CONTRIBUTING/CHANGELOG/docs rather than duplicating; **inherited sections > ~40 lines are wrapped in `<details>`** and noted in the summary | Never-collapse; summarise-and-link | Preserves text, controls scroll length. |
| H5 | No README → create from scratch, same structure. `README.rst`/`.txt` → **Markdown draft** preserving content; checklist note if a manifest points at the `.rst`. Case-insensitive match | Match-format; markdown-only | Mermaid doesn't render in RST on GitHub. |

## I. Readability

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| I1 | **Soft target 200–300 visible lines** (excludes `<details>` bodies and the review block) **+ per-section caps**: Overview ≤8 lines, Setup ≤40 visible, Trade-offs 3–6 bullets, Limitations ≤8 bullets, tree ≤12 lines. Over budget → collapse, never cut inherited text | Hard cap; no budget | Length control that doesn't violate H1. |
| I2 | **Setup opens with a 3-command Quick start block**, then full detail. No separate section | Separate section; none | Fast path first, no index bloat. |
| I3 | **Define jargon on first use, in-line, ≤10 words; no glossary section** (an inherited one is preserved) | Glossary when ≥3 terms; links-only | Intern-friendly without a new section. |
| I4 | **Order:** Header → Index → Overview → Setup → Architecture → Usage → Configuration → Design decisions & trade-offs → Known limitations → Roadmap → Contributing → License & credits. **Fold map:** screenshots/demo → Overview; API/examples → Usage; env/config → Configuration; FAQ → Known limitations (or Usage if how-to); dev setup → Contributing; Acknowledgments/Sponsors/Citation → License & credits | Architecture-first | Get-it-running before understand-it, for the intern reader. |

## J. Future work

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| J1 | **"Roadmap" only when evidence exists**; every item attributed; intent language ("planned", "under consideration"), **never "coming soon", no dates unless documented**; omitted from body and index when nothing is found | Always-present; fold into limitations | "May state future work" is permissive, not mandatory. |

## K. Scope & edge cases

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| K1 | **First-class stacks:** Node/TS, Python, Go, Rust, JVM (Maven/Gradle), Docker-only; **generic fallback** for everything else (CI-derived commands; license/CI badges only) | Node+Python only; top-10 | Coverage vs. reference-file size. |
| K2 | **Monorepo:** root draft = repo-level architecture + package table linking each package's README; **invoked inside a package → that package is the repo**; never N drafts in one run | Root+all; none | Detects npm/pnpm/yarn workspaces, Cargo/uv workspaces, go.work, Nx/Turbo. |
| K3 | **Non-code repos:** same skeleton with rename map — Architecture→Structure, Setup→How to use/view, Trade-offs→Methodology choices | "Not applicable" filler; out-of-scope | Honesty rules and index still apply. |

## L. Quality gate

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| L1 | **Mandatory final self-review gate; failing any item blocks writing.** Checks: index ↔ headings ↔ anchors; Mermaid sanity (balanced brackets, no reserved ids like `end`); every badge → catalog artifact; every command → source; zero banned words; every T3 claim has a marker; Status + Limitations present; length budget; **content ledger** mapping every original section → kept / moved / edited / collapsed / removed | Light gate; no gate | Makes "built on the original" provable. |
| L2 | **Top of draft:** marker checklist + 1-line pointer. **Sidecar `README.draft.review.md`:** change summary + content ledger + sources used. Both say "delete before promoting" | Everything-top; chat-only | Draft stays near-final; audit trail is complete and persistent. |
| L3 | **Validate with a synthetic fixture repo with planted traps + one real repo you name.** Traps: stale README claim, unpublished-package badge, CI command ≠ README command, orphan FAQ, TODO comments, no LICENSE | Real-only; fixture-only; no test | Fixture exercises every rule; real repo checks realism. |

## M. Skill meta

| # | Decision | Rejected | Why / consequence |
|---|---|---|---|
| M1 | Name **`barbican`** (folder `barbican/`) | honest-readme; readme-refresh; readme | The fortified gate to the repo. |
| M2 | **Narrow trigger**: README create/update/refresh/audit, README badges, README architecture section. Description explicitly excludes CHANGELOG, API reference, docstrings, CONTRIBUTING, wiki | Broad; explicit-only | Fewer false activations in auto-loading runtimes. |
| M3 | **Personal skills directory** `~/.claude/skills/barbican` (optionally symlinked to `~/.agents/skills/barbican` for other runtimes). Built in this workspace at `/home/user/barbican/` | Standalone repo + dogfood; project dir | Personal use first; format stays portable. |
| M4 | **New content always English; inherited text untouched; no flag** | Match original language; English+flag | **Accepted cost:** mixed-language output on non-English repos. |
| M5 | Re-run **overwrites both draft files**. The skill may write **only** those two files — never `README.md`, manifests, `.gitignore`, or anything else | Numbered drafts; refuse | Drafts are disposable by design. |

---

## N. Micro-defaults assumed underneath your answers (veto any)

1. **Marker syntax:** `> ⚠️ TODO(maintainer): <what to confirm> — <why barbican couldn't>`. Only emoji allowed in new text; all markers are deleted on promotion, so the final README has no emoji unless inherited.
2. **Title & one-liner provenance:** title = manifest name / repo name (T1). One-liner = manifest `description` (T1) → else first sentence of original README verbatim (T2) → else derived from entrypoint + marker (T3).
3. **Status vocabulary (fixed):** `Experimental` · `Active development` · `Maintained` · `Low activity` (no commits > 12 months) · `Archived` (GitHub flag / notice). Basis stated in the marker, e.g. "inferred from v0.4.2, no 1.0 tag, last commit 3 days ago".
4. **Mermaid conventions:** `flowchart LR`; subgraph "This repo" vs. external; node labels carry the folder/module path; edges labelled only when the data/protocol is known; alphanumeric ids; reserved words avoided.
5. **Badges link to their target** (workflow page, LICENSE file, registry page) and carry meaningful alt text.
6. **Tone:** neutral, imperative for instructions, present tense, no first person, no hand-typed "last updated" dates (they rot).
7. **Usage section present only with evidence:** CLI definitions in code (argparse/click/commander/clap/cobra — read, not run), `examples/`, tests that demonstrate usage, inherited usage text.
8. **Configuration section present only with evidence:** `.env.example`, config files, env lookups in code. Table `Variable | Required | Default | Purpose | Source`. **Never copies values from real `.env`/secrets; never includes tokens or credentialed URLs.**
9. **Contributing section:** link CONTRIBUTING.md if present; else 2–3 lines derived from CI ("PRs must pass: lint, test (Node 18/20)"); omitted if neither exists.
10. **License & credits:** SPDX detected from LICENSE text; **no LICENSE file → "No license file found" + marker** (unlicensed code is all-rights-reserved by default — worth stating). Credits = inherited Acknowledgments/Sponsors/Citation verbatim.
11. **Git mining bounds:** `git log -n 200` + merge bodies; bot authors excluded; rationale keywords: because, instead of, switch, migrate, replace, revert, due to, trade-off, perf.
12. **`gh` usage (read-only, only if `gh auth status` succeeds):** `repo view --json isPrivate,isArchived,description,licenseInfo`, `issue list --label enhancement|bug --limit 20`, `pr list --state merged --limit 30`.
13. **Exploration bounds:** manifests, CI, docs/, top-level dirs, entrypoints, first ~50 lines of each top-level module, `.env.example`, compose files. No recursive full-source read.
14. **Frontmatter:** `name: barbican`, narrow `description`, `license: MIT` (skill itself), `metadata: {version: 0.1.0}`, `compatibility: "Requires git. gh CLI optional (read-only)."` No `allowed-tools` (portability); write-boundary enforced by instruction.
15. **SKILL.md body ≤ ~300 lines;** everything heavy lives in references.

## O. Planned file layout

```
barbican/
├── SKILL.md                       # workflow, hard rules, gate; links to references
├── references/
│   ├── evidence-rules.md          # B1 tiers + phrasing table, marker syntax, status vocabulary
│   ├── language-policy.md         # B3 ban list + evidence-or-delete rule
│   ├── badge-catalog.md           # C1–C5: artifact → badge, publish-step signatures, order, private-repo rule
│   ├── diagram-guide.md           # D1–D4: Mermaid conventions, dashed/inferred classes, ASCII fallback, tiny-repo rule
│   ├── section-guide.md           # I4 order, fold map, K3 rename map, per-section caps and presence rules
│   ├── stack-detection.md         # K1: six ecosystems — pin locations, idiomatic commands, publish steps, workspace signals
│   ├── source-mining.md           # F1 chain, G1 chain, git/gh bounds, security exclusions
│   └── review-gate.md             # L1 checklist, ledger format, sidecar template
└── assets/
    ├── README.skeleton.md         # canonical skeleton with placeholders and per-section guidance comments
    └── README.draft.review.md     # sidecar template
```

## P. Build & test plan (after sign-off)

1. Write `references/` first (they are the spec), then `SKILL.md` as a thin orchestrator over them.
2. Build fixture repo `~/barbican-fixture/` (Python or Node — your call) with the planted traps from L3.
3. Dry-run the skill against the fixture by following SKILL.md literally; check every trap is caught; fix the references, not the output.
4. Dry-run against the real repo you name.
5. Deliver: `barbican/` folder + install line (`cp -r barbican ~/.claude/skills/`).

## Q. Open items for sign-off

- [ ] Any veto on micro-defaults N1–N15?
- [ ] Fixture stack: Python or Node?
- [ ] Which real repo for the second test (path or URL), or defer?
