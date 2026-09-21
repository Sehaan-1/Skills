# Architecture Decision Records (ADR) Discipline

# ADRs

A closed card is a conversation that ended. An **ADR** is the durable, citable record. Other cards, Notes, CI comments, and the handoff cite **ADR-NNNN Title**, never a gist alone.

## When to write one

| Closed card | ADR? |
| --- | --- |
| ask | **Always.** |
| look | **Always** (the choice + pointer to Proof). |
| find | Only if the finding *locks a constraint* others must honor. Otherwise leave it as a linked finding. |
| chore | No. |
| not-this-effort | **Yes** if the exclusion should stay citable. Decision = out of this effort, with consequences. |

Write it in the **same sitting** as the close. Do not batch "ADRs later."

## Where

```text
docs/adr/NNNN-spoken-slug.md     # never reuse or renumber NNNN
docs/adr/README.md               # replaceable index: number, title, status, supersedes
```

NNNN is four digits, next unused. The file is the record. Git versions it next to the code. The GitHub card stays closed; it *points* at the ADR.

## Format (required)

Spoken-English title. Same voice as the card for Context and Decision. Consequences must say what this means *downstream* — for people and for later work — not only what was picked.

```markdown
# ADR-NNNN: <spoken title>

- **Status:** proposed | accepted | deprecated | superseded
- **Date:** YYYY-MM-DD
- **Card:** [<card name>](issue url)
- **Board:** [<board name>](issue url)
- **Supersedes:** ADR-MMMM | none
- **Superseded by:** none | ADR-PPPP

## Context
Why this came up. What we already knew. What we were choosing between (A/B/C in outcome language). Link the card.

## Decision
The locked choice, in a sentence they could say. Same as the card's Answer.

## Consequences
What this means from now on:
- **People notice:** …
- **Later cards/ADRs must:** …
- **We give up:** …
- **Look/CI/proof:** paths or jobs this commits us to, if any

## History
Append-only. Do not edit Context or Decision as if the past changed.
- YYYY-MM-DD accepted
- YYYY-MM-DD superseded by ADR-PPPP — <one line why>
```

## Status lifecycle

```text
proposed → accepted → deprecated
                     ↘ superseded → (new ADR is accepted)
```

- **proposed** — optional draft while the card is still open (big forks only). Default is to write on accept.
- **accepted** — in force. Listed under Notes → ADRs in force and on the parent Decided list.
- **deprecated** — historically true, no longer in force, no replacement yet. Remove from ADRs in force. Keep the file. Append History. Do **not** delete. Do **not** reopen the card to rewrite it.
- **superseded** — a newer ADR replaces it. Old file: set Status, set Superseded by, append History. New file: Status accepted, Supersedes ADR-NNNN. ADRs in force lists only the new one.

Never rewrite Decision on an accepted ADR. Correction = new ADR.

## Index (`docs/adr/README.md`)

Replace this table whenever status changes. Do not copy Decision text here.

```markdown
# Decisions in force

| ID | Title | Status | Supersedes |
| --- | --- | --- | --- |
| [ADR-0001](../../examples/invoicing/adr/0001-who-owes-us.md) | Who owes us? | accepted | |
| [ADR-0002](../../examples/invoicing/adr/0002-where-the-invoice-goes.md) | Where does the invoice go? | accepted | |
```

## Citing

In cards, Notes, handoff, and chat:

> Already decided: [ADR-0001 Who owes us?](../../examples/invoicing/adr/0001-who-owes-us.md)

Not: "see #12" or "as we said last week."

---

