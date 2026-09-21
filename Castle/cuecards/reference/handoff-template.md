# Handoff Template and Slicing Sequence

# Handoff

Cuecards output is excellent **context**. It is not a build plan. After the board is done, write a decomposition a building agent can follow. Then stop.

`docs/cuecards/handoff-<board-slug>.md`

```markdown
# Handoff: <board spoken name>

**For a building agent.** Do not start this from Cuecards. Cuecards sitting ends when this file is written.

## Provenance
- Board: [<board name>](<url>)
- For-you cards decided by human: <N> of <N>
- Last human answer recorded: <ISO date or "see issue #NN">
- Handoff written by: <agent name>

## Where we're headed
<from the board>

## How we'll know we're there
- Walk:
- Proof:
- Enforced:

## Constraints (from Notes)
- …

## ADRs this implements (in force)
- [ADR-0001 Who owes us?](../../examples/invoicing/adr/0001-who-owes-us.md)
- …

## Not this effort
- [ADR-00NN …](…) — <gist>

## Sequence
Ordered slices. Each slice is independently checkable. Cite ADRs. Name the walk/proof this slice advances. Do not paste product code.

### Slice 1: <spoken name>
- **ADRs:** ADR-0001, ADR-0002
- **Does:** <what exists when this slice is done>
- **Check:** <walk or test>
- **Depends on:** none

### Slice 2: …
- **Depends on:** Slice 1
```

No placeholders. If you cannot sequence it, an ADR is missing or still fuzzy — go back to the board, do not invent a fake plan.

Show the human the file. Stop. The next sitting (different skill or a human "go build") executes it.

---

