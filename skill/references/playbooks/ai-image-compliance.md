# Playbook — AI & Image Compliance Gate (22 Oct 2026)

**Purpose:** block listings that violate Etsy's AI and listing-image policies before the user publishes them. This is the second hard gate in the system, alongside `trademark-stoplist.md`.

**Where it runs:** SKILL.md Phase 4G — every REWRITE and CREATE, before output. Also surfaced in the pre-publish checklist and the `EXISTING LISTING AUDIT` block.

**Policy verified:** 22 October 2026 against:
- Seller Handbook — *Important updates to AI use on Etsy*: https://www.etsy.com/seller-handbook/article/1522733284810
- Listing Image Requirements: https://www.etsy.com/legal/policy/listing-image-requirements/253962679005
- Etsy's stance on AI creations: https://www.etsy.com/seller-handbook/article/1275449912004
- Creativity Standards: https://www.etsy.com/legal/creativity

---

## 1. The six rules that matter

| # | Rule | Consequence |
|---|---|---|
| 1 | Most listings need **at least one unedited photo of the actual item against a real background** (see product-type exceptions in §2) | A buyer case for "materially different" can make the seller liable for the refund; listing removal |
| 2 | **All** images must accurately show colour, condition, scale, and materials — no hidden flaws or damage | Misleading-imagery reports; removal; repeat violations → shop removal |
| 3 | Outside the required photo, AI/photo editing is allowed (lighting, colour, crop, resize, background) **as long as the item still looks like what ships** | Same as above if the item appears different |
| 4 | **Bot-generated listings are prohibited.** Every item needs direct, individual human prompting, curation, and creative input | Listing removal; shop removal |
| 5 | **AI-generated functional instructions are prohibited** — patterns, recipes, building/woodworking plans, manuals, instructional guides/e-books | Listing removal |
| 6 | **AI prompt bundles are prohibited** — prompts may not be sold separately from finished artwork | Listing removal; item does not qualify as "designed by a seller" |

**Allowed:** seller-prompted AI art and AI-assisted designs, sold as physical or digital items, when the seller played a real creative role **and discloses AI use in the listing description** (Creativity Standards → "Seller-prompted AI creations").

**Not a license to relax anything else:** IP, trademark, prohibited-items, and accuracy rules still apply to AI-generated output.

---

## 2. Image requirements by product type

| Product type | Required image evidence | AI/edited imagery |
|---|---|---|
| **Physical handmade / made by seller** | ≥1 real unedited photo of the actual item, real background. First image must be original photo/video content of the final product | Extra slots may be AI-edited if accurate |
| **Personalised / customised / made-to-order** | Photos of real, finished items the seller has made. First image must show a finished customised item — never a blank product or "Your Text Here" placeholder | Extra slots may be AI-edited if accurate |
| **Print-on-demand (POD)** | Stock mockups allowed **only if the mockup owner authorises their use** | Mockups must preserve the real print placement, scale, colour, and base product |
| **Digital download (design files)** | Visual preview or excerpt of the actual files (design grid, page preview, layer view) | Representative/AI imagery allowed for the lifestyle slots, as long as it doesn't mislead about what is downloaded |
| **Digital audio / no visual content** | Representative imagery allowed, including AI-generated | Must not imply delivered visual assets |
| **Patterns, recipes, seeds** | ≥1 real unedited photo of something made using the product (finished project, baked result, grown plant) | AI images **cannot be the only** finished-result images |
| **Functional instructions sold as a file** | Same finished-result photo rule, plus the instructions must be the seller's own work | Instructions themselves may not be AI-generated |

---

## 3. Allowed vs prohibited edits

| ✅ Allowed | ❌ Prohibited |
|---|---|
| Adjusting lighting, exposure, colour balance to match real life | Changing the product's actual colour, texture, or condition |
| Cropping, resizing, straightening | Removing or hiding defects, cracks, or damage |
| Cleaning up or replacing the background (product unchanged) | Using AI to change the core design or features of a physical item |
| Adding text/graphics that don't imply extra included items | Showing a simulated finished result as if it were a real one |
| Licensed POD stock mockups | Mockups that change print scale/placement/quality |

