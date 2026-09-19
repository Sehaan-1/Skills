# Invoices for customers

## Where we're headed
A customer of the bookkeeping app can create an invoice, send it, and see when it was paid — without doing any of that by hand.

## How we'll know we're there
- **Walk:** create an invoice for a real customer, send it, and watch it change to "paid" — end to end, without us in the room
- **Proof:** a screenshot trace of that walk, plus the `invoice-flow` test
- **Enforced:** the `e2e:invoice-flow` CI job fails if the walk regresses

## How to read this
One card = one choice. Open a **Ready now** card. Ignore agent notes.
**We'll handle this** runs without you.

## Notes
- **Domain:** a two-person bookkeeping app; customers are small businesses; no existing billing code
- **Standing rules:** stdlib first; tests stay green; every email is a template a person can edit
- **Consult:** `docs/adr/`
- **ADRs in force:** [ADR-0001 Who owes us?](adr/0001-who-owes-us.md), [ADR-0002 Where does the invoice go?](adr/0002-where-the-invoice-goes.md), [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md)

## Ready now — for you
_(none — the board is decided)_

## Ready now — unattended
_(none)_

## Waiting
_(none)_

## Decided
- [ADR-0001 Who owes us?](adr/0001-who-owes-us.md) · [Who owes us money?](cards/001-who-owes-us.md) · accepted: the customer owes the app owner; the app never touches money
- [ADR-0002 Where does the invoice go?](adr/0002-where-the-invoice-goes.md) · [Where does the invoice go?](cards/002-where-the-invoice-goes.md) · accepted: an email that opens a live page showing the invoice's real state
- [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md) · [Does the app take the money?](cards/003-does-the-app-take-the-money.md) · accepted: out of this effort — the customer pays however they like, the owner marks it paid

## Not sharp enough to ask yet
_(none — everything sharp is decided)_

## Not this effort
- Online payments: no providers, no "pay now" buttons — ruled out by ADR-0003; a future effort with its own board
