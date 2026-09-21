# Research Protocol

Use this protocol when implementation needs an external topic investigated, official docs or API facts gathered, or reading that would stall the implementation session. Do **not** use it to choose what the product should be (that is cuecards).

## Workflow

Spin up a **background agent** (or parallel subagent) to do the reading so you can keep scaffolding, testing, and writing work that does **not** depend on the answer. If this harness has no background/subagent tool, do the research yourself **first**, write the file, then implement — do not skip the artifact.

### Research agent duties

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up. Follow every claim back to the source that owns it.
2. Write findings to a **single Markdown file**, citing each claim's source (link + what it actually says).
3. Save it where the repo already keeps such notes (prefer `docs/research/<slice-slug>.md`).

### Rules

- **One question per research file.** If the slice has two independent unknowns, run two agents and produce two files.
- **Evidence for implementation, not a new ADR.** If findings contradict an ADR or the slice definition, stop — send it back to cuecards rather than making a silent product change.
- **Do not commit code that assumes an answer until the research file exists.**
- **Link the file** from the GitHub issue comment when you report progress.
