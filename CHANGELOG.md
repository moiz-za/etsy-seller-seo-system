# Changelog

All notable changes to the Etsy Seller System.

Schema versions are bumped only when state file formats change in ways that require migration.

## [2.2.1] — October 2026

**2026 operations sweep — brings the guidance up to date beyond AI/image.** State schema remains 2.0.

### Added
- **Payment account & payouts (8 Sep 2026):** Current / Pending / Total balance model, Ready for Deposit, reserves folded into Pending, negative Current balances, and sale-vs-non-sale fee timing (`operations.md`).
- **Etsy Purchase Protection (7 Apr 2026, effective 7 May):** $250 USD per eligible order including postage/tax, even above a $250 order total; eligibility standards; 48-hour Help with Order response; human review (`operations.md`).
- **US tariffs & DDP (9 Jun 2026):** US de minimis ended 29 Aug 2025; DDP required for US orders from 9 Jul 2026 to qualify for Purchase Protection; duties up front and US-specific pricing (`operations.md`).
- **EU packaging & EPR / PPWR (3 Sep 2026, effective 12 Aug 2026):** producer registration, EPR numbers in Shop Manager, Authorised Representative, packaging reporting, compliance-scheme fees (`policies.md §3`, `operations.md`).
- **Policy violations page & appeals (23 Jul 2026):** removal history, appeal routes, timing, and "appeal instead of relisting" (`policies.md §5`).

### Changed
- **Cases:** buyer case window is now 30 days after eligibility begins; late delivery defined as 7+ days after the estimated delivery date (`operations.md`).
- **Review rating:** clarified that rating, text, and count share the lifetime timeframe; Star Seller remains 3 months.
- **Policy baseline** moved to 23 October 2026 in `policies.md`; README policy badge and `SKILL.md` policy version updated.
- **Portable edition v2.2.1:** new operations summary, source URLs, and quick-reference rows.
- Source URLs for all six updates added to the portable edition.

---

## [2.2.0] — October 2026

**Policy-breaking release: Etsy's 22 October 2026 AI and listing-image rules.** State schema remains 2.0 (new fields are optional; no migration).

### Added
- **Law 6 — AI & Image Compliance Gate** (`playbooks/ai-image-compliance.md`): a hard gate alongside the trademark stoplist. Blocks AI prompt bundles, AI-generated functional instructions (patterns, recipes, plans, manuals, guides), bot-generated listings, and undisclosed AI creations. Emits a `✅ PASS / ⚠️ ACTION REQUIRED / ⛔ BLOCKED` result in every output.
- **Listing-image compliance rules**: required unedited real photo for physical/customised/pattern-recipe-seed listings, file preview/excerpt for digital downloads, licensed stock mockups for POD, finished-customised-item first image for personalised listings, and no misleading edits.
- **AI disclosure logic**: AI-created items now require `Created with AI assistance using my own prompts and refined by me.` in the description; AI-edited photos get an optional note; functional guides get an authorship line.
- **California SB 1050** synthetic-performer guidance (effective 1 Jan 2027) in image, video, and Pinterest briefs.
- **Public policy section in README** — the October 2026 rules in plain language with source links, plus how the repo enforces them.
- **Optional `AI & image compliance` state block** in the listing schema and template.
- **Phase 2 freshness check** now searches for Etsy AI-policy and image-requirement updates; baseline moved to 22 October 2026.
- **Monthly Policy Freshness workflow** (`scripts/check_policy_freshness.py` + `.github/workflows/policy-freshness.yml`) — opens a `policy-freshness` issue when the baseline is more than 120 days old.

### Changed
- `policies.md` §7 documents the image and AI rules, product-type exceptions, enforcement/refund exposure, and the corrected Creativity Standards URL (`etsy.com/legal/creativity`).
- `policies.md` audit checklist expanded from 10 to 17 items covering AI categories, image evidence, and synthetic media.
- `listing-guide.md` §6 rewritten as *Photos, Video & Image Compliance*; hero-shot guidance is now product-type-aware instead of "lifestyle mockup" for every listing.
- Description Block 8 renamed to *AI & Image Disclosure* with three conditional templates.
- `listing-health-score.md` compliance scoring rebalanced to 6 checks (still 10 points), including prohibited categories and image compliance.
- Batch mode now states the human-in-the-loop requirement explicitly (no auto-generated or auto-published listings).
- Portable edition mirrored: Law 6, gate, image rules, disclosure templates, audit checklist, policy URLs, quick-reference rows.
- `sync_etsy_policy.py` playbook list includes `ai-image-compliance.md`.

