# Castle

Three agent skills that take a fuzzy idea all the way to a shipped, checkable destination — with a human deciding what a human should decide.

Each skill is small, self-contained, and composable. They work with any agent that reads skill files, and every durable artifact they produce lands in your repo — issues, ADRs, a handoff, a map — so the work survives the session that made it.

## The pipeline

```
fuzzy idea ──▶ CUECARDS ──▶ ADRs + handoff ──▶ ONESLICE ──▶ one proven slice
                  (decide)                      (build)
                                                    LANES ──▶ the whole destination, in parallel
                                                           (ship)
```

| Skill | Use when | Leaves behind |
| --- | --- | --- |
| [cuecards](cuecards/SKILL.md) | An idea is too big or too fuzzy for one sitting, and choices must be made before anyone builds | A board of choice cards (GitHub issues), ADRs in `docs/adr/`, a handoff in `docs/cuecards/` |
| [oneslice](oneslice/SKILL.md) | Implementing one slice of a decided handoff | One slice that passed a strict quality bar, on a short-lived branch, with a human-readable ticket |
| [lanes](lanes/SKILL.md) | Shipping the whole destination, with parallel workstreams or a time/spend budget | A committed map in `docs/lanes/`, lanes that did not collide, the destination Check passing |

Each skill knows its lane: cuecards never ships, oneslice never decides product, lanes never reopens product. The handoff and the ADRs are the contract between them.

## Install

Run from your **project root** — no cloning needed:

```bash
# All three skills (full pipeline)
npx degit Sehaan-1/Skills/Castle/cuecards  .claude/skills/cuecards
npx degit Sehaan-1/Skills/Castle/oneslice  .claude/skills/oneslice
npx degit Sehaan-1/Skills/Castle/lanes     .claude/skills/lanes
```

Or just the one you need right now:

```bash
npx degit Sehaan-1/Skills/Castle/cuecards  .claude/skills/cuecards
```

Any agent that reads skill files works the same way: each `Castle/<name>/` directory (its `SKILL.md` plus `agents/`) is one self-contained skill. No configuration needed — the board lives on your repo's GitHub issues, and ADRs, the handoff, and the map live in the repo.

> Note: the `npx skills` CLI auto-discovers skills under a top-level `skills/` folder, and this collection deliberately lives under `Castle/` — so it installs by copy. In your own fork, `mv Castle skills` restores CLI discovery if you prefer it.

## A full run, in one paragraph

An idea arrives that is too big for one session. **Cuecards** names the destination with you — including *how we'll know we're there*: a walk, proof, and something that enforces it — then lays the effort out as a board of choice cards on GitHub that a non-technical person can read and answer. Unattended cards (look-ups, chores) run in parallel; for-you cards wait for you. Each decision closes into a numbered ADR in `docs/adr/`. When the board is done, cuecards writes a handoff and stops. **Oneslice** then builds one handoff slice at a time, each independently checkable, each held to a hard quality bar: no spaghetti, no secrets, research cited to primary sources, tickets in spoken English. When many slices can move at once — or a team is on it — **Lanes** cuts the work into parallel lanes around committed seams, locks the destination Check, and loops in measured rounds until the walk works, a named human blocks it, or the budget says stop starting.

## Worked example

[`examples/invoicing/`](examples/invoicing/) walks the whole pipeline on one tiny effort — a board, three cards, three ADRs, a handoff, and a lanes map — so you can see every artifact before you run the skills.

## Design notes

- **Plan, don't do.** Cuecards produces decisions, not deliverables. The pull to start building is the signal the board has reached its edge.
- **A checkable destination.** "Done" is a walk that works, proof in the repo, and CI that fails if it regresses — not a vibe and not a wall of agreed words.
- **Verifiable provenance.** An agent cannot close its own choice cards, self-certify checks by assertion, or name itself integration owner. Claims without committed artifacts are red flags, not completion.
- **Decisions are ADRs.** Closed cards point at numbered, append-only ADRs that later cards and later agents cite by name. Supersede; never rewrite.
- **Easy words, hard thinking.** Every human-facing artifact (card, ticket, map) is written for a smart person who does not know the stack — after, not instead of, the deep review.
- **One slice per sitting; lock, then loop.** Oneslice stops when its slice's Check passes. Lanes locks the target and keeps rounding until the destination Check passes or a named human blocks it. A budget stops you *starting* work — it never buys a weaker Check.
