# Map Quality Bar and Red Flags

## Map quality (offstage, before anyone sees it)

Think first. The timid map is one lane because contracts felt like work. The sloppy map is eight lanes that all edit `src/app.ts`. Aim at a map a strong tech lead would defend.

1. **Real parallelism.** For every "Parallel with," you can say why they will not collide (disjoint files, or a written seam).
2. **Ownership becomes architecture.** The Owns lines are the module boundaries you want in six months, not a snapshot of today's accidents. Cut lanes along the architecture you want.
3. **Vertical over horizontal.** Prefer a lane with a user-visible Check (someone can do X) over a "DB lane" and an "API lane" that cannot land alone â€” unless the team is actually specialized and the seam is clean.
4. **Seam lanes are rare and honest.** Extract a contract/platform lane only when it unblocks two others. A seam lane with no consumer this sitting is theatre.
5. **Right-sized.** A lane is one to a few handoff slices that share ownership and have one Check. More lanes than people (or agents) â†’ merge lanes. A lane that is "the rest of the product" â†’ cut again.
6. **Now is takeable.** Everything in **Now** has Waits on: none, shared contracts written or owned by a Now lane that writes them first this sitting.
7. **The destination still fits.** Not this effort did not sneak in. Uncited ADRs did not sneak in.
8. **Spoken names.** "Who gets paid" not `ledger-sync-worker`. Same voice as cuecards.
9. **Briefable.** Each lane can be handed to an agent as a packet smaller than the map. If you cannot brief it thinly, the lane is still fuzzy â€” cut again.

If you cannot defend the map against "is this actually how a larger team ships without colliding?", rewrite it. Do not present a queue in costume.

### Red flags

| Thought | Reality |
| --- | --- |
| "We'll discover ownership in the PR." | You will collide. Put Owns on the map first. |
| "These two lanes are parallel if they rebase carefully." | They are one lane. |
| "A shared util file is fine, both can edit it." | That file is a seam, or it belongs to one owner. |
| "Layer lanes (schema / API / UI) look clean on a slide." | Nothing user-visible lands until the last layer. Cut vertical unless the seam is real. |
| "Eight lanes, two people." | Merge until lanes â‰¤ people, plus one seam lane if it unblocks. |
| "The handoff order is already the map." | The handoff is a sequence for one builder. The map is parallel + ownership + shared contracts. It may regroup slices. It may not change what gets built. |
| "We'll write the contract when both sides meet." | Both sides will invent a different contract. Write it first. |
| "Ship faster by skipping oneslice." | Then you shipped a mess. Stop. |
| "The destination is huge, so lower the bar." | Honest map + Now lanes at full bar. Never a cheap finish. |
| "Integration at the end, once." | You will spend the last day merging fiction. Integrate after every lane. |
| "New teammate can ask in chat." | Then the map failed. They should pick an unclaimed Now lane from the file. |
| "Give every agent the full context to be safe." | You will burn spend and they will touch the wrong files. Thin brief. |
| "Serialize the agents so merging is easier." | If they don't share files, you paid latency for fear. Dispatch together. |
| "Degrade this lane so we hit the time box." | Hit the limit with less, done well. |
| "Don't measure, just keep cutting." | Then you cannot tell a round from thrashing. |
| "Restart every lane because one failed." | Isolate the failure. The others keep moving. |

---

