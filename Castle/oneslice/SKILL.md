---
name: oneslice
description: "Use when implementing one Cuecards handoff slice, one ticket, or one milestone of an already-decided board. Use when the user asks to build, implement, or code from a handoff. Use when a slice is blocked on official docs, API facts, or source-of-truth reading. Use when a slice defines or changes an API, module boundary, or public contract. Use when a slice handles untrusted input, auth, secrets, or third-party services. Do not use to decide product questions or to ship the whole destination in one sitting."
---

# Oneslice

Build **one** handoff slice. Prove it. Stop.

Cuecards decided. The handoff sequenced. This skill cuts code for a single slice — a ticket or milestone — and holds it to an unusually strict quality bar. It does not reopen product questions. It does not start the next slice. It does not rubber-stamp "it works."

Announce at start: `Using oneslice to [pick the slice | research | track | increment | build | prove | review | stop].`

## Hard gates

1. **No handoff, no build.** Read `docs/cuecards/handoff-<slug>.md`. If it is missing, incomplete, or full of placeholders, stop and send them to cuecards. Do not invent a plan while coding.
2. **One slice per sitting.** The unit is one handoff `### Slice N`. Not the board. Not "while I'm here." Not the rest of the milestone list. When that slice's **Check** passes and the quality bar passes, stop.
3. **ADRs are law.** Cited ADRs for this slice are closed decisions. Do not quietly contradict them. If the code cannot honor an ADR, stop and say which ADR — that is a cuecards sitting, not a clever workaround.
4. **The slice Check is the definition of done.** Walk / proof / test named on the slice (and the board's **How we'll know we're there**, if this slice advances it). A green vibe is not done.
5. **Working is not the bar.** Behavior-correct spaghetti is a failed slice. Restructure before you call it done.
6. **Do not swell the destination.** Notes, "Not this effort," and uncited ADRs are out of scope. New product questions go back to cuecards, as cards, not as bonus code.
7. **Claim before you cut.** If the slice maps to a GitHub issue or milestone, assign it first. Comment the result on that issue when you stop. Do not open extra issues to hide extra work.
8. **Do not guess at facts you do not own.** If the slice depends on a third-party API, official docs, a spec, or source outside this working tree, investigate against **primary sources** and capture a cited Markdown file **before** (or in parallel with) writing the code that depends on those facts. Do not code from memory, a blog, or a secondary write-up. Do not turn research into a product decision — that is cuecards.
9. **The ticket is for a person.** The GitHub issue for this slice is written in spoken English. Status, what landed, and what you didn't touch must be readable without you translating. Agent jargon as the live status is a defect.
10. **Thin increments inside the slice.** Implement → test → verify → commit. The tree stays compilable. One logical thing per commit. Adjacent mess is logged, not "cleaned up while I'm here."
11. **Save points on a short-lived branch.** Branch off the default. Commit when an increment is green. Revert to the last commit if the next one fails. Never commit secrets. `main` stays deployable.
12. **Contract before code** when this slice is a public surface (API, module boundary, props, schema). Types first. One error shape. Validate at the edge. Additive fields only. Honour an idempotency key atomically, or don't accept one.
13. **Name the trust boundary before you cut** when this slice accepts untrusted data, does auth, stores PII, talks to third parties, handles uploads/webhooks, or uses LLM output. Five-minute threat model. Ask the human before new auth, PII, uploads, CORS, or integrations. Never commit secrets.

<!-- ── PROVENANCE GATES (added to prevent self-adjudication) ──────────────── -->

14. **Research artifact committed before dependent code.** Gate 8 allows research to happen
    "in parallel" — but that window closes at commit time. You may not commit code that
    assumes an API or doc fact unless the research Markdown file (with cited primary sources)
    is already committed to the branch in the same or an earlier commit. If the research is
    not yet written, commit the research file first as a standalone commit, then commit the
    code. A commit message that says "research TBD" or "will verify later" is a defect. The
    research file path must appear in the GitHub issue comment that records the increment.

15. **"Check passed" requires a reproducible artifact, not a claim.** When you update the
    ticket status to `Check passed`, you must link:
    - The commit SHA that the Check ran against, and
    - Either a CI run URL **or** a terminal transcript (timestamped, showing the walk
      command and its output) saved under `docs/research/<slice-slug>-check.md`.

    "I ran it and it passed" with no linked artifact is not `Check passed`. It is
    `In progress`. The same agent that wrote the code cannot self-certify by assertion —
    the artifact is the certification. If CI is not yet wired for this slice, save the
    transcript before updating the ticket.

<!-- ──────────────────────────────────────────────────────────────────────── -->

## Pick the slice

1. Open the handoff.
2. Take the slice they named. If they named none, take the first slice whose **Depends on** is done.
3. Read, in order: that slice block, every ADR it cites, board Notes / constraints, the slice **Check**, and any look-card proof it depends on.
4. Say out loud: `Building Slice N: <spoken name>. ADRs: …. Check: …. Then I stop.`
5. If the slice is not independently checkable, or depends on an unfinished slice, do not start. Say what's missing.

If two slices are independent and they explicitly ask to do both: still do **one**, prove it, then ask. Default is one.

## Human-readable tracker

The live ticket is the GitHub issue for this slice (or a comment on the board issue if the slice has no child). Write it so a non-technical person can open it and know what is going on.

On claim, post or set the body to:

```markdown
## Slice N: <spoken name>

**For you to read.**

### What this slice does
<from the handoff, one short paragraph>

### How we'll know
<the Check, in everyday words>

### Decisions this honors
- [ADR-NNNN Title](path)

### Status
In progress — claimed.

### What landed
_(empty until an increment commits)_

### What I didn't touch (on purpose)
_(scope discipline — fill as you notice adjacent mess)_

### Blocked
nothing

### Provenance
- Research file: <path or "none needed">
- Check artifact: <CI run URL or transcript path — required before status = Check passed>
```

After every increment and when you stop, **update that ticket in the same voice**. Refer to the slice and ADRs **by name**. Never a bare `#42`. Never dump a compiler log as the status.

Status is one of: `In progress` · `Check passed` · `Blocked: <plain reason>` · `Handed back to cuecards: <which ADR/question>`.

---

# Research (when the slice depends on facts you do not own)

Use this when implementation needs a topic investigated, official docs or API facts gathered, or reading that would stall the sitting. Do **not** use it to choose what the product should be.

Spin up a **background agent** (or parallel subagent) to do the reading so you can keep measuring, scaffolding, and cutting work that does **not** depend on the answer. If this harness has no background/subagent tool, do the research yourself **first**, write the file, then cut — still do not skip the artifact.

The research agent's job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a **single Markdown file**, citing each claim's source (link + what it actually says).
3. Save it where the repo already keeps such notes; match the existing convention. If there is none, put it somewhere sensible (prefer `docs/research/<slice-slug>.md`) and say where.

Rules:

- One question per research file. If the slice has two independent unknowns, two agents / two files.
- The file is evidence for *how* to implement this slice, not a new ADR. If the finding contradicts an ADR or the slice **Does**, stop — cuecards, not a silent product change.
- You may keep cutting parts of the slice that do not depend on the finding. Do not merge code that assumes the answer until the file exists and you have read it.
- Link the file from the GitHub issue comment when you report.

---

# Core prompt

Start from this baseline, then the standards below:

> Implement this one slice so the named Check passes.
> Rethink how to structure the change so the code is simpler, smaller, more direct, and more elegant than the first idea.
> Improve abstractions and modularity. Reduce spaghetti. Improve succinctness and legibility.
> Be ambitious: if a clear path to a better implementation means restructuring some of the codebase, take it — as long as you do not enlarge the slice.
> Be extremely thorough. Measure twice, cut once.
> Preserve behavior required by the ADRs and the Check. Delete incidental complexity.

You are not a reviewer leaving comments for someone else. You **build**, then you **hold your own diff to this bar**, and you rewrite until it passes or you stop and say what blocked you.

## Non-negotiable standards

0. **Be ambitious about structural simplification.**
   - Do not stop at "this could be a bit cleaner."
   - Reframe so whole branches, helpers, modes, conditionals, or layers disappear.
   - Prefer the solution that feels inevitable in hindsight.
   - Assume a "code judo" move exists: a reorganization that uses the existing architecture and makes the change dramatically simpler.
   - If you can delete complexity rather than rearrange it, do that.

1. **Do not push a file from under 1k lines to over 1k lines without a very strong reason.**
   - Treat that as a smell. Extract helpers, modules, or local abstractions.
   - If the diff would cross 1000 lines, decompose first. Only waive if there is a compelling structural reason and the file stays clearly organized.
   - Do not "just finish the slice" by dumping into a giant file.

2. **Do not allow random spaghetti growth.**
   - No ad-hoc conditionals, scattered special cases, or one-off branches in unrelated flows.
   - "Weird if statements in random places" is a design problem. Put the logic in a dedicated abstraction, helper, state machine, policy, or module.
   - If the surrounding code gets harder to reason about, the slice is not done.

3. **Bias toward cleaning the design, not accepting working code.**
   - Same behavior, cleaner structure → take the cleaner structure.
   - Do not ship an "it works" implementation that leaves the codebase messier.
   - Prefer removing moving pieces over spreading the same complexity around.

4. **Prefer direct, boring, maintainable code over hacky or magical code.**
   - Brittle, ad-hoc, or "magic" behavior is a quality failure.
   - Be skeptical of generic mechanisms that hide simple data-shape assumptions.
   - Thin wrappers, identity abstractions, and pass-through helpers that add indirection without clarity: delete them.

5. **Push hard on type and boundary cleanliness.**
   - Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer boundary could exist.
   - Prefer explicit typed models or shared contracts over loosely-shaped ad-hoc objects.
   - Silent fallbacks that paper over an unclear invariant: make the boundary explicit.

6. **Keep logic in the canonical layer and reuse existing helpers.**
   - No feature logic leaking into shared paths. No implementation details leaking through APIs.
   - Prefer existing canonical utilities over bespoke one-offs.
   - Put code in the package, service, or module that already owns the concept.

7. **Treat unnecessary sequential orchestration and non-atomic updates as smells when the cleaner structure is obvious.**
   - Independent work serialized for no reason → simplify; parallelize if that also clarifies.
   - Related updates that can leave state half-applied → make them atomic.
   - Do not chase micro-optimizations. Do flag orchestration that makes the slice more brittle.

8. **Honor the slice boundary.**
   - Files, tests, and commits belong to this slice's **Does** and **Check**.
   - A "while I'm here" refactor that is not required to make this slice inevitable: leave it, or call it out and get a yes before expanding.
   - Code judo inside the slice is required. Rewriting the rest of the product is not this sitting.

## Primary questions (ask of your own diff)

- Is there a code-judo move that would make this dramatically simpler?
- Can this be reframed so fewer concepts, branches, or helper layers are needed?
- Does this improve or worsen the local architecture?
- Did the diff add branching where a better abstraction should exist?
- Did a cohesive module become more coupled, more stateful, or harder to scan?
- Is this logic in the right file and layer?
- Did this enlarge a file or component past a healthy size?
- Are there repeated conditionals that signal a missing model or helper?
- Is the implementation direct, or special-casey?
- Is this abstraction earning its keep, or is it a wrapper?
- Did I introduce casts, optionality, or ad-hoc shapes that hide the invariant?
- Did I leak details across a boundary?
- Is orchestration more sequential or less atomic than it needs to be?
- Does the named **Check** actually fail when I break this slice on purpose?
- Did I contradict an ADR?
- Did I code a foreign API/docs shape from memory or a blog instead of a cited primary source?
- Can a non-technical person read the GitHub ticket and know status?
- Did I leave the tree broken between increments, or mix two logical things in one commit?
- If this is a public surface: did the contract exist before the implementation?
- If this crosses a trust boundary: can I name the boundary, the asset, and the abuse case?

## What you must not ship

Everything a Hard gate or Non-negotiable standard forbids is on this list too. On top of them:

- A refactor that moves code around but does not reduce concepts a reader must hold
- Narrow edge-case handling in the middle of an already busy function
- "Temporary" branching that will become permanent debt
- Tests that pass while the code is less modular or less readable
- Extra product behavior not in this slice, these ADRs, or this Check
- A Check you never ran, or a Check that would still pass if the slice were broken

## Preferred remedies (do these)

- Delete a whole layer of indirection rather than polishing it
- Reframe the state model so conditionals disappear
- Change the ownership boundary so the feature is a natural extension of an existing abstraction
- Turn special-case logic into a simpler default with fewer exceptions
- Extract a helper or pure function; split a file that has grown past its shape
- Replace condition chains with a typed model or explicit dispatcher
- Reuse the canonical helper; move logic to the module that owns the concept
- Make related updates atomic; parallelize independent work when it also simplifies orchestration

Do not be satisfied with "maybe rename this" when the issue is structural.
Do not be satisfied with a merely cleaner version of the same messy idea if a much simpler idea is available.

## Tone

Be direct, serious, and demanding about quality — including toward your own first draft.
Do not be rude. Do not soften a maintainability failure into a note for later.
If the code makes the codebase messier, say so and fix it before you stop.
If you missed a dramatic simplification, take it before you stop.

Useful self-talk (and useful things to tell the human if you must stop):

- `this pushes the file past 1k lines. decomposing first.`
- `this adds a special-case branch into an already busy flow. moving it behind its own abstraction.`
- `this works, but it makes the surrounding code more spaghetti. keeping behavior, restructuring.`
- `feature logic was leaking into a shared path. isolating it.`
- `this abstraction is unnecessary. keeping the direct flow.`
- `this needs a cast/optional. making the boundary explicit instead.`
- `bespoke helper duplicates a canonical one. reusing the canonical one.`
- `code-judo: reframing so these branches disappear.`
- `this refactor moved complexity but didn't delete it. simplifying the model.`
- `this contradicts ADR-NNNN. stopping. cuecards sitting, not a workaround.`
- `slice Check still wouldn't catch a break. fixing the proof before calling done.`
- `this depends on their API/docs. background research on primary sources; cutting the rest in parallel.`
- `finding contradicts ADR-NNNN. stopping. cuecards sitting.`
- `tracker was jargon. rewriting in spoken English.`
- `about to write 200 lines before a test. stopping, proving, committing.`
- `this is a public surface. contract first.`
- `can't name the trust boundary. not ready to cut.`
- `new auth/PII/upload/CORS. asking the human first.`
- `staged diff has a token. aborting the commit.`

---

# Inner increments (inside this one slice)

The handoff slice is the sitting. Inside it, still cut **thin vertical pieces**: one complete path, then test, then commit.

```
Implement ──→ Test ──→ Verify ──→ Commit ──→ next increment
                 (project still builds; existing tests still pass)
```

- **Simplest thing that could work.** Three similar lines beat a premature EventBus. Naive-correct first; abstract on the third real use, not the first.
- **One logical thing** per increment. Do not mix a new endpoint, a refactor, and a config change.
- **Keep it compilable.** Never leave the tree broken between increments.
- **Safe defaults.** New behavior is opt-in / conservative unless the ADR says otherwise.
- **Rollback-friendly.** Additive when you can. Don't delete and replace in the same commit.
- **Feature flags** if this increment must merge before the slice is user-visible.
- **Scope discipline.** Adjacent mess goes under **What I didn't touch** on the tracker. Do not "clean up while I'm here."
- If you are about to write more than ~100 lines before tests: you already skipped a slice-inside-the-slice. Stop, test, commit, then continue.
- Vertical (DB + API + thinnest UI for one action) beats horizontal layers. Riskiest unknown first when the slice has one.

**When NOT to subdivide:** a single-file, single-function change that is already the whole Check.

# Git

`main` (or the repo default) stays deployable. Work on a **short-lived** branch: `feature/<slice-spoken-slug>` or `fix/<…>`. Merge in days, not weeks. Prefer a flag over a long-lived branch.

**Save-point pattern:** increment passes → commit → continue. Increment fails → revert to last commit → investigate. You never lose more than one increment.

**Atomic commits.** One logical thing. Message:

```
<type>: <short description>

<why, not what. name the slice and ADR-NNNN.>
```

Types: `feat` `fix` `refactor` `test` `docs` `chore`. Do not combine format-only changes with behavior.

**Size.** Aim ~100 lines per commit. A ~300-line single logical change is acceptable. Crossing ~1000 lines: split before you commit.

**Before every commit:**

1. `git diff --staged` — you know what you're saving
2. Scan the staged diff for secrets (`password`, `secret`, `api_key`, `token`)
3. Run this repo's test, lint, and typecheck commands (discover them; don't invent)
4. Do not re-run the same command on unchanged code "to be sure"

