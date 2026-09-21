# Keystone Operations, Tone, and Approval Bar

# Board operations (GitHub)

This skill does not run a board. It adds ADRs to `docs/adr/NNNN-….md` under the numbering cuecards owns, and it files structural work as issues on the existing board when the record produces follow-up work.

- **ADR** — write it in the same sitting as the decision, using cuecards' format (`Context` / `Decision` / `Consequences` / `History`, spoken-English title, `Supersedes` / `Superseded by`). Append to `docs/adr/README.md`.
- **Follow-up issues** — one per structural defect the record found, titled in spoken English, labelled `keystone` plus the priority label the board already uses (`now` / `next` / `later`). Body is technical; the first line is plain. Sub-issue them to the board parent and wire native `blocked_by` using the same `gh api` incantations as cuecards' **Board operations**.
- **Reference in the record** — cite issues by name (the audience note at the top owns the no-bare-`#42` law).

If `gh` cannot see the repo, say so out loud, and write the ADRs and follow-ups as files. Never pretend issues exist.

---

# Stop

The record is committed, the enforcement runs in CI, the stress test shows three violations caught, the ADRs are filed, and the deferred decisions have triggers. Say:

`Shape set. Contexts: <N> — <names>. Core: <name>. Fitness functions: <M> enforced, <K> unenforced. Deferred: <list>. Then I stop.`

Oneslice and lanes build inside this shape and cite the record. If a builder finds that a boundary here is wrong, that is a new keystone sitting against the same question, with the counterexample on the table — not a quiet patch. Heraldry never hears about any of this.

---

# Tone

Direct, technical, and unwilling to accept a claim in place of a measurement — including from your own first draft. This skill's reader has fifteen years of scar tissue; do not explain polymorphism to them and do not let them get away with "it's clean now."

Useful self-talk (and useful things to say out loud to the human):

- `no handoff, no shape. cuecards, not boxes drawn in the air.`
- `these two change on the same clock. one component, not two.`
- `that invariant spans aggregates. either merge them or name the mechanism and the time bound.`
- `the core is everything, so the core is nothing. distilling again.`
- `this boundary has never been crossed. leaving it partial with a facade.`
- `the dependency rule is a diagram nobody can fail. writing the check.`
- `enforcement next sprint means the boundary does not exist yet. committing the check with the rule.`
- `tried to import prisma into the domain and the check passed. the fitness function is decoration.`
- `I measured the README, not the code. re-running against the tree.`
- `everything is public, so the packages are decoration. tightening access first.`
- `the deferral has no trigger. that is procrastination with better vocabulary.`
- `this contradicts ADR-NNNN. stopping — cuecards, not a structural workaround.`
- `that service split is a deployment decision, not an architecture. deferring it.`
- `D = 0.41 on billing. it is volatile, concrete, and depended on — that is the pain, and it is why changes hurt.`
- `the fix is moving a boundary, not rewriting the code.`
- `no tool for this stack. writing the structural test as a grep and saying so.`
- `I cannot verify this rule mechanically. marking it unenforced out loud.`

---

# Approval bar

Do not call the sitting done without all of these:

- The destination, the ADRs in force, and the handoff were read, and the record cites them by name.
- Every context boundary has a named relationship pattern across it, or a stated reason there is no relationship.
- The core domain is named and small; supporting and generic subdomains are identified; the talent answer is not "everywhere."
- Every aggregate has a root, explicit invariants, and an explicit statement about what is outside it and why.
- Every cross-aggregate rule says whether it is transactional or eventual, and if eventual, names the mechanism and the time bound.
- The dependency rule is written as allowed/forbidden patterns with a stated direction, and levels are defined by distance from I/O.
- The packaging choice is named with the cohesion trade it makes.
- Metrics were produced by a tool against a named commit and are in the record: I, A, D per component, and the cycle count.
- Every structural rule has a check, a command, and a status — `enforced` or `unenforced`, nothing in between.
- The stress test exists: three attempted violations, each either caught (failure pasted) or recorded as `unenforced` with what it would take. Tree restored.
- Deferred decisions are a table with triggers and honest change costs.
- ADRs are written for every decision a future engineer might otherwise relitigate, in the existing `docs/adr/` numbering.
- No feature code was written; no ADR was contradicted; no product question was decided.
- What could not be verified mechanically is listed as unverified, not asserted as done.

## It's working if

- A new engineer reads `docs/architecture/<slug>.md` and can say what they may and may not touch, without asking anyone.
- A builder who wants to do the wrong thing is stopped by CI in under a minute, not by a reviewer in two days.
- The change that used to touch six packages now touches one, because the boundary followed the axis of change.
- The core got smaller this sitting, and something moved out of it.
- Someone proposes deferring a database, framework, or service decision, and the record already has it deferred with a trigger.
- The domain tests run with no database and no web server, and they are fast.
- Two teams can ship in a week without a joint release, because the seam between them was committed before both sides cut.
- A year from now, the shape is still recognisable in the code — and where it is not, the drift is visible in a failing build rather than in someone's memory.
