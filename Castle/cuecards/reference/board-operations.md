# Board Operations (GitHub & Local Fallback)

The live board lives as issues on GitHub via the `gh` CLI. If `gh` is unavailable, use the local filesystem fallback under `.cuecards/boards/<slug>/`.

## Label Setup

Create labels if they do not exist:
```bash
gh label create type:ask --color "0E8A16" --description "Decision card" || true
gh label create type:look --color "1D76DB" --description "Evidence/prototype card" || true
gh label create type:find --color "5319E7" --description "Fact research card" || true
gh label create type:chore --color "D93F0B" --description "Unblocking task card" || true
gh label create mode:for-you --color "B60205" --description "Needs human decision" || true
gh label create mode:unattended --color "0E8A16" --description "Agent handles" || true
gh label create priority:now --color "B60205" || true
gh label create priority:next --color "FBCA04" || true
gh label create priority:later --color "CCCCCC" || true
```

---

## Creating Board & Cards

### Create parent board issue
```bash
gh issue create \
  --title "<spoken board name>" \
  --body-file <board-body.md>
```

### Create child card issue
```bash
gh issue create \
  --title "<spoken card name>" \
  --body-file <card-body.md> \
  --label "type:ask,mode:for-you,priority:now"
```

---

## Claiming, Updating, and Closing

- **Claim:** Assign the issue to yourself:
  ```bash
  gh issue edit <issue-number> --add-assignee "@me"
  ```
- **Comment progress:**
  ```bash
  gh issue comment <issue-number> --body "<update in spoken English>"
  ```
- **Close card:**
  ```bash
  gh issue close <issue-number> --comment "Decided: <verbatim human answer>. Recorded in [ADR-NNNN](../adr/NNNN-slug.md)."
  ```

---

## Local Fallback YAML Format

When GitHub is not accessible, save individual cards under `.cuecards/boards/<slug>/cards/<NNN>.md` with frontmatter:

```yaml
---
id: "001"
title: "<spoken-English name>"
type: ask               # ask | look | find | chore
status: open            # open | claimed | closed | not-this-effort
needs_you: true         # true for for-you, false for unattended
priority: now           # now | next | later
who_decides: you
claimed_by: ""
blocked_by: []
blocks: []
created: YYYY-MM-DD
human_answer: ""        # required verbatim quote on close
---
```
