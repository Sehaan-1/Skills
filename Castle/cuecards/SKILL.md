---
name: cuecards
description: Clarifying product intent, drafting structured decision cards, managing GitHub issue boards, recording ADRs, and producing implementation handoffs.
disable-model-invocation: true
---

# Cuecards

Cuecards turns vague product intent into structured decisions, drives ask-rounds with humans, commits architectural decisions (ADRs), and hands off ordered slices to builders.

## Hard gates

1. **Do not ship the destination from this skill.** Look-cards may add a real working slice, fixtures, screenshots, or a CI check as *evidence for a choice*. Chores may unblock. Find-cards write findings. Write ADRs and, when the board is done, a handoff. Do not start the rest of the product.
2. **A card is a choice, not a sprint job.** If the title could be a to-do ("build login", "add Stripe"), it is mis-typed — unless it is a **look** card (produce real evidence so a choice can be made) or a **chore** (unblock a choice). Rewrite anything else as a question, or it is still fuzzy.
3. **The body is for a non-technical reader.** YAML, labels, and `## For the agent` / `## Tracking` are for you. If a tired founder cannot answer the card in a few minutes, rewrite it before you file it. Jargon in the human body is a defect.
4. **Think, then simplify, then present.** Never show a question or a recommendation you have not run through the depth review. Plain language is pass two. Pass one is: is this the real fork, and does the recommendation aim at a product that would actually be impressive?
5. **Review before create or present.** Depth review, then quality bar. Do not dump thin cards. Do not think out loud at them in jargon.
6. **If it needs them, they speak.** Never answer a for-you question yourself. Never pick the look-card. Facts are your job.
7. **File the whole sharp frontier.** Do not starve the board. Unattended cards run in parallel this sitting. For-you cards may be batched when they are independent and the human agrees; otherwise one for-you thread at a time so they are not flooded.
8. **Where we're headed must be testable.** If you cannot name the walk, the proof, and how it is enforced, you do not have a destination yet. A sentence they can say is how a *card* locks. It is not how the *board* is done.
9. **The live board lives on the repo's issue tracker.** By default GitHub, via `gh`. If `gh` cannot see this repo (not GitHub, or auth fails), say so out loud, then use the local fallback under `.cuecards/boards/<slug>/`. Never leave the live board only in chat, and never pretend issues exist.
10. **Durable choices are ADRs.** A closed-card gist on the parent is an index line, not the record. Write `docs/adr/NNNN-slug.md`, cite it as **ADR-NNNN** by name, and never reopen a closed card to rewrite history. Supersede with a new ADR.
11. **A decided board is not a build plan.** After the board is done, write the handoff. Do not hand a building agent only a pile of closed issues.

<!-- ── PROVENANCE GATES (added to prevent self-adjudication) ──────────────── -->

12. **You cannot close a for-you card.** A for-you card is closed only when the human posts
    a reply, picks an option, or explicitly says "close it." You must quote their answer
    verbatim in the issue comment that records the close. An agent-only session that opens
    and closes for-you cards in the same window without a quoted human reply has not produced
    a decided board — it has produced fabricated provenance. If no human answer exists,
    the card stays open and you say so out loud.

13. **The board is done only when every for-you card has a verifiable human answer on record.**
    "Verifiable" means: the closing comment on the GitHub issue quotes the human's words,
    or the local fallback YAML records `answered_by: human` with a direct quote under
    `human_answer:`. A for-you card closed with no such record is not closed — reopen it.
    Inspect every child issue before writing the handoff. Do not count closed issues.
    Count issues with a quoted human answer.

14. **Write the handoff only after gate 13 passes.** A handoff written before any for-you
    card has a verifiable human answer is a fabricated plan. If the board is not done, say
    so and stop. The handoff header must include:

    ```markdown
    ## Provenance
    - Board: [<board name>](<url>)
    - For-you cards decided by human: <N> of <N>
    - Last human answer recorded: <ISO date or "see issue #NN">
    - Handoff written by: <agent name>
    ```

    An agent filling in its own name under "decided by human" is a defect. Fill the count
    from the issue record, not from memory.

<!-- ──────────────────────────────────────────────────────────────────────── -->


## Core Lifecycle

`
[Board Layout] -> [Card Craft & Review] -> [Ask Round] -> [ADR Record] -> [Handoff Sequence]
`

1. **Board Layout**: Establish parent issue or docs/cuecards/<board>.md with clear destination criteria and initial card frontier.
2. **Card Craft & Two-Pass Review**: Draft 2-4 viable options per fork. Run Pass 1 (Product Bar & ## For the agent) and Pass 2 (Quality Bar).
3. **Ask Rounds**: Present frontier cards to human. Record decisions verbatim.
4. **ADR Recording**: Convert binding architectural choices into permanent records in docs/adr/.
5. **Handoff Sequence**: Group closed decisions into sequential implementation slices (docs/cuecards/<board>-handoff.md).

## Artifact Contracts

### Card Shape
`markdown
# <spoken-English name>
## In one sentence
## Why this, why now
## What we already know
## The question
## What this is not asking
## Options (A, B, C: 2-4 options)
## Recommendation
## How you'll know it's answered
## Proof (required for look-cards)
## After you answer
## For the agent (5 self-check questions)
`

### Board Shape
`markdown
# <spoken name>
## Where we're headed
## How we'll know we're there
## Ready now — for you
## Ready now — unattended
## Waiting
## Decided
## Not this effort
`

## Reference Index

- [reference/card-craft.md](reference/card-craft.md) - The 8 jobs of a card, complete card anatomy, voice, and the 5 card types.
- [reference/depth-review.md](reference/depth-review.md) - Two-pass depth review, product bar, 5 agent-facing questions, red flags, and good/bad comparisons.
- [reference/board-and-rounds.md](reference/board-and-rounds.md) - Full board template, column states, ask-round mechanics, and completion criteria.
- [reference/adr-discipline.md](reference/adr-discipline.md) - ADR specification, status lifecycle, indexing, and decisions in force.
- [reference/handoff-template.md](reference/handoff-template.md) - Handoff document template, sequence rules, and slicing discipline.
- [reference/board-operations.md](reference/board-operations.md) - GitHub CLI (gh) operations, labels, dependencies, query commands, and local fallback.
