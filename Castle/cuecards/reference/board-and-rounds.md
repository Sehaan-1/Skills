# Board Structure and Ask Rounds

# The board

The board is the **parent GitHub issue**. It is an index, not a store. A choice lives on its card issue. The board gists, links, and lists what is takeable.

A non-technical person should open the parent issue and know what to do.

```markdown
# <spoken name>

## Where we're headed
<one or two lines. outcome language.>

## How we'll know we're there
- **Walk:** <the person can do X, end to end, without us in the room>
- **Proof:** <screenshot trace of that walk, and/or DOM fixture path, and/or test name>
- **Enforced:** <CI job that fails if this regresses. If none yet, the look-card that will add it.>

If any of the three is missing, this heading is not ready. Keep asking.

## How to read this
One card = one choice. Open a **Ready now** card. Ignore agent notes.
**We'll handle this** runs without you.

## Notes
- **Domain:** <who it's for, what already exists>
- **Standing rules:** <constraints every sitting must honor â€” examples: stdlib first; tests stay green; dry-run enforced three ways>
- **Consult:** <files or skills every sitting should read, including `docs/adr/`>
- **ADRs in force:** [ADR-0001 Title](docs/adr/0001-â€¦.md), â€¦
Do not leave this empty. Cards should not have to repeat these rules. Cite ADRs by name, never by a bare number.

## Ready now â€” for you
- [<name>](url) Â· **now** Â· blocks [<name>](url): <question in one line>

## Ready now â€” unattended
- [<name>](url) Â· **now**: <what we'll handle>

## Waiting
- [<name>](url) Â· waiting on [<name>](url) Â· blocks [<name>](url)

## Decided
- [ADR-NNNN Title](docs/adr/NNNN-slug.md) Â· [<card name>](url) Â· accepted: <one-line gist>
- (deprecated / superseded ADRs stay in `docs/adr/README.md`, not here, unless Notes still need the warning)

## Not sharp enough to ask yet
- <suspected question, why it isn't a card yet>

## Not this effort
- <gist + why it sits past where we're headed>
```

**Fuzzy or card?** Can you state the question precisely *now* â€” not can you answer it now.

- Sharp â†’ card, even if waiting, and even if several are open at once. Cover the edge.
- Not sharp â†’ **Not sharp enough**. Do not pre-slice into fake cards.

**Not this effort** is scope, not fuzz. Close those issues as `not-this-effort`; they do not belong under Decided.

Where you're headed, **How we'll know we're there**, and **Notes** are agreed **before** any card exists.

---

# Lay out the board

One sitting. Create the parent issue and every sharp card. Resolve none except **start all unattended find-cards in parallel**.

1. **Name where you're headed** and fill **How we'll know we're there** (walk, proof, enforcement). Think first about impressive-and-checkable, then ask rounds in plain language. Get an explicit yes. No cards before this. A timid heading with no proof is not done.
2. **Fill Notes** (domain, standing rules, consult). Get a nod.
3. **Fan out, breadth-first.** What is already askable across the whole space? What is still fuzzy? Do not deep-dive one thread. Do not stop at two cards if eight sharp questions exist.
4. **Nothing fuzzy, and it fits one sitting?** Then Sort said so already â€” do not create a board, say so.
5. **Create the parent issue.** Then create every sharp card as a child issue. Wire `blocked_by` / `blocks` (native + Tracking) in a **second pass**. Set priority `now` / `next` / `later`. Set `for-you` vs `unattended`.
6. **Both reviews pass on every card** before you file it. No thin stubs. No timid defaults. Filing many excellent cards is the point.
7. **Start every ready unattended card now** (find, and chores you can do). Parallel.
8. **Stop the for-you side.** Show: destination, how we'll know, Notes, Ready now (both lists). Next sitting works the frontier. Do not answer for-you cards while laying out.

## Work the board

1. Load the **parent issue** (low-res). Refresh Ready now from GitHub (open, unassigned, blockers closed).
2. **Run all Ready now â€” unattended** in parallel this sitting.
3. **For-you:** take the highest `now` card. If several are independent and they want speed, batch them in one sitting as separate numbered questions â€” still wait, still do not answer for them. If they want one at a time, honor that.
4. **Claim** (assign) before work.
5. Re-run depth review if the world changed. Present the card almost as written. Wait. If they ask what a word means, fix the card. If options feel small, go back to the product bar.
6. **Look-cards:** build the real slice / capture the walk / add the fixture or CI pin; link Proof; then they pick. Keep the artifact.
7. Record **Answer** on the issue (comment + close). For every closed **ask** or **look**, **write or accept the ADR in the same sitting**. Gist the parent **Decided** line as `ADR-NNNN Title â€” gist`, linking both the ADR file and the card. Update Ready now / Waiting / blocks. Add the ADR to Notes â†’ ADRs in force and to `docs/adr/README.md`.
8. Graduate newly sharp questions into quality-bar cards (create issues, wire edges). Rule out of this effort if a card now sits past the destination. Durable exclusions get an ADR too (`Status: accepted`, decision = out of this effort) so later cards can cite them.
9. Unattended work does not wait for a for-you card to finish. Do not end the sitting while ready unattended cards remain.

Wrong closed choice: do **not** reopen the card to rewrite it. Write a new ADR that **supersedes** the old one. On the old ADR, append History and set Status to superseded (append-only). Comment on the closed card: "Superseded by ADR-NNNN" as a pointer only. Update Notes â†’ ADRs in force.

### The board is done when

- Where we're headed still matches.
- **Walk** works end to end.
- **Proof** exists in the repo (screenshot trace and/or DOM fixture and/or named test).
- **Enforced:** CI fails if that walk regresses â€” or a closed look-card added that pin and it is green.
- No open cards.
- Nothing left under Not sharp enough.
- Every accepted choice has an **ADR-NNNN** file; the parent Decided list cites those names.
- `docs/adr/README.md` matches reality (status, supersession).

Then **write the handoff**. Stop. Do not ship extra product. The handoff is the last Cuecards artifact; code beyond look-card evidence is a different sitting and a different skill.

## Ask rounds

Think first, then ask only what you cannot look up. Independent questions in one round, each with a recommendation. Wait.

```text
â“ Q1 - <spoken title>
<the question>
A / B / C in outcome language

âž¡ï¸ I recommend A because <one reason>
```

Do not ask a question that depends on another still open in this round.

User instructions (`AGENTS.md`, a direct request) outrank this skill.

---

