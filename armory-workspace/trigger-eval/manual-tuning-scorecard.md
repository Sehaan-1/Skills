# Manual trigger-description tuning — armory

Date: 2026-09-22 · Method: judgment-based scoring (no `claude` CLI in this sandbox, so live trigger-rate testing via `run_loop.py` was not possible). Each query was judged as a capable model would, seeing only `name: armory` + the description. Note the name "armory" carries zero SDK signal, so the description bears the full triggering burden.

**Changes old → new:**
1. Added the "SDK vs nothing" variant explicitly ("whether to adopt an SDK at all or call a REST API directly") — should-trigger queries #4 and #10 ask exactly this.
2. Added explicit "maintained" phrasing ("which of several gems/crates/packages is actually maintained") — matches query #3's framing.
3. Added "standardizing a library choice across a team" — matches query #9's framing.
4. Added a `Do NOT use` clause (precedent: `Castle/oneslice` uses the same pattern) covering: using/debugging/migrating/configuring an already-chosen library, standalone legal/license questions, conceptual SDK-vs-API questions, dependency audits/CVE checks, and service/model selection.

## Per-query scorecard

| # | Query (abridged) | Should | Old desc. | New desc. | Notes |
|---|---|---|---|---|---|
| 1 | Postmark SDK vs nodemailer (Express) | ✅ trigger | ✅ | ✅ | Covered both ways |
| 2 | python lib for GCS on django 5 | ✅ trigger | ✅ | ✅ | "client library" match |
| 3 | Twilio gems, "which is actually maintained" | ✅ trigger | ✅ likely | ✅ | New text mirrors the phrasing |
| 4 | Go CLI — "do I even need an SDK?" | ✅ trigger | ⚠️ borderline | ✅ | Fixed by "SDK at all vs REST" clause |
| 5 | expo firebase vs react-native-firebase | ✅ trigger | ✅ | ✅ | Compare-package-set match |
| 6 | Kafka client, Java, Apache-2.0 constraint | ✅ trigger | ✅ | ✅ | License mention aligns |
| 7 | iOS Stripe SDK vs RevenueCat | ✅ trigger | ✅ | ✅ | "choose between integration libraries" |
| 8 | best rust crate for postgres/axum | ✅ trigger | ✅ | ✅ | |
| 9 | OpenTelemetry .NET standardization | ✅ trigger | ⚠️ borderline | ✅ | Fixed by "standardizing" clause |
| 10 | Elixir Shopify hex pkg vs raw REST | ✅ trigger | ⚠️ borderline | ✅ | Fixed by "SDK at all vs REST" clause |
| 11 | Stripe webhook signature, already installed | ❌ no | ⚠️ risk | ✅ | Excluded: using an already-chosen library |
| 12 | boto3 upload fn, "already standardized" | ❌ no | ⚠️ risk | ✅ | Excluded: code with chosen library |
| 13 | "difference between an SDK and an API?" | ❌ no | ⚠️ risk | ✅ | Excluded: conceptual question |
| 14 | rdkafka rebalancing debug | ❌ no | ⚠️ risk | ✅ | Excluded: debugging chosen library |
| 15 | REST vs gRPC API design | ❌ no | ✅ | ✅ | No positive clause matches |
| 16 | stripe-node v12→v22 migration | ❌ no | ⚠️ risk | ✅ | Excluded: migrating chosen library |
| 17 | which LLM, GPT-5 vs Claude | ❌ no | ✅ likely | ✅ | Explicit "(e.g., which LLM)" example |
| 18 | MIT vs GPL dynamic-linking legal Q | ❌ no | ⚠️ risk | ✅ | Excluded: licensing w/o library decision |
| 19 | package.json audit, outdated/CVEs | ❌ no | ⚠️ borderline | ✅ | Excluded: dependency audits |
| 20 | Terraform module for S3 | ❌ no | ✅ | ✅ | Not an SDK selection |

**Estimated result:** old ≈ 14 confident / 6 borderline-or-risky → new ≈ 20/20 confident.
**Known residual risk:** queries that mix a *new* integration into an *existing* SDK codebase (e.g., "add Twilio to our app that already uses stripe-node") should still trigger — the negative clause targets work on the already-chosen library, not the presence of other libraries.

## Follow-up (when run in an environment with the `claude` CLI)

Run the automated loop to validate with real trigger rates (3 runs/query, train/test split):

```bash
cd skill-creator
python -m scripts.run_loop \
  --eval-set ../armory-workspace/trigger-eval/trigger-eval.json \
  --skill-path ../armory \
  --description "$(sed -n 's/^description: *"\(.*\)"$/\1/p' ../armory/SKILL.md)" \
  --model <model-id-powering-the-session> \
  --max-iterations 5 --verbose
```
