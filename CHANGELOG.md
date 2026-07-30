# Changelog

All notable changes to the Etsy Seller System.

Schema versions are bumped only when state file formats change in ways that require migration.

## [2.1.0] — July 2026

**Major update introducing Caveman Output Mode and 5 Immutable System Laws across Full Skill and Portable editions.**

### Added & Refined
- **🦣 Caveman Output Mode (Token Efficiency):** Output responses are formatted in high-density, bullet-first, zero-fluff text ("Caveman Mode"), saving up to 70% of output tokens per turn while maintaining 100% of SERP research and keyword tracking in local markdown state (`~/etsy-listings/`).
- **📜 5 Immutable System Laws (`skill/references/playbooks/system-laws.md`):** Non-bypassable execution laws:
  1. *Law 1: Immutable Operational Integrity* — Sequential execution of Mode 1/2 workflows, difficulty assessment, and listing output phases without skipping.
  2. *Law 2: Zero-Hallucination Evidence Traceability* — Live search data or explicit `[Data Source: Reasoning Engine Fallback]` tagging.
  3. *Law 3: Mandatory 20-Character Tag Limit & Overlap Rules* — Exactly 13 tags, every tag ≤20 chars (including spaces), max 2 tags share phrase cluster, zero emojis/special symbols in tags.
  4. *Law 4: Caveman Output Protocol* — Concise, high-density outputs by default; full raw SERP breakdowns unlocked on demand (`"expand"`, `"full report"`).
  5. *Law 5: Strict Listing Format & No-Emoji Mandate* — Mandatory Title Formula (`[Primary Keyword] [Style Descriptor] | [Format]`), Title Word Count (6–12 words, max 14), Prohibited Subjective Words Stoplist (`cute`, `beautiful`, etc.), zero emojis in description text or section headers, Etsy 2026 AI Disclosure, Hero Alt Text, and Pinterest Marketing Block.
- **🚫 Strict No-Emoji Description Rule:** Updated `skill/references/listing-guide.md` §4 banning emojis from description text or section headers.
- **🔄 Dual-Repo Policy Sync:** Auto-synchronized rulebooks bidirectionally with `svg-design-intelligence-system`.

---

## [2.0.2] — July 2026

**Policy updates, zip archive packaging fix, and dual-layout bootstrap resolution.**

### Added & Fixed
- **Policy Update (August 11, 2026 Enforcement):** Updated `skill/references/policies.md` §1 with Etsy's Creativity Standards rules for computerized/Cricut/laser tools (mandatory original design requirement) and exact AI creation disclosure dropdown settings (*"I did"*, *"Made to order"*, *"Finished product / Digital file"*).
- **`etsy-seller.skill` Packaging Fix:** Rebuilt distribution archive to include missing `state-templates/` directory (`state-templates/etsy-listings/`), fixing first-run bootstrap template errors for `.skill` zip installs.
- **`bootstrap.py` Path Fix:** Updated `find_default_templates_dir()` to support dual-layout path resolution (zip install layout vs. git clone layout) and added `.DS_Store` / dotfile filtering during template copying.
- **Repository Maintenance:** Created `.gitignore` ignoring OS artifacts (`.DS_Store`), python caches (`__pycache__`), and internal build scripts.
- **README Polish:** Added active status badges, PRs Welcome badge, and a **🤝 Companion Repository** section linking to `svg-design-intelligence-system`.

---

## [2.0.1] — May 2026

**Documentation polish + GitHub language stats fix.**

### Added
- README: new "Using this for free (no paid account)" section — explicit free-tier workflow with per-tool support matrix (claude.ai / chatgpt.com / gemini.google.com / Perplexity)
- `.gitattributes` — forces GitHub Linguist to count Markdown files (fixes the "100% Python" language bar misrepresentation)

### Why these matter
- Most paid Etsy SEO tools cost $9–$50/month; the free-path documentation makes it clear users don't need a paid AI account
- Repo language bar now accurately shows Markdown as the dominant language

No schema changes. No skill behavior changes. Pure documentation + cosmetic fix.

---

## [2.0.0] — May 2026

**Major restructure. Single-namespace listing database, two-mode auto-detected workflow.**

### Architecture changes

