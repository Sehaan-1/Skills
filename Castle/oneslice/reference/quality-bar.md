# Quality Bar & Code Standards

Hold your implementation to an unusually strict standard. Behavior-correct spaghetti is a failed slice.

## Core prompt

Start from this baseline, then the standards below:

> Implement this one slice so the named Check passes.  
> Rethink how to structure the change so the code is simpler, smaller, more direct, and more elegant than the first idea.  
> Improve abstractions and modularity. Reduce spaghetti. Improve succinctness and legibility.  
> Be ambitious: if a clear path to a better implementation means restructuring some of the codebase, take it — as long as you do not enlarge the slice.  
> Be extremely thorough. Measure twice, cut once.  
> Preserve behavior required by the ADRs and the Check. Delete incidental complexity.  

You are not a reviewer leaving comments for someone else. You **build**, then you **hold your own diff to this bar**, and you rewrite until it passes or you stop and say what blocked you.

---

## Non-negotiable standards

0. **Be ambitious about structural simplification.**
   - Do not stop at "this could be a bit cleaner."
   - Reframe so whole branches, helpers, modes, conditionals, or layers disappear.
   - Prefer the solution that feels inevitable in hindsight.
   - Assume a simplifying reorganization exists that uses the existing architecture and makes the change dramatically simpler.
   - If you can delete complexity rather than rearrange it, do that.

1. **Do not push a file from under 1k lines to over 1k lines without a very strong reason.**
   - Treat that as a smell. Extract helpers, modules, or local abstractions.
   - If the diff would cross 1000 lines, decompose first. Only waive if there is a compelling structural reason and the file stays clearly organized.
   - Do not "just finish the slice" by dumping into a giant file.

2. **Do not allow random spaghetti growth.**
   - No ad-hoc conditionals, scattered special cases, or one-off branches in unrelated flows.
   - "Weird if statements in random places" is a design problem. Put the logic in a dedicated abstraction, helper, state machine, policy, or module.
   - If the surrounding code gets harder to reason about, the slice is not done.

3. **Bias toward cleaning the design, not accepting working code.**
   - Same behavior, cleaner structure → take the cleaner structure.
   - Do not ship an "it works" implementation that leaves the codebase messier.
   - Prefer removing moving pieces over spreading the same complexity around.

4. **Prefer direct, boring, maintainable code over hacky or magical code.**
   - Brittle, ad-hoc, or "magic" behavior is a quality failure.
   - Be skeptical of generic mechanisms that hide simple data-shape assumptions.
   - Thin wrappers, identity abstractions, and pass-through helpers that add indirection without clarity: delete them.

5. **Push hard on type and boundary cleanliness.**
   - Question unnecessary optionality, `unknown`, `any`, or cast-heavy code when a clearer boundary could exist.
   - Prefer explicit typed models or shared contracts over loosely-shaped ad-hoc objects.
   - Silent fallbacks that paper over an unclear invariant: make the boundary explicit.

6. **Keep logic in the canonical layer and reuse existing helpers.**
   - No feature logic leaking into shared paths. No implementation details leaking through APIs.
   - Prefer existing canonical utilities over bespoke one-offs.
   - Put code in the package, service, or module that already owns the concept.

7. **Treat unnecessary sequential orchestration and non-atomic updates as smells when the cleaner structure is obvious.**
   - Independent work serialized for no reason → simplify; parallelize if that also clarifies.
   - Related updates that can leave state half-applied → make them atomic.
   - Do not chase micro-optimizations. Do flag orchestration that makes the slice more brittle.

8. **Honor the slice boundary.**
   - Files, tests, and commits belong to this slice's **Does** and **Check**.
   - A "while I'm here" refactor that is not required to make this slice inevitable: leave it, or call it out and get approval before expanding.
   - Simplifying code inside the slice is required. Rewriting the rest of the product is out of scope for this session.

---

## Primary questions (ask of your own diff)

- Is there a refactoring move that would make this dramatically simpler — a reframing so fewer concepts, branches, or helper layers are needed?
- Does this improve or worsen the local architecture?
- Did a cohesive module become more coupled, more stateful, or harder to scan?
- Is this logic in the right file and layer?
- Did this enlarge a file or component past a healthy size?
- Are there repeated conditionals that signal a missing model or helper?
- Is the implementation direct, or special-casey?
- Is this abstraction earning its keep, or is it a wrapper?
- Did I introduce casts, optionality, or ad-hoc shapes that hide the invariant?
- Did I leak details across a boundary?
- Is orchestration more sequential or less atomic than it needs to be?
- Does the named **Check** actually fail when I break this slice on purpose?
- Did I contradict an ADR?
- Did I code a foreign API/docs shape from memory or a blog instead of a cited primary source?
- Can a non-technical person read the GitHub ticket and know status?
- Did I leave the tree broken between increments, or mix two logical things in one commit?
- If this is a public surface: did the contract exist before the implementation?
- If this crosses a trust boundary: can I name the boundary, the asset, and the abuse case?

---

## What you must not ship

- A refactor that moves code around but does not reduce concepts a reader must hold
- Narrow edge-case handling in the middle of an already busy function
- "Temporary" branching that will become permanent debt
- Tests that pass while the code is less modular or less readable
- Extra product behavior not in this slice, these ADRs, or this Check
- A Check you never ran, or a Check that would still pass if the slice were broken

---

## Preferred remedies

- Delete a whole layer of indirection rather than polishing it
- Reframe the state model so conditionals disappear
- Change the ownership boundary so the feature is a natural extension of an existing abstraction
- Turn special-case logic into a simpler default with fewer exceptions
- Extract a helper or pure function; split a file that has grown past its shape
- Replace condition chains with a typed model or explicit dispatcher
- Reuse canonical helpers; move logic to the module that owns the concept
- Make related updates atomic; parallelize independent work when it also simplifies orchestration

---

## Approval bar

Behavior correct is not enough. All of these must hold before calling a slice done:

- No clear structural regression
- No obvious missed opportunity to make the implementation dramatically simpler
- No unjustified file-size explosion
- No obvious spaghetti-growth from special-case branching
- No hacky or magical abstraction that makes the code harder to reason about
- No unnecessary wrapper / cast / optionality churn obscuring the design
- No architecture-boundary leak or avoidable canonical-helper duplication
- No missed obvious decomposition that would materially improve maintainability
- Slice **Check** ran and would fail if this slice were broken
- Cited ADRs still true
- If `DESIGN.md` exists: user-visible work matches the design system, and any change was deliberate, same-commit, and stated
- If `docs/architecture/` has a record: no boundary crossed, no fitness function weakened
- Nothing from **Not this effort** landed
- You did not start the next slice
- Tracker issue is updated in spoken English (what landed, what you didn't touch)
- Increments were committed atomically; tests ran before each commit; no secrets in the diff
- If this slice exposed an interface: contract first, one error shape, validate at edge, additive fields, idempotency honoured if you accepted a key
- If this slice crossed a trust boundary: threat model written, always/never rules held, ask-first items actually asked

Any line above that fails is a blocker unless you can justify it in one sentence to the human. If the bar is not met, do not stop with "LGTM, nits later." Fix it, or explicitly hand back a blocked slice.

---

## It's working if

- Exactly one handoff slice changed behavior, its Check passed, and you know the Check can fail.
- The diff is simpler than the first draft, not merely larger.
- The human is not staring at the rest of the product half-built in this session.
- Cuecards was not asked to decide anything you could have coded around.
