# Playbook — Platform Fit Check

**Purpose:** when a user wants to enter a saturated niche with a generic product, give them an honest reality check about realistic ceiling and alternative platforms — BEFORE they invest 6 months of effort.

**Why this exists:** Etsy is the right marketplace for many product types but not all. Some niches are essentially closed to new entrants. Telling someone "great, let's optimize your listing" when they're entering a niche with thousands of established sellers is dishonest. Better to flag the math upfront.

**Where it triggers:** Phase 8 of CREATE (and sometimes REWRITE) when ALL of the following are true:
1. Phase 4C difficulty assessment = Very High (>100K competing listings)
2. Product appears generic — no distinguishing style / recipient / format anchor in the user's context
3. Top 3 SERP shops are mature — Star Seller badges, 1,000+ sales, 500+ reviews each
4. User has no clear differentiation in their input (no unique angle, no premium tier, no underserved sub-niche)

---

## When to trigger (precise criteria)

ALL four must be true. If any one is false, skip the platform-fit check — proceed with normal output.

**Criterion 1 — Difficulty Very High:**
- From Phase 4C: results count > 100,000 for the candidate primary keyword
- AND ad density on the first 8 results ≥ 3 (i.e., active paid competition)

**Criterion 2 — Generic product:**
- The user's input describes the product without a distinguishing modifier
- Examples of GENERIC inputs that trigger:
  - "Cat SVG bundle, 20 designs, SVG and PNG"
  - "Wedding clipart"
  - "Halloween stickers"
  - "Coffee mug"
- Examples of NOT generic (a specific angle is present — skip platform-fit-check):
  - "Funny CAT MOM coffee mug for crazy cat ladies, ceramic 11oz, dishwasher safe"
  - "Boho cat mom SVG bundle for Cricut crafters, 20 watercolor designs"
  - "Kawaii Halloween stickers featuring chibi black cats and pumpkins"

**Criterion 3 — Mature dominant competitors:**
- From Phase 4B competitor SERP scrape, top 3 ORGANIC listings (skip ads) show:
  - All 3 are Star Sellers
  - All 3 have ≥ 500 reviews
  - All 3 have shops with ≥ 1,000 total sales
  - At least 2 of 3 listings are visibly older than 12 months

**Criterion 4 — No clear differentiation from user:**
- User did not mention a premium tier, specialized service, unique style, or commercial advantage in their input
- User did not mention a connection to an underserved buyer segment

If all 4 hit → output the reality check block.

---

## The reality check output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ PLATFORM FIT REALITY CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before I build your listing, you should see what you're walking into.

YOUR TARGET KEYWORD: "[primary keyword]"

SERP TOPLINE:
- Total competing listings: ~[X] (Very High difficulty)
- Top 3 organic results:
  • #1: <Shop A name> — Star Seller, [N] reviews, ~[Y] total sales, listing ~[N] [months/years] old
  • #2: <Shop B name> — Star Seller, [N] reviews, ~[Y] total sales, listing ~[N] [months/years] old
  • #3: <Shop C name> — Star Seller, [N] reviews, ~[Y] total sales, listing ~[N] [months/years] old

REALISTIC CEILING FOR A NEW LISTING HERE:
- Position 50–100 within 30 days (post-indexing + recency boost)
- Position 20–50 within 6 months IF you also nail hero image, price, video, 
  and start accumulating reviews
- Top 10 is unlikely within the first 12 months without:
  - A genuinely differentiated product (not just a tag rewrite)
  - 100+ reviews of your own (compounds slowly)
  - Star Seller status (3-month grind)
  - External traffic from Pinterest/social (compounds external-signal ranking)

ONE OF THREE THINGS NEEDS TO BE TRUE FOR THIS LISTING TO WORK ON ETSY:

[1] You differentiate aggressively. A generic "[primary keyword]" listing 
    won't win. A "[primary keyword] for [specific underserved buyer segment]" 
    listing might. Re-frame your product with a tighter buyer focus.

[2] You commit to a 12-month compounding strategy. Etsy rewards consistency. 
    You'd need to launch this PLUS related listings (10+ in the niche) and 
    maintain them with refresh cycles, while building reviews and 
    Pinterest traffic in parallel.

[3] You consider a different platform where the competition density is lower 
    for this product type:
    
    - PINTEREST + SHOPIFY/WEBSITE: better for visually-driven products where 
      you control the funnel. Pinterest's algorithm rewards new pinners; you 
      don't compete in someone else's search results.
    
    - FAIRE: wholesale B2B marketplace. Better fit for inventory-oriented 
      brands targeting boutique retailers, not direct consumers.
    
    - AMAZON HANDMADE: better for utility products where buyers search by 
      feature/function rather than by maker.
    
    - YOUR OWN WEBSITE + SOCIAL: highest control, highest effort. Worth it 
      if you already have an audience.

WHAT WOULD YOU LIKE TO DO?

[a] Proceed anyway — I'll build the best possible Etsy listing for "[primary keyword]"
[b] Re-frame the product with a tighter buyer-segment angle — give me a more 
    specific input (e.g., "[primary keyword] for [target buyer]") and I'll 
    research that narrower niche
[c] Hold off on Etsy for this product — investigate the alternative platforms above

Default if no reply: [a] proceed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## After the reality check

- If user chooses [a]: build the listing normally, but the listing's state file notes the platform-fit warning was issued. At day 30 iteration check-in, this gets surfaced — "remember the platform-fit warning we discussed? If results match the realistic ceiling forecast, that's not failure — that's expected for this niche position."

- If user chooses [b]: ask for the refined input (specific buyer segment, occasion, style anchor). Re-run Phase 4 with the narrower seed. Re-assess difficulty. If now Low-Medium or Medium → proceed with build. If still Very High → loop back to [a] or [c].

- If user chooses [c]: don't build the Etsy listing. Output a brief follow-up suggesting which alternative platform fits their product best, with one concrete next-step resource for that platform. Then exit the run.

---

## Tone rules for the reality check

- Honest but not discouraging. The math is the math; the user deserves to know it.
- Concrete: real numbers from real SERP data, not generic warnings.
- Always offer 3 paths, not just "give up."
- Default to proceeding — the user is the decision-maker. The skill informs; it does not block.
- Never sound preachy or moralistic. State the facts, list the options, let them choose.

---

## What the reality check does NOT do

- Does NOT decide for the user. They can override and proceed.
- Does NOT apply to niche-specific products with clear differentiation (criterion 4 fails → no warning).
- Does NOT apply to REWRITE of an existing listing (the listing is already up; sunk-cost reality is different).
- Does NOT promise success on the alternative platforms either — every platform has its own bar.

---

## When this playbook saves the user

For a struggling seller, the most expensive mistake is not bad SEO — it's 6 months of optimizing a listing in a niche where no amount of optimization will work. The platform-fit check costs 30 seconds of warning. Avoiding 6 months of wasted effort is worth that.

For 90% of users, this playbook does NOT trigger (their product has differentiation or their niche isn't saturated). For the 10% who do trigger it, this is the most valuable single thing the skill ever tells them.
