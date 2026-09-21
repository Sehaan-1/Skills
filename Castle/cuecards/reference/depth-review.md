# Depth Review: Two-Pass Quality Bar

# Depth review (pass one — before they ever see it)

Do this **privately**. Fill `## For the agent`. Do not show this block as the conversation. Then quality bar. Then present.

1. **Think** — real fork, what would *great* look like.
2. **Draft** — options include the ambitious-right one.
3. **Depth review** — this list.
4. **Simplify** — same thinking, easier words.
5. **Present or file.**

If you cannot defend the question and recommendation against "would this help us build something impressive?", you are not ready.

### The product bar

Impressive is **taste on the right axis**, not more features and not more cards.

- **Real fork.** Experience-level choice, not a vendor/tool proxy.
- **Name great.** What would people tell someone else if we got this right? If no option points at that, the options are wrong.
- **Recommendation honesty.** If you picked easy/cheap/agent-convenient, change it or say the trade in the open.
- **Hidden option.** If you dropped a better option because it was hard to say simply, that is a writing failure.
- **Six-month regret.** Do not recommend the pick that makes this feel like every other product.
- **Cut extra knobs, not ambition.**
- **Cost is honest.**

### `## For the agent` (required)

```markdown
## For the agent

### What would impressive look like here
### Real fork
### Why this recommendation isn't the lazy one
### Option I almost hid
### Six-month generic
```

Empty or a shrug: do not present.

## Quality bar (pass two)

Read the card as someone who cannot code. Thinking stays; words get simpler.

1. Title you'd say out loud
2. Exactly one question
3. Not a sprint job (unless look/chore as defined)
4. Self-contained with named gists
5. So-that chain is obvious
6. Fence is real
7. 2–4 outcome-named options with notice / cost / give-up
8. Recommendation rejectable, not a hedge
9. Done sentence they could utter
10. Unlocks **and** blocks named
11. No ungossed jargon in the human body
12. One short scroll (or it is two cards / still fuzzy)
13. Banner matches for-you vs unattended
14. Assumptions labeled
15. Depth block filled
16. Ambition survived simplifying
17. **Look-cards:** Proof names a walk, an artifact that will be kept, and (when the destination is UI) how a screenshot / DOM fixture / CI job will pin it
18. **Priority** is set: now / next / later
19. **Closing an ask or look:** an ADR is drafted or accepted in the same sitting (see ADRs). The board gist cites **ADR-NNNN**, not only the issue.

Fail any one: rewrite. Do not file. Do not present.

### Red flags

| Thought | Reality |
| --- | --- |
| "They'll know what I mean" | The card has to carry it. |
| "I'll put the real detail only in Tracking" | Then they decide blind. |
| "Build the X" | Find the question — unless this is a look-card producing evidence. |
| "Just list the technical options" | Name outcomes. Recommend. |
| "Keep the board tiny so we look careful" | Starving the frontier is a defect. File every sharp question. |
| "Simple words means a simple recommendation" | Simple words, hard call. |
| "I'll recommend A because we'll have to build it later" | Recommend the impressive product. |
| "Throwaway mock is enough for a look-card" | Produce something real and keep it. |
| "They said yes, so the board is done" | Done is the walk + proof + enforcement, not a vibe. |
| "I'll figure out the real question while they answer" | Depth review is before present. |
| "The gist on the board is enough" | The gist is an index. The ADR is the record. |
| "I'll edit the closed issue to change the decision" | Write ADR-NNNN+1 that supersedes. Append History on the old ADR. Leave the card closed. |
| "The closed board is the build plan" | Write the handoff. Closed issues are context, not sequence. |

### Bad vs good

Bad title: `Select auth provider`  
Good title: `How do people sign in?`

Bad question: `Should we use Stripe or Braintree for PCI-DSS SAQ-A?`  
Good question: `When someone pays, do they type their card on our site, or on a checkout page that belongs to a payments company?`

Bad option: `A — Postgres. B — Mongo.`  
Good option: `A — One list of invoices we can all trust, even if that takes longer to set up.`

Bad look-card: a sketch you delete.  
Good look-card: a running slice in the repo, screenshot (or fixture) linked, CI pin if it is a UI walk, they pick A/B/C facing that.

Bad "done": "we agreed in chat."  
Good "done" for the board: a named walk works, proof is in the repo, CI fails if it regresses.

---

