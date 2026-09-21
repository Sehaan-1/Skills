# Engine: Payment-matcher

- **Status:** proposed
- **Date:** 2026-09-21
- **Wall:** matching incoming bank-export payments to open invoices under exact-decimal money, duplicate amounts, and truncated free-text references.
- **Tickets:** [Which payment pays which invoice?](../invoicing/board.md) → 2 children (see [tickets.md](tickets.md))
- **Dossier:** [docs/research/payment-matcher.md](dossier.md) — worked example: [dossier.md](dossier.md)
- **ADRs honored:** [ADR-0003 Money moves outside the app](../invoicing/adr/0003-money-moves-outside-the-app.md) — the engine *suggests*; a human always confirms. The app never moves money.

> Worked example for the [invoicing effort](../invoicing/board.md).

## 1. Problem, formally

**Inputs:** a payment list (amount as the export's raw string, date, reference string, external id) and the open-invoice list (id, total in minor units, issue date, status = open).

**Outputs:** for each payment, either a ranked suggestion list of 1–3 invoices or "no suggestion," each suggestion carrying a reason code (`REF_MATCH`, `EXACT_SINGLE`, `AMBIGUOUS`).

**Success condition:** exact where money is involved — a suggested invoice's total must equal the payment amount exactly, in integer minor units. Deterministic: same inputs, same order of outputs, byte for byte, on every machine. Suggestions are advisory; nothing in the app's state changes until a human confirms (ADR-0003).

## 2. Contracts

- **Preconditions:** every amount parses to an integer number of minor units (locale comma handled by the parser); every invoice passed in has status open.
- **Postconditions:** no output ever names an invoice whose total differs from the payment amount; no output names a closed invoice; identical inputs produce identical outputs.
- **Refusal, loud:** an unparseable amount or a malformed date is a hard error naming the offending line — never a skipped row, never a guess. The engine has no silent fallbacks.

## 3. The engine

Deterministic cascade, first hit wins; ties fall through to the next rule:

1. **Parse and normalize.** Amount string → integer minor units (`toMinorUnits`, exponent fixed per dossier F2). Date string → date object (`DD.MM.YYYY` per F3).
2. **S1 — reference match.** Candidates = open invoices whose total equals the payment amount exactly **and** whose invoice number appears as a substring of the payment's reference string (case-insensitive, ignoring common separators). One candidate → suggest it, `REF_MATCH`. Several → rank by newest issue date, then lowest id, take the first, mark `AMBIGUOUS` with the runner-up listed. Zero → S2.
3. **S2 — exact single.** Candidates = open invoices whose total equals the payment amount exactly. One → suggest, `EXACT_SINGLE`. Several → S3.
4. **S3 — ambiguous.** Rank the equal-amount candidates: oldest issue date first, then ascending invoice id. Suggest the first two, `AMBIGUOUS`. The human decides.
5. **No candidates at any rule** → "no suggestion."

Ordering rules are total (every comparison ends in a tiebreak on the unique invoice id), which is what makes determinism a property of the spec and not of the runtime.

## 4. Why it is correct

- **Exactness (DERIVED).** After normalization, amounts are integers; integer equality is exact by construction; S1–S3 compare only equality, never floats. Induction over the pipeline: if ingest preserves value (one-time property, pinned by the known-answer vectors in §6), every downstream comparison preserves it.
- **No false positives across rules (DERIVED).** Every rule's candidate filter includes the exact-amount predicate from §2; a suggestion naming a different-amount invoice would require the filter to have passed, contradiction. Same argument for closed invoices: the candidate set is drawn only from the open list (§1 precondition, enforced at the boundary).
- **Determinism (DERIVED).** Every ordering key sequence ends in the invoice id, which is unique. No hash-order, no locale-order, no clock anywhere in the decision path.
- **Counterexample hunt:** duplicate invoices at the same total (S1 tie-break exercised, `AMBIGUOUS` on purpose); reference string containing a *closed* invoice's number (filter removes it — closed invoices are not candidates); reference string with a truncated number (F3 — substring fails, falls through to S2, degrades safely); amount with thousands separator and comma decimal (parser vectors); payment smaller than every invoice (no suggestion); adversarial reference strings that embed another invoice's number (S1 requires the amount to match too — a wrong-number-right-amount hit is caught by the confirm step, which is why nothing is ever auto-applied).

## 5. Cost

| Path | Time | Space |
| --- | --- | --- |
| Parse + normalize | O(p + i) | O(p + i) |
| S1 | O(p × i) substring tests, early-exit on first hit | — |
| S2 | O(p × i) integer compares | — |
| S3 | O(k log k) per ambiguous payment, k = equal-amount candidates (small in practice) | — |

At the real n (dossier F4: ~1,000 open invoices, a day of payments): on the order of a million integer comparisons and substring tests per day's batch — the naive baseline's cost. The engine adds rules, not complexity: it does not regress the measured baseline. A payment index by exact amount would take S2 to O(p + i), and that is the first optimization to reach for if the batch ever feels slow — not before.

## 6. Numbers

- Representation: integer minor units everywhere past the parser (dossier F1, F2). No floats in the comparison path, ever.
- Parser vectors (known-answer, lifted from the fixture and the decimal docs' exactness examples): `"1.234,56"` → 123456; `"0.10"` → 10; `"10"` → 1000. Each asserted against the integer, not against a float rendering.
- Comparison epsilon: none. Equality is `==` on integers; an epsilon would be a bug.

## 7. Edges and failures

Empty payment list → empty output. Empty open-invoice list → every payment gets "no suggestion." Huge batch → streaming per payment; memory O(i). Adversarial reference strings → see §4. Untrusted input at the boundary: the export is outside data — every field validated at ingest, failures loud with the line number (§2).

## 8. Alternatives the sources offer

| Alternative | Why rejected | Cost of the rejection |
| --- | --- | --- |
| Naive all-pairs exact match, human picks from equal-amount list (the baseline) | Kept as the differential oracle; also the production fallback when S1–S3 say nothing | It is the floor, not the engine |
| Fuzzy amount matching (tolerance band for fees) | Contradicts the effort's contract: a suggestion must be exact, and fee tolerance silently shifts money — a decision, not an implementation detail | Would go back to the board as a cuecards card if the owner wants it |
| Learn matches from history (ML) | Unverifiable at this scale, non-deterministic in the ways §1 forbids, and the real n is a day of payments | Wrong tool at this n; revisit only with months of confirmed-match history |

## 9. Novelty

None, and that is the finding. The engine is a composition of exact integer comparison (CITED, dossier F1/F2), substring containment, and total orderings (DERIVED). Fitting a known, boring engine well is the fine outcome; the discipline went into the contracts, the determinism, and the checks, not into invention.

## 10. Check (for the builder)

- **Known-answer vectors** (§6, from the fixture): parse vectors plus five end-to-end cases — ref-match hit, ref-match truncated fall-through, exact-single, ambiguous pair, no candidate.
- **Differential vs the naive baseline:** exact agreement on every payment where the naive matcher has exactly one equal-amount open invoice; on all inputs with n ≤ 12, plus 10,000 randomized cases (random amounts from a distribution with deliberate duplicates, random references containing real, truncated, and unrelated invoice numbers).
- **Property tests:** no output names a different-amount or closed invoice (§2 postconditions); same input twice → byte-identical output; unparseable line → hard error naming the line.
- **Measured threshold:** a day's batch at the real n runs comfortably under the naive baseline's measured bound (dossier F4); regress past it and the Check fails.

## 11. Open risks

The "payers put the number in the reference" premise is unverified (dossier Unverified). If a month of real exports shows S1 almost never fires, the engine still stands — S2 and S3 carry it — but the owner's time saved shrinks, and the look-card's data decides whether suggestions stay worth the screen space.
