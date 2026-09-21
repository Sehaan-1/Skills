# Cutting Lanes

# Cut lanes

Start from the handoff. Do not start from the org chart, and do not start from a blank architecture wish.

1. List every handoff slice, its **Depends on**, its **Check**, the files it must touch (guess, then verify against the tree).
2. Group slices that share ownership and can share a Check. That group is a candidate lane.
3. Where two candidate lanes would touch the same surface, either **merge them** or **extract a seam** (contract owned by one lane, consumed by the other).
4. Name **Now / Next / Then** from true waits, not from habit. Independent groups go Now, in parallel.
5. Name an **integration owner**. If you invoked this skill, that is you unless the map says otherwise.
6. Depth-review the map. Commit it. File or update one GitHub issue per lane (spoken English, same tracker shape as oneslice, plus Owns / Parallel with / Waits on). Point each issue at the map.

Regrouping slices onto lanes is allowed. Changing **Does**, sneaking past **Not this effort**, or contradicting an ADR is not.

**When the honest map is one lane:** write that. Then run it (still this skill if they asked to ship the destination — you keep going through every slice in that lane until the destination Check, each slice at the oneslice bar). Do not fake Lane B.

---

