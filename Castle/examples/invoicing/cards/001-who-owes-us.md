# Who owes us money?

> **For you** — please decide.

## In one sentence
We need to decide who the invoice is a claim against, so that sending and tracking payment have a real subject.

## Why this, why now
Every screen and rule in invoicing hangs on this: who receives it, who must pay, who is "late". Guess it wrong and the app is a fancy memo pad — or an accidental payment service.

## What we already know
- **Where we're headed:** create, send, track — without handwork
- **Already decided:** nothing yet
- **Waiting on:** nothing

## The question
When the app sends an invoice, who is being asked to pay?

## What this is not asking
- How the money actually moves (bank, card, whatever) — that is its own card, and maybe its own effort
- Whether the app charges you for using the app itself

## Options
### A — The customer owes your business
You create the invoice; the recipient is your customer. The app is paper, not a bank.
- **You'd notice:** invoices are addressed to real customers, with your business name on them
- **It costs:** nothing extra — it is the normal case
- **You give up:** the app will never handle money itself, in this effort

### B — A shared pool of issuers
Several people in your business issue invoices into one shared account.
- **You'd notice:** any teammate can invoice, and the money lands in one place
- **It costs:** you must sort out who can send and whose name is on the invoice
- **You give up:** a single-owner view of the books for now

## Recommendation
**A**, because one business, one owner, and the app as paper is the only shape where this effort stays small and stays legal. Shared invoicing is a later card with its own name, not a knob here.

## How you'll know it's answered
You can say: "The invoice is my claim on my customer — the app never touches the money."

## After you answer
- **Unlocks / this blocks:** Where does the invoice go? · Does the app take the money?
- **Still later:** how the money actually moves
- **ADR:** ADR-0001 (accepted)

## For the agent

### What would impressive look like here
The customer opens the emailed invoice and it reads like a real business document, because the whole model is a clean claim between two parties.

### Real fork
Paper (record a claim) vs money (move funds). That fork shapes every later card.

### Why this recommendation isn't the lazy one
A is cheapest too, but it is also the only shape that keeps the effort small *and* keeps "paid" a real state both sides can see — which is what makes the destination impressive instead of generic.

### Option I almost hid
B, because "multi-tenant invoicing" sounds like growth. It is a different product, not a better option here.

### Six-month generic
Every app that records an invoice does A badly by treating it as a form. Ours makes the claim — and its state — the star.

## Answer
A — "The customer owes us; the app never touches the money."

Closed as [ADR-0001](../adr/0001-who-owes-us.md).

## Tracking
- Board: [Invoices for customers](../board.md)
- Type: ask
- Mode: for-you
- Priority: now
- Blocked by: none
- Blocks: Where does the invoice go? · Does the app take the money?
