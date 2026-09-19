# Does the app take the money?

> **For you** — please decide.

## In one sentence
We need to decide whether taking payment (cards, transfers) is part of this effort.

## Why this, why now
It is the biggest fork left on the board. If yes, the effort is a payment integration, not an invoicing feature, and the whole board reshapes.

## What we already know
- **Where we're headed:** create, send, track — without handwork
- **Already decided:** [ADR-0001 Who owes us?](../adr/0001-who-owes-us.md): the app is paper, not a bank
- **Waiting on:** nothing

## The question
Should this effort take money?

## What this is not asking
- Whether you will *ever* want payments — only whether **this** effort does them

## Options
### A — No. The customer pays however they like; you mark it paid
- **You'd notice:** a "mark paid" button, and nothing more
- **It costs:** none of the payment world — no provider, no security review, no compliance
- **You give up:** no payment links, no automatic "paid"

### B — Yes. The customer pays from the invoice page
- **You'd notice:** a "pay now" button that actually works
- **It costs:** a provider, a security review, PCI questions, and a much longer effort
- **You give up:** shipping the invoicing feature this season

## Recommendation
**A** for this effort. B is a real product with its own name, its own board, and its own fog — not a bad answer, just a later one.

## How you'll know it's answered
You can say: "This effort ships invoicing; payments is the next effort."

## After you answer
- **Unlocks / this blocks:** rules the rest of the board must honor
- **Still later:** the payments effort, when you want it
- **ADR:** ADR-0003 (accepted)

## Answer
Out of this effort.

Closed as `not-this-effort`; [ADR-0003](../adr/0003-money-moves-outside-the-app.md) keeps the ruling citable.

## Tracking
- Board: [Invoices for customers](../board.md)
- Type: ask
- Mode: for-you
- Priority: now
- Blocked by: Who owes us money?
- Blocks: nothing (it fences the board)
