# Playbook — Action Layer Pointers

**Purpose:** when the skill diagnoses a problem that is NOT SEO, give the user concrete next steps with real data — not just "this isn't SEO scope, sorry."

**Why this exists:** the biggest reason Etsy advice fails struggling sellers is that everyone tells them "fix your SEO" no matter what the actual problem is. They waste 3 months. This skill refuses to do that, but goes further — when the problem ISN'T SEO, it routes the user to the actual action layer that matters, with specific recommendations from data already gathered (competitor SERP scrape, price comparison, etc.).

**Where it triggers:** Phase 8 of every REWRITE or CREATE run, when the diagnosis is out of SEO scope.

---

## Diagnosis-to-action mapping

### CTR problem (impressions exist, clicks < 1%)

Output to user:

```
DIAGNOSIS: CTR PROBLEM (impressions but no clicks)

This isn't an SEO problem. Rewriting your title or tags won't fix this. 
What's actually broken is one or more of:

1. HERO IMAGE (most common)
   I just scraped the top 3 organic listings for your target keyword. Their hero patterns:
   - Top #1: <observed style — e.g., "lifestyle mockup on white desk, single product centered, soft natural light">
   - Top #2: <observed style — e.g., "hand-held product, warm tones, text overlay">
   - Top #3: <observed style — e.g., "flat-lay with niche-appropriate props, color palette matching the aesthetic">
   
   Your current hero (inferred): <best guess from listing description or "unknown — please screenshot for review">
   
   Concrete next steps:
   - Match the dominant pattern (lifestyle vs flat-lay vs hand-held)
   - Add text overlay with primary keyword if competitors use one
   - Use the niche's color palette (warm/cool/muted) — copying SERP winners is fine
   
   Free tools to make hero images:
   - Canva (templates + drag/drop) — canva.com
   - Placeit (product mockups, ~$8/mo or free trial) — placeit.net
   - Photopea (free Photoshop alternative in browser) — photopea.com

2. TITLE CLARITY (mobile preview test)
   Your title's first 40 chars: "[first 40 of current title]"
   This is what buyers see on mobile. Does it clearly say what the product is + the key feature?
   If yes → CTR problem is in the image, not the title.
   If no → rewrite the title to lead with [product noun] + [key benefit].

3. PRICE OUTLIER
   Your price: $X.XX
   SERP top-10 price range: $A.AA – $E.EE (median $C.CC)
   
   - If you're above the 75th percentile without visible quality signals (Star Seller, lifestyle photos, video) → CTR drag.
     Test lowering by 15-25% for 14 days. Measure CTR change.
   - If you're below the 10th percentile → buyers may read as "cheap quality."
     Test raising 10-15% for 14 days.

4. STAR SELLER BADGE (minor but real)
   If competitors have the badge and you don't, expect 3-8% CTR drag.
   Path to Star Seller status: response rate 95%+ within 24h, on-time dispatch 95%+ 
   (digital = automatic), review rating 4.8+, $300+ sales or 5+ orders in last 3 months.

PRIORITY ORDER for your fix:
1. Hero image (biggest lever, takes 1-2 hours)
2. Price (free to test, takes 14 days to confirm)
3. Title clarity (only if first 40 chars are genuinely unclear)
4. Star Seller path (3-month build)

I can still rewrite your tags if you want. Expect marginal impact (~5-10%) 
until the hero image is fixed.
```

---

### Conversion problem (clicks but no sales — CR < 0.5%)

Output:

```
DIAGNOSIS: CONVERSION FLOOR PROBLEM (CR < 0.5%)

Etsy actively suppresses listings whose conversion rate falls below ~0.5%. 
This isn't an SEO problem. Rewriting tags won't help. What's broken:

1. PHOTOS AFTER THE HERO
   Etsy listings get up to 20 photos. Top performers use 8-12 minimum.
   Your hero brought buyers in; the rest must close the sale.
   
   Audit your photos:
   - Photo 2: All designs displayed clearly (digital) or second angle (physical)
   - Photo 3: Close-up of best detail
   - Photo 4: Lifestyle mockup of finished result
   - Photo 5: What's Included infographic (digital) or scale reference (physical)
   - Photo 6+: Compatibility / variants / seasonal applications

2. DESCRIPTION VS PHOTOS MISMATCH
   Buyers compare your description against what they see. If photos show 20 designs 
   but description says 12, abandonment is guaranteed.
   
   Verify: every number/specification in your description matches the photos exactly.

3. PRICE-VALUE MISMATCH
   Same data as the CTR problem analysis above. If buyers click but don't buy, 
   your perceived value at your price point is too low.
   
   Test:
   - Add more "what's included" specifics in the description
   - Add a video (5–15 sec) showing the finished result
   - Bundle quantity matters: 20 designs at $12 reads as better value than 5 designs at $8

4. REVIEWS DEFICIT
   Listings under 5 reviews convert at half the rate of established listings.
   This is the hardest fix because it requires time + sales.
   
   Concrete near-term moves:
   - Respond professionally to ALL existing reviews (future buyers read responses)
   - Make sure file delivery / shipping is perfect to earn the next 5 reviews
   - Do NOT incentivize reviews — Etsy policy violation, ban risk

5. SHIPPING / DELIVERY FRICTION (physical only)
   US shipping > $6 actively reduces search visibility AND conversion.
   Bake shipping into the item price + offer free shipping.

WARNING: 
If you stay below 0.5% CR for 200+ clicks, Etsy suppresses the listing harder. 
Consider PAUSING the listing while you fix the underlying issue. Pausing 
preserves your shop quality score; leaving a broken listing live actively damages it.

I will NOT run an SEO rewrite on a conversion-floor listing. Fix conversion first. 
Re-run me at day 30 after the fix to see if SEO ALSO needs work.
```

---

### Wrong-price problem (detected via SERP price analysis)

Output:

```
DIAGNOSIS: PRICE POSITIONING (your price is significantly off the SERP median)

Your price: $X.XX
SERP top-10 distribution: min $A.AA · median $C.CC · max $E.EE · 25th-75th: $B.BB–$D.DD

You're [above/below] the credible competitive zone.

This affects:
- CTR (price shows on the SERP result card; outliers get scrolled past)
- Ranking (Etsy uses price as part of predicted purchase score)
- Conversion (mismatched price vs perceived value)

CONCRETE RECOMMENDATION:
- Target zone: $B.BB – $C.CC (25th to median percentile of SERP)
- Test a price change of $X.XX → $Y.YY for 14 days
- Don't change price more than once per 30 days — destabilizes ranking
- Don't permanently "sale price" — Etsy detects and dismisses

EXCEPTION: If your product has visible quality differentiation (Star Seller badge, 
lifestyle photos vs product-on-white, more designs than competitors, commercial use 
included) — premium pricing above median is defensible. Without visible signals → 
match the median.
```

---

### Wrong-niche-platform problem (detected via Phase 4C Very-High difficulty + generic product)

→ Route to `platform-fit-check.md` playbook.

---

### Tag-rejection silent failure (detected from existing listing audit)

Output:

```
DIAGNOSIS: SILENT TAG REJECTION (the #1 cause of "I published but nothing happened")

Your existing listing has [N] tags over the 20-character limit (INCLUDING spaces):
- "[tag 1]" = [X] chars (Etsy silently dropped this from your index)
- "[tag 2]" = [X] chars
- ...

These tags are INVISIBLE to Etsy's search. Your listing has been running with 
fewer indexed tags than you think. No warning was ever shown — Etsy just drops them.

THIS IS THE FIX. Rewriting these tags within the 20-char limit will surface the 
listing for queries it should already have been ranking for.

I'm rewriting the tags now. The rewrite includes 13 tags, each verified ≤20 chars, 
each evidence-traced to actual buyer queries. Within 24–72 hours of you saving 
this in Etsy, you should see impression recovery on these queries.
```

---

## How the skill picks which pointer to display

In Phase 8 of every REWRITE / CREATE:

1. If user provided stats → use them to classify (CTR / conversion / SEO / wrong-niche).
2. If user did not provide stats → use heuristics:
   - Multiple silent-rejection tags found → tag-rejection routing
   - Phase 4 difficulty = Very High AND generic product → platform-fit-check
   - Otherwise → no out-of-scope warning; SEO rewrite is appropriate
3. Display the matching pointer block AFTER the listing output, not before. The user still gets the rewrite; the pointer is supplementary.

---

## Tone rules

- Honest, not blunt. The user is often struggling and demoralized.
- Specific, not generic. Use data already gathered (SERP scrape, price scan).
- Always include "I can still help with the SEO part" — don't leave them stranded.
- Free-tool recommendations are concrete; no upsells, no affiliate links.
- Never moralize ("you should have done X earlier"). Just route to the fix.