### Fixed
- Removed the unsafe default that omitted AI disclosure whenever the user didn't mention AI. Unknown status now produces a conditional disclosure reminder instead of a silent pass.
- Removed stale "Lifestyle mockup" hero guidance that conflicted with the unedited-photo requirement.
- Replaced the stale creativity-standards help-centre link with the live policy page.

---

## [2.1.2] — October 2026

**Sync & consistency release: repo-wide audit fixes, install-path correction, Etsy April 2026 title guidance, and CI hardening. State schema remains 2.0.**

### Fixed
- **Install path (Claude/Cowork):** the documented `cp -r skill …` install copied only `skill/`, so `bootstrap.py` could not find `state-templates/` and `~/etsy-listings/` was never auto-created. Install steps now copy both folders, include the missing `git clone` step, and document the packaged `.skill` download.
- **Archive rebuild:** `sync_etsy_policy.py` only rebuilt `etsy-seller.skill` during a cross-repo sync. Added a `--build` mode that rebuilds it deterministically from `skill/` + `state-templates/` with no sibling repo, plus an **Archive Check** CI job that fails if the zip drifts from source.
- **Leak Guard:** first-push/new-branch pushes scanned nothing (a single-commit `git diff`) and diff errors were swallowed. Both the workflow and `.githooks/pre-push` now diff against the empty tree and fail closed.
- **Rule sync (skill ⇄ portable):** portable subjective-words stoplist expanded to the canonical 17; phrase-overlap rule aligned to "2+ word"; title word-count guardrail stated consistently (6–12, max 14); added the "no foreign-language tags" rule.
- **Stale references:** removed pointers to the long-deleted `renewal-timing.md`, `shop-profile.md`, `target_markets` field, and the `Shop_Master.xlsx` mirror; corrected a `listing-guide.md` relative path.
- **Phase / MODE drift:** corrected keyword-research references from the old Phase 3 to the current Phase 4 (and subphases 4A–4F), fixed Phase 2→3 and Phase 5→7 references, and reworded orphaned MODE 3–8 references (only Modes 1–2 exist).
- **Description structure:** corrected the mislabeled "8-block" description to the canonical **9-block** structure everywhere.

### Added
- **Etsy title guidance (April 2026):** new `seo-guide.md` / `policies.md` material reflecting Etsy's April 27, 2026 Seller Handbook "New Guidance for Listing Titles" (state the item once; top-3 descriptors color/material/size; holidays only if essential; avoid aspirational/gifting phrase repetition; move subjective words to tags/attributes; remove sales/shipping) plus the new AI title tool.
- **Archive Check workflow** and deterministic `.skill` packaging.
- **`NOTICE`** now referenced from the README License section.

### Changed
- **Policy labeling:** references now use "Etsy Policies — 2026" with dated updates instead of a single month label.
- **Version metadata:** README badge / changelog table and the portable edition header aligned to 2.1.2; corrected the `SKILL.md` header that mislabeled the state schema version.

---

## [2.1.1] — September 2026

**Maintenance release: archive fixes, maintainer-script path sanitization, and SellWren integration links.**

### Fixed
- **`etsy-seller.skill` Archive Regression:** The v2.1.0 archive accidentally dropped the `state-templates/` directory that v2.0.2 added — zip installs hit first-run bootstrap template errors. Rebuilt with `skill/` + `state-templates/` (25 entries).
- **`sync_etsy_policy.py` Path Fix:** Replaced hardcoded maintainer machine paths with auto-detection (repo-relative with `ESVG_REPO`/`SELLER_REPO` env overrides). The script now works from any clone location and rebuilds both skill archives on sync.
- **Archive Rebuild on Sync:** The sync engine now rebuilds both skill archives when it detects cross-repo rulebook drift.

### Added
- **🛠️ SellWren Integration:** New "Related: SellWren" section — the free point-and-click Etsy tools (Tag Verifier, Title Builder, IP Scanner, Description Builder) and live shop dashboard built on the same rulebooks by the same team. See README and INSTALL for links.

---

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

### v2.x (exploratory)
- First-run quick-start tutorial
- "Why this matters" educational notes in rationale outputs

### v3.0 (speculative)
- Integration with Etsy Open API (if Etsy makes it more accessible to sellers)
- Multi-language support beyond US/UK/EU/AU variants
- Automated Pinterest pin scheduling

These are aspirational. v2.0 is fully functional without them.
