# Forbidden UI Tells

## Forbidden (the tells)

These are the signatures a machine produces when it tries to look designed. Treat them as hard bans unless the brief explicitly asks for one.

### The single worst one

**The em dash is banned in the interface.** Zero. Not "sparingly" — zero. Not in headlines, eyebrows, pills, buttons, body copy, quotes, attribution, captions, or alt text. Use a period, a comma, a colon, or parentheses. *(This ban governs shipped interface copy the product authored. Docs, ADRs, tickets, and skill files are not the interface.)*

**The en dash is allowed in exactly one place**: between two numbers, as a range (`2018–2026`) — that is what it is for. Anywhere else it is an em dash in disguise. Outside a numeric range, a user should see nothing but the regular hyphen and the math minus sign. If verbatim third-party text you must quote contains a banned dash, normalize the punctuation, or accept it in the walk record out loud — still a fail, but a named one.

### Visual

No neon or outer glow, no pure black, no oversaturated accents, no gradient text on large headings, no custom mouse cursors, and no decorative crosshair or hairline grids drawn just to look designed.

### Hero and labels

No version labels (`v0.6`, BETA, INVITE-ONLY) unless the brief is a launch. No micro-eyebrows that number the brand ("Brand, No. 01"). No section-number eyebrows (`00 / INDEX`, `06 / how it works`), and no `01 / 4` counters on tiles. No scroll cues ("Scroll to explore", bouncing chevrons) and no decoration strips across the bottom of the hero (`BRAND. MOTION. SPATIAL.`). No floating explainer paragraph in the top-right of a section header, no tiny tagline under the hero buttons, and no trust logo row inside the hero.

### Separators and decoration

The middle dot is rationed to one per line, and only inside metadata. No colored status dots on every row, badge, or nav item; a dot that repeats the word beside it is decoration. No pills or tags overlaid on photographs, and no photo-credit captions used as filler. No vertical rotated text unless the brief is genuinely experimental and it organizes real content. No version or build footers (`v1.4.2`, `Build 0048`, `last sync 4s ago`) on marketing pages, and no locale, time, or weather strips. No `<br>`-split-and-italicized headlines.

### Fake things

**No div-built fake screenshots.** A hand-made "product preview" out of styled rectangles, fake dashboards, fake terminals, or fake task lists is the number one tell. Use a real screenshot, a generated image, a real mini-version of the component, or nothing at all. The same goes for fake version footers planted inside an invented preview, performance numbers nobody measured, placeholder names, and invented brand shells. No random remote image URLs that may break; use a seeded placeholder or a real asset. No hand-rolled decorative SVG when a library or a generated asset would do, and no icon drawn by hand from path data; pick one family (Phosphor, HugeIcons, Tabler, or similar) at one stroke width.

### Marketing voice

No coy social-proof headings ("Quietly in use at", "Quietly trusted by"). No poetic section labels ("From the field", "Currently on the bench", "Loose plates") where a plain one would do. No mock-humble nods at other people in the industry, and no throat-clearing sentence under a label. No numbered step labels ("Stage 1", "Phase 02") where the verb would do the job: "Install", "Configure", "Ship".

### Layout

No three equal feature cards. No rule above and below every row of a long list. No filled progress tracks used as decoration for comparisons. No centered hero above Boldness 4. No navigation that wraps to two lines at desktop. No layout family used twice on one page.

### Content

No generic names, stock avatars, or suspiciously round numbers. No filler verbs. No emoji, unless the brief is explicitly playful and social, and then sparingly. One copy register per page.

---

