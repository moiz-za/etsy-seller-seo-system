# Playbook — Regional Handling

**Purpose:** Etsy buyers in different English-speaking regions use different language. A US-optimized listing misses 30–40% of UK/EU/AU buyers because the spelling and vocabulary are different. This playbook adds regional autocomplete seeds and adjusts tag strategy for multi-region shops.

**Where it runs:** Phase 3G during keyword research. Triggered when the shop's `target_markets` field includes non-US regions.

---

## Why this matters

Etsy's NLP understands some synonyms but NOT cross-spelling variants:
- US "mom" vs UK "mum" — these are different tokens; "cat mom svg" and "cat mum svg" generate separate impression pools
- US "candy" vs UK "sweets" — different searches
- US "color" vs UK "colour" — Etsy normalizes some but not all instances

If your shop ships to or targets UK/EU/AU, you should capture both.

---

## Regional vocabulary swaps (most impactful)

| US English | UK / AU / EU English | Notes |
|---|---|---|
| mom | mum / mam | Highest-impact swap for parenting niches |
| Mother's Day | Mothering Sunday | UK celebrates earlier (4th Sunday Lent) — different date AND name |
| pacifier | dummy | Baby niche |
| diaper | nappy | Baby niche |
| candy | sweets | Food/treat niche |
| cookie | biscuit | Food niche (Etsy uses "cookie" globally for crackers/biscuits but "biscuits" wins UK SERP) |
| stroller | pushchair / pram | Baby niche |
| color, colored | colour, coloured | All niches |
| favorite | favourite | All niches |
| customize | customise | All niches |
| organize | organise | All niches |
| jewelry | jewellery | Jewelry niche |
| pants | trousers | Apparel (UK "pants" = US "underwear" — major confusion risk) |
| sweater | jumper | Apparel |
| sneakers | trainers | Apparel/shoes |
| bachelorette party | hen party / hen do | Wedding niche |
| baby shower | baby shower | Same — no swap needed |
| wedding shower | bridal shower | Both used in US; UK uses neither (no equivalent custom) |
| graduation | graduation | Same — no swap needed |
| Halloween | Halloween | Universal — no swap |
| 4th of July / Independence Day | (no UK/EU equivalent) | US-only |
| Boxing Day | Boxing Day | UK/AU/CA — not US |

### Australian-specific
- "thongs" (AU) = flip-flops (US/UK)
- "esky" (AU) = cooler (US)
- "togs" (AU) = swimwear

### Date format
- US: MM/DD/YYYY (e.g., 12/25/2026)
- UK/EU/AU: DD/MM/YYYY (e.g., 25/12/2026)
- If you list dates in a printable, OFFER BOTH or default to the buyer's likely region

### Currency
- US: $, "USD", "dollars"
- UK: £, "GBP", "pounds"
- EU: €, "EUR", "euros"
- AU: A$, "AUD"

---

## Regional autocomplete seeds (in addition to Phase 3A)

For a shop with target market including UK/EU:
- Seed 4 in Phase 3A (`[niche] [holiday]`) — add UK variant if seasonal: e.g., `cat mum mothering sunday`
- Add an extra seed run: `[niche-UK-spelling] [product type]`

For a shop with AU target:
- Add seeds with AU vocabulary where applicable

---

## Tag strategy for multi-region shops

You have 13 tag slots. Allocation suggestion:
- 8 tags: US-vocabulary primary + US-language long-tails
- 2 tags: UK-vocabulary variant if the niche has clear UK terms (e.g., "cat mum svg")
- 1 tag: AU-specific if relevant
- 2 tags: universal terms (works in all regions)

This trades some US tag depth for broader regional reach. Tradeoff worth it ONLY if your shop actually ships internationally AND you see UK/EU/AU buyers in your stats.

---

## Display block

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGIONAL HANDLING — <shop-slug>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Target markets:           [list from shop-profile.md]

Detected regional swap opportunities for primary cluster:
  US "<term>" → UK "<term>"
  US "<term>" → AU "<term>"

Recommended tag allocation:
  US-focused tags:        N
  UK variant tags:        N
  AU variant tags:        N
  Universal tags:         N

Specific tag suggestions (add to MODE 1/2 output if multi-region):
  - <UK-variant tag>
  - <AU-variant tag>

Date/currency format in description: <default to user's primary market; explicitly offer alternate if applicable>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Rules

1. **Don't do regional swaps for shops that only ship US.** Adding UK tags to a US-only shop wastes tag slots that could capture US long-tails.
2. **Don't do regional swaps for global-universal niches.** "Wedding clipart" works in every English-speaking market — no swap needed for the niche itself, only for specific recipient/occasion language.
3. **Test the impact.** After adding regional variants, run MODE 6 at day 30 with SQR data. If UK/EU/AU queries aren't showing meaningful impressions, those tags can be redirected back to US long-tails.
4. **EU = many languages.** This playbook covers English variants only. For non-English EU markets (France, Germany, Spain, Italy), Etsy auto-translates — you cannot force foreign-language tags. Focus on universal terms + visual signaling in mockups.
