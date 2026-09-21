# Handoff Specification & Template

Cuecards outputs decisions and context. The handoff is the bridge between decisions and execution. When the board is finished, write this handoff before ending the cuecards session.

Location: `docs/cuecards/handoff-<board-slug>.md`

## Handoff Template

```markdown
# Handoff: <board spoken name>

**For an implementing agent.** Cuecards session ends when this file is committed.

## Provenance
- Board: [<board name>](<url>)
- For-you cards decided by human: <N> of <N>
- Last human answer recorded: <ISO date or "see issue #NN">
- Handoff written by: <agent name>

## Where we're headed
<from parent issue, in outcome language>

## How we'll know we're there
- **Verification walk:** <end-to-end user scenario>
- **Proof:** <screenshot trace, fixture path, or test name>
- **Enforced:** <CI command or test script that fails if regressed>

## Constraints
- <Standing rules, dependencies, boundaries>

## ADRs this implements (in force)
- [ADR-0001 Title](../adr/0001-slug.md)
- [ADR-0002 Title](../adr/0002-slug.md)

## Not this effort
- [ADR-00NN Title](../adr/00NN-slug.md) — <summary of excluded scope>

## Sequence

### Slice 1: <spoken name>
- **Does:** <one clear paragraph describing behavior change>
- **Check:** <independent test, verification walk, or artifact to inspect>
- **Depends on:** nothing
- **Honors:** ADR-0001, ADR-0002
- **Does not touch:** <adjacent scope to preserve>

### Slice 2: <spoken name>
- **Does:** <behavior change>
- **Check:** <independent verification>
- **Depends on:** Slice 1
- **Honors:** ADR-0003
```
