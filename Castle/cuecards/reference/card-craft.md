# Card Craft

# Card craft (the point of this skill)

Assume the reader is intelligent, busy, and does not know Git, APIs, databases, "auth", "schema", or your tools. They *do* know their customer, their money, their time, and what they are trying to get done.

You write for that person. Labels, YAML, and Tracking are for the agent and CI.

## A card must do eight jobs

1. **Name** itself in spoken English.
2. **Place** itself: where we are, what is already decided, why this question now.
3. **Ask exactly one question** in everyday words.
4. **Fence** what it is not asking.
5. **Offer 2â€“4 options** in outcome language (what a person would notice, what it costs, what you give up) â€” not library names.
6. **Recommend** one option, with a short reason they can reject. The recommendation is the one you'd defend to a great product person, not the one that is easiest to build or easiest to explain.
7. **Define done** as a sentence they could say out loud. Look-cards *also* attach real evidence (see types).
8. **Show the chain:** answering this unlocks X; also list **what this blocks**.

If any job is missing, it is not filed yet.

## Shape

Every card issue uses this body. Do not skip sections. Shorten them; do not omit them.

```markdown
# <spoken-English name>

> **For you** â€” please decide.
> (or: **We'll handle this** â€” unattended. You do not need to answer.)
> (or: **For you** â€” look, then pick. A real slice will exist to react to.)
> (or: **A chore** â€” then we can decide.)

## In one sentence
We need to decide <X> so that <Y>.

## Why this, why now
<2â€“5 sentences. The chain from where we're headed to this question.
 What goes wrong if we skip it or guess.>

## What we already know
- **Where we're headed:** <one line>
- **Already decided:** [ADR-NNNN Title](docs/adr/NNNN-slug.md) ([card](url)): <gist>
- **Waiting on:** nothing / [<card name>](url)

## The question
<exactly one question. everyday words.>

## What this is not asking
- <nearby question that belongs elsewhere, or is not this effort>

## Options
### A â€” <name a person would use>
- **You'd notice:**
- **It costs:**
- **You give up:**

### B â€” ...
### C â€” ...   (2â€“4. never one. never seven.)

## Recommendation
**A**, because <one short reason>. <what would change your mind.>

## How you'll know it's answered
You can say: "<a sentence in their voice that locks the choice>."

## Proof (required for look-cards; optional elsewhere)
- **Walk:** <what someone does>
- **Artifact:** <path, screenshot, fixture, or CI job that will exist>
- **Keep:** yes. Link it here when it exists.

## After you answer
- **Unlocks / this blocks:** <names>
- **Still later:** <what this does not settle>
- **ADR:** ADR-NNNN (accepted) / none â€” find and chore usually none

## For the agent
<!-- required before present. human can ignore. -->

## Tracking
- Board: [<board name>](url)
- Type: ask | look | find | chore
- Mode: for-you | unattended
- Priority: now | next | later
- Blocked by: [<name>](url)
- Blocks: [<name>](url)
```

YAML in local fallback (agent only):

```yaml
id: "001"
title: <same spoken-English name>
type: ask               # ask | look | find | chore
status: open            # open | claimed | closed | not-this-effort
needs_you: true         # for-you. false = unattended
priority: now           # now | next | later
who_decides: you
claimed_by: ""
blocked_by: []
blocks: []
created: YYYY-MM-DD
```

On GitHub, the same facts are **labels + assignee + native blocked-by + Tracking**. Keep them in sync.

## Voice

- Titles you'd say to a friend: "Who pays?" "Where does the invoice go?"
- Not: `billing-entity-model`, `auth-provider-selection`.
- Refer to every board, card, and ADR **by name** (ADR-NNNN plus title), wrapping the link. Never a bare `#42` or a bare `0001`.
- Prefer "you" and "we".
- Options named after outcomes, not libraries.
- Gloss the rare unavoidable term once.
- Cut. If you would not read it on a phone, it is too long.
- Facts vs choices: look up prices and what exists. Ask them only for preferences, taste, risk, and who it is for.

### Ban-list in the human body

Do not use unless immediately glossed: auth, OAuth, schema, API, endpoint, repo, PR, webhook, idempotent, eventual consistency, "the stack", class names, file paths.

File paths belong in Proof, Tracking, or `## For the agent`.

## Types

| Type | Mode | Banner | When | Done when |
| --- | --- | --- | --- | --- |
| ask | for-you | **For you** â€” please decide. | Talking can settle it. Default. | They pick (or rewrite) an option. |
| look | for-you | **For you** â€” look, then pick. | Talking cannot settle how it looks / feels / goes. | A **real kept artifact** exists, they pick using it, Proof is filled and linked. |
| find | unattended | **We'll handle this.** | A fact you can look up is blocking a choice. | A one-page finding in plain language, linked on the issue. They do not do homework. |
| chore | unattended if you can, else for-you | **A chore** â€” then we can decide. | Signup, access, moving data so its shape can be seen. | Checklist complete. Never "build the destination." |

**Look-cards are real.** They exist to produce something you can run or inspect: a working module or slice in the repo, captured screenshots, DOM fixtures, a canary run, a CI check that fails when the slice regresses. Label nothing "throwaway you do not keep." Cheap and rough is fine; fake is not. You still do not pick the option â€” they do, facing the artifact.

**Find-cards** stay unattended. Findings are rewritten so the next ask-card can use them without opening a white paper.

**Chore** unblocks a question. "Implement accounts" is still a build job in disguise: delete it.

---

