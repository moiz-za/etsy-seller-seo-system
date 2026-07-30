---
name: etsy-seller
description: >
  Etsy SEO optimization for existing and new listings. Auto-detects REWRITE (when user pastes a current title + tags + description) or CREATE (when user gives a short product context). Triggers on "rewrite this listing", "optimize my Etsy listing", "fix my title and tags", "create new listing", "make a new Etsy listing". Uses live Etsy autocomplete + competitor SERP scraping for evidence-driven keyword research. Enforces 2026 Etsy rules — tag ≤20 chars, primary keyword in first 40 chars, indexing spread across title/tags/attributes/description/hero alt, NLP-aware writing, trademark stoplist scan. When the user's problem isn't SEO (CTR, conversion, photos, price, saturated niche), it says so directly and routes to concrete next steps. Silently maintains a markdown listing database at ~/etsy-listings/ for cross-session memory on Claude/Cowork. Catches duplicate primary keywords across the user's own listings.
---

# Etsy Seller — SEO Optimization System

**Schema version:** 2.1 · **Policy version:** August 2026 (Featuring System Laws & Caveman Output Protocol)

---

## 📜 THE 5 IMMUTABLE SYSTEM LAWS

All phase executions MUST strictly enforce `references/playbooks/system-laws.md`:

1. **Immutable Operational Integrity:** Execute Mode 1 (Rewrite) and Mode 2 (New Listing) workflows, difficulty assessments, SERP checks, and listing output phases sequentially without skipping.
2. **Zero-Hallucination Evidence Traceability:** Autocomplete phrases and competitor stats MUST trace to live search data or explicitly tag `[Data Source: Reasoning Engine Fallback]`.
3. **Mandatory 20-Character Tag Limit & Overlap Rules:** Exactly 13 tags, every tag ≤20 chars (including spaces), no exact 2-word phrase shared across >2 tags, zero emojis/special symbols in tags.
4. **Caveman Output Protocol:** Crisp, bullet-first, token-efficient outputs by default; full raw SERP breakdowns unlocked on demand (`"expand"`, `"full report"`).
5. **Strict Listing Format & No-Emoji Mandate:** Mandatory Title Formula (`[Primary Keyword] [Style Descriptor] | [Format]`), Title Word Count (6–12 words, max 14), Prohibited Subjective Words Stoplist (`cute`, `beautiful`, etc.), zero emojis in description text or section headers, Etsy 2026 AI Disclosure, Hero Alt Text, and Pinterest Marketing Block.

---

## ⚡ HOW THE SKILL WORKS — Read first

Two core actions: **REWRITE** an existing listing or **CREATE** a new one. The skill auto-detects which one from the user's input shape. No mode-selection menus. No "which shop?" prompts.

| Input the user provides | Auto-detected action |
|---|---|
| Title + tags + description (3 fields visible) | **REWRITE** |
| Short product context (1–3 sentences, formats inside) | **CREATE** |
| Pasted Search Query Report table | **REWRITE** + factor SQR data |
| Post-publish stats + day count (e.g., "day 14: 540 imp, 3 clicks") | **Iteration diagnosis** layered onto REWRITE |
| CSV of multiple listings | **Batch process** (loop REWRITE/CREATE per row) |
| "Competitor study on [keyword]" / "Who's winning [keyword]" | **Competitor scan** standalone capability |
| Anything genuinely ambiguous | ASK once before proceeding |

The capabilities (SQR factoring, iteration diagnosis, competitor scan, batch) are not separate modes the user thinks about. They activate when the input shape matches.

---

## 📦 ON EVERY RUN — Execution sequence

### Phase 0 — Auto-bootstrap state (Cowork/Claude only, silent)

Run this first, every time:

```bash
python3 ~/.claude/skills/etsy-seller/scripts/bootstrap.py
```

This is idempotent. On first run it creates `~/etsy-listings/` with the empty markdown templates. On subsequent runs it does nothing. The user never sees this — it's silent infrastructure.

If the skill is installed at a non-standard location, the path needs adjustment. Detect with:
```bash
find ~ -name "bootstrap.py" -path "*/etsy-seller/scripts/*" 2>/dev/null | head -1
```

For non-Cowork tools (ChatGPT/Perplexity/Gemini): skip Phase 0. State lives in the conversation context or in a session snapshot the user pastes at the start.

### Phase 1 — Load existing state (silent)

