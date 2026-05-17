# Playbook — Search Intent Classification

**Purpose:** Etsy buyers don't all search the same way. The same listing optimized for one intent will fail for another. Classify the primary keyword's intent, then frame the listing accordingly.

**Where it runs:** Phase 3E (during keyword research). Output influences title, hero image brief, description block 1, Pinterest framing.

---

## The four intents

### 1. Browse / Inspiration intent
**Pattern:** vague, exploratory queries. The buyer doesn't know exactly what they want yet.

Examples:
- "svg ideas"
- "cat mom designs"
- "cute halloween clipart"
- "wedding decor inspiration"
- "boho ideas"

**Buyer mindset:** scrolling, comparing, gathering inspiration. Will favorite multiple listings, not buy yet.

**How to frame the listing:**
- Title: lead with variety / style descriptor, less specific format
- Hero image: lifestyle context, multiple designs visible, dreamy
- Description first 160 chars: emphasize the range / aesthetic, not specs
- Pinterest framing: full inspiration mode ("DIY ideas to...")
- Expect lower CTR but higher favorite rate; conversion is delayed

### 2. Specific hunt intent
**Pattern:** narrow, often format-anchored queries. The buyer knows exactly what they want.

Examples:
- "cat mom svg cricut"
- "funny dog mom svg bundle"
- "boho wedding invitation pdf editable"
- "kawaii halloween png transparent"

**Buyer mindset:** ready to buy. Looking for the right product spec.

**How to frame the listing:**
- Title: exact-match phrasing, lead with the most-searched specific phrase
- Hero image: clear demonstration of the product specs (e.g., the actual designs grid)
- Description first 160 chars: lead with format + quantity + key spec ("Instantly downloadable cat mom SVG bundle — 20 designs ready for Cricut. SVG + PNG + EPS included.")
- Pinterest framing: still inspirational but with explicit format mention
- Expect higher CTR than browse, faster conversion

### 3. Gifting intent
**Pattern:** recipient-anchored queries. The buyer is looking for something to give, not to use.

Examples:
- "gift for cat mom"
- "best mother's day svg"
- "birthday gift for teacher"
- "wedding gift for couple"

**Buyer mindset:** time-pressured, occasion-driven, often less price-sensitive but more emotion-sensitive. Needs to know the gift will "land".

**How to frame the listing:**
- Title: lead with recipient + occasion, not the format
- Hero image: gift context — wrapped item, finished product in someone's hands, lifestyle reaction
- Description first 160 chars: emphasize "perfect gift for [recipient]" + emotional payoff
- Pinterest framing: gift-guide style ("unique gift ideas for...")
- Always include the gift occasion (Mother's Day, birthday, etc.) explicitly in tags + description if relevant

### 4. Trend / current intent
**Pattern:** time-anchored queries. The buyer is acting on a current trend or season.

Examples:
- "trending svg 2026"
- "viral cat mom svg"
- "new halloween designs"
- "summer 2026 wedding trend"

**Buyer mindset:** wants the "now" thing. Will not be interested next quarter.

**How to frame the listing:**
- Title: include the year, season, or trend descriptor
- Hero image: visibly current (colors, styling matching this year's aesthetic)
- Description first 160 chars: emphasize freshness / recency
- Pinterest framing: trend-of-the-moment ("2026 trending ideas for...")
- These listings have shorter shelf life — schedule refresh more aggressively (60-day cadence not 90)

---

## Classification algorithm

Given a primary keyword, assign intent by feature detection:

| Feature in query | Intent |
|---|---|
| Contains "ideas", "inspiration", or no format word | Browse |
| Contains specific format (svg, png, pdf, cricut, etc.) + product type | Specific hunt |
| Contains "for [recipient]" or "gift" or occasion (mother's day, birthday, etc.) | Gifting |
| Contains year, "trending", "new", season, or "viral" | Trend |
| Ambiguous (no clear signal) | Default to Specific hunt (it's the most common Etsy intent) |

Multi-intent queries (e.g., "halloween gift for cat mom svg") get the highest-priority intent flag:
- Gifting > Trend > Specific hunt > Browse

If gifting words are present, gifting wins — the "gift" framing is the most distinctive.

---

## How to use the classification

After Phase 3 keyword research, output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEARCH INTENT CLASSIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Primary keyword:  <phrase>
Detected intent:  [Browse / Specific hunt / Gifting / Trend]
Framing rule:     <pulled from this playbook for the matched intent>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then thread the framing rule through:
- Title formula
- Hero image brief (in IMAGE BRIEF section of output)
- Description Block 1 (the hook — first 160 chars)
- Pinterest pin title

---

## Common mistakes this playbook prevents

1. **Optimizing a gifting query like a specific-hunt query.** "Gift for cat mom" optimized as "Cat Mom SVG Bundle Cricut" loses the gifting buyer entirely. They wanted recipient framing, not format specs.
2. **Forcing format words on browse queries.** Adding "svg cricut" to "cat mom ideas" reduces the browse-buyer's interest — they're not at the format-decision stage yet.
3. **Ignoring trend queries' short shelf life.** A listing primary'd on "trending 2026 cat svg" needs scheduled refresh at 60 days, not 90. By Q4 the trend has shifted; by next year the keyword is dead.

---

## Edge case: what if your product fits one intent but you want to capture another?

You can dual-target by:
- Using the primary intent's framing for title + Phase 1 SEO surfaces
- Using a SECONDARY tag set to capture the other intent
- For gifting overlap: add 2–3 gifting-intent tags ("cat mom gift", "gift for cat mama") on a specific-hunt-framed listing

But don't try to capture all 4 intents in one listing — the framing dilutes and CTR suffers. Better: create separate listings for materially different intent angles (subject to cannibalization check).
