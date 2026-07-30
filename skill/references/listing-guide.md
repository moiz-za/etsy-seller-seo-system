# Listing Structure Guide — Universal

## Table of Contents
1. [Title Rules](#1-title-rules)
2. [Tag Rules](#2-tag-rules)
3. [Attributes — Keyword Real Estate](#3-attributes--keyword-real-estate)
4. [Description Rules](#4-description-rules)
5. [Category Selection](#5-category-selection)
6. [Photos, Video & Image Alt Text](#6-photos-video--image-alt-text)
7. [Delivery Setup](#7-delivery-setup)
8. [Indexing Spread Check](#8-indexing-spread-check)
9. [MODE 1 — Rewrite Process](#9-mode-1--rewrite-process)
10. [MODE 2 — New Listing Process](#10-mode-2--new-listing-process)

---

## 1. Title Rules

### Hard Limits & Prohibitions
- **STRICT WORD COUNT GUARDRAIL: MUST be 6–12 words. ABSOLUTE MAXIMUM: 14 words.** Any title with 15 or more words is INVALID and MUST be rejected and rewritten immediately.
- **Maximum 140 characters** — spaces count.
- **Primary keyword in first 40 characters** — critical for mobile display and search algorithm indexing.
- **PROHIBITED SUBJECTIVE WORDS STOPLIST (ZERO ALLOWED):** Do NOT use filler adjectives or subjective fluff: `cute`, `adorable`, `beautiful`, `perfect`, `stunning`, `amazing`, `incredible`, `pretty`, `awesome`, `gorgeous`, `lovely`, `sweet`, `unique`, `best`, `top`, `wonderful`, `charming`. Subjective fluff wastes character space, dilutes search relevance, and triggers Etsy promotional filters.
- No trademarked names, brand names, or celebrity names.
- No sales/shipping/price information — Etsy badges these automatically.
- No promotional language: "on sale", "free", "best seller".

### Mandatory Formula
```
[Primary Keyword] [Style/Theme Descriptor] | [Format or Use-Case]
```

### Title Verification (MUST display in output)
```
[First 40 chars: "Primary keyword appears here..."] ✅
[Word count: X words (MUST be 6–12, MAX 14)] ✅
[Char count: X / 140] ✅
[Subjective words check: 0 subjective words used] ✅
```

### Title Examples by Product Type

**Digital SVG/clipart bundle:**
`[Niche] SVG Bundle | [Theme] Clipart [File Formats]`
e.g. `Funny Cat Mom SVG Bundle | Cricut Clipart PNG EPS`

**Printable/digital download:**
`[Niche] [Product Name] Printable | [Size/Format] Instant Download`
e.g. `Boho Wedding Invitation Printable | A5 Editable PDF`

**Canva template:**
`[Niche] Canva Template | [Use Case] Editable Design`
e.g. `Minimalist Resume Canva Template | Modern Editable CV`

**Physical product:**
`[Product Noun] [Material] [Key Feature] | [Occasion or Style]`
e.g. `Personalized Leather Bookmark | Custom Name Reader Gift`

### 2026 NLP Note
Etsy's algorithm understands meaning and intent — not just keyword matching. Write naturally. A title that reads well to a human ranks better than a keyword chain. "Funny Cat Mom SVG Bundle" ranks better than "Cat Mom SVG Cat Clipart Cat Mom Bundle Cat SVG Files."

---

## 2. Tag Rules

### Platform Hard Limits
- **13 tags maximum** — use every slot
- **Each tag ≤ 20 characters INCLUDING spaces** — tags over 20 are silently rejected with no error
- Tags must be unique — no two identical tags
- **Phrase Overlap Limit:** No exact 2+ word phrase may repeat across more than 2 tags (maximum 2 tags may share a 2-word phrase cluster).
- Letters, numbers, spaces, hyphens, apostrophes only
- No foreign language tags — Etsy auto-translates
- Do not repeat exact phrases from categories or attributes

### ⛔ MANDATORY 3-CHECK VERIFICATION BEFORE EVERY TAG OUTPUT

Every tag must pass all three checks. Reject and rewrite any tag that fails any one of them.

**Check 1 — Character count (≤20 including spaces):**
```
Count: every letter + every space = total
≤ 20 → PASS → output with count: funny cat mom svg (17 ✅)
> 20 → FAIL → rewrite shorter → recount → verify → then output
```

**Check 2 — Evidence trace (every tag has a verified source):**
Each tag must trace back to one of:
- Etsy autocomplete suggestion (from Phase 3A)
- Common 2–3 word phrase across SERP top 10 (from Phase 3B)
- Buyer-intent expansion from Google or related-searches strip (from Phase 3D / 3A fallback)

If a tag has no source in the Evidence Log, it's a guess — reject and replace.

**Check 3 — Phrase coherence (would a buyer actually type this?):**
Read each tag aloud. Ask: "Would someone type this, verbatim, into Etsy's search bar?"
- ✅ `funny cat mom svg` — yes, real search phrase
- ❌ `shirt decal print` — three SEO words mashed together, no buyer types this
- ❌ `cute svg digital` — vague keyword stack, no real intent
- ✅ `cricut cut file` — yes, real buyer phrase
- ✅ `cat lover gift` — yes, gift-search pattern

Reject and rewrite any tag that fails the say-it-aloud test.

### Win Small Searches, Not Lose Big Ones
"Cat" competes with millions of listings. "Funny cat mom cricut" competes with hundreds. A tag ranking #3 in 200 results drives more real traffic than one ranking #47,000 in 50 million. Every tag must be specific enough to win its search — not broad enough to drown in it. Always choose the precise long-tail phrase over the broad single word.

**Concrete illustration — same product, two strategies:**

| Tag candidate | Approx. competing listings | Realistic ranking outcome | Real traffic |
|---|---|---|---|
| `mug` | ~50,000,000 | Ranked #47,000+ | Zero impressions |
| `coffee mug` | ~3,000,000 | Ranked #6,000+ | Trickle |
| `cowboy mug` | ~25,000 | Ranked #200–500 | Some, intermittent |
| `cowboy coffee mug` | ~200 | Ranked top 5 | Steady, qualified buyers |
| `western kitchen gift` | ~1,500 | Ranked top 20 | Captures gifting intent |

The lesson: a tag's value is its rank × searcher volume, not its raw search volume. A "mug" tag captures 0% of 50M searches because it's invisible. A "cowboy coffee mug" tag captures 30%+ of 200 searches because it's near the top. Long-tail wins because it can actually rank.

### How to Count Characters
```
Every letter counts as 1.
Every space counts as 1.
No exceptions.

Example:
"funny cat mom svg"
f(1)u(2)n(3)n(4)y(5) (6)c(7)a(8)t(9) (10)m(11)o(12)m(13) (14)s(15)v(16)g(17)
= 17 chars ✅

"funny cat mom clipart"
= 21 chars ❌ REJECTED — rewrite required
```

### Safe Tag Length Guide
- 2-word tags → 8–16 chars → safe zone
- 3-word tags → 14–20 chars → verify every one
- 4-word tags → almost always over 20 → avoid unless all words are very short

### Splitting Long Phrases
When a target phrase exceeds 20 characters, split it across two tag slots:
- "cat mom cricut design" (21) → `cat mom cricut` (14 ✅) + `mom svg design` (14 ✅)
- "nurse appreciation gift" (23) → `nurse appreciation` (18 ✅) + `nurse gift idea` (15 ✅)
- "boho wedding invitation" (23) → `boho wedding` (12 ✅) + `wedding invitation` (18 ✅)

### Word-Repetition Rule (CORRECTED)

The old "no word repeated across tags" rule was too strict and worked against indexing reinforcement. The actual rule:

**OK — primary niche noun MAY repeat in 2–3 tags (cross-surface reinforcement helps ranking):**
- `cat mom svg` + `cat mama png` + `cat lover gift` — the word "cat" appearing 3× is fine and actively helps the algorithm understand the listing's primary noun cluster
- This is part of how the indexing spread check works

**NOT OK — exact 2+ word phrase repeated (wasteful, no incremental signal):**
- `cat mom svg` + `cat mom png` + `cat mom gift` — the phrase "cat mom" carries no new information when repeated this way
- Each of those slots could cover a different buyer search angle

**Practical rule:**
- Pick your primary niche noun (e.g. "cat"). Let it appear in 2–3 tags max, each time inside a *different* phrase.
- Every tag must still cover a distinct buyer search angle.
- After writing all 13 tags, list every unique word used; if the same word appears in 4+ tags, prune.

### Tag Slot Blueprint (Universal — adapt to actual evidence)

| Slot | Angle | Source must be |
|---|---|---|
| 1 | Core niche + product noun | Top autocomplete suggestion |
| 2 | Design theme variant | Autocomplete or SERP common phrase |
| 3 | Style descriptor (matches Style attribute language) | Autocomplete |
| 4 | Software / format 1 (only if user confirmed) | Autocomplete or product context |
| 5 | Software / format 2 (only if user confirmed) | Autocomplete or product context |
| 6 | File format / delivery focus | Autocomplete |
| 7 | Gifting occasion | Autocomplete or Google buyer-intent |
| 8 | Recipient / persona | Autocomplete or Google buyer-intent |
| 9 | Use-case / product type buyers want to make | SERP top 10 common phrase |
| 10 | Seasonal (only if within 6 weeks) | Seasonal autocomplete |
| 11 | Niche sub-category | Autocomplete or SERP |
| 12 | Complementary product type | Autocomplete |
| 13 | Long-tail buyer intent (4 words, very specific) | Autocomplete deep-suggest or SERP |

*Slot purposes are illustrative — always adapt to the actual evidence and niche. Never invent a tag to fill a slot if the evidence pool doesn't support it; better to skip the slot and reallocate to a different evidence-backed phrase.*

### Seasonal Tag Rules
- Add seasonal/holiday tags 4–6 weeks before the event
- Remove 1–2 weeks after the holiday ends
- Only replace tags NOT currently driving traffic — check Shop Stats first
- If all tags perform, add seasonal keywords to description instead

### Final Verification Before Output
1. All 13 tags listed
2. Every tag has: char count ≤20 ✓ · evidence source noted ✓ · phrase coherence confirmed ✓
3. List every unique word used across all 13 tags; primary niche noun may appear in 2–3 tags max; no exact 2+ word phrase repeated
4. Indexing spread check: primary cluster appears in ≥3 of the 13 tags

---

## 3. Attributes — Keyword Real Estate

Attributes are not metadata. They are a search surface — Etsy indexes attribute values as keywords, and many buyers filter by them. Each attribute filled correctly is a free keyword. Each attribute filled poorly (or skipped) is lost traffic.

**Rule of thumb:** the attribute value should be a word that matches actual buyer search language, not whatever generic descriptor sounds correct. If buyers search "kawaii cat mom svg", set Style = Kawaii — not Cute, not Modern.

| Attribute | Treat as keyword surface | How to choose value |
|---|---|---|
| Primary Color | Yes — buyers filter and search by color | Pick the value that matches the most dominant color buyers would describe; align with autocomplete if a color appears in suggestions |
| Secondary Color | Yes | Second strongest filterable color |
| Material | Yes (physical) / blank or "Digital Download" (digital) | Use the exact material buyers search ("leather", "stainless steel", "linen") not made-up trade terms |
| Style | **Critical keyword surface** | Use the style word buyers actually search — Boho, Funny, Minimalist, Vintage, Kawaii, Gothic, Rustic, Modern. This MUST match a phrase used in the Phase 3 evidence pool. |
| Occasion | **Critical keyword surface** | Birthday, Wedding, Christmas, Mother's Day, Everyday, Graduation. Pick the one(s) that appear in autocomplete / buyer-intent phrases. |
| Recipient | **Critical keyword surface** | Her, Him, Friend, Mom, Teacher, Pet Lover, Couple, Kids. Pick the one matching buyer-intent phrases from Phase 3. |
| File Type | Yes (digital) | List formats exactly as the user provided — SVG, PNG, PDF, EPS, DXF, Canva. Do not invent formats. |
| Size/Dimensions | Yes | Physical dimensions or digital canvas dimensions if applicable |
| Pattern | Yes (where applicable) | Fabric, paper, or wallpaper pattern type |

**Indexing spread implication:** at least ONE attribute value should literally include or echo a word from the primary keyword cluster. Example: primary keyword is "funny cat mom svg" → Style = "Funny" and Recipient = "Pet Lover" both reinforce the cluster.

Do NOT add a standalone tag for anything already covered by an attribute — that's a wasted tag slot.

---

## 4. Description Rules

### Critical SEO Zones
- **First 40 characters:** primary keyword must appear here — strongest Etsy + Google SEO signal
- **First 160 characters:** meta description shown in Etsy search AND Google — must read as a complete product pitch
- **NLP indexing:** Etsy reads descriptions for meaning and context — natural language beats keyword chains
- **ChatGPT Instant Checkout:** descriptions are also parsed by AI for product matching — clear, specific content converts better
- **Length:** 250–700 words. No stuffing anywhere.

### Verification Display
```
[Meta zone — first 160 chars: "Instantly downloadable [product]...
...for [who it's for]. [Key benefit]. [File formats / what's included]."] ✅
```

### 8-Block Structure

**Block 1 — Hook (1–2 sentences)**
Primary keyword in first 40 characters. First 160 characters = complete product pitch.
Write as if you're describing the product to a person who has 5 seconds to decide.

**Hook template depends on search intent** (classified in Phase 3E — see `playbooks/search-intent-classification.md`):

| Intent | What the first 160 chars should lead with | Template |
|---|---|---|
| **Specific hunt** (most common — buyer ready to purchase, knows the format) | Primary keyword + product clarity + key spec | `[Primary keyword] — [X] designs ready for [software/use]. [File formats] included. [Brief benefit].` |
| **Gifting** (buyer is shopping for someone else, time-pressured) | Recipient + occasion + product + emotional payoff | `Perfect [occasion] gift for the [recipient] in your life — [primary keyword]. [Brief specs to reassure].` |
| **Browse** (buyer is exploring, no specific format chosen yet) | Variety + style + scope | `[Primary keyword] collection — [N] designs across [style 1], [style 2], and [style 3]. [Brief use cases].` |
| **Trend** (buyer wants something current/viral) | Time anchor + freshness signal + niche fit | `New for [year] — [primary keyword]. [Trend or aesthetic reference]. [Brief specs].` |

**Critical regardless of intent:** primary keyword must appear in first 40 characters. "Vibe first, specs last" is a common bit of advice that's only correct for gifting intent — for specific-hunt intent (the most common), spec-first wins.

**Examples:**

✅ Specific hunt: `Funny cat mom SVG bundle — 20 designs ready for Cricut. SVG + PNG + EPS included. Commercial use OK.`
✅ Gifting: `Perfect Mother's Day gift for the cat mom in your life — funny cat mom SVG bundle, 20 designs.`
✅ Browse: `Cat mom SVG collection — 20 designs across funny, minimal, and watercolor styles. Perfect for crafters exploring options.`
✅ Trend: `New for 2026 — viral cat mom SVG bundle. 20 designs in the trending hand-lettered aesthetic. Cricut-ready.`

❌ `Thank you for visiting my shop! I'm so excited to share this...`
❌ `This listing is for a digital download of...`
❌ `Beautiful, stunning cat mom SVG designs that will make your heart melt...` (subjective adjectives, no keyword in first 40, no clarity)

**Block 2 — Features (2–3 sentences)**
What makes this product special. Design style, theme, mood, quality. What the buyer will DO or MAKE with it.

**Block 3 — What's Included (bullet list)**
List exactly what the buyer receives — file types, quantities, sizes, resolutions.
Use the actual file formats from the product context. Do not invent formats not provided.
```
• [File type] ([quantity]) — [specs: resolution, dimensions, compatibility note]
• [File type] ([quantity]) — [specs]
• Total: [number] files / [ZIP or individual files]
```

**Block 4 — How It Works / Delivery**
State how the buyer receives the product:
- Digital instant: "After purchase, your files are instantly available to download from Etsy. No physical item is shipped."
- Digital custom: State turnaround time and what information buyer needs to provide
- Physical: Materials, dimensions, care instructions, shipping notes

**Block 5 — Compatibility (digital products only)**
What software opens or works with each file type.
Use only the formats that actually come with the product.
Omit this block entirely for physical products.

**Block 6 — Usage Rights (if applicable)**
State clearly whether commercial use is included or not.
If not mentioned by the user → do not claim it.
If commercial use IS included → specify what it covers and any limits.
Omit this block if usage rights are not relevant to the product.

**Block 7 — Personalization Instructions (if applicable)**
What information the buyer needs to put in the order note.
Be exact — vague instructions cause errors and bad reviews.
Omit entirely if the product is not personalizable.

**Block 8 — AI Disclosure (if applicable)**
Only include if the user confirms the product was AI-assisted:
`"This design was created with AI assistance and refined for quality."`
Do NOT add this if the user did not mention AI use.

**Block 9 — Closing**
`Questions? Message [SHOPNAME] — we respond within 24 hours.`

### Description Rules

| ✅ Always | ❌ Never |
|---|---|
| Primary keyword in first 40 chars | Start with "This listing is for..." |
| Natural conversational language | Copy title verbatim as first line |
| Bullet list for What's Included | Keyword stuffing or comma lists |
| State only the actual file formats provided | Invent formats not in the product |
| State delivery method clearly | Generic AI-template copy |
| [SHOPNAME] in closing | Off-platform contact details |
| Proofread before output | ALL CAPS sections |
| Clean text formatting | Emojis in description text or headers |

---

## 5. Category Selection

Always select the most specific subcategory available. The subcategory automatically includes the listing in all parent categories above it — free additional search surface. Accurate categorization is mandatory — miscategorization leads to listing removal.

**Output format:**
```
CATEGORY: [Top Level] > [Mid Level] > [Most Specific Subcategory]
```

**Common paths by product type:**
- SVG cut files: `Craft Supplies & Tools > Patterns & How To > SVG Files`
- Digital art prints: `Art & Collectibles > Prints > Digital Prints`
- Clipart bundles: `Craft Supplies & Tools > Patterns & How To > Clip Art`
- Printable planners/stationery: `Paper & Party Supplies > Paper > Stationery`
- Canva templates: `Craft Supplies & Tools > Patterns & How To > Digital Stamps`
- Physical handmade items: select the most specific product category
- Personalized physical items: select most specific product type category

Do not duplicate exact category phrases as standalone tags — categories already act as search signals.

---

## 6. Photos, Video & Image Alt Text

| Spec | Value |
|---|---|
| Maximum photos | 20 per listing (increased August 2025) |
| Minimum resolution | 2000px on shortest side |
| Recommended | 2000×2000px or 2000×1600px (5:4 ratio) |
| Hero shot | Lifestyle mockup — show product IN USE or finished result |
| Video | 5–15 seconds, autoplays on mobile — strong conversion signal |
| Hero image filename | Include primary keyword: `funny-cat-mom-svg-bundle-hero.jpg` |
| Hero image alt text | 100–150 chars including primary keyword |

**Photo strategy — adapt to product type:**

| Slot | Digital Products | Physical Products |
|---|---|---|
| 1 | Lifestyle mockup of finished result (shirt, mug, wall art) | Product in natural lifestyle context |
| 2 | All designs in the bundle displayed clearly | Second angle / lifestyle shot |
| 3 | Close-up of best individual design | Detail / texture close-up |
| 4 | Second lifestyle mockup (different product application) | Scale reference |
| 5 | What's included infographic (formats, count, compatibility) | All variations together |
| 6+ | Compatibility graphic, additional mockups, seasonal variants | Packaging, additional angles |

**Key rule for digital products:** Never show just the file — show what the buyer will MAKE with it.

**Image alt text rule (NEW):** the hero image alt text is part of the indexing spread check. It must contain the primary keyword phrase, describe the image accurately, and read naturally. Example: `Funny cat mom SVG design displayed on a white t-shirt, perfect Cricut craft project for pet lovers.`

**Pinterest Marketing Block Rule:** Pin title (≤100 chars), Board name (25–40 chars), Board description (150–300 chars), Pin description (220–232 chars, no hashtags). *Count and Adjust Instruction:* Write naturally first, then count characters and explicitly expand or trim to land within the 220–232 character target range before finalizing.

---

## 7. Delivery Setup

### Digital Products
- Listing type: "Digital download"
- Premade files → processing time: "Instant"
- Custom/made-to-order digital → state turnaround time; deliver manually via Etsy Messages
- Files over 20MB → deliver via Google Drive/Dropbox link in order message; state this in description
- Always specify in description: "No physical item is shipped"

### Physical Products
- Set accurate processing times — late dispatch is penalized in search ranking
- US shipping: keep shipping price at $6 or below — over $6 reduces search visibility (2026 algorithm)
- Free shipping improves conversion and search ranking
- Upload tracking on all orders; required for orders over $250

---

## 8. Indexing Spread Check

Etsy's NLP indexes a phrase more strongly the more times the phrase cluster appears across the listing's distinct surfaces. A keyword that lives only in the title is a half-indexed keyword.

**Cross-surface reinforcement rule** — the primary keyword cluster MUST appear in:

| Surface | Requirement |
|---|---|
| Title | Within first 40 chars |
| Tags | At least 3 of 13 tags contain a primary-cluster word (each in a different phrase) |
| Attributes | At least 1 attribute value echoes a primary-cluster word (usually Style, Occasion, or Recipient) |
| Description first 160 chars | Primary keyword appears here |
| Hero image alt text | Primary keyword appears here |

Display the spread check in the final output block. If any surface is missing the cluster, fix it before publishing.

```
INDEXING SPREAD CHECK — primary cluster "[primary keyword]"
Title (first 40 chars):     ✅
Tags (≥3 with cluster):     Tag #X, Tag #Y, Tag #Z ✅
Attributes (≥1):            [attribute name + value] ✅
Description first 160:      ✅
Hero image alt text:        ✅
```

---

## 9. MODE 1 — Rewrite Process

**Input:** Existing title + all existing tags + existing description (+ ideally Shop Stats showing impressions/clicks/orders)

### Step 1 — Extract product details from existing listing
Before running Phase 3 keyword research, read the existing description and extract:
- Product type and niche
- File formats actually included
- Commercial use status
- AI disclosure presence (flag if missing where applicable)
- Delivery method
- Target market signals

### Step 2 — Run SKILL.md Phases 1–4 (evidence-driven keyword research)

### Step 3 — Audit the existing listing
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXISTING LISTING AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Title issues:        [word count / keyword not in first 40 chars / prohibited terms]
Tag issues:          [tags over 20 chars: list them | exact 2+ word phrases repeated | empty slots | tags with no evidence backing]
Description issues:  [keyword not in first 40 chars / missing sections / stuffing / wrong formats listed]
Attribute issues:    [missing attributes | values don't match buyer language]
Diagnosis:           [SEO problem / CTR problem / conversion problem / combination]
Scope of this fix:   [what the rewrite will and will not address — see below]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 3.5 — Scope honesty before rewriting

If the diagnosis is purely CTR or conversion (impressions exist but clicks/sales don't), tell the user plainly that rewriting title/tags/description will not fix the problem. The fix is:
- **CTR problem:** stronger hero mockup, clearer product offer in first photo, more competitive price, less clutter in title.
- **Conversion problem:** more detailed mockups, more lifestyle photos, better description specificity, more/better reviews, price-vs-perceived-value alignment.

Offer to still do the SEO rewrite if useful, but flag expected marginal impact. Get user confirmation before proceeding.

### Step 4 — Extract salvageable keywords from original
Look for keywords in the original that DO appear in the new Phase 3 evidence pool — these can be kept. Discard the rest.

### Step 5 — Build new title, 13 verified tags (all three checks), full description using live research

### Step 6 — Run indexing spread check

### Step 7 — Generate Pinterest pin block

### Step 8 — Output complete block including Evidence Log, Spread Check, and Post-Publish Notes

Do NOT preserve the original structure if it violates the rules. Rewrite completely.

---

## 10. MODE 2 — New Listing Process

**Input:** User provides:
- What the product is
- File formats included (or product type for physical items)
- Any other relevant details (number of designs, style, commercial use, AI assistance)

**If critical details are missing, ask before generating:**
- "What file formats are included?"
- "Is commercial use included?"
- "Is this AI-assisted?"

### Step 1 — Run SKILL.md Phases 1–4 (evidence-driven keyword research)

### Step 2 — Clarify product details from user context

### Step 3 — Build complete title, 13 verified tags (all three checks), full description using Phase 3 evidence pool

### Step 4 — Apply only what the user provided — no invented file formats or assumed features

### Step 5 — Run indexing spread check

### Step 6 — Generate Pinterest pin block

### Step 7 — Output complete block including Evidence Log, Spread Check, and Post-Publish Notes