- **Dropped shop concept entirely.** No registry, no shop folders, no shop-profile.md, no cross-shop tracking.
- **Flat listing database** at `~/etsy-listings/` — all listings live in one logical set.
- **Multi-shop sellers use separate chat threads** — each thread is its own database.
- **Auto-detection of REWRITE vs CREATE** from input shape (no mode selection menus).
- **Removed xlsx mirror** and openpyxl dependency. All state is markdown.
- **Removed `regenerate_xlsx.py` and `onboard_shop.py`** scripts.
- **Simplified `bootstrap.py`** — pure stdlib Python, just creates the flat folder structure.

### New features

- **Keyword reuse soft warning** — when a candidate primary keyword matches an existing listing's cluster, the skill flags it and suggests sibling phrases. No enforced pivot.
- **Action layer pointers** — when the skill diagnoses a CTR/conversion/pricing problem, it gives concrete next steps with real competitor data, free-tool recommendations, and prioritized actions. Replaces the bland "this isn't SEO scope, sorry" response.
- **Platform fit check** — when the user enters a saturated niche (>100K results, mature competitors, generic product), the skill issues a reality check about realistic ceiling and alternative platforms BEFORE building the listing.
- **Pre-publish checklist** — copy-paste checklist at the end of every output to catch silent failures (forgot to update attributes, etc.).
- **Mobile preview line** — literal ASCII rendering of what the first 40 chars look like on Etsy mobile search.
- **Diff view for rewrites** — shows what changed from the user's original and why (title diff, tag fixes, description diff).
- **Concise default output, "show full" on request** — respects token budgets and reduces wall-of-text.

### Dropped (intentional scope tightening)

- ~~MODE 4 — Shop-wide audit~~ (out of strict SEO scope)
- ~~MODE 5/6/7/8 as standalone modes~~ — folded into core REWRITE/CREATE flow as input-triggered capabilities
- ~~Cross-shop cannibalization architecture~~ — replaced with simpler within-database reuse warning
- ~~`playbooks/cannibalization-check.md`~~ — replaced with inline logic in SKILL.md Phase 5
- ~~`playbooks/shop-architecture.md`~~ — out of scope
- ~~`playbooks/renewal-timing.md`~~ — compressed to a 3-line note in seo-guide.md
- ~~`playbooks/off-platform-amplification.md`~~ — out of strict SEO scope
- ~~`playbooks/star-seller-path.md`~~ — out of strict SEO scope (Star Seller info remains in operations.md as reference)

### Renamed

- `state-templates/etsy-shops/` → `state-templates/etsy-listings/`
- `keyword-map.csv` → `keyword-map.md`
- `refresh-schedule.csv` → `refresh-schedule.md`

### Schema migration from v1.x

Schema version 2.0 is NOT backwards-compatible with v1.x state files. Users upgrading:
1. Back up your old `~/Claude Working/etsy-shops/` folder
2. Manually combine all per-shop CSVs into the new unified `~/etsy-listings/keyword-map.md` (markdown table format)
3. Same for refresh-schedule
4. Existing listing state files can be moved as-is into the new `~/etsy-listings/listings/` folder

Or — start fresh. v2.0 builds a new database from your first listing input.

---

## [1.1.0] — May 2026

Automation + minimal-friction input contract + overview PDF.

- New `skill/scripts/bootstrap.py`, `regenerate_xlsx.py`, `onboard_shop.py`
- Input contract simplified — MODE 1 takes only title+tags+description; MODE 2 takes short free-text
- listing-guide.md §2: added "200 results vs 50M" illustration
- listing-guide.md §4 Block 1: per-intent description hook templates
- seo-guide.md §12: Common Myths section debunking outdated SEO advice
- 14-page Etsy_Seller_System_Overview.pdf

---

## [1.0.0] — May 2026

Initial release. Full 8-mode shop intelligence system.

- MODE 1–8: Rewrite, Create, SQR-Opt, Shop-Audit, Refresh, Iteration, Batch, Competitor
- Persistent state across multiple shops via `etsy-shops/` directory
- Portable Shop_Master.xlsx mirror for non-Cowork tools
- Evidence-driven keyword research (live autocomplete + SERP scrape)
- Cross-shop cannibalization detection
- Indexing spread check
- 0–100 health score
- Search intent classification
- 13 playbooks

---

## Roadmap (potential future versions)

### v2.1 (not committed)
- First-run quick-start tutorial
- "Why this matters" educational notes in rationale outputs
- Rebuilt PDF overview reflecting v2.0 architecture

### v3.0 (speculative)
- Integration with Etsy Open API (if Etsy makes it more accessible to sellers)
- Multi-language support beyond US/UK/EU/AU variants
- Automated Pinterest pin scheduling

These are aspirational. v2.0 is fully functional without them.