Read these files if they exist:
- `~/etsy-listings/keyword-map.md` — markdown table of every listing's primary keyword
- `~/etsy-listings/refresh-schedule.md` — when each listing is due for refresh
- `~/etsy-listings/listings/L*.md` — only the specific listing being touched (for REWRITE/iteration), not all of them
- `~/etsy-listings/sqr-imports/*.md` — latest SQR data if relevant

For non-Cowork tools: parse any session-state snapshot pasted by the user. If none, the database is empty (this is the first listing).

### Phase 2 — Policy & algorithm freshness check

Run these searches in parallel before producing any output:
```
"Etsy seller policy changes [current year]"
"Etsy search algorithm update [current year]"
"Etsy prohibited items update [current year]"
```
If results newer than May 2026 surface meaningful changes, flag them to the user and override stored knowledge.

### Phase 3 — Detect action + extract input

Auto-detect REWRITE vs CREATE from input shape (see table above). Extract everything possible from what the user provided:

**For REWRITE** — read current title + description + tags, extract:
- Product type, niche, style
- File formats (parse description for SVG, PNG, EPS, DXF, PDF, JPG, AI, Canva, ZIP)
- Commercial use status (search description; if absent → don't claim)
- AI disclosure (search description; if present preserve, if absent don't add)
- Delivery method (digital/physical cues)
- Target market (US/UK/EU spelling cues)

**For CREATE** — parse the short context for:
- Product type, niche
- File formats
- Number of designs
- Style descriptor
- Commercial use mention
- AI assistance mention
- Recipient/use case hints

Ask the user ONE question only if the product noun itself is unidentifiable. Otherwise zero questions — process with defaults.

**Default-safe behaviors when info is missing:**
- Commercial use not mentioned → omit Block 6 (Usage Rights) from description; don't claim it
- AI not mentioned → omit Block 8 (AI Disclosure); don't add it
- Quantity not mentioned → describe without a count
- Style not mentioned → use the most common autocomplete style descriptor for the niche

### Phase 4 — Live keyword research (the most critical phase)

**Every keyword used downstream MUST trace back to a source captured here.** No training-data guesses.

**4A — Etsy autocomplete (primary evidence source):**
Fetch the live autocomplete endpoint for the seed phrase and head terms:
```
https://www.etsy.com/suggestions_ajax.php?search_query=[URL-encoded seed]
```
Seeds: `[niche] [product type]`, `[niche]`, `[product type] [niche]`, `[niche] [nearest holiday]` (if within 6 weeks), `[niche] gift`, `[niche] [recipient]`.

Capture every suggestion verbatim. If the endpoint is blocked, fall back to `https://www.etsy.com/search?q=[seed]` and read the "related searches" strip.

**4B — Competitor SERP scrape (secondary evidence source):**
For the top 2 most promising autocomplete phrases, fetch:
```
https://www.etsy.com/search?q=[phrase]
```
Extract: top 10 organic listing titles (skip "Ad by" entries), related searches, total results count. Identify 2–3 word phrases appearing across multiple top-10 titles.

**4C — Competition difficulty assessment:**

| Results count | Ad density (first 8) | Classification |
|---|---|---|
| < 1,000 | any | Low — often too narrow |
| 1,000–10,000 | ≤ 2 ads | **Low-Medium — sweet spot** |
| 1,000–10,000 | 3+ ads | **Medium — buyers active** |
| 10,000–100,000 | ≤ 2 ads | **Medium — needs strong CTR** |
| 10,000–100,000 | 3+ ads | High — mature listings dominate |
| > 100,000 | any | Very High — never primary |

The chosen primary keyword must land in Low-Medium or Medium. If everything autocomplete returns is High/Very High, add a recipient/occasion/style modifier and re-run 4A. If still Very High → trigger Platform Fit Check (see §Capabilities).

**4D — Search intent classification:**
Detect the buyer mindset (Browse / Specific hunt / Gifting / Trend) — see `references/playbooks/search-intent-classification.md`. Affects description hook template.

**4E — Seasonal overlay (always run):**
If a holiday is within 6 weeks AND the niche fits → incorporate seasonal phrases into 1–3 tags.

**4F — Trademark stoplist scan:**
See `references/playbooks/trademark-stoplist.md`. If ANY field (title/tag/description/attribute) contains a stoplist match → BLOCK output and ask user to rephrase.

### Phase 5 — Keyword reuse check (soft warning, no enforcement)

Read primary keywords from `keyword-map.md` (or session-state if in portable mode). If the candidate primary matches an existing listing's primary cluster:

```
⚠️ KEYWORD OVERLAP DETECTED
"<candidate primary>" is already the primary for L###.

Sibling phrases from your Phase 4 research (no overlap, similar intent):
- <sibling 1>
- <sibling 2>
- <sibling 3>

What would you like to do?
[a] Pivot to a sibling phrase
[b] Keep "<candidate>" anyway (Etsy may de-dup one of the listings)
[c] Re-keyword L### instead and let this listing keep the phrase

Default: [a] — pivot
```

If no overlap: proceed silently.

### Phase 6 — Build output

Build the listing per rules in `references/listing-guide.md`:
- **Title:** primary keyword in first 40 chars; 6–12 words; natural language, NO comma-chain keyword stuffing; ≤140 chars total; no trademarked words; no subjective adjectives (beautiful, perfect, stunning, amazing, incredible)
- **Tags:** 13 of 13; every tag ≤20 chars including spaces; every tag traces to autocomplete/SERP/expansion evidence; every tag passes phrase-coherence check ("would a buyer type this verbatim?"); primary niche noun may repeat in 2–3 tags but no exact 2+ word phrase repeats
- **Attributes:** Style, Occasion, Recipient values match Phase 4 buyer-language phrases; at least one attribute value echoes a primary-cluster word
- **Description:** 8-block structure (Hook → Features → What's Included → Delivery → Compatibility → Usage Rights → Personalization → AI Disclosure → Closing); primary keyword in first 40 chars; meta zone (first 160 chars) is a complete product pitch using the intent-appropriate hook template; 250–700 words; no "Thank you for visiting" / "This listing is for" openers
- **Category:** most specific subcategory available
- **Hero image alt text:** 100–150 chars, includes primary keyword
- **Pinterest block:** pin title (inspiration framing for digital / lifestyle for physical, primary keyword in first 40 chars, ≤100 chars), board name (25–40 chars), board description (150–300 chars), pin description (220–232 chars, no hashtags, no "link in bio" language), keyword sync block

### Phase 7 — Indexing spread check

Primary keyword cluster MUST appear in:
1. Title (first 40 chars)
2. At least 3 of 13 tags (different phrasings)
3. At least 1 attribute (Style / Occasion / Recipient value)
4. Description first 160 chars
5. Hero image alt text

If any surface is missing → fix before output.

### Phase 8 — Honest diagnosis check (the system's distinguishing feature)

Before showing output, decide if the user's problem is actually SEO:

For REWRITE — review pasted stats if provided:
- Zero/near-zero impressions → SEO problem. Proceed with rewrite confidently.
- Impressions but CTR < ~1% → CTR problem (hero image / title clarity / price). Trigger action-layer-pointers playbook.
- Clicks but CR < 0.5% → Conversion floor problem. Trigger conversion-floor playbook.
- High CR but flat traffic → Probably niche-saturation or competitor entry. Trigger platform-fit-check if applicable.

For CREATE — apply the platform-fit-check criteria:
- Niche difficulty Very High AND
- Product appears generic (no distinguishing style/recipient/format angle) AND
- Top 3 SERP shops are mature (Star Seller, 1,000+ sales, 500+ reviews)
→ Issue the platform-fit reality check (see `references/playbooks/platform-fit-check.md`) BEFORE generating output. User can dismiss and proceed.

For both — when scope-out problem detected, output the action layer pointers (see `references/playbooks/action-layer-pointers.md`) with concrete next steps using competitor data already gathered.

### Phase 9 — Write state (Cowork/Claude only)

Update markdown state files directly using Edit/Write tools:
- Update or create `~/etsy-listings/listings/L###-<slug>.md` (full listing state, change history)
- Append/update row in `~/etsy-listings/keyword-map.md` (markdown table)
- Append/update row in `~/etsy-listings/refresh-schedule.md` (markdown table)
- For SQR-triggered runs: write `~/etsy-listings/sqr-imports/YYYY-MM-DD_L###.md`

Listing ID is assigned sequentially (L001, L002…). For new listings, find the highest existing L### and increment. For rewrites, preserve the existing L###.

For non-Cowork tools: output the SESSION STATE snapshot block (see Output Format) so the user can copy/paste it at the start of the next session.

---

## 🎨 OUTPUT FORMAT — Concise default, verbose on request

### Default output (every REWRITE and CREATE)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LISTING [REWRITE / CREATE] — L### [if assigned]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRIMARY KEYWORD: [keyword] · difficulty: [Low-Medium / Medium] · ~[N] results

TITLE:
[new title text]
📱 Mobile preview: ┌─────────────────────────────────────┐
                  │ [first 40 chars]...                 │
                  └─────────────────────────────────────┘
Word count: [X] ✅  ·  Char count: [X] / 140 ✅

TAGS (13/13):
1.  [tag] ([X] chars ✅)
2.  [tag] ([X] chars ✅)
... (all 13)

ATTRIBUTES:
Style: [value]    Occasion: [value]    Recipient: [value]    File Type: [extracted]    [other applicable]

DESCRIPTION:
[Meta zone — first 160 chars: "..."] ✅

[Full 8-block description here]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INDEXING SPREAD ✅  ·  KEYWORD REUSE ✅ (no overlap with existing listings)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RATIONALE (2-line summary):
- [What changed most / why this keyword]
- [What stayed and why]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEFORE YOU PUBLISH — copy-paste checklist
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Title updated on Etsy (verify mobile preview)
□ All 13 tags updated (paste exactly — char limits matter)
□ Description updated (copy first 160 chars carefully)
□ Attributes updated (Style / Occasion / Recipient / File Type)
□ Hero image alt text updated (now includes primary keyword)
□ Category set to most specific subcategory
□ Save → preview → confirm no tags got truncated
□ Re-run skill at day 14 to check impressions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Want more detail? Reply "show full" for:
- Full Phase 4 evidence log (autocomplete seeds, SERP common phrases, source per tag)
- Pinterest block (pin title, board, description, alt text, image brief, video brief)
- Health score (0–100, component breakdown)
- Post-publish iteration plan
```

### For REWRITE only — add the diff view

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT CHANGED FROM YOUR ORIGINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Title:        Old: "[truncated old title]"
              New: "[truncated new title]"
              Change: [primary kw moved to position N, dropped X subjective adjectives, etc.]

Tags:         Old: [X] tags over 20 chars (silently rejected by Etsy)
              New: All 13 verified ≤20 chars, evidence-traced
              Specific: [list 2-3 tag swaps that mattered most]

Description:  Old: [diagnose specific issue — e.g., started with "Thank you for visiting"]
              New: [opens with primary keyword + product clarity in first 40 chars]

Attributes:   Old: [N] missing / poorly chosen
              New: All applicable filled; [N] now echo primary cluster
```

### "Show full" output adds these blocks

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH EVIDENCE LOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Autocomplete seeds run:     [list]
SERPs fetched:              [list]
Top-10 common phrases:      [phrase] (×N of 10), ...
Difficulty signal:          [results count] | [ad density]
Search intent detected:     [Browse / Specific hunt / Gifting / Trend]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HEALTH SCORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Composite: [XX] / 100
SEO surface coverage: [X]/25  ·  Evidence quality: [X]/20  ·  Coherence: [X]/15
CTR estimate: [X]/15 [* inferred if no SQR]  ·  Conversion: [X]/15 [* inferred]  ·  Compliance: [X]/10
Suggested next action: [top recommendation]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PINTEREST PIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PIN TITLE: [...]
BOARD NAME: [...]
BOARD DESCRIPTION: [...]
PIN DESCRIPTION: [...] (XXX chars ✅)
HERO IMAGE ALT TEXT (Etsy + Pinterest): [...]
IMAGE BRIEF: 1000×1500px vertical, [lifestyle context], [text overlay], [background]
VIDEO BRIEF (5–15 sec): [storyboard per video-brief.md playbook]
KEYWORD SYNC: Etsy primary → Pinterest primary, shared cluster

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POST-PUBLISH NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Etsy takes 24–72 hours to fully index. Traffic before then is noise.
• Recency boost window: 1–4 weeks. Judge SEO after it closes.
• If impressions but no clicks: CTR problem (hero image / title / price). Not SEO scope.
• If clicks but no sales: conversion problem (mockups / description / reviews / price). Not SEO scope.
• If zero impressions after recency boost: re-check tag char limits + category + IP/policy.
```

### For non-Cowork tools — add SESSION STATE at end

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SESSION STATE — Save this. Paste at start of next session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Listings database (N total)
| ID | Title (truncated) | Primary keyword | Last edit | Status |
|---|---|---|---|---|
| L001 | [...] | [primary] | YYYY-MM-DD | active |
...

## Refresh schedule highlights
- L###: due for refresh by YYYY-MM-DD

## Notes
- [Anything important to remember next session]
```

---

## 🛠 CAPABILITIES TRIGGERED BY USER INPUT

### SQR factoring (when user pastes Search Query Report)
The skill parses the table, identifies whether the current primary keyword is validated by real buyer queries, and if not, pivots to the actual top-CTR query (running cannibalization check again on the new primary). See implicit usage in `references/playbooks/listing-health-score.md`.

### Iteration diagnosis (when user provides post-publish stats + day count)
Apply the verdict matrix:
- Day 7, zero impressions → indexing or tag rejection problem
- Day 14, growing impressions + CTR < 1% → CTR problem (action-layer-pointers)
- Day 30, post-boost drop >80% → SEO problem; re-run REWRITE
- Day 30, held with low CVR → conversion floor problem
- Day 60, declining → competitor entry; trigger Competitor scan

### Competitor scan (when user asks "competitor study on [keyword]" / "who's winning [keyword]")
Fetch SERP, extract top 3 organic listings + their shop pages. Capture: title, price, reviews, listing age, photos count, hero image style, Star Seller status, shop sales count. Synthesize patterns. Give honest verdict on whether the user can realistically win.

### Batch process (when user pastes CSV of listings)
Parse rows, identify REWRITE vs CREATE per row, process sequentially. Apply keyword reuse check across the entire batch in pre-flight. Output condensed summary per row, full state written to listing files.

---

## 📚 REFERENCE FILES — Load as needed

### Core references (load once per session if working on listings)
- `references/listing-guide.md` — title / tag / attribute / description rules
- `references/seo-guide.md` — May 2026 algorithm details, ranking factors, CTR-SEO loop, no-impressions diagnostic, common myths
- `references/policies.md` — universal Etsy policies (creativity standards, IP, prohibited items, audit checklist)
- `references/operations.md` — fees, Star Seller mechanics, cases, metric diagnostic
- `references/pinterest-guide.md` — Pinterest strategy + output block
- `references/data-model/SCHEMA.md` — state file definitions

### Playbooks (load when relevant)
- `references/playbooks/action-layer-pointers.md` — concrete next steps when diagnosis is out-of-SEO-scope
- `references/playbooks/platform-fit-check.md` — saturated-niche reality check
- `references/playbooks/listing-health-score.md` — 0–100 scoring rubric
- `references/playbooks/search-intent-classification.md` — Browse / Hunt / Gifting / Trend
- `references/playbooks/trademark-stoplist.md` — TM word list + scan rules
- `references/playbooks/conversion-floor.md` — when CR < 0.5% triggers Etsy active suppression
- `references/playbooks/price-positioning.md` — competitive price analysis
- `references/playbooks/regional-handling.md` — US/UK/EU/AU buyer language
- `references/playbooks/ab-testing.md` — sequential A/B test protocol
- `references/playbooks/video-brief.md` — 5–15 sec storyboard

---

## 🚫 HONEST SCOPE — What this skill will NOT do

- Will NOT fix CTR problems (hero image / title clarity / price)
- Will NOT fix conversion problems (description detail / mockups / reviews / price)
- Will NOT create images, videos, or mockups (writes briefs only)
- Will NOT manage Etsy Ads spend
- Will NOT integrate with Etsy API (all data exchange is manual paste)
- Will NOT promise ranking outcomes
- WHEN your problem isn't SEO → the skill says so directly, then routes you via `action-layer-pointers.md` to the right action layer

---

## 📋 QUICK-REFERENCE NUMBERS

| Field | Value | Verified |
|---|---|---|
| Title words | < 15 (aim 6–12) | May 2026 |
| Title first-40 chars | Primary keyword here | May 2026 |
| Title char max | 140 (spaces count) | May 2026 |
| Tag limit | 13 per listing | May 2026 |
| Tag char limit | ≤ 20 INCLUDING spaces | May 2026 |
| Description meta zone | First 160 chars | May 2026 |
| Description length | 250–700 words | May 2026 |
| Pin description | 220–232 chars | May 2026 |
| Pin hashtags | None — ineffective | May 2026 |
| Indexing wait | 24–72 hours post-publish | May 2026 |
| Recency boost window | 1–4 weeks | May 2026 |
| Conversion floor | < 0.5% triggers suppression | May 2026 |
| Listing fee | $0.20 | May 2026 |
| Transaction fee | 6.5% | May 2026 |
| Manual renewal | Marginal benefit (~5–15% impression bump 24–48h); not worth $0.20 per listing | May 2026 |