If a secret ever hits a remote: **rotate it first**, then purge. Deleting the line is not enough.

**After each increment, tell the human:**

```
CHANGES MADE:
- <path>: <what and why>

THINGS I DIDN'T TOUCH (intentionally):
- <path>: <why out of scope>

POTENTIAL CONCERNS:
- <assumption to confirm>
```

Do not force-push shared branches. Do not commit `node_modules/`, `.env`, or build output. Honor `.gitignore`.

If this slice is a **consumer-facing release**, version is `MAJOR.MINOR.PATCH` (breaking / additive / fix), tag is source of truth, changelog is curated impact — not `git log`. Write the changelog entry in the same change. When unsure if it's breaking, assume it is (Hyrum: if they can observe it, they depend on it).

Worktrees are allowed when two agents must not share a working tree. Still one slice per sitting per worktree.

# Interfaces (when this slice is a public surface)

If the slice designs or changes an API, module boundary, component props, GraphQL schema, or frontend/backend contract: write the contract **before** implementation.

- **Contract first.** Typed input (what the caller sends) vs output (including server-generated fields). Discriminated unions for variants. Branded IDs so a UserId is not a TaskId. Types are the spec.
- **Hyrum's Law.** Every observable behavior is a potential commitment. Don't leak internals. Plan deprecation when you add, not when you regret.
- **One version.** Extend; don't fork a second API "for now."
- **One error shape** everywhere. Don't mix throw / null / `{ error }`. REST: same body (`code` + `message` + optional `details`); 400 invalid · 401 unauthenticated · 403 forbidden · 404 missing · 409 conflict · 422 semantically invalid · 500 server (never internals).
- **Validate at the edge** (HTTP, forms, env, **third-party responses**). Trust internals that already share the contract. Do not re-validate between internal functions. Third-party JSON is untrusted.
- **Add optional fields.** Don't change types or remove fields.
- **Naming.** REST paths: plural nouns, no verbs (`GET /api/tasks`, not `/api/createTask`). JSON fields camelCase; booleans `is`/`has`/`can`; enums UPPER_SNAKE. PATCH for partial; PUT only when the client sends the whole object. Lists paginate from the start (`data` + `pagination`).
- **Idempotency:** accepting a key is not honouring it. Key from the **client**, stable across retries of one intent. Claim **atomically** (unique constraint, not check-then-act). Same key + different body fails loudly (422). In-flight duplicate is a deliberate 409 / wait / 202. Retention outlives the longest retry path (including dead-letter). Timeouts are a third outcome: **unknown**. State-changing endpoints honour a key or are marked unsafe to retry.