**Best practice (Etsy's own recommendation):** make the first photo the clearest, most realistic representation of the item, and if you edited any photos with AI, say so in the description.

---

## 4. The gate — five questions

Answer internally for every listing. Do not print the questions; print the result block in §5.

| # | Question | If yes / result |
|---|---|---|
| G1 | Is the product an **AI prompt bundle**, prompt pack, or prompts sold without finished artwork? | ⛔ **BLOCK** — prohibited category |
| G2 | Is the product **functional instructions** (pattern, recipe, plan, manual, instructional guide/e-book) **whose text was generated by AI**? | ⛔ **BLOCK** — prohibited category |
| G3 | Is this listing part of **bulk/bot-generated output** with no individual human review of this specific item? | ⛔ **BLOCK** — bot-generated listings prohibited |
| G4 | Was the item **created with AI** (seller-prompted art, AI-assisted design)? | Disclosure required → ⛔ **BLOCKED until the disclosure line is in the description**; then ✅ PASS with the line present |
| G5 | Does the image plan include the **required evidence** for this product type (§2)? | Plan includes the required slot → include it and PASS. Seller says only AI/simulated images exist, or the plan cannot satisfy the rule → ⚠️ **ACTION REQUIRED** (blocking prompt, user may override with explicit acknowledgement) |

**Unknown AI status is never a pass for claims.** If the user didn't say whether AI was used, do not claim "no AI", "100% handmade", or "hand-drawn". Print the conditional reminder in §5 so the seller adds a disclosure if any AI touched the item, instructions, or photos. This is a reminder, not a block — confirmed AI use is what triggers the hard requirement.

**Unmentioned photos are not a violation.** If the seller simply hasn't described their photos, generate a compliant plan with the required slot and PASS — the publish checklist carries the upload step. ACTION REQUIRED is for stated conflicts (AI-only images, no real finished result, no preview possible).

---

## 5. Output block (add to every REWRITE/CREATE)

```
AI & IMAGE COMPLIANCE
Item origin:     [human-made / seller-prompted AI / unknown — do not guess]
Content type:    [physical / digital design / functional instructions / prompt bundle]
Image plan:      [unedited photo confirmed / content preview / licensed POD mockup / ACTION REQUIRED: <what's missing>]
Disclosure:      [required — added / required — MISSING / not stated — add only if AI was used]
Gate:            ✅ PASS  ·  ⚠️ ACTION REQUIRED  ·  ⛔ BLOCKED
```

### Disclosure wording (use verbatim, no embellishment)

**AI-created item (required when G4 = yes):**
`Created with AI assistance using my own prompts and refined by me.`

**AI-edited photos only (recommended, not mandatory):**
`Some listing images were edited with AI tools for lighting and background; the item itself is shown accurately.`

**Functional instructions authored by the seller (use when the product is a pattern/recipe/plan):**
`This pattern was written and tested by me. The instructions were not generated with AI.`

Do not stack multiple disclosure lines when one covers it. Never use the disclosure as marketing copy.

---

## 6. California SB 1050 — synthetic performers (effective 1 January 2027)

Listing images or videos that prominently feature an **AI-generated synthetic performer** (a realistic human figure/voice created with generative AI that is not an identifiable real person) may be treated as advertising to California buyers and may require a clear disclosure.

Gate rule:
- If the image/video brief specifies an AI-generated human (not a real model and not the seller), add a disclosure line and flag it in the output.
- Prefer a real person, the seller's own hands, or a non-human scene. It is almost always the lower-risk choice.
- The skill does not provide legal advice; sellers should confirm their own obligations with counsel.

---

## 7. Blocking behaviour

- **⛔ BLOCKED** — do not output the listing package. Explain the specific rule, cite the source, and offer the compliant alternative (e.g., "rewrite the pattern yourself", "sell the finished artwork instead of the prompt pack", "process one listing at a time with your own review").
- **⚠️ ACTION REQUIRED** — output the listing, but prepend the missing item to the "BEFORE YOU PUBLISH" checklist. Do not let the user proceed silently.
- **✅ PASS** — one line in the output block; no extra prose.

**Never**:
- invent an image the seller hasn't taken,
- describe an AI-generated result as a real finished project,
- mark a listing compliant because the text is fine when the image plan is non-compliant,
- claim AI was not used when the seller didn't say.

---

## 8. Rewrite audit hook

For MODE 1 (REWRITE), add this row to the existing-listing audit:

```
AI & image:   [prompt bundle / AI-authored instructions / undisclosed AI creation / no unedited photo / preview missing / compliant]
```

Any finding here outranks SEO issues — a non-compliant listing can be removed regardless of how well it ranks.

---

## 9. Test matrix (maintainer check)

Paste each fixture as a CREATE request and confirm the gate line. Re-run after any policy update.

| # | Fixture | Expected |
|---|---|---|
| 1 | "Funny cat mom SVG bundle, 20 designs, SVG PNG EPS, digital download" | ✅ PASS — image plan requires a file preview, no unedited-photo demand |
| 2 | "POD t-shirt with my original design, printed by Printful" | ✅ PASS — licensed stock mockup noted |
| 3 | "Crochet baby blanket pattern, PDF, written by me" | ✅ PASS — allowed category; plan leads with a real finished-result photo |
| 4 | "Crochet pattern, the instructions were written with ChatGPT" | ⛔ BLOCKED — AI-generated functional instructions |
| 5 | "Midjourney prompt pack, 500 prompts, no images" | ⛔ BLOCKED — AI prompt bundle |
| 6 | "Handmade ceramic mug" (no photos mentioned) | ✅ PASS — plan leads with a real unedited photo; checklist carries the upload step |
| 6b | "Handmade ceramic mug — all my photos are AI renders" | ⚠️ ACTION REQUIRED — no real photo asset |
| 7 | "AI-generated fantasy art print, 300dpi JPG" (no disclosure) | ✅ PASS once the skill inserts `Created with AI assistance…`; if the seller removes it → ⛔ BLOCKED |
| 8 | CSV of 20 listings | PASS per row, with the human-review notice; banned rows flagged, not processed |

**Failure signature:** if a fixture returns ✅ PASS when the table says BLOCK/ACTION, the gate is not running. Check that Phase 4G is present in `SKILL.md` and that this playbook is listed in the reference files.
