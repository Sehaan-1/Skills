# Castle

Four agent skills that take a fuzzy idea all the way to a shipped, checkable destination — with a human deciding what a human should decide, and the interface actually looking like something.

Each skill is small, self-contained, and composable. They work with any agent that reads skill files, and every durable artifact they produce lands in your repo — issues, ADRs, a handoff, a map, a `DESIGN.md`, a walk record — so the work survives the session that made it.

## The pipeline

```
fuzzy idea ──▶ CUECARDS ──▶ ADRs + handoff ──▶ ONESLICE ──▶ one proven slice
                  (decide)                      (build)
                                                    LANES ──▶ the whole destination, in parallel
                                                    (ship)

                              HERALDRY ──▶ the arms, and an interface that can prove it wears them
                              (design: runs beside oneslice and lanes)
```

| Skill | Use when | Leaves behind |
| --- | --- | --- |
| [cuecards](cuecards/SKILL.md) | An idea is too big or too fuzzy for one sitting, and choices must be made before anyone builds | A board of choice cards (GitHub issues), ADRs in `docs/adr/`, a handoff in `docs/cuecards/` |
| [oneslice](oneslice/SKILL.md) | Implementing one slice of a decided handoff | One slice that passed a strict quality bar, on a short-lived branch, with a human-readable ticket |
| [lanes](lanes/SKILL.md) | Shipping the whole destination, with parallel workstreams or a time/spend budget | A committed map in `docs/lanes/`, lanes that did not collide, the destination Check passing |
| [heraldry](heraldry/SKILL.md) | Any interface has to be designed, built, redesigned, or made to look good: a page, a screen, a component, a design system, a visual direction, a reference board, or a `DESIGN.md` | A board of three cast tiles with a human's pick, `DESIGN.md` (the arms) at the repo root, a critique table, and a walk record in `docs/heraldry/` |

Each skill knows its lane: cuecards never ships, oneslice never decides product, lanes never reopens product, heraldry never decides what to build. The handoff and the ADRs are the contract between them. `DESIGN.md` is the contract for how it looks, and both oneslice and lanes cite it instead of inventing a visual language mid-slice.

## Install

Run from your **project root** — no cloning needed:

```bash
# All four skills (full pipeline)
npx degit Sehaan-1/Skills/Castle/cuecards  .claude/skills/cuecards
npx degit Sehaan-1/Skills/Castle/oneslice  .claude/skills/oneslice
npx degit Sehaan-1/Skills/Castle/lanes     .claude/skills/lanes
npx degit Sehaan-1/Skills/Castle/heraldry  .claude/skills/heraldry
```

Or just the one you need right now:

```bash
npx degit Sehaan-1/Skills/Castle/heraldry  .claude/skills/heraldry
```

Any agent that reads skill files works the same way: each `Castle/<name>/` directory (its `SKILL.md` plus `agents/`) is one self-contained skill. No configuration needed — the board lives on your repo's GitHub issues, and ADRs, the handoff, the map, and the arms live in the repo.

> Note: the `npx skills` CLI auto-discovers skills under a top-level `skills/` folder, and this collection deliberately lives under `Castle/` — so it installs by copy. In your own fork, `mv Castle skills` restores CLI discovery if you prefer it.

## A full run, in one paragraph

An idea arrives that is too big for one session. **Cuecards** names the destination with you — including *how we'll know we're there*: a walk, proof, and something that enforces it — then lays the effort out as a board of choice cards on GitHub that a non-technical person can read and answer. Unattended cards (look-ups, chores) run in parallel; for-you cards wait for you. Each decision closes into a numbered ADR in `docs/adr/`. When the board is done, cuecards writes a handoff and stops. **Heraldry** reads the brief, says out loud what this thing should feel like and which register it belongs to, casts three tiles of the same screen in three directions, and lets the human point at one. Then it writes `DESIGN.md` — the arms: one accent, one radius system, one theme, an explicit list of what is banned. It then builds or critiques the interface against those arms in short loops, and refuses to call a screen done until there are fresh renders at three widths in both themes, a critique table, and a walk record in the repo. **Oneslice** then builds one handoff slice at a time, each independently checkable, each held to a hard quality bar: no spaghetti, no secrets, research cited to primary sources, tickets in spoken English. When many slices can move at once — or a team is on it — **Lanes** cuts the work into parallel lanes around committed seams, locks the destination Check, and loops in measured rounds until the walk works, a named human blocks it, or the budget says stop starting.

