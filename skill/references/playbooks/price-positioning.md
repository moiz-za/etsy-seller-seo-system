# Playbook — Price Positioning

**Purpose:** Etsy ranks listings partly by predicted purchase likelihood, which is heavily influenced by price relative to comparable competitors. SEO alone cannot overcome a price out of the competitive range.

**Where it runs:** MODE 8 (competitor study) extracts top-3 prices automatically. This playbook formalizes how to use that data.

---

## The principle

If the SERP for your target keyword has top 3 listings at $5, $7, $9, your $20 listing will not rank — Etsy's algorithm reads "buyers here pay $5–$9" and pushes you down regardless of how well-optimized your other surfaces are.

The reverse is also true: a $1 listing in a category where buyers expect $10+ signals low quality and depresses CTR + CVR.

---

## How to position price

### Step 1 — Establish the SERP price range

From MODE 8 output (or a manual check):
- Capture prices of top 10 organic listings (skip ads)
- Compute: min, median, max
- Note distribution shape (tight cluster vs wide spread)

### Step 2 — Identify your target zone

| Goal | Target zone within SERP range |
|---|---|
| Maximize traffic, low margin | At or below 25th percentile of top 10 |
| Balanced traffic + margin | 25th–50th percentile (sweet spot for most shops) |
| Premium positioning | 50th–75th percentile + strong quality signals (lifestyle photos, video, reviews) |
| Avoid: bottom 10% | Suggests low quality, depresses CTR |
| Avoid: top 10% | Suggests overpriced; ranking suffers |

### Step 3 — Sanity-check against shop average

Use `<shop>/shop-profile.md` "Average shop price". If the listing's price is significantly off your shop's normal range:
- Either the listing is positioned wrong for your shop's brand
- Or your shop is positioning inconsistently across listings (creates buyer confusion)

### Step 4 — Account for value perception

Variables that move the credible price range UP for the same product:
- Bundle quantity (50 designs vs 10 designs)
- Commercial use included (vs personal-use-only)
- File format breadth (SVG + PNG + EPS + DXF vs just SVG)
- Premium style positioning (boutique, designer, artisan)
- Star Seller badge

Variables that move it DOWN:
- Generic style (mass-market clipart aesthetic)
- Limited formats
- No commercial use
- New shop with few reviews

---

## Display block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRICE POSITIONING — L###
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your current price:     $X.XX
Shop average:           $Y.YY

SERP TOP 10 PRICE RANGE (target keyword "<phrase>"):
  Min:                  $A.AA
  25th percentile:      $B.BB
  Median:               $C.CC
  75th percentile:      $D.DD
  Max:                  $E.EE
  Distribution shape:   [Tight cluster ±$X / Wide spread $Y range]

YOUR PRICE POSITION:    [Below floor / Below median / At median / Above median / Above ceiling]

VERDICT:                [Competitive / Slightly off / Significantly mispriced]

RECOMMENDED ACTION:
  [No change needed / Adjust to $X.XX–$Y.YY range / Investigate value perception gap]
  
RATIONALE:              <one-paragraph reasoning>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Rules

1. **Never just "match the lowest".** Match the median if you have no quality differentiation; price slightly above only if you have visible differentiation (Star Seller, more designs, better reviews).
2. **Don't change price more than once per 30 days.** Price changes disrupt ranking; constant changes signal instability and Etsy's algorithm reads it as suspicious activity.
3. **Test up before testing down.** If your goal is more margin, test a 10% price increase first — if CTR holds, you've found free money. Test down only if your CTR is already weak.
4. **Shipping in price matters (physical only).** Etsy's algorithm reads (price + shipping) for US shipping >$6. A $5 item with $7 shipping ranks worse than a $10 item with $2 shipping. Always include shipping in the total for SERP comparison.
5. **Sale prices distort SERPs.** When you see a SERP with many "25% off" listings, the displayed prices are temporary. Use the regular price for analysis. Your listing should be priced to its regular price, not a permanent sale price (which Etsy detects and dismisses).

---

## When to ignore price-positioning advice

- **You're testing a premium brand strategy intentionally.** A $40 listing in a $5–$15 SERP can win if you have lifestyle photography that signals luxury and a clear quality differentiator. But understand: you're sacrificing search-volume traffic for high-margin sales. This is a brand bet, not an SEO bet.
- **Your conversion rate proves the price is right.** If your CVR is already 5%+ at the current price, the market is validating you — don't second-guess.
- **You're capacity-constrained (physical products).** Higher prices can be the right call when you can't fulfill more orders. Slower demand at higher margin > burnout.
