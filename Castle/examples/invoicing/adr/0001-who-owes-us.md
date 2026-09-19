# ADR-0001: Who owes us?

- **Status:** accepted
- **Date:** 2026-09-20
- **Card:** [Who owes us money?](../cards/001-who-owes-us.md)
- **Board:** [Invoices for customers](../board.md)
- **Supersedes:** none
- **Superseded by:** none

## Context
Invoicing can be paper (we record a claim) or money (we move funds). The whole feature — who receives, who is late, what "paid" means — hangs on which one. We chose between the customer owing the app owner (A) and a shared pool of issuers (B).

## Decision
The invoice is the app owner's claim on their customer. The app never touches money.

## Consequences
- **People notice:** invoices carry the business's name; the customer is the one who must pay
- **Later cards/ADRs must:** treat "paid" as a recorded state, never an automated event
- **We give up:** shared multi-issuer invoicing, until a later effort says otherwise
- **Look/CI/proof:** none

## History
- 2026-09-20 accepted
