# Inquest

The castle's court of inquiry. Where Castle decides and builds from a fuzzy idea, Inquest cross-examines what is already on the table — a design, a system, a document — and returns a verdict: where it is weak, what it will cost, and whether it stands when the load arrives.

Each skill below is small, self-contained, and works with any agent that reads skill files. Skills that examine things which already exist convene here.

## Skills

| Skill | Use when | Leaves behind |
| --- | --- | --- |
| [rampart](rampart/SKILL.md) | A system must be designed, reviewed, scaled, or sized: "design a URL shortener", "review this architecture", "how many servers for 10M DAU?", "SQL or NoSQL?", back-of-the-envelope math, or system design / object-oriented design interview prep | A 4-step design or a review verdict with the trade-off named at every stone — requirements and assumptions, estimates, architecture, bottleneck pass, closing checklist — plus a scored rubric and flashcard decks for interview drill |

## How rampart wires into the others

Rampart sits between the decision skills and the build skills: it sizes the problem and produces the design or the verdict, then hands off.

```
CUECARDS ──▶ RAMPART ──▶ KEYSTONE ──▶ ONESLICE / LANES
(settle scope)  (size + design      (shape the       (build it)
                 or review)          code)
                     │
                     ├── SIEGECRAFT ◀── a number must be provably right,
                     │                  not order-of-magnitude
                     ├── ARMORY ◀── the architecture chose a slot
                     │             ("we need a queue"); pick the package
                     └── HERALDRY ◀── how it looks (never rampart)
```

Each direction is written into both skills: rampart's "Adjacent skills" table in [`SKILL.md`](rampart/SKILL.md), and one sentence each in cuecards, keystone, siegecraft, and armory naming when the sitting belongs to rampart.

## Install

Run from your **project root** — no cloning needed:

```bash
npx degit Sehaan-1/Skills/Inquest/rampart .claude/skills/rampart
```

Or from the packaged file:

```bash
npx degit Sehaan-1/Skills/Inquest/rampart/rampart.skill .
unzip rampart.skill -d .claude/skills/
```

**claude.ai** — Settings → Features → Custom Skills → upload `rampart.skill`, then invoke by name — "use rampart to review this design". It does not auto-activate; see the invocation note below.

**Slash command (Claude Code, optional)** — copy the stub shipped inside the package:

```bash
cp .claude/skills/rampart/commands/system-design.md .claude/commands/system-design.md
# /system-design design a rate limiter
```

**Any agent** — point it at `Inquest/rampart/SKILL.md` and say "follow this skill" or "use rampart to review this design".

**Modes** — `interview` · `design` · `review` · `estimate` · `decide` · `ood` · `study` (see the Invocation section in `SKILL.md`; each mode loads only its own reference files). Routing edge cases: `references/examples.md`.

**Study drill decks** (standalone):

```bash
python3 .claude/skills/rampart/scripts/gen_flashcards.py --deck anki --format tsv --out anki.tsv   # primer's 56 extracted cards
python3 .claude/skills/rampart/scripts/gen_flashcards.py --deck all --format markdown              # built-in + primer cards
```

## Validate & rebuild the package

```bash
# after any edit:
python3 Inquest/rampart/scripts/validate_skill.py --zip Inquest/rampart/rampart.skill
(cd Inquest && rm -f rampart/rampart.skill && zip -r rampart/rampart.skill rampart -x '*.DS_Store' -x '*__pycache__*' -x '*.pyc')
python3 Inquest/rampart/scripts/validate_skill.py --zip Inquest/rampart/rampart.skill   # confirms zip ↔ directory parity
```

## Provenance

rampart is a synthesis, not a fork. The knowledge was distilled from [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) (MIT) into a self-contained skill and re-named to this collection's theme. The primer's full text, images, and notebooks are not re-hosted; `references/repo-map.md` maps every upstream section and solution to its package counterpart, and the package degrades gracefully when the upstream repo is absent (Standalone mode in `SKILL.md`).

Inquest is MIT-licensed: see [LICENSE](../LICENSE).

## Changelog

- **rampart 6.2.0** — wired into the collection: `disable-model-invocation: true` (explicit invocation only — never fires on its own), "Adjacent skills" handoff table to cuecards / keystone / siegecraft / heraldry / oneslice / lanes / armory; matching one-line handoffs added to those skills. Invocation section reworded (description documents scope, not a trigger).
- **rampart 6.1.0** — added to `Sehaan-1/Skills` as `Inquest/rampart`: themed rename (aliases keep `system-design`), `agents/openai.yaml` manifest, slash-command stub bundled at `commands/system-design.md`, `.skill` package co-located with the skill folder. Content unchanged from the primer distillation (6.0.0).
