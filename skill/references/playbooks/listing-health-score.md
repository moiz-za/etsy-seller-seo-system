# Playbook — Listing Health Score (0–100)

**Purpose:** assign every listing a composite 0–100 health score so the user can prioritize which to fix first.

**Where it runs:** every MODE 1/2 run computes and writes a fresh score. MODE 4 (shop audit) computes scores across all listings to find the worst.

---

## Components and weights

| Component | Max | What it measures |
|---|---|---|
| SEO surface coverage | 25 | Indexing spread + tag verification |
| Evidence quality | 20 | How well keywords trace to live evidence |
| Coherence | 15 | Does the listing read like a real product |
| CTR estimate | 15 | Hero-image / title-clarity / price signaling |
| Conversion estimate | 15 | Description / mockup quality / reviews / price |
| Compliance | 10 | IP, prohibited content, accurate claims |
| **Total** | **100** | |

---

## Scoring rubric per component

### 1. SEO surface coverage (max 25)

| Check | Points |
|---|---|
| Primary keyword in title first 40 chars | 5 |
| All 13 tags filled | 3 |
| Every tag char count ≤ 20 (verified, no silent rejections) | 4 |
| Tags pass evidence trace (every tag sources to autocomplete/SERP/expansion) | 3 |
| Tags pass phrase coherence (no SEO-word soup) | 3 |
| Primary cluster appears in ≥ 3 tags | 3 |
| Primary cluster appears in ≥ 1 attribute | 2 |
| Primary keyword in description first 160 chars | 1 |
| Hero image alt text contains primary keyword | 1 |

### 2. Evidence quality (max 20)

| Check | Points |
|---|---|
| Primary keyword from Etsy autocomplete (not training data) | 6 |
| Primary keyword appears in ≥ 3 of top 10 SERP titles | 5 |
| Primary keyword difficulty is Low-Medium or Medium (not Very High) | 4 |
| Secondary keywords (4–6) each have a source label | 3 |
| Seasonal phrase used (if holiday within 6 weeks AND niche fits) | 2 |

### 3. Coherence (max 15)

| Check | Points |
|---|---|
| Title reads naturally (not keyword chain) | 5 |
| Description first sentence is product pitch, not greeting | 3 |
| Description follows 8-block structure | 3 |
| What's Included block uses only actual file formats user confirmed | 2 |
| No "this listing is for" / "thank you for visiting" preamble | 2 |

### 4. CTR estimate (max 15)

If SQR data is available:
- CTR ≥ 3.0% → 15 points
- CTR 2.0–2.99% → 12 points
- CTR 1.5–1.99% → 9 points
- CTR 1.0–1.49% → 5 points
- CTR < 1.0% → 0 points

If SQR data is not available (new listing or no impressions yet):
- Estimate from proxies (mark with `*` to denote inferred):
  - Title clarity score (subjective, 0–5)
  - Hero image brief present and detailed (3 points)
  - Price within competitive range (per MODE 8 context, 4 points)
  - Star Seller status of shop (3 points)
- Max inferred score: 15
- Always flag as inferential in the output

### 5. Conversion estimate (max 15)

If shop-stats provide CVR for the listing:
- CVR ≥ 5% → 15 points
- CVR 3–4.99% → 12 points
- CVR 1.5–2.99% → 9 points
- CVR 0.5–1.49% → 5 points
- CVR < 0.5% → 0 points + flag as conversion-floor problem (see conversion-floor.md)

If no stats:
- Inferred proxies (mark `*`):
  - Description quality (specific vs generic, 0–5)
  - Number of photos described in image brief (3 points if ≥6, otherwise 1 point)
  - Video brief included (3 points)
  - Commercial use clearly stated if claimed (2 points)
  - Personalization instructions clear if applicable (2 points)

### 6. Compliance (max 10)

| Check | Points |
|---|---|
| No trademarked / brand / celebrity names anywhere | 4 |
| AI disclosure present if AI was used | 2 |
| Commercial use claim is backed by actual license | 2 |
| All claimed file formats are actually in the product | 2 |

Any compliance fail = listing is at risk of removal regardless of SEO. A listing with a 0/10 here should be paused, not optimized.

---

## Score interpretation

| Band | Score | Meaning |
|---|---|---|
| Excellent | 90–100 | High-performing listing. Don't break it. Minor refreshes only. |
| Good | 75–89 | Solid. Specific component(s) have room. Targeted improvement, not full rewrite. |
| Needs work | 60–74 | Real gaps. Run targeted MODE 5 / MODE 3 / hero image rewrite. |
| Broken | 40–59 | Multiple systems failing. Full MODE 1 rewrite warranted. |
| Urgent | 0–39 | Compliance risk OR fundamental SEO failure OR conversion floor breached. Stop everything else and fix this first. |

---

## Display block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HEALTH SCORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Composite:                      [XX] / 100   [Excellent / Good / Needs work / Broken / Urgent]

Component breakdown:
  SEO surface coverage:         [X] / 25     [✅ / ⚠️]
  Evidence quality:             [X] / 20     [✅ / ⚠️]
  Coherence:                    [X] / 15     [✅ / ⚠️]
  CTR estimate:                 [X] / 15     [✅ / ⚠️] [* inferred if no SQR]
  Conversion estimate:          [X] / 15     [✅ / ⚠️] [* inferred if no stats]
  Compliance:                   [X] / 10     [✅ / ⚠️]

Lowest component:               [name] ([X] / [max]) — [one-line diagnosis]
Suggested next action:          [most leverage action]
Re-score after:                 [day count or after which MODE run]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Rules

1. **Never inflate inferred scores.** When SQR/stats aren't available, the CTR + Conversion components together max out at ~10 inferred points instead of 30 measured points. The composite ceiling for a new listing without data is ~80, not 100. This is honest — you literally don't know what the listing's CTR is until day 14+.
2. **Compliance failures cap the composite.** If Compliance < 5/10, cap the composite at 50 regardless of other components. A listing about to be removed for IP can't be "Good".
3. **Score is written, not just displayed.** Every score write updates the listing's state file AND the Listings Index sheet in Shop_Master.xlsx.
4. **Score change matters more than absolute score.** A listing going 45 → 78 in one MODE 1 rewrite is a clear win. A listing that was 85 and is now 82 after a "refresh" — that refresh broke something. Always show pre vs post.
