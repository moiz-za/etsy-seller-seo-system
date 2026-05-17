# Playbook — Conversion Floor

**Purpose:** Etsy actively suppresses listings whose conversion rate falls below ~0.5% (impressions-to-orders ratio). This isn't an SEO problem — it's a quality-signal problem. No amount of keyword optimization fixes it.

**Where it runs:** MODE 4 (shop audit) and MODE 6 (iteration check-in) flag this. This playbook diagnoses the cause and prescribes the action layer.

---

## Why the conversion floor exists

Etsy's algorithm uses predicted purchase score to rank. A listing that:
- Gets impressions
- Gets clicks
- But never converts

is read by the algorithm as: "buyers are finding this but it's not what they want." The fix isn't more impressions — Etsy is intentionally cutting your impressions to redirect them to listings that DO convert.

Below ~0.5% CVR, this suppression activates. Above ~1.5%, it disengages. Between 0.5% and 1.5% is the "neutral" band — neither boosted nor suppressed.

---

## Diagnosis algorithm

When CVR < 0.5% is detected:

### Step 1 — Verify it's a real signal, not small-sample noise

CVR = orders / clicks. With low click counts, CVR is statistically unstable.
- Minimum clicks for meaningful CVR: 50 over the reporting window
- < 50 clicks: too small to draw conclusions. Wait until more clicks accumulate before acting.

### Step 2 — Identify the layer

| Pattern | Likely cause | Action layer |
|---|---|---|
| Low CVR + high CTR | Mockup over-promises; description disappoints | Description rewrite (specifics, expectations); photo audit |
| Low CVR + low CTR | Both layers weak; comprehensive problem | MODE 1 full rewrite + hero image rewrite |
| Low CVR + price >median of SERP | Price-value mismatch | See price-positioning.md |
| Low CVR + < 5 reviews | Trust deficit (early shop) | Time + organic review accumulation |
| Low CVR + recent rating drop | New negatives are killing buyer confidence | Address root cause of negatives first |
| Low CVR + high favorite rate | Buyers want it but won't commit at this price | Price test (down 10–20%) |
| Low CVR + low favorite rate | Buyers don't want it after clicking | Mockup or description disconnect; major rework |

### Step 3 — Specific causes to audit

For LOW CVR, audit in this order:

1. **Photos vs description match.** Open the listing and ask: do the photos and description tell the same story? Common mismatch: photos show 20 designs but description says 12.
2. **Price vs SERP context.** Run a quick MODE 8 lite — what are similar listings priced at? If you're 20%+ above median, that's likely it.
3. **Reviews displayed.** Even good reviews can hurt if displayed reviews mention something that contradicts the listing (e.g., "Worked great on Cricut once I converted the file"). Buyer reads: "needs file conversion"). Audit displayed reviews.
4. **Description specifics.** Does the description clearly state: number of designs, exact formats, resolution, commercial use status, what's NOT included? Vagueness creates abandonment.
5. **Hero image accuracy.** Is the hero image showing a state of the product the buyer cannot recreate themselves easily? (e.g., professional studio lighting on a mockup the buyer can't replicate). Adjust to lifestyle-realistic mockups.
6. **Variant complexity.** If the listing has 5 size variants, 3 color variants, and 2 material variants — buyers freeze. Reduce variant count.

---

## Display block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONVERSION FLOOR ALERT — L###
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current CVR:              [X.X]% (over [N] clicks in last [window])
Floor threshold:          0.5%
Status:                   [BELOW FLOOR — active suppression / IN NEUTRAL BAND / ABOVE — boosted]

Sample size validity:     [Statistically meaningful / Sample too small (need ≥50 clicks)]

DIAGNOSIS:                [pattern matched from algorithm above]
ROOT CAUSE HYPOTHESIS:    <one-sentence>

WHY THIS IS NOT AN SEO PROBLEM:
  More tags / better keywords / refreshed title will not fix this.
  Etsy is intentionally throttling impressions because buyers click but don't buy.

ACTION LAYER:             [Photos / Description / Price / Reviews / Variants]
SPECIFIC ACTION:          <concrete, actionable change>
RE-CHECK AT:              [day count after action — typically 14 days]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Rules

1. **Do not run MODE 1 (full SEO rewrite) on a conversion-floor listing.** It won't help and wastes time. Fix the conversion layer first.
2. **Don't keep changing things weekly.** Change one variable, wait 14 days minimum, measure, then iterate. Constant changes contaminate the signal.
3. **If the listing is below 0.3% CVR over 200+ clicks: pause it.** Etsy is actively suppressing; the listing is harming your shop's overall score. Better to deactivate and rework than leave it live as a drag.
4. **For new listings with no purchase history: this playbook doesn't apply yet.** Conversion floor only triggers after meaningful click volume.

---

## When conversion floor problems are NOT solvable

Some products are just hard to convert on Etsy:
- Highly customized items where buyers want extensive consultation (Etsy isn't a great venue for high-touch sales)
- Premium-priced items in price-sensitive categories
- Items that compete on platform features Etsy doesn't have (e.g., extensive size guides for apparel — Amazon does this better)

If you've tried the action layer and CVR hasn't moved after 3 cycles (90 days), this product may simply be wrong for Etsy. The honest answer might be: discontinue and reallocate to better-converting products.
