---
name: oneslice
description: "Use when implementing one Cuecards handoff slice, one ticket, or one milestone of an already-decided board. Use when building or coding from a handoff, when an API contract or module boundary must be defined, or when handling untrusted input, auth, secrets, or third-party services. Do not use to decide product questions or to build the whole product in one sitting."
---

# Oneslice

Build **one** handoff slice. Prove it. Stop.

Cuecards decided. The handoff sequenced. This skill implements a single slice — a ticket or milestone — and holds it to a strict quality bar. It does not reopen product questions. It does not start the next slice. It does not rubber-stamp "it works."

Announce at start: `Using oneslice to [pick the slice | research | track | increment | build | prove | review | stop].`

## Hard gates

1. **No handoff, no build.** Read `docs/cuecards/handoff-<slug>.md`. If missing or incomplete, stop and refer to cuecards. Do not invent a plan while coding.
2. **One slice per session.** Implement one handoff `### Slice N`. Not the whole board or milestone list. When that slice's Check and quality bar pass, stop.
3. **ADRs are law.** Cited ADRs are closed decisions. If the code cannot honor an ADR, stop and state which one — that requires cuecards, not a workaround.
4. **The slice Check is the definition of done.** Walk, proof, or automated test named in the slice. A green vibe is not done.
5. **Working is not the bar.** Spaghetti code is a failed slice. Restructure before calling it done (see [reference/quality-bar.md](reference/quality-bar.md)).
6. **Do not expand scope.** Out-of-scope ideas go back to cuecards as cards, not bonus code.
7. **Claim before you build.** Assign the GitHub issue or milestone first. Comment the result on that issue when you stop.
8. **Verify external facts.** If the slice depends on a third-party API or external spec, verify against primary sources and commit findings first (see [reference/research-protocol.md](reference/research-protocol.md)).
9. **The ticket is for a person.** Write the GitHub issue in plain, spoken English without agent jargon.
10. **Thin vertical increments.** Implement → test → verify → commit. Keep the build green with one logical concern per commit.
11. **Save points on short-lived branches.** Branch off default. Commit when an increment passes; revert to the last commit if it fails (see [reference/branch-discipline.md](reference/branch-discipline.md)).
12. **Contract before code.** For public APIs or module boundaries: define types, single error shapes, edge validation, and atomic idempotency first (see [reference/api-contracts.md](reference/api-contracts.md)).
13. **Threat model before implementation.** For untrusted data, auth, PII, webhooks, or LLM output: run a 5-minute threat model. Ask the human before adding auth or storing PII (see [reference/security-gates.md](reference/security-gates.md)).
14. **Research committed before dependent code.** Research Markdown files must be committed before or with the dependent code (see [reference/provenance.md](reference/provenance.md)).
15. **Check passed requires reproducible artifacts.** Link the commit SHA and a CI run URL or terminal transcript at `docs/research/<slice-slug>-check.md` before marking done (see [reference/provenance.md](reference/provenance.md)).
16. **Existing design and architecture are law.** If `DESIGN.md` exists, follow its design tokens. If `docs/architecture/` exists, stay within its boundaries; do not bypass architectural rules.

## Pick the slice

1. Open the handoff file.
2. Take the named slice, or the first slice whose dependencies are met.
3. Read the slice definition, cited ADRs, constraints, and slice Check.
4. Announce: `Building Slice N: <spoken name>. ADRs: …. Check: …. Then I stop.`
5. If the slice is not independently checkable or dependencies are incomplete, stop and explain what is missing.

## Human-readable tracker

The live ticket is the GitHub issue for this slice (or a comment on the board issue if there is no child issue). Write in spoken English.

On claim, post or set the body to:

```markdown
## Slice N: <spoken name>

### What this slice does
<from the handoff, one short paragraph>

### How we'll know
<the Check, in everyday words>

### Decisions this honors
- [ADR-NNNN Title](path)

### Status
In progress — claimed.

### What landed
_(updated as increments commit)_

### What I didn't touch (on purpose)
_(intentional scope boundaries)_

### Blocked
nothing

### Provenance
- Research file: <path or "none needed">
- Check artifact: <CI run URL or transcript path — required before status = Check passed>
```

After every increment and when stopping, update the ticket in the same voice. Status is one of: `In progress` · `Check passed` · `Blocked: <plain reason>` · `Handed back to cuecards: <which ADR/question>`.

## Build loop

1. **Measure:** Restate slice goals, Check, and ADRs. Review `DESIGN.md` and `docs/architecture/` if present. Dispatch research if external facts are needed.
2. **Increment:** Build the smallest complete vertical increment.
3. **Prove increment:** Run tests, linter, and type checks. Ensure tests fail before adding new behavior.
4. **Commit increment:** Save atomic commit with clear rationale. Update tracker.
5. **Repeat steps 2–4** until the slice Check can pass.
6. **Prove the slice:** Run the Check. Verify failure when new behavior is temporarily disabled.
7. **Review diff:** Check against quality bar, API contracts, and security checklists.
8. **Refactor:** Restructure for simplicity and clarity before finalizing.
9. **Report:** Update the GitHub issue with linked artifacts and human-readable summary.
10. **Stop:** Do not begin the next slice.

## Reference guides

- [reference/quality-bar.md](reference/quality-bar.md) — Simplification standards, self-review questions, and approval bar.
- [reference/research-protocol.md](reference/research-protocol.md) — Primary-source research workflow and rules.
- [reference/api-contracts.md](reference/api-contracts.md) — Contract-first API design, error formats, and idempotency.
- [reference/security-gates.md](reference/security-gates.md) — Threat modeling, trust boundaries, and security rules.
- [reference/branch-discipline.md](reference/branch-discipline.md) — Increments, commit discipline, and git hygiene.
- [reference/provenance.md](reference/provenance.md) — Artifact verification standards.