If the contract would break an ADR or a consumer, stop — that is cuecards or an explicit major, not a quiet field change.

# Security (when this slice crosses a trust boundary)

If the slice handles user input, auth, sessions, PII, payments, uploads, webhooks, third-party APIs, or LLM output: five minutes of threat model first — trust boundaries (trust follows who *wrote* the value), assets, STRIDE, one abuse case next to the use case. If you cannot name the boundaries, you are not ready to cut.

**Always:** validate at the boundary; parameterize queries; encode output; HTTPS; hash passwords (bcrypt/scrypt/argon2); security headers; httpOnly/secure/sameSite cookies; audit the lockfile before release.

**Ask the human first:** new auth flows, new PII/payment storage, new external integrations, CORS changes, uploads, rate-limit changes, elevated roles.

**Never:** commit or log secrets; trust client-side validation as the boundary; `eval` / `innerHTML` with untrusted data; sessions in `localStorage`; stack traces to users; fetch a user-supplied URL without an allowlist (SSRF); treat LLM output as a command.

Also: authz ≠ authn — after authenticate, check this user may touch *this* resource. Rate-limit auth on a shared store if more than one process. PII: collect only against a stated purpose; working delete. LLM output is untrusted; no secrets or other users' data in context; confirm destructive tool calls. A delete/move/overwrite whose target is derived from a payload is not "a path shape check" — allowlisted root after symlink resolve, not the root itself, ownership evidence **before** the call. If a secret hits a remote: **rotate first**, then purge history.

