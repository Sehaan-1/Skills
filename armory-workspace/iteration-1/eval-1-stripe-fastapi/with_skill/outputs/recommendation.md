# SDK Recommendation: Stripe card payments (PaymentIntents) — Python/FastAPI

**Top pick: `stripe` (MIT, v15.6.1)** — the official SDK, released 20 days ago, tracking the Stripe API version-by-version; at checkout-flow scale there is no meaningful performance argument against it.

## Why it wins

- **Maintenance 5/5** — v15.6.1 published 2026-09-01 (live PyPI data); Stripe ships SDK releases in lockstep with API changes, and the `StripeClient` API (v8+) is the actively developed surface — the legacy module-level pattern is headed for deprecation, so new code should use `StripeClient`.
- **License 5/5** — MIT (verified live via PyPI classifiers); zero friction for any project.
- **DX 5/5** — official docs with FastAPI-relevant examples, typed resource objects, first-class error hierarchy, webhook signature helpers, and by far the largest pool of community answers. Python 3.9+ supported.
- **Performance 4/5** — thin HTTP wrapper; you can plug in `requests`/`urllib`/`pycurl` transports. For a checkout flow doing a handful of API calls per request, SDK overhead is irrelevant.

## Comparison

| Candidate | Performance | Maintenance | License | DX | Weighted |
|---|---|---|---|---|---|
| `stripe` (official) | 4/5 | 5/5 | ✅ MIT | 5/5 | **4.8/5** |
| `httpx` + raw Stripe REST API | 4/5 | 3/5 | ✅ BSD-3-Clause | 2/5 | **3.5/5** |

Weights used: 25/25/25/25 (no priorities stated). Facts verified live on 2026-09-22 (PyPI + stripe-python README). `dj-stripe` was considered and excluded — it's Django-specific and doesn't apply to FastAPI.

## Trade-offs

- The SDK client is **synchronous** — in FastAPI, call it via `run_in_threadpool` (or an async worker) rather than directly inside `async def` handlers, or you'll block the event loop.
- You inherit Stripe's release cadence and API-version pinning; a major SDK bump (like the recent v15 `StripeObject` changes) occasionally needs migration attention.
- Skipping to raw `httpx` buys you zero SDK dependency and full control — but you'd own idempotency keys, error mapping, webhook signature verification, and API drift yourself. Only worth it if you're integrating a single trivial endpoint; for a checkout flow it isn't.

## Getting started

```bash
pip install stripe requests
```

```python
from stripe import StripeClient
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool

app = FastAPI()
client = StripeClient("sk_test_your_secret_key")  # use env config in real code

@app.post("/create-payment-intent")
async def create_payment_intent():
    def _create():
        return client.v1.payment_intents.create(params={
            "amount": 2000,                                   # $20.00 in cents
            "currency": "usd",
            "automatic_payment_methods": {"enabled": True},
        })

    pi = await run_in_threadpool(_create)   # SDK is sync — keep it off the event loop
    return {"client_secret": pi.client_secret}
```

## Assumptions & caveats

- Assumed equal weighting across the four axes (no priorities stated) and a permissive project license (MIT SDK passes any gate anyway).
- Assumed server-side PaymentIntent creation; the frontend still needs Stripe.js (`@stripe/stripe-js`) to confirm the payment — a separate decision from this SDK.
- All facts live-verified 2026-09-22 except the FastAPI threading guidance (standard practice, not doc-verified). Snippet API shape verified against the current stripe-python README (`StripeClient` + `client.v1.*`).
