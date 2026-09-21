# Card Craft & Review Standards

A card is a clear choice, not a sprint task. Write for an intelligent, busy person who does not know Git, APIs, schemas, or technical jargon, but knows their customer, money, time, and goals.

## The Eight Jobs of a Card

1. **Name** itself in spoken English ("Who pays?", not `billing-entity-model`).
2. **Place** itself: where we are, what is already decided, why this question now.
3. **Ask exactly one question** in everyday language.
4. **Fence** what it is not asking.
5. **Offer 2–4 options** in outcome language (notice / cost / give-up), not library names.
6. **Recommend** one option with an honest reason that can be rejected.
7. **Define done** as a sentence the decider could say out loud.
8. **Show the chain:** what answering this unlocks, and what it blocks.

---

## Card Types

| Type | Mode | Banner | When | Done when |
| --- | --- | --- | --- | --- |
| **ask** | for-you | **For you** — please decide. | Conversation can settle it. Default. | Decider picks (or rewrites) an option. |
| **look** | for-you | **For you** — look, then pick. | Conversation cannot settle look/feel/flow. | Real working artifact exists, decider picks using it. |
| **find** | unattended | **We'll handle this.** | A fact lookup blocks a choice. | One-page plain-language finding linked on issue. |
| **chore** | unattended / for-you | **A chore** — then we can decide. | Setup, credentials, or exposing data shape. | Checklist complete. Never "build the destination." |

---

## Voice & Ban-List

### Banned in human body unless immediately glossed:
`auth`, `OAuth`, `schema`, `API`, `endpoint`, `repo`, `PR`, `webhook`, `idempotent`, `eventual consistency`, `the stack`, class names, file paths.

File paths and technical commands belong in `Proof`, `Tracking`, or `## For the agent`.

---

## Depth Review (Pass One — Private)

Run this privately before presenting or filing:
1. **Real fork:** Is this a user-experience choice rather than an engineering proxy?
2. **Name great:** Would this help build something truly impressive?
3. **Honest recommendation:** Did you recommend the best outcome, or just the easiest for the agent to build?
4. **Hidden options:** Did you discard a superior option because it was hard to explain simply?
5. **Six-month test:** Will this choice feel like every other generic tool in six months?

Fill `## For the agent` block:
```markdown
## For the agent
### What would impressive look like here
### Real fork
### Why this recommendation isn't the lazy one
### Option I almost hid
### Six-month generic
```

---

## Quality Bar (Pass Two — Polish)

Check every item before filing:
- [ ] Title is a spoken-English phrase
- [ ] Exactly one question
- [ ] Outcome-based options (notice / cost / give-up)
- [ ] Recommendation is rejectable, not a hedge
- [ ] Clear sentence locking the choice
- [ ] No unglossed technical jargon in human body
- [ ] Priority set (`now` / `next` / `later`)
- [ ] Dependencies wired (`blocked_by` / `blocks`)
- [ ] Look-cards include link to real reproducible verification artifact
