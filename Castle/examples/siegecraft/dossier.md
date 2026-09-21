# Dossier: Which open invoice does an incoming bank payment belong to?

- **For engine:** [engine.md](engine.md) — the payment-matcher
- **Date:** 2026-09-21 · **Researched by:** siegecraft sitting (worked example)

> Worked example for the [invoicing effort](../invoicing/board.md). The effort is fictional; the format, the discipline, and the kind of every claim (CITED / DERIVED / UNVERIFIED) are the point.

The wall: ADR-0003 keeps money outside the app, so payments arrive as lines in the owner's bank export, and today the owner eyeballs each line against open invoices and types the match by hand. "Suggest the match" is only safe if the suggestion is deterministic, exact where money is involved, and never silent about ambiguity. This dossier owns the facts the matcher may assume.

## Sources consulted

| # | Source | Kind | What it owns | Link / path |
| --- | --- | --- | --- | --- |
| 1 | Python `decimal` module docs — why base-10 arithmetic is exact where binary float approximates a decimal fraction | primary docs | exactness of money math | docs.python.org/3/library/decimal.html |
| 2 | ISO 4217 | primary standard | every currency has a minor-unit exponent (2 for the currencies this owner invoices in); money compares at minor units, not display strings | iso.org/iso-4217-currency-codes |
| 3 | The bank export itself: header row plus three real export files the owner runs on today | first-party data | column order, date format, decimal comma, reference-string shape | `fixtures/bank-export-sample.csv` (committed by the look-card that produced it) |
| 4 | The naive matcher written and run this sitting (scratch, not committed) | measurement | the baseline's answers and cost — the differential oracle | see Measured |

## Findings

### F1. Money must not be compared as floats
- **CITED** — Python `decimal` docs, design rationale: base-10 decimal arithmetic is exact where binary float is an approximation of a decimal fraction (0.10 has no exact binary representation).
- **So what:** the matcher converts every amount to an integer count of minor units at ingest and never compares floats. Amount equality becomes integer equality.

### F2. Minor units are a property of the currency, and this effort is single-currency
- **CITED** — ISO 4217: the minor-unit exponent is defined per currency (2 for the ones in use here).
- **So what:** a `toMinorUnits(str)` normalize step with the exponent fixed for this effort. Supporting a second currency is a new ticket, not a silent constant change. The exactness argument itself is DERIVED — integer equality is exact by construction; written out in spec §4.

### F3. The export's real shape is known and stable
- **CITED** — the export fixture (first-party): dates are `DD.MM.YYYY`, the decimal separator is a comma, and reference strings are free text the payer typed, truncated at 40 characters.
- **So what:** parsing is a real sub-task (locale decimal comma, date order), and reference strings can carry the invoice number whole or clipped. The matcher's S1 rule keys on substring containment, so truncation degrades the rule; it does not break it.

### F4. The naive baseline is exact and fast enough at the real n
- **CITED / MEASURED** — scratch run this sitting: all-pairs exact compare at the real scale (1,000 open invoices × a day of payments) is on the order of a million integer comparisons — well under a second on the owner's laptop-class machine.
- **So what:** the engine's added rules buy *fewer wrong suggestions*, not speed. The spec's cost claims are about not regressing this baseline, and the baseline stays in the spec as the differential oracle.

## Measured

Scratch script (not committed): all-pairs exact compare, 10 runs at n = 1,000 × 1,000, owner-laptop-class machine, 2026-09-21 — every run well under one second. Command and output recorded in the sitting log. Conclusion recorded honestly: the engine is justified by correctness of suggestions, not by asymptotics.

## Unverified

- "Payers usually put the invoice number in the reference string." The owner believes it; three fixture files cannot carry it. **The engine does not rest on it**: S1 (reference hit) is the only rule that uses the premise, and the fallback rules do not. Confirming it is a look-card over a month of real exports before suggestions are ever trusted without a glance — and the engine confirms-by-default anyway.

## Contradictions

None found. The export doc's field order and the fixture's header row agree (F3 was checked against both).
