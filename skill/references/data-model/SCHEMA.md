# Data Model SCHEMA

**Schema version:** 2.0 (May 2026)

This document defines the flat-namespace markdown state files the skill reads and writes. There is no shop concept, no registry, no xlsx. All state lives in `~/etsy-listings/` (Claude/Cowork) or as a session snapshot (other AI tools).

---

## File tree (Cowork/Claude — auto-managed)

```
~/etsy-listings/
├── keyword-map.md                       # markdown table — one row per listing
├── refresh-schedule.md                  # markdown table — refresh cadence
├── listings/
│   ├── L001-funny-cat-mom-svg.md        # full per-listing state
│   └── L002-boho-wedding-clipart.md
└── sqr-imports/
    └── 2026-05-15_L001.md               # archived SQR pastes
```

That's it. No shop folders. No registry. No conflicts log file. No xlsx.

---

## File 1 — `keyword-map.md`

**Purpose:** the index of every listing's primary keyword. Used for the keyword reuse check.

**Format:**

```markdown
# Keyword Map

**Schema version:** 2.0
**Last updated:** YYYY-MM-DD

| Listing ID | Short slug | Primary keyword | Cluster words | Secondary keywords | Difficulty | Assigned | Status |
|---|---|---|---|---|---|---|---|
| L001 | funny-cat-mom-svg | funny cat mom svg | funny;cat;mom;svg | cat mama svg;pet mom svg;cricut cat mom | Medium | 2026-05-14 | active |
| L002 | boho-wedding-clipart | boho wedding clipart | boho;wedding;clipart | wedding floral clipart;rustic wedding clipart | Medium | 2026-05-14 | active |
```

**Columns:**
- `Listing ID` — L### (permanent, sequentially assigned)
- `Short slug` — derived from current title for human readability
- `Primary keyword` — the exact phrase
- `Cluster words` — semicolon-separated; used for keyword reuse check
- `Secondary keywords` — semicolon-separated supporting phrases
- `Difficulty` — Low / Low-Medium / Medium / High / Very High
- `Assigned` — date primary keyword was assigned
- `Status` — active / archived / paused

**Update rule:** one row written/updated per REWRITE or CREATE run. Skill reads this file first to check if the candidate primary matches an existing one.

---

## File 2 — `refresh-schedule.md`

**Purpose:** when to next-touch each listing.

**Format:**

```markdown
# Refresh Schedule

**Schema version:** 2.0
**Last updated:** YYYY-MM-DD

Minor refresh: every 90 days. Full review: every 180 days.
P1 = overdue · P2 = within 30 days · P3 = within 90 days · Recent = skip

| Listing ID | Last full edit | Last minor edit | Next minor | Next full review | Priority | Notes |
|---|---|---|---|---|---|---|
| L001 | 2026-05-14 | 2026-05-14 | 2026-08-14 | 2026-11-14 | P3 | Initial creation |
| L002 | 2026-02-10 | 2026-04-05 | 2026-07-05 | 2026-08-10 | P2 | Minor refresh April 5 |
```

**Update rule:** dates updated on every listing touch. Priority recalculated against today.

---

## File 3 — `listings/L###-<slug>.md`

**Purpose:** full state of one listing — current fields, change history, health score, SQR data references.

**Format:**

