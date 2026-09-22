# Primer Anki decks (extracted) + company blogs

## Anki cards

The repo's three `.apkg` decks are extracted to **`data/anki_cards.json`** (source: `resources/flash_cards/*.apkg`):

| Deck key | Origin | Cards | Use |
|---|---|---|---|
| `system` | System Design.apkg | 42 | Concept drills: performance vs scalability, CAP, consistency patterns, availability, DNS/CDN/LB/DB/cache/async/comm topics |
| `exercises` | System Design Exercises.apkg | 8 | The 8 system-design questions (Mint, Pastebin, sales rank, …) — recall the 4-step shape |
| `oo` | OO Design.apkg | 6 | OOD questions with constraints/assumption prompts |

Generate study output with:

```bash
python3 scripts/gen_flashcards.py --deck anki --format tsv --out anki.tsv          # all 56, Anki import
python3 scripts/gen_flashcards.py --deck anki-system --format markdown             # concepts only
```

Built-in decks from the skill itself: `core`, `numbers`, `scaling`, `all` (see `gen_flashcards.py`). Prefer the primer's own `system` deck for breadth; prefer `core`/`numbers`/`scaling` for exam-style bite-size recall.

Full decks also ship as `.apkg` in `resources/flash_cards/` when the repo is present (import into [Anki](https://apps.ankiweb.net/) directly for spaced repetition scheduling).

## Company engineering blogs (full list from README appendix)

Read a few for target companies before interviews — questions often come from the same domain.

Airbnb · Atlassian · AWS · Bitly · Box · Cloudera · Dropbox · Quora · eBay · Evernote · Etsy · Facebook · Flickr · Foursquare · GitHub · Google Research · Groupon · Heroku · HubSpot · High Scalability · Instagram · Intel · Jane Street · LinkedIn · Microsoft (+ MS Python) · Netflix · Paypal · Pinterest · Reddit · Salesforce · Slack · Spotify · Stripe · Twilio · Twitter · Uber · Yahoo · Yelp · Zynga

Aggregators: [kilimchoi/engineering-blogs](https://github.com/kilimchoi/engineering-blogs) · [High Scalability](http://highscalability.com/)

## Company architectures (README appendix — pattern-spotting)

Amazon · Cinchcast · DataSift · Dropbox · ESPN · Google · Instagram · Justin.tv · Facebook · Flickr · Mailbox · Netflix · Pinterest · Playfish · PlentyOfFish · Salesforce · Stack Overflow · TripAdvisor · Tumblr · Twitter · Uber · WhatsApp · YouTube — each links a deep-dive write-up in the primer's "Company architectures" table (repo present: `README.md` §Appendix).

## "Under development" topics (primer backlog — mention as stretch goals)

- Distributed computing with **MapReduce** (solutions show the pattern: sales_rank, mint, crawler dedup, pastebin analytics)
- **Consistent hashing** (playbook covers the trade-off; primer lists it as incomplete)
- **Scatter gather** (twitter/web_crawler search uses it — scatter-gather across search cluster)
