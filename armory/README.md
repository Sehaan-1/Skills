# armory

The castle's armory is where you pick the right weapon before the campaign. This skill does that for SDKs.

Give it a **language + framework + use case** and it returns a single recommended SDK: it builds a candidate set, pulls live registry facts (`scripts/fetch_package_facts.py` — PyPI, npm, crates.io, RubyGems, NuGet, Maven, Go), scores candidates on four axes — performance, active maintenance, license compatibility, developer experience (rubrics in `references/`) — and outputs a short report with the top pick, honest trade-offs, and a ready-to-run initialization snippet.

- Entry point: [`SKILL.md`](SKILL.md)
- Installable package: [`armory.skill`](armory.skill)
