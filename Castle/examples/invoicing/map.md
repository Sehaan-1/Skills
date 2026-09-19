# Map: Invoices for customers

**For the team.** Cuecards decided. This file is how we ship it without colliding.

- **Handoff:** [handoff](handoff.md)
- **Board:** [Invoices for customers](board.md)
- **Integration owner:** the agent that invoked lanes
- **Status:** Round 1
- **Time budget:** none
- **Spend ceiling:** none
- **Round:** 1
- **Agents in flight:** Lane A

## Where we're headed
A customer of the bookkeeping app can create an invoice, send it, and see when it was paid — without doing any of that by hand.

## How we'll know we're there
- **Walk:** create an invoice for a real customer, send it, and watch it change to "paid" — end to end, without us in the room
- **Proof:** a screenshot trace of that walk, plus the `invoice-flow` test
- **Enforced:** the `e2e:invoice-flow` CI job fails if the walk regresses

This is the locked target. Rounds do not rewrite it.

## Decisions we honor
- [ADR-0001 Who owes us?](adr/0001-who-owes-us.md)
- [ADR-0002 Where does the invoice go?](adr/0002-where-the-invoice-goes.md)
- [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md)

## Not this effort
- [ADR-0003 Money moves outside the app](adr/0003-money-moves-outside-the-app.md) — no payment providers or links

## Seams (shared contracts)
A seam is anything two lanes both touch: API, schema, event, package, fixture, env.

### Seam: the invoice model
- **Contract:** `src/invoices/invoice.ts` — the Invoice type, its state, the list API; written before both sides cut
- **Owned by:** Lane A
- **Consumed by:** Lane B, Lane C
- **Status:** written

## Lanes

### Lane A — Make an invoice
- **Check:** create an invoice and see it in the list; `invoice-create` passes
- **Does:** the invoice model, the create form, the list (handoff Slice 1)
- **Handoff slices:** Slice 1
- **Owns (files/packages):** `src/invoices/`
- **Does not touch:** `src/emails/`, `src/invoice-page/`, `src/status/`
- **Needs seams:** writes the invoice-model seam
- **Parallel with:** none (the seam is the first move)
- **Waits on:** none
- **Claimed by:** the lanes agent
- **Ticket:** [Make an invoice](<issue url>)
- **Brief:** thin packet — this block, the seam, the ADRs; nothing else
- **Status:** in progress

### Lane B — Send an invoice
- **Check:** send a test invoice; the customer's email opens the live page; `invoice-send` passes
- **Does:** the send action, the email template, the read-only invoice page (handoff Slice 2)
- **Handoff slices:** Slice 2
- **Owns (files/packages):** `src/emails/`, `src/invoice-page/`
- **Does not touch:** `src/invoices/` (reads the seam only), `src/status/`
- **Needs seams:** the invoice model
- **Parallel with:** Lane C (disjoint files; the seam is written)
- **Waits on:** Lane A merge (the seam)
- **Claimed by:** unclaimed
- **Ticket:** [Send an invoice](<issue url>)
- **Brief:** thin packet — this block, the seam, the ADRs; nothing else
- **Status:** unclaimed

### Lane C — Show who's paid
- **Check:** mark a sent invoice paid; the page flips; `invoice-flow` passes end to end
- **Does:** the mark-paid action and its state in the list (handoff Slice 3)
- **Handoff slices:** Slice 3
- **Owns (files/packages):** `src/status/`
- **Does not touch:** `src/invoices/` (seam, read-only), `src/emails/`, `src/invoice-page/`
- **Needs seams:** the invoice model
- **Parallel with:** Lane B (disjoint files; the seam is written)
- **Waits on:** Lane A merge (the seam)
- **Claimed by:** unclaimed
- **Ticket:** [Show who's paid](<issue url>)
- **Brief:** thin packet — this block, the seam, the ADRs; nothing else
- **Status:** unclaimed

## Now / Next / Then
- **Now, in parallel:** A
- **Next:** B, C (both need A's seam merged)
- **Then:** destination walk

## Integration
- Merge to the default branch after every lane Check, not only at the end
- After each merge, walk as far as the destination currently allows
- Final: full walk + proof + enforced

## Sitting profile (this round)
- **Takeable now:** A
- **Idle / waiting on:** B and C wait on the seam — not started, because an idle agent is a bottleneck, not progress
- **Bottleneck:** the invoice-model seam, in Lane A
- **Duplicate work or duplicate context:** none
- **Walk before → after this round:** nothing can be created → (after A merges) an invoice can be created and listed

## What landed
_(nothing yet — round 1 in flight)_

## Blocked
nothing
