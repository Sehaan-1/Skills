# The split: payment-matcher tickets

> Worked example for the [invoicing effort](../invoicing/board.md). This is what the board looks like after [engine.md](engine.md) is committed: the parent becomes an index, the children carry the two-layer shape, the edges are native blocked-by.

## Parent (rewritten as an index)

```markdown
## Which payment pays which invoice?

**For the board:** when money arrives, the app suggests which invoice it belongs to. A human always confirms — the app never moves the money.

**Builds:** [Engine: Payment-matcher](engine.md) — wall, spec, checks
**Researched in:** [Dossier](dossier.md)
**Honors:** [ADR-0003 Money moves outside the app](../invoicing/adr/0003-money-moves-outside-the-app.md)

Children, each independently checkable:
1. [Payments arrive as exact numbers](#engine-ticket-1-of-2-payments-arrive-as-exact-numbers) — parser + normalizer, spec §1–§2, §6
2. [The matcher suggests, a human confirms](#engine-ticket-2-of-2-the-matcher-suggests-a-human-confirms) — cascade S1–S3, spec §3–§4, §10

Edges: 2 blocked by 1. Status labels and native blocked-by wired on the board issues.
```

## Engine ticket 1 of 2: Payments arrive as exact numbers

**For the board:** bank-export lines land in the app as exact money — right amounts, right dates, every weird row named out loud instead of quietly skipped.

**Builds:** [Engine: Payment-matcher](engine.md) §1–§2, §6
**Researched in:** [Dossier](dossier.md) — F1 (floats), F2 (minor units), F3 (export shape)
**Honors:** [ADR-0003 Money moves outside the app](../invoicing/adr/0003-money-moves-outside-the-app.md)

### What this ticket does

Ingest the bank export: parse `DD.MM.YYYY` dates and comma-decimal amounts into a typed payment record whose amount is an **integer count of minor units**. Validate every field at the boundary; an unparseable amount or date is a hard error carrying the line number — never a skipped row. No comparison-path float may exist at any point in this ticket's code.

### Contract inherited

Spec §2: preconditions (parseable input), postconditions (integer minor units; lossless value), refusal is loud. The parser's exponent is fixed for this effort's currencies (dossier F2) — supporting another currency is a new ticket, not a constant change.

### Check

- Known-answer parse vectors from spec §6: `"1.234,56"` → 123456; `"0.10"` → 10; `"10"` → 1000; plus the malformed-row vectors (missing amount, bad date, stray currency symbol) each asserting the hard error names the line.
- Property: for randomized valid amounts, `toMinorUnits` round-trips against a naive decimal-string reference (the differential baseline for this ticket) with zero disagreements.
- No float anywhere in the comparison path: structural grep test fails on `float(` / `parseFloat` in the module.

### Blocked by / Blocks

Blocked by: none. Blocks: [Engine ticket 2 of 2](#engine-ticket-2-of-2-the-matcher-suggests-a-human-confirms).

## Engine ticket 2 of 2: The matcher suggests, a human confirms

**For the board:** the app proposes which invoice a payment belongs to and shows its reason; the owner confirms with one tap or picks another. Money still moves outside the app.

**Builds:** [Engine: Payment-matcher](engine.md) §3–§4, §10
**Researched in:** [Dossier](dossier.md) — F3 (reference strings), F4 (baseline cost)
**Honors:** [ADR-0003 Money moves outside the app](../invoicing/adr/0003-money-moves-outside-the-app.md)

### What this ticket does

Implement the cascade S1 → S2 → S3 exactly as spec §3 orders it: reference-substring match on exact-amount candidates, then unique exact amount, then a ranked ambiguous list — every ordering key sequence ending in the unique invoice id. Output carries a reason code (`REF_MATCH` / `EXACT_SINGLE` / `AMBIGUOUS`) and never mutates invoice state; the confirm step is the only writer, and it is human-gated.

### Contract inherited

Spec §2 postconditions: no suggestion names a different-amount or closed invoice; identical inputs produce byte-identical output. Spec §4's determinism argument is the contract this ticket must not break — no hash order, no locale order, no clock in the decision path.

### Check

- Differential vs the naive all-pairs baseline (spec §8): exact agreement on every payment where the baseline has exactly one equal-amount open invoice; full agreement on all inputs with n ≤ 12 plus 10,000 randomized cases with deliberate duplicate amounts and real / truncated / unrelated reference strings.
- Property tests: postconditions above; run twice → byte-identical output.
- The five end-to-end known-answer cases from spec §10 (ref-match hit, truncated fall-through, exact-single, ambiguous pair, no candidate).
- A day's batch at the real n stays under the measured baseline bound (dossier F4).

### Blocked by / Blocks

Blocked by: [Engine ticket 1 of 2](#engine-ticket-1-of-2-payments-arrive-as-exact-numbers). Blocks: the handoff slice that puts the suggestion on the owner's screen.
