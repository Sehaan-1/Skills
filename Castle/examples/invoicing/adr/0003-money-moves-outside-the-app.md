# ADR-0003: Money moves outside the app

- **Status:** accepted
- **Date:** 2026-09-20
- **Card:** [Does the app take the money?](../cards/003-does-the-app-take-the-money.md)
- **Board:** [Invoices for customers](../board.md)
- **Supersedes:** none
- **Superseded by:** none

## Context
The biggest fork left: taking money makes this a payment integration, not an invoicing feature. We ruled it out of this effort rather than letting it silently reshape the board.

## Decision
Out of this effort: the app does not take money. The customer pays however they like; the owner marks the invoice paid.

## Consequences
- **People notice:** "mark paid" is a human action, and only that
- **Later cards/ADRs must:** not reintroduce payment providers, payment links, or automatic paid-states
- **We give up:** a "pay now" button, until a payments effort with its own board
- **Look/CI/proof:** none

## History
- 2026-09-20 accepted
