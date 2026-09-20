# Handoff: Invoices for customers

**For a building agent.** Do not start this from Cuecards. The Cuecards sitting ended when this file was written.

## Provenance
- Board: [Invoices for customers](board.md)
- For-you cards decided by human: 3 of 3
- Last human answer recorded: 2026-09-20
- Handoff written by: cuecards agent

## Where we're headed
A customer of the bookkeeping app can create an invoice, send it, and see when it was paid — without doing any of that by hand.

## How we'll know we're there
- **Walk:** create an invoice for a real customer, send it, and watch it change to "paid" — end to end, without us in the room
- **Proof:** a screenshot trace of that walk, plus the `invoice-flow` test
- **Enforced:** the `e2e:invoice-flow` CI job fails if the walk regresses

## Constraints (from Notes)
- stdlib first; tests stay green; every email is a template a person can edit
- the app never touches money (ADR-0001, ADR-0003)

## ADRs this implements (in force)
- [ADR-0001 Who owes us?](adr/0001-who-owes-us.md)
- [ADR-0002 Where does the invoice go?](adr/0002-where-the-invoice-goes.md)
- [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md)

## Not this effort
- [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md) — no providers, no payment links, no automatic paid-states

## Sequence
Ordered slices. Each slice is independently checkable. Cite ADRs. Name the walk/proof this slice advances. Do not paste product code.

### Slice 1: An invoice can be created
- **ADRs:** ADR-0001
- **Does:** an invoice exists — customer, line items, total — and shows in the list
- **Check:** create an invoice and see it in the list; the `invoice-create` test passes
- **Depends on:** none

### Slice 2: An invoice can be sent
- **ADRs:** ADR-0001, ADR-0002
- **Does:** sending delivers an email that opens the live invoice page (the kept send-slice becomes this code)
- **Check:** send a test invoice; the customer's email opens a page showing it; the `invoice-send` test passes
- **Depends on:** Slice 1

### Slice 3: An invoice shows its payment state
- **ADRs:** ADR-0001, ADR-0003
- **Does:** the owner marks an invoice paid; the list and the page show it
- **Check:** mark a sent invoice paid; the page flips; the `invoice-flow` test passes end to end
- **Depends on:** Slice 2