```markdown
# Listing L001 — funny-cat-mom-svg

**Schema version:** 2.0
**Listing ID:** L001
**Created:** YYYY-MM-DD
**Last full edit:** YYYY-MM-DD
**Last minor edit:** YYYY-MM-DD
**Listing URL on Etsy:** https://www.etsy.com/listing/[id]/[slug]  (if user shared)

---

## Current state

### Title
<current title text>
- First 40 chars: "..." ✅
- Word count: X · Char count: X / 140

### Primary keyword
**<primary keyword>**
- Difficulty: <Low-Medium / Medium>
- Source: autocomplete (×N) + SERP top-10 (×M)
- Last verified: YYYY-MM-DD
- Search intent: <Browse / Specific hunt / Gifting / Trend>

### Secondary keywords
- phrase 1 (autocomplete)
- phrase 2 (SERP top-10)
- ...

### Tags (13/13)
| # | Tag | Chars | Source |
|---|---|---|---|
| 1 | <tag> | X | autocomplete |
| 2 | <tag> | X | SERP top-10 |
| ... | | | |

### Attributes
| Attribute | Value |
|---|---|
| Style | <value> |
| Occasion | <value> |
| Recipient | <value> |
| File Type | <value> |

### Category
<Top> > <Mid> > <Sub>

### Description (full text)
```
<paste full description>
```

### Hero image alt text
<alt text — 100–150 chars, includes primary keyword>

### Pinterest block
- Pin title: <text>
- Board: <name>
- Board description: <text>
- Pin description: <text> (XXX chars)
- Image brief: <text>
- Video brief: <storyboard summary>

---

## Indexing spread check (latest)
- Title (first 40): ✅
- Tags (≥3 with cluster): Tag #X, #Y, #Z ✅
- Attribute echo: Style="<value>" ✅
- Description first 160: ✅
- Hero alt text: ✅

---

## Health score (latest)
**Composite: XX / 100**

| Component | Score |
|---|---|
| SEO surface coverage | X / 25 |
| Evidence quality | X / 20 |
| Coherence | X / 15 |
| CTR estimate | X / 15 [* inferred if no SQR] |
| Conversion estimate | X / 15 [* inferred] |
| Compliance | X / 10 |

Suggested next action: <one-line recommendation>

---

## SQR data (if available)

Latest import: `sqr-imports/YYYY-MM-DD_L001.md`

| Query | Impressions | Clicks | Orders | CTR | CVR |
|---|---|---|---|---|---|
| cat mom svg | 1240 | 18 | 2 | 1.5% | 11.1% |
| funny cat mom svg | 890 | 41 | 7 | 4.6% | 17.1% |

Primary keyword match: ✅ / ⚠️ (pivot recommended)

---

## Change history

### YYYY-MM-DD — Action description
- Field(s) changed: <list>
- Reason: <SEO problem / SQR pivot / refresh / etc.>
- Old → new: <where applicable>

### YYYY-MM-DD — Created
- Initial primary: <phrase>
- Initial difficulty: <classification>

---

## Iteration check-ins (if user provided stats)

### Day 7 (YYYY-MM-DD)
- Impressions: __ · CTR: __% · Orders: __
- Verdict: <on-track / under-impressions / impressions-but-no-clicks / clicks-but-no-sales>
- Action: <none / monitor / pivot / fix hero image / etc.>

### Day 14, 30, 60, 90 — same structure
```

**Update rule:** new "Change history" entry on every touch. Health score updated. Iteration check-ins added when user provides stats.

---

## File 4 — `sqr-imports/YYYY-MM-DD_L###.md`

**Purpose:** archived Search Query Report paste from Etsy Shop Stats.

**Format:**

```markdown
# SQR Import — L001 — YYYY-MM-DD

**Reporting window:** last 30 days
**Source:** Etsy Shop Stats → listing → Search Terms tab (manual paste)

---

## Parsed table

| Search query | Impressions | Clicks | Orders | CTR | CVR |
|---|---|---|---|---|---|
| cat mom svg | 247 | 8 | 1 | 3.2% | 12.5% |
| funny cat mom | 189 | 12 | 2 | 6.3% | 16.7% |

---

## Auto-analysis (filled by skill on import)

- Top performer: <query> — CTR <X>%, CVR <Y>%
- Underperforming primary: <if applicable>
- Recommended pivot: <new primary suggestion>
- New tag candidates: <queries not yet in tags>
- Tags to drop: <tags with no SQR presence>
```

**Update rule:** new file per SQR paste. Older files retained for trend analysis.

---

## Session State snapshot (non-Cowork tools only)

For users on ChatGPT / Perplexity / Gemini who can't persist files on disk. The skill outputs a snapshot at end of session; user pastes it back at the start of the next session.

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SESSION STATE — Save this. Paste at start of next session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Listings database (N total)
| ID | Title (truncated) | Primary keyword | Last edit | Status |
|---|---|---|---|---|
| L001 | ... | ... | YYYY-MM-DD | active |

## Refresh schedule highlights
- L###: due for refresh by YYYY-MM-DD (priority P1/P2)

## Notes
- <anything important to carry forward>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

When the user starts a new session and pastes this, the skill loads it as Phase 1 state — equivalent to reading the .md files in Cowork mode.

---

## Listing ID assignment

- Sequential within a single database. L001, L002, L003…
- The skill reads existing IDs from `keyword-map.md` and increments.
- IDs are permanent — never reassigned even after a listing is archived.
- For non-Cowork tools, IDs are sequential within the chat thread; if a user pastes a session-state snapshot with L047 as the highest, the next new listing = L048.

---

## What's NOT in the schema (intentional drops from v1.x)

- ❌ Shop folders (`<shop-slug>/`)
- ❌ Shop registry (`_registry.md`)
- ❌ Shop profile files (`shop-profile.md`)
- ❌ Keyword conflicts log (`_keyword-conflicts.md`)
- ❌ xlsx mirror (`Shop_Master.xlsx`)
- ❌ Template shop folder (`_TEMPLATE_shop/`)
- ❌ Cross-shop cannibalization tracking

The skill treats all listings in a single database as one logical set. Multi-shop sellers use separate chat threads if they want separation. Within a thread, the skill provides a soft keyword-reuse warning but no enforced separation.

---

## Schema versioning

If a future Etsy platform change requires a state format change (new attribute type, new field on the SERP, etc.), bump the schema version and document the migration in CHANGELOG.md.

Schema version 2.0 is NOT backwards-compatible with v1.x state files. Users migrating from v1.x must manually flatten their per-shop CSVs into the unified `keyword-map.md`.
