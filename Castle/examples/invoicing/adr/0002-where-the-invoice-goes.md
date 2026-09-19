# ADR-0002: Where does the invoice go?

- **Status:** accepted
- **Date:** 2026-09-20
- **Card:** [Where does the invoice go?](../cards/002-where-the-invoice-goes.md)
- **Board:** [Invoices for customers](../board.md)
- **Supersedes:** none
- **Superseded by:** none

## Context
"Send" needs a destination. We chose between an email with an attached file (A) and an email that opens a live page on our site (B), after looking at the working slice the card linked.

## Decision
The customer gets an email that opens a live page showing the invoice's real state.

## Consequences
- **People notice:** the page flips to "paid" when the owner marks it paid
- **Later cards/ADRs must:** keep the page read-only — it is a view of the invoice, not an editor
- **We give up:** nothing — the page is built from the same data as the invoice
- **Look/CI/proof:** the send-slice artifact linked on the card is kept and becomes the base of the send code

## History
- 2026-09-20 accepted
