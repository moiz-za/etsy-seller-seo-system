# Playbook — A/B Testing

**Purpose:** Etsy has no built-in split-testing tool. You can only show one version of a listing at a time. But you can run sequential A/B tests over time, comparing two versions across equal-length windows.

**Where it runs:** when the user has a listing that's mid-performing and wants to test variants — typically after a MODE 6 day-30 check-in showing the listing is alive but not winning.

---

## What you can A/B test on Etsy

| Element | Testable? | Notes |
|---|---|---|
| Title | Yes (sequential) | High-impact; biggest CTR lever |
| Hero image | Yes (sequential) | Highest-impact; biggest CTR lever |
| Price | Yes (sequential) | Moderate impact; affects both CTR and CVR |
| Tags | Yes (sequential) | Affects which queries surface; SEO not CTR |
| First photo angle | Yes (sequential) | Same as hero image |
| Description first 160 chars | Yes (sequential) | Moderate CTR impact (meta zone) |

What you cannot meaningfully A/B on Etsy:
- Whole-description prose (signal too weak vs noise)
- Attribute values (rarely move CTR alone)
- Category (re-categorizing is too disruptive to test)

---

## Test design

### Minimum requirements

- **Listing must already be receiving ≥ 200 impressions per week.** Below that, statistical signal is too weak; you'll be reading noise.
- **Window length:** 7 days minimum per variant. 14 days preferred. Both windows the same length.
- **Hold all else constant.** If you change the title AND the hero image at the same time, you can't attribute the result. One variable per test.
- **Avoid testing during recency-boost period.** Boost adds noise. Start tests at day 30+.
- **Don't run two tests in parallel.** They contaminate each other.

### Variables to record

For each variant, capture from Shop Stats:
- Impressions
- Clicks (→ CTR)
- Orders (→ CVR if relevant)
- Favorites

### Decision rule

| Metric improvement | Decision |
|---|---|
| CTR up ≥ 20% AND impressions stable | Variant B wins, keep it |
| CTR up < 20%, impressions stable | Probably noise, no clear winner |
| CTR up but impressions dropped | Confounded — variant B has worse SEO, abandon |
| CTR flat, CVR up | Variant B converts better; keep it |
| Anything ambiguous after 14 days | Default back to original variant |

---

## Common test ideas

### Title test

Test variants:
- Variant A (current): "Funny Cat Mom SVG Bundle | Cricut Clipart PNG EPS"
- Variant B (lead with intent word): "Cat Mom Gift SVG Bundle | Funny Cricut Clipart"
- Variant C (lead with recipient): "Cat Lover Mom SVG Bundle Funny Cricut Designs"

Hypothesis: "Gift" in title attracts gifting-intent buyers (often higher CVR).

### Hero image test

Test variants:
- Variant A (current): SVG designs displayed on a styled flat lay
- Variant B: SVG designs applied to a finished t-shirt being worn
- Variant C: All 20 designs gridded with overlay text "20 Designs"

Hypothesis: lifestyle-on-product (B) outperforms flat-lay (A) for crafting-intent buyers.

### Price test

Test variants:
- Variant A (current): $8.99
- Variant B: $6.99 (lower) or $11.99 (higher)

Hypothesis: lower price increases CTR + CVR by clearing the perceived-value threshold; OR higher price signals quality and reduces price-sensitive bounces.

Critical: price changes can disrupt search ranking (Etsy uses price as a ranking factor). Watch impressions, not just CTR.

---

## Display block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A/B TEST PLAN — L###
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Element under test:    [Title / Hero image / Price / Tags / Description hook]
Variant A (current):   <description>
Variant B (proposed):  <description>

Hypothesis:            <one-sentence claim being tested>
Success metric:        [CTR / CVR / both]
Window length:         [7 / 14] days each

Schedule:
  Variant A in market: YYYY-MM-DD → YYYY-MM-DD (capture metrics on YYYY-MM-DD)
  Apply Variant B:     YYYY-MM-DD
  Variant B in market: YYYY-MM-DD → YYYY-MM-DD (capture metrics on YYYY-MM-DD)
  Decision date:       YYYY-MM-DD

State note: an active A/B test sets the listing's `next_minor_refresh` to AFTER the test window ends. Refreshes mid-test would contaminate results.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After both windows complete, run MODE 6 with the results and the skill will declare a winner using the decision rule.
```

---

## Rules

1. **One variable at a time.** Period.
2. **Equal-length windows.** Period.
3. **Don't peek mid-test.** Looking at day-3 metrics will tempt you to call it early. Wait for the full window.
4. **Day-of-week matters.** Etsy traffic skews higher Sun–Tue. If you're running 7-day tests, both windows must cover the same days of week (so don't run A Mon–Sun and B Wed–Tue; both should be Mon–Sun).
5. **Test in priority order:** Hero image → Title → Price → Description hook → Tags. CTR levers first because they compound through the ranking score.
6. **Sample size is real.** A listing with 50 impressions/week can't meaningfully test. Wait until traffic is high enough OR accept inconclusive results.