---

# Build loop

1. **Measure.** Restate **Does**, **Check**, ADRs. Name files. If that already looks like two slices, stop and split the handoff. List foreign facts → **dispatch research**. If this slice is an interface, write the contract first. If it crosses a trust boundary, write the five-minute threat model. Post the human-readable tracker. Branch off default. Claim the issue.
2. **Increment.** Smallest complete piece. Simplest thing that could work. Existing patterns win. Do not assume researched facts until the note exists. Do not touch files the slice does not require.
3. **Prove that increment.** Repo test/lint/typecheck. Build stays green. Watch new tests fail first when you add behavior.
4. **Commit** that increment (atomic, why-message, no secrets, no mixed concerns). Update the tracker: What landed / What I didn't touch.
5. Repeat 2–4 until the slice **Check** can pass.
6. **Prove the slice.** Run the Check. Walk it if it's a walk. Keep fixtures/screenshots/CI pins. Break the new behavior on purpose and watch the Check fail, then restore.
7. **Review the whole slice diff** against the quality bar, interface checklist (if any), and security checklist (if any). Fix structure before nits.
8. **Rewrite** until the approval bar passes, or hand back a blocked slice (ADR conflict, Check impossible, secret/auth question, slice too big).
9. **Report** on the ticket in spoken English. Link research notes, contract types, and Check proof.
10. **Stop.** Do not start Slice N+1.

