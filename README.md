# Skills

Agent skills. Three collections live here:

- **[`Castle/`](Castle/README.md)** — six skills that take a fuzzy idea all the way to a shipped, checkable destination: decide, build, architect, design, coordinate, research. Start at [Castle/README.md](Castle/README.md).
- **[`Inquest/`](Inquest/README.md)** — the court of inquiry: skills that cross-examine what already exists — a design, a system, a document — and return a verdict: where it is weak, what it will cost, whether it stands under load. First in: [rampart](Inquest/rampart/SKILL.md), a system design architect + interview coach distilled from the [System Design Primer](https://github.com/donnemartin/system-design-primer) — review a design, estimate the numbers, weigh the trade-offs, drill the interview. See [Inquest/README.md](Inquest/README.md).
- **[`armory/`](armory/)** — a standalone skill that recommends the right SDK or client library for a language + framework + use case, scored on performance, maintenance, license compatibility, and developer experience. See [armory/README.md](armory/README.md).

## Install

Each collection's README carries its own install notes. Quickest form — from your **project root**, no cloning needed:

```bash
npx degit Sehaan-1/Skills/Castle/cuecards   .claude/skills/cuecards
npx degit Sehaan-1/Skills/Inquest/rampart   .claude/skills/rampart
npx degit Sehaan-1/Skills/armory            .claude/skills/armory
```

Each skill folder holds its `SKILL.md` plus everything the skill needs; packaged `.skill` files are co-located with their source folders.

**License:** MIT — see [LICENSE](LICENSE).
