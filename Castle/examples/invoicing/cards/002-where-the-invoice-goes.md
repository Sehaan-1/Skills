# Where does the invoice go?

> **For you** — look, then pick. A real slice will exist to react to.

## In one sentence
We need to decide what the customer receives when you send an invoice, so that "sent" means something they can act on.

## Why this, why now
"Send" is the heart of the destination. If the customer cannot receive it, there is nothing to mark paid.

## What we already know
- **Where we're headed:** create, send, track — without handwork
- **Already decided:** [ADR-0001 Who owes us?](../adr/0001-who-owes-us.md): the app is paper, not a bank
- **Waiting on:** nothing

## The question
When you send an invoice, what does the customer get — and how do they open it?

## What this is not asking
- Visual polish of the invoice — a later look-card, if this is not enough
- Delivery guarantees — it is email; email is what it is

## Options
### A — Just an email, with the invoice attached
- **You'd notice:** one email, a file to download
- **It costs:** the least to build
- **You give up:** the customer is stuck with a file; no live "paid" state they can see

### B — An email that opens a live page
The email says "your invoice" and opens a page on our site that shows the invoice's real state.
- **You'd notice:** the page updates when you mark it paid
- **It costs:** a small read-only page per invoice
- **You give up:** nothing — the page is built from the same data

## Recommendation
**B**, because the page is what makes "paid" real for both of you instead of a file rotting in an inbox. Try it below before you answer.

## How you'll know it's answered
You can say: "They get an email that opens a page that tells the truth."

## Proof
- **Walk:** create a test invoice, send it, open the emailed link, watch it flip to "paid"
- **Artifact:** the working send-slice in the repo (`src/send-slice/`), with the screenshot trace linked on the issue
- **Keep:** yes — it becomes the base of the real sending code

## After you answer
- **Unlocks / this blocks:** the send slice in the handoff
- **Still later:** how the money actually moves
- **ADR:** ADR-0002 (accepted)

## For the agent

### What would impressive look like here
The customer taps the email and sees *their* invoice as a living document — not a PDF clone.

### Real fork
Dead file (A) vs live view (B). B is what makes the payment state visible to both sides.

### Why this recommendation isn't the lazy one
B costs one read-only page; A would look cheaper in review and leave the destination's "paid" state invisible to the person who matters.

### Option I almost hid
A, because "email attachments are what people expect". Expectation is not the impressive axis.

### Six-month generic
A is every invoicing app's default. A page that tells the truth is not.

## Answer
B — an email that opens a live page.

Closed as [ADR-0002](../adr/0002-where-the-invoice-goes.md).

## Tracking
- Board: [Invoices for customers](../board.md)
- Type: look
- Mode: for-you
- Priority: now
- Blocked by: Who owes us money?
- Blocks: (the send slice in the handoff)
