# Architectural Smells, Comparisons, and Red Flags

# Smell → cause

Read down the left, land on the right. Each row is a structural failure, not a code-style failure.

| You see | It usually means |
| --- | --- |
| Every feature touches six packages | Boundaries drawn by technical kind, not by axis of change |
| "We can't test this without the database" | A detail crossed into policy; the persistence port is missing or drawn on the wrong side |
| ORM annotations on domain types | No adapter ring; the database is not a detail here, it is a load-bearing decision nobody made |
| One giant `utils` / `common` / `shared` package | Undistilled model; no home for a concept, so it went where everyone can reach it |
| Two services that must deploy together | A distributed monolith: the boundary was drawn in the wrong place, or not drawn at all |
| Integration through a shared database | Two contexts with no named relationship; the schema has become the published language, unversioned |
| A change to one service breaks three others | Shared mutable state across a boundary that looked like an interface |
| Every class is public | Packages are folders. Encapsulation is decorative and so is the architecture. |
| `instanceof` at a boundary | LSP violated; the plugin is not substitutable, so it is not a plugin |
| An entity with forty fields and no behaviour | Anemic domain model; the model is the schema, and the logic is in services |
| A transaction that spans two services | Cross-context invariant treated as transactional; either merge the contexts or make it eventual and name the mechanism |
| Circular imports | ADP violated. Break with DIP or extract the shared part. |
| Abstract classes nothing implements | Zone of Uselessness; someone designed for a future that did not arrive |
| Config-driven everything ("we'll just add a flag") | Deferral as procrastination; the decision was avoided rather than deferred, and the branching is now permanent |
| Tests break on every refactor | Structural coupling; no testing API; the suite mirrors the production class tree |
| A rewrite is proposed as the fix | Usually: the boundaries are wrong, not the code. Rewriting inside the same shape reproduces it. |

---

# Bad vs good

**Bad boundary:** "We'll split it into a `core` module and a `web` module."
**Good boundary:** "Booking and Yield Analysis are separate contexts. Yield needs a subset of Booking's data, runs a different model on different technology, and changes on its own clock. Booking is upstream, Yield is downstream, customer/supplier: Yield's acceptance tests run in Booking's CI, so Booking can change freely."

**Bad dependency rule:** "The domain shouldn't depend on infrastructure, ideally."
**Good:** "`packages/domain/**` may not import from `packages/infra/**`, `@prisma/*`, `express`, or `axios`. Enforced by `dependency-cruiser` (`depcruise --config .dependency-cruiser.cjs src`), wired into `ci` at `.github/workflows/ci.yml:41`. Output of the last run, commit 9f3a1c2: 0 violations, 0 cycles."

**Bad invariant:** "The order total must always match the sum of its line items."
**Good:** "Invariant I2: `order.total == sum(lineItems.amount)`, enforced transactionally within the `Order` aggregate on every commit. The `Order` aggregate root is `Order`; `LineItem` has local identity and is not reachable except by traversal from `Order`. Consequence: `LineItem` may not be loaded or mutated directly, and there is no `LineItemRepository`."

**Bad cross-context rule:** "Inventory will let us know when stock changes."
**Good:** "Cross-context rule: an order may not be confirmed for more units than are available. This is **not** transactional across `Ordering` and `Inventory`. Ordering publishes `OrderPlaced`; Inventory consumes it and replies `StockReserved` or `StockRejected` within 5 s; Ordering compensates on rejection or on no reply after 30 s. Reconciliation job `reconcile-reservations` runs hourly and is the backstop. Worst-case oversell: bounded by the 30 s window at current peak rate ≈ 12 orders."

**Bad deferral:** "We'll decide on the database later."
**Good:** "| Persistence engine | The repository port is the only thing the core needs; any of Postgres, DynamoDB, or flat files satisfies it | First load test above 2k writes/s, or the first reporting query that needs a join | Swap the adapter: ~3 days. No core change. |"

**Bad metric claim:** "Coupling is reasonable now."
**Good:** "Measured at 9f3a1c2: `billing` I=0.21 A=0.44 D=0.23; `notifications` I=0.86 A=0.10 D=0.24; `pricing` I=0.05 A=0.62 D=0.33. Cycles: 0. `shared-kernel` sits at I=0.00 A=0.31 — deliberately near the Zone of Pain; it is low-volatility by agreement, and the joint test suite in CI is what keeps it that way."

**Bad review:** "This is a bit messy."
**Good:** "Drifts. `orders/exports.ts` imports `prisma` directly and queries `lineItem` by id, bypassing the `Order` root — that is rule 4 of the record (aggregate access only through the root) and it is unenforced, because the fitness function only checks package-level imports, not intra-package access. Two fixes: route through `OrderRepository`, and add the intra-package rule."

---

# Red flags

| Thought | Reality |
| --- | --- |
| "We'll just use the framework's way" | The framework is a tool, not an architecture. An architecture supplied by a framework cannot be based on your use cases. |
| "The database is the model" | The database is a detail. It is a tool the business rules use indirectly, behind an interface. |
| "Services give us decoupling" | Services decouple at the level of variables and are strongly coupled by the data they share and the interfaces they agree on. A new field that five services read couples all five. |
| "Let's make it generic so we can reuse it" | REP pulls against CCP and CRP for a reason. Reuse is the thing you sacrifice early. |
| "We'll add the boundary later when we need it" | Adding a boundary where none exists is expensive even with a comprehensive test suite and refactoring discipline. Later is the most expensive time. |
| "We need to anticipate every abstraction" | Over-engineering is often worse than under-engineering. Draw where the friction is; keep the rest partial; watch. |
| "The diagram shows the architecture" | The diagram is a claim. The source tree and a tool run are evidence. |
| "It's only a small shortcut across the layer" | A relaxed layered architecture with one bypass has no architecture; every bypass is a precedent. |
| "We'll enforce it in code review" | Review is fallible, the feedback loop is a pull request long, and the loop closes after the violation is merged. |
| "One more shared package won't hurt" | Everything can reach it, so it becomes the model — the least distilled part of the system. |
| "The tests pass, so the structure is fine" | Tests verify behavior. Architecture is about the cost of the next change, which no passing test measures. |
| "I'll model it the way I did at my last job" | Context differs. Forces differ. The last architecture solved the last team's problem. |
| "The domain expert agrees with my model" | Agreement is cheap when the words are yours. Use their words and see if it still holds. |
| "We'll refactor toward deeper insight later" | Insight arrives while building, and evaporates if the sitting does not capture it. Write it down now. |
| "Microservices will fix our modularity" | Services are function calls across process boundaries. Some are architecturally significant; most are not. Modularity is a property of the dependency structure, not the deployment topology. |

---

