# Architecture Decision Records (ADRs)

A closed card is a conversation that completed. An **ADR** is the durable, versioned record committed to the repository.

## File Location & Naming

```text
docs/adr/NNNN-spoken-slug.md     # 4-digit zero-padded index; never reuse NNNN
docs/adr/README.md               # Current index table
```

---

## When to Write an ADR

| Closed Card Type | Write ADR? |
| --- | --- |
| **ask** | **Always.** |
| **look** | **Always.** Record choice and pointer to kept proof. |
| **find** | Only if the finding locks a durable constraint. |
| **chore** | No. |
| **not-this-effort** | **Yes**, if excluding this scope should remain citable. |

Write the ADR in the **same session** that closes the card.

---

## Required ADR Template

```markdown
# ADR-NNNN: <spoken title>

- **Status:** proposed | accepted | deprecated | superseded
- **Date:** YYYY-MM-DD
- **Card:** [<card name>](issue url)
- **Board:** [<board name>](issue url)
- **Supersedes:** ADR-MMMM | none
- **Superseded by:** none | ADR-PPPP

## Context
Why this decision arose. What we evaluated (options A/B/C in outcome language).

## Decision
The locked choice, stated as a clear sentence.

## Consequences
What this means downstream:
- **People notice:** …
- **Later work must:** …
- **We give up:** …
- **Verification / checks:** tests or CI requirements committed to

## History
- YYYY-MM-DD accepted
- YYYY-MM-DD superseded by ADR-PPPP — <one-line reason>
```

---

## Lifecycle Rules

```text
proposed → accepted → deprecated
                     ↘ superseded → (new ADR accepted)
```

1. **Never edit an accepted decision in place.** If a choice changes, write a new ADR that supersedes the old one.
2. **Append to History.** Mark the old ADR as `superseded` and cite the new one.
3. Update `docs/adr/README.md` index table whenever status changes.
