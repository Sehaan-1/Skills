# GitHub Board Operations and Execution

# Board operations (GitHub)

Use `gh` in the current repo. `{owner}/{repo}` from `gh repo view --json nameWithOwner -q .nameWithOwner`.

## Labels (create if missing)

`cuecards`, `board`, `card`, `ask`, `look`, `find`, `chore`, `for-you`, `unattended`, `now`, `next`, `later`

```bash
for l in cuecards board card ask look find chore for-you unattended now next later; do
  gh label create "$l" -c "0E8A16" -d "$l" 2>/dev/null || true
done
```

## Create the board (parent)

```bash
gh issue create --title "<spoken board name>" --label cuecards,board --body-file /tmp/board.md
```

## Create a card (child)

```bash
gh issue create --title "<spoken card name>" --label cuecards,card,<type>,<for-you|unattended>,<now|next|later> --body-file /tmp/card.md
```

Make it a sub-issue of the board (`ISSUE_ID` is the child's numeric `id`, not the number):

```bash
CHILD_ID=$(gh api repos/{owner}/{repo}/issues/<child-number> --jq .id)
gh api -X POST repos/{owner}/{repo}/issues/<board-number>/sub_issues -f sub_issue_id="$CHILD_ID"
```

## Native blocked-by

```bash
BLOCKER_ID=$(gh api repos/{owner}/{repo}/issues/<blocker-number> --jq .id)
gh api -X POST repos/{owner}/{repo}/issues/<blocked-number>/dependencies/blocked_by -f issue_id="$BLOCKER_ID"
```

If that API is unavailable, still write Blocked by / Blocks in **Tracking** and on the parent lists. Never leave edges only in your head.

## Claim / close / comment

- Claim: `gh issue edit <n> --add-assignee @me`
- Answer + close: comment the **Answer** in their voice plus `ADR-NNNN` path, then `gh issue close <n>`
- After every close or new card: **edit the parent body** so Ready now / Waiting / Decided / blocks still tell the truth
- Commit ADR files and `docs/adr/README.md` in the same sitting as the close

## Query the frontier

Ready now: open, label `card`, no assignee, not blocked (or all blockers closed). Split by `for-you` vs `unattended`. Sort `now` before `next` before `later`.

## Local fallback (only if GitHub is impossible)

```text
.cuecards/boards/<slug>/
  BOARD.md
  cards/001-<slug>.md
  assets/
```

Same bodies. Say out loud that issues were not created. ADRs still go in `docs/adr/` â€” they are repo files, not issues.

## It's working if

- The board is a GitHub issue; every card is a child issue with labels, edges, and priority.
- A non-technical reader can pick a Ready now â€” for you issue and decide.
- Unattended cards actually run without them, in parallel.
- Notes hold standing rules **and ADRs in force** so cards don't repeat them.
- Look-cards left a kept artifact and (when UI) a pin CI can fail on.
- How we'll know we're there has walk + proof + enforcement, and the board is not called done until those pass.
- Every accepted ask/look has `docs/adr/NNNN-â€¦.md` with Context, Decision, Consequences, and a status. Later cards cite **ADR-NNNN** by name.
- Supersession is a new ADR plus History on the old file â€” closed issues are not rewritten.
- When the board is done, `docs/cuecards/handoff-<slug>.md` sequences slices that cite ADRs. That file exists before anyone writes destination code.
- Every open card still reads as one question, with options and a recommendation, in easy words, after hard thinking.
- You did not ship the destination as a side effect.