## Approval bar (do not call the slice done without this)

Behavior correct is not enough. All of these must hold:

- No clear structural regression
- No obvious missed opportunity to make the implementation dramatically simpler when such a path is visible
- No unjustified file-size explosion
- No obvious spaghetti-growth from special-case branching
- No hacky or magical abstraction that makes the code harder to reason about
- No unnecessary wrapper / cast / optionality churn obscuring the design
- No architecture-boundary leak or avoidable canonical-helper duplication
- No missed obvious decomposition that would materially improve maintainability
- Slice **Check** ran and would fail if this slice were broken
- Cited ADRs still true
- Nothing from **Not this effort** landed
- You did not start the next slice
- Tracker issue is updated in spoken English (what landed, what you didn't touch)
- Increments were committed atomically; tests ran before each commit; no secrets in the diff
- If this slice exposed an interface: contract first, one error shape, validate at edge, additive fields, idempotency honoured if you accepted a key
- If this slice crossed a trust boundary: threat model written, always/never rules held, ask-first items actually asked

Any line above that fails is a blocker unless you can justify it in one sentence to the human. If the bar is not met, do not stop with "LGTM, nits later." Fix it, or explicitly hand back a blocked slice.

## It's working if

- Exactly one handoff slice changed behavior, its Check passed, and you know the Check can fail.
- The diff is simpler than the first draft, not merely larger.
- The human is not staring at the rest of the product half-built in this sitting.
- Cuecards was not asked to decide anything you could have coded around.