## Worked examples

[`examples/invoicing/`](examples/invoicing/) walks the whole pipeline on one tiny effort — a board, three cards, three ADRs, a handoff, and a lanes map — so you can see every artifact before you run the skills.

[`examples/heraldry/`](examples/heraldry/) carries the arms for that same effort: a `DESIGN.md`, a critique table, and a walk record. Read the three files in order and you have seen everything heraldry produces.

## Sources and further reading

[heraldry](heraldry/SKILL.md) is a synthesis, not a fork. The rules were merged, deduplicated, re-scoped to this pipeline, and rewritten in this collection's voice, so nothing in the skill file is a quote from anywhere. The reading list below is here so you can go deeper, track an upstream as it evolves, or borrow the parts heraldry chose to leave out.

**Directly drawn on**

| Skill | Where to read it | What to take from it |
| --- | --- | --- |
| `design-taste-frontend` (taste-skill v2) | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/taste-skill) · [upstream](https://github.com/Leonxlnx/taste-skill) | the reading-the-room pass, the three dials, layout discipline, content density, the tells catalogue, the redesign protocol |
| `design-taste-frontend-v1` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/taste-skill-v1) · [upstream](https://github.com/Leonxlnx/taste-skill) | the baseline-config format and the pre-flight checklist shape |
| `gpt-taste` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/gpt-tasteskill) · [upstream](https://github.com/Leonxlnx/taste-skill) | the hero line limit, gapless bento grids, the meta-label ban |
| `stitch-design-taste` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/stitch-skill) · [upstream](https://github.com/Leonxlnx/taste-skill) | the `DESIGN.md` section model: atmosphere, palette, typography, components, layout, motion, bans |
| `design-md` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/design-md) · [upstream](https://github.com/google-labs-code/stitch-skills/blob/main/plugins/stitch-utilities/skills/design-md/SKILL.md) | `DESIGN.md` as a managed single source of truth |
| `stitch-loop` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/stitch-loop) · [upstream](https://github.com/google-labs-code/stitch-skills/blob/main/plugins/stitch-utilities/skills/stitch-loop/SKILL.md) | the critique → adjust → ship fidelity loop |
| `emil-design-eng` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/emil-design-eng) · [upstream](https://github.com/emilkowalski/skills) | the animation decision framework, easing curves, duration bands, springs, origin-aware popovers, performance reality |
| `emilkowalski-motion` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/emilkowalski-motion) · [upstream](https://emilkowal.ski) | post-generation motion restraint |
| `frontend-design` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/frontend-design) · [upstream](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | commit to one aesthetic, build the real interface, refine craft, self-review |
| `web-design-guidelines` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/web-design-guidelines) · [upstream](https://github.com/vercel-labs/web-interface-guidelines) | the accessibility, focus, form, and product-UI rules in the pre-flight |
| `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`, `image-to-code-skill` | [web](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-web) · [mobile](https://github.com/nexu-io/open-design/tree/main/skills/imagegen-frontend-mobile) · [brandkit](https://github.com/nexu-io/open-design/tree/main/skills/brandkit) · [image-to-code](https://github.com/nexu-io/open-design/tree/main/skills/image-to-code-skill) · [upstream](https://github.com/Leonxlnx/taste-skill) | generate the reference image first, one image per direction rather than a collage, then build against it with a fidelity check |
| `impeccable-design-polish` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/impeccable-design-polish) · [upstream](https://github.com/pbakaus/impeccable) | the follow-up modes: audit, critique, polish, animate, harden, live |
| `design-review` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/design-review) · [upstream](https://github.com/garrytan/gstack) | audit first, then fix, in leverage order |
| `plan-design-review` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/plan-design-review) · [upstream](https://github.com/garrytan/gstack) | rating each dimension against what a ten looks like |
| `redesign-skill` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/redesign-skill) · [upstream](https://github.com/Leonxlnx/taste-skill) | the preservation rules and modernization levers |
| `minimalist-ui`, `high-end-visual-design`, `brutalist-skill` | [minimalist](https://github.com/nexu-io/open-design/tree/main/skills/minimalist-skill) · [soft](https://github.com/nexu-io/open-design/tree/main/skills/soft-skill) · [brutalist](https://github.com/nexu-io/open-design/tree/main/skills/brutalist-skill) · [upstream](https://github.com/Leonxlnx/taste-skill) | banned-default lists and negative constraints by aesthetic family |
| `ui-skills` | [catalogue](https://github.com/nexu-io/open-design/tree/main/skills/ui-skills) · [upstream](https://github.com/ibelick/ui-skills) | opinionated, evolving interface constraints |

**Also worth reading**

- [`taste-design`](https://github.com/google-labs-code/stitch-skills/blob/main/plugins/stitch-utilities/skills/taste-design/SKILL.md) and [`extract-design-md`](https://github.com/google-labs-code/stitch-skills/blob/main/plugins/stitch-design/skills/extract-design-md/SKILL.md): the sibling workflow for pulling a `DESIGN.md` back out of an existing screen, which heraldry's audit step does by hand.

- [`color-expert`](https://github.com/meodai/skill.color-expert) for OKLCH, palette generation, and contrast science beyond the arithmetic in the pre-flight.
- [`apple-hig`](https://github.com/raintree-technology/apple-hig-skills) and [`platform-design`](https://github.com/ehmo/platform-design-skills) for the platforms heraldry lists as out of scope.
- [`frontend-skill`](https://github.com/openai/skills) for restrained composition on marketing surfaces.
- The catalogue these were read from: [nexu-io/open-design → `skills/`](https://github.com/nexu-io/open-design/tree/main/skills).

Licensing differs per upstream (MIT for most, Apache-2.0 for Anthropic's and Vercel's): check before you redistribute their files. heraldry itself copies no text from any of them.

## Design notes

- **Plan, don't do.** Cuecards produces decisions, not deliverables. The pull to start building is the signal the board has reached its edge.
- **A checkable destination.** "Done" is a walk that works, proof in the repo, and CI that fails if it regresses — not a vibe and not a wall of agreed words.
- **Verifiable provenance.** An agent cannot close its own choice cards, self-certify checks by assertion, or name itself integration owner. Claims without committed artifacts are red flags, not completion.
- **Decisions are ADRs.** Closed cards point at numbered, append-only ADRs that later cards and later agents cite by name. Supersede; never rewrite.
- **Easy words, hard thinking.** Every human-facing artifact (card, ticket, map) is written for a smart person who does not know the stack — after, not instead of, the deep review.
- **One slice per sitting; lock, then loop.** Oneslice stops when its slice's Check passes. Lanes locks the target and keeps rounding until the destination Check passes or a named human blocks it. A budget stops you *starting* work — it never buys a weaker Check.
- **The arms are written, not remembered.** Heraldry commits `DESIGN.md` before the second screen, so two agents a week apart produce the same castle instead of two opinions. The bans are part of the design system; a system without them is a mood board.
- **Breadth lives in registers, not in forks.** Nine named registers (Keep, Scriptorium, Cathedral, Barbican, Armoury, Watchtower, Solar, Bazaar, Masquerade) carry the range that would otherwise become nine drifting stylesheets. One skill, one contract, nine starting positions, and the arms still govern whatever a register starts.
- **Picture before prose.** "Premium" and "calm" mean ten things each. Three tiles of the same real screen in three registers, one deliberate outlier among them, and a human pointing at one settles in a minute what a page of adjectives cannot settle at all. The tile is a promise; the walk is where you check whether the build kept it.
- **Taste is shown, not claimed.** Fresh renders at 375 / 768 / 1440 in both themes, a critique table, and a mechanical pre-flight with pasted output — or the honest word `unrendered`. An agent may not certify its own taste by assertion, and a walk that could not fail is a slideshow, not a check.
