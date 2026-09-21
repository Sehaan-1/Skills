---
name: cuecards
description: "Use when you need choice cards a non-technical person can read and answer, when an idea is too big or too fuzzy for one sitting, when work items would otherwise come out as engineering tasks or jargon, when a board of questions is needed before anyone builds, or when the user asks for cuecards, note cards, or better questions."
disable-model-invocation: true
---

# Cuecards

Write choice cards so clear that a person with no technical background can open one, understand why it exists, and decide.

Cards live as **GitHub issues** on the repository: one parent issue for the board, child issues for cards. Choices close into named **Architecture Decision Records (ADRs)**. When the board is finished, generate a sequenced **handoff** for implementation.

Announce at start: `Using cuecards to [sort | lay out | write cards | work the board | record ADR | hand off].`

## Hard gates

1. **Do not build product from this skill.** Produce choices, evidence prototypes, ADRs, and a handoff. Do not write feature code for the final product.
2. **A card is a choice, not a task.** Frame items as questions with trade-offs, not engineering to-do tickets.
3. **Write for a non-technical decider.** Explain choices in terms of customer outcomes and trade-offs. Technical jargon in human-facing text is a defect.
4. **Depth review before presenting.** Run the private depth review (product bar, real fork, ambitious options) before sharing (see [reference/card-craft.md](reference/card-craft.md)).
5. **Deciders decide.** Never answer a `for-you` card on behalf of the user. Never pick options for them.
6. **Cover the frontier.** File all sharp questions breadth-first. Run unattended research and chores in parallel.
7. **Destination must be checkable.** Name an end-to-end user flow, kept proof artifacts, and automated verification before closing.
8. **Live board on issue tracker.** Use GitHub issues via `gh` CLI, or local fallback under `.cuecards/boards/<slug>/` if unreachable (see [reference/board-operations.md](reference/board-operations.md)).
9. **Durable choices become ADRs.** Close cards into `docs/adr/NNNN-slug.md` cited by name. Never silently rewrite closed history (see [reference/adr-discipline.md](reference/adr-discipline.md)).
10. **A decided board requires a handoff.** Do not hand off an unsorted list of closed tickets. Produce `docs/cuecards/handoff-<slug>.md` (see [reference/handoff-template.md](reference/handoff-template.md)).
11. **Agent cannot close for-you cards.** A `for-you` card closes only when the human replies. Quote their response verbatim in the closing comment.
12. **Board is complete only when all for-you cards have recorded human answers.** Inspect every child issue before writing the handoff.
13. **Write handoff only after all decisions are recorded.** Handoff must include verifiable provenance counts.
14. **Cite ADRs by name.** Always reference `[ADR-NNNN Title](path)`, never bare numbers like `#42`.

## Workflow

### 1. Triage (Sort)
- **One conversation:** Settle questions directly in chat without creating a board.
- **Still fuzzy:** Goal is known but route is wide; create parent board and card issues.
- **Decided:** Destination and ADRs exist; generate handoff and transition to implementation.

### 2. Lay out the board
1. Define **Where we're headed** and **How we'll know we're there** (user flow, proof, check).
2. Record standing rules and domain notes.
3. Create parent issue on GitHub.
4. Create sharp child issues (`type:ask`, `type:look`, `type:find`, `type:chore`). Wire dependencies (`blocked_by` / `blocks`).
5. Dispatch unattended `find` and `chore` cards in parallel.

### 3. Work the board
1. Pull open `now` cards.
2. Present one `for-you` decision at a time (or batch independent questions).
3. On human decision, comment quoted response, close issue, and write `docs/adr/NNNN-slug.md`.
4. Update parent issue index.
5. When all cards resolve, generate `docs/cuecards/handoff-<slug>.md` and stop.

## Card Shape

Every card issue uses this structure:

```markdown
# <spoken-English name>

> **For you** — please decide. (or: **We'll handle this** — unattended.)

## In one sentence
We need to decide <X> so that <Y>.

## Why this, why now
<Context and impact of not deciding>

## The question
<Exactly one question in everyday words>

## Options
### A — <Outcome-based name>
- **You'd notice:** …
- **It costs:** …
- **You give up:** …

### B — <Outcome-based name>
...

## Recommendation
**A**, because <honest rationale>. <What would change this recommendation>.

## How you'll know it's answered
You can say: "<Clear sentence locking the choice>."

## Tracking
- Type: ask | look | find | chore
- Mode: for-you | unattended
- Priority: now | next | later
- Blocked by: []
- Blocks: []
```

## Reference guides

- [reference/card-craft.md](reference/card-craft.md) — 8 jobs of a card, ban-list, depth review, quality checklist.
- [reference/board-operations.md](reference/board-operations.md) — `gh` CLI commands, labels, blocking syntax, local fallback.
- [reference/adr-discipline.md](reference/adr-discipline.md) — ADR templates, status lifecycle, indexing, and citing.
- [reference/handoff-template.md](reference/handoff-template.md) — Handoff schema, slice sequencing, and acceptance criteria.
