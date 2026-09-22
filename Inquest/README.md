# Inquest

The castle's court of inquiry. Where Castle decides and builds from a fuzzy idea, Inquest cross-examines what is already on the table — a design, a system, a document — and returns a verdict: where it is weak, what it will cost, and whether it stands when the load arrives.

Each skill below is small, self-contained, and works with any agent that reads skill files. Skills that examine things which already exist convene here.

## Skills

| Skill | Use when | Leaves behind |
| --- | --- | --- |
| [rampart](rampart/SKILL.md) | A system must be designed, reviewed, scaled, or sized: "design a URL shortener", "review this architecture", "how many servers for 10M DAU?", "SQL or NoSQL?", back-of-the-envelope math, or system design / object-oriented design interview prep | A 4-step design or a review verdict with the trade-off named at every stone — requirements and assumptions, estimates, architecture, bottleneck pass, closing checklist — plus a scored rubric and flashcard decks for interview drill |

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

**claude.ai** — Settings → Features → Custom Skills → upload `rampart.skill`; it auto-activates by description.

**Slash command (Claude Code, optional)** — copy the stub shipped inside the package:

```bash
cp .claude/skills/rampart/commands/system-design.md .claude/commands/system-design.md
# /system-design design a rate limiter
```

**Any agent** — point it at `Inquest/rampart/SKILL.md` and say "follow this skill." Auto-invocation needs no syntax: the frontmatter `description` matches requests like *"design a URL shortener"*, *"review this architecture"*, *"SQL or NoSQL?"*, *"back-of-the-envelope for 10M DAU"*, *"system design interview prep"*.

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

rampart is a synthesis, not a fork. The knowledge was distilled from [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) (MIT) into a self-contained skill, then ported here from [Areej-ui-sehaan/system-design-primer → `skills/`](https://github.com/Areej-ui-sehaan/system-design-primer/tree/master/skills) and re-named to this collection's theme. The primer's full text, images, and notebooks are not re-hosted; `references/repo-map.md` maps every upstream section and solution to its package counterpart, and the package degrades gracefully when the upstream repo is absent (Standalone mode in `SKILL.md`).

Inquest is MIT-licensed: see [LICENSE](../LICENSE).

## Changelog

- **rampart 6.1.0** — ported into `Sehaan-1/Skills` as `Inquest/rampart`: themed rename (aliases keep `system-design`), `agents/openai.yaml` manifest, slash-command stub bundled at `commands/system-design.md`, `.skill` package co-located with the skill folder. Content unchanged from upstream 6.0.0.
