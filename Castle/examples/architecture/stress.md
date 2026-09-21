# Stress: Invoices — three violations, attempted 2026-09-21

Every attempt ran against commit 4f9c2e1 (illustrative). Tree restored after each.

## 1. Import a detail into the core

**Tried:** `core/invoice.ts` gained `import { transporter } from "../adapters/mail/send"`, and `markSent()` called it directly.

**Caught:** dependency-cruiser, rule `core-no-outbound`:

```text
error core/invoice.ts:3 — dependency violates rule
  from: invoicing/core  to: adapters/mail  (forbidden)
```

**Fix:** reverted. `markSent` returns the email as plain data; the use case hands it to `Outbox`. The failure names the file, as required.

## 2. Reach past the aggregate root

**Tried:** a page handler set `invoice.status = "paid"` on a row loaded straight from the store, skipping the root and the state history.

**Caught:** `npm run check:status` (structural test):

```text
FAIL check:status — assignment to .status outside invoicing/core
  adapters/web/mark-paid.ts:12
```

**Fix:** reverted. The handler calls the `markPaid` use case, which goes through the root and records the transition. This is the rule the grep exists for: without it, I2 is enforced by convention only, and conventions do not survive a deadline.

## 3. Cross the context without the port

**Tried:** rendered an invoice email inline in the web handler using the mail library's payload type, so the "pay" deep link could ship one day sooner.

**Caught:** `npm run check:templates`:

```text
FAIL check:templates — email body built outside Delivery templates
  adapters/web/invoice-page.ts:41
```

**Fix:** reverted. The payload goes through `Outbox`, Delivery renders, and the link stays data like everything else in the message.

## What would make this shape wrong?

A second product line that reads invoices — quotes, receipts, a customer portal with logins — moves `Customer` out of "outside by design" into its own context, and probably promotes the live page to a context of its own. Multi-currency puts a `Money` value object in core: a one-day change, *because* the aggregate already pins minor units. A third person owning email full-time is the one force that changes nothing — Delivery's customer/supplier seam already matches that org chart.

## What is the cost of being wrong?

The boundaries are cheap: every rule is one grep or one depcruise line, and the largest re-draw (a Customer context) is about a week. The expensive mistake available here is the one the stress test watches for — letting the email path mutate invoice state — because that makes Delivery a second writer on the core aggregate, and the optimistic-concurrency story quietly dies with nobody noticing until the first lost update.
