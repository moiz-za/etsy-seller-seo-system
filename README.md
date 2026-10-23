# Etsy Seller SEO System

A free, evidence-driven **Etsy SEO tool** for AI assistants. It optimizes Etsy listings — titles, all 13 tags, attributes, and descriptions — using live Etsy autocomplete research, top-10 competitor SERP analysis, and current 2026 Etsy policy checks, including the October 2026 AI and listing-image rules. Runs inside Claude, ChatGPT, Perplexity, or Gemini on free tiers, with no shop registration, setup forms, or API keys.

**Quick start:** paste [`portable/Etsy_Listing_System_Instructions.md`](./portable/Etsy_Listing_System_Instructions.md) into any AI chat as your first message, then send your listing. Installing the Claude skill takes three commands — see [Installation](#installation).

[![Version](https://img.shields.io/badge/version-2.2.1-blue?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Etsy policy](https://img.shields.io/badge/Etsy_policy-23_Oct_2026-green?style=flat-square)](skill/references/policies.md)
[![Stars](https://img.shields.io/github/stars/moiz-za/etsy-seller-seo-system?style=flat-square&label=stars)](https://github.com/moiz-za/etsy-seller-seo-system/stargazers)
[![Forks](https://img.shields.io/github/forks/moiz-za/etsy-seller-seo-system?style=flat-square&label=forks)](https://github.com/moiz-za/etsy-seller-seo-system/forks)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Discussions](https://img.shields.io/badge/community-discussions-blueviolet?style=flat-square)](https://github.com/moiz-za/etsy-seller-seo-system/discussions)

---

## Table of Contents

- [Features](#features)
- [Etsy AI & Image Policy (October 2026)](#etsy-ai--image-policy-october-2026)
- [Scope and Limits](#scope-and-limits)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Free vs Paid](#free-vs-paid)
- [Comparison with Other Etsy SEO Tools](#comparison-with-other-etsy-seo-tools)
- [Who It's For](#who-its-for)
- [Repository Structure](#repository-structure)
- [Related Projects](#related-projects)
- [FAQ](#faq)
- [Community](#community)
- [Changelog](#changelog)
- [Author and Maintainer](#author-and-maintainer)
- [License](#license)

---

## Features

Everything below is built for Etsy SEO in 2026 — Etsy titles, Etsy tags, attributes, and descriptions.

### Caveman Output Mode

Crisp, bullet-first output that reduces token usage by up to 70%. Full raw SERP breakdowns and keyword tracking stay in state and unlock on demand (`"expand"`, `"full report"`).

### Six Immutable System Laws

Non-bypassable execution discipline (`skill/references/playbooks/system-laws.md`):

1. **Zero state skips** — sequential workflows with difficulty assessment and output phases.
2. **Zero hallucination** — live search data, or explicit `[Data Source: Reasoning Engine Fallback]` tagging.
3. **Strict listing rules** — exactly 13 tags, each 20 characters or fewer, with at most 2 tags per phrase cluster.
4. **Caveman output protocol** — concise by default, details on request.
5. **Strict format mandate** — mandatory title formula, title word count, no-emoji rule, and AI/image disclosure blocks.
6. **AI & image compliance gate** — blocks bot-generated listings, AI-authored patterns/recipes/guides, AI prompt bundles, and undisclosed AI creations.

### Live Research Engine

- **Real Etsy autocomplete** — what buyers are typing right now.
- **Top 10 competitor SERP scraping** — what is winning for a given keyword.
- **Competition difficulty assessment** — whether a keyword is realistic or saturated.

### Optimized Etsy Titles, Tags, and Descriptions

- Mandatory title formula `[Primary Keyword] [Style Descriptor] | [Format]` within the first 40 characters, with a mobile preview line.
- A 6–12 word title limit (maximum 14), plus a prohibited subjective-words stoplist (`cute`, `beautiful`, and similar).
- All 13 tags verified at 20 characters or fewer, with phrase-overlap rules enforced.
- No emojis in description text or section headers — clean formatting and screen-reader accessibility.
- NLP-aware natural-language writing, with no keyword chains, which Etsy's 2026 algorithm penalizes.

### Trademark, AI & Image Policy Guard

- Flags trademarked words before a listing is taken down.
- Runs a hard AI & image gate on every listing: bot-generated listings, AI-authored patterns/recipes/plans, AI prompt bundles, and undisclosed AI creations are blocked before output.
- Enforces the 22 October 2026 listing-image rules — required unedited real photo, digital-file previews, licensed POD mockups, and no misleading edits.
- Checks Etsy's current 2026 policies each session via live web search (Phase 2), with a maintainer dual-repo sync engine (`skill/scripts/sync_etsy_policy.py`) that keeps the rulebooks aligned.
- Platform fit check on saturated niches (over 100K results) before a listing is built.

### Honest Scope Diagnosis

- Identifies when the problem is not SEO, and what it actually is.
- Action-layer pointers with competitor data, price ranges, and free-tool recommendations.
- Diff view for rewrites, showing exactly what changed and why.

### Pinterest Content

- Generates Pinterest marketing content with explicit 220–232 character counts and adjust guidance.

### Cross-Session Memory

- Remembers listings across sessions on Claude, avoiding duplicate keyword suggestions.
- Silent local database at `~/etsy-listings/` for the keyword map, refresh schedule, and listing state.
- Keyword reuse warnings with sibling-phrase suggestions.

---

## Etsy AI & Image Policy (October 2026)

On **22 October 2026**, Etsy published [new rules for AI use and listing images](https://www.etsy.com/seller-handbook/article/1522733284810). They apply to every seller, not just AI-heavy shops. Short version:

| Rule | What it means for your shop |
|---|---|
| **Unedited photo required** | Most listings need at least one real, unedited photo of the actual item against a real background. Don't AI-edit or retouch that photo. |
| **Images must be truthful** | No hiding flaws, damage, or changing colour, texture, scale, or materials. Other photos may be AI-edited for lighting/background if the item still looks like what ships. |
| **No bot-generated listings** | Every item needs your own prompts, curation, and review. Mass-automated listing generation is prohibited. |
| **No AI-generated instructions** | Patterns, recipes, building plans, manuals, and instructional guides must be your own work — not AI-generated. |
| **No AI prompt bundles** | You can't sell prompts separately from the finished artwork. |
| **Disclose AI creations** | If AI created the item, say so in the listing description. |

Product-type exceptions ([Listing Image Requirements](https://www.etsy.com/legal/policy/listing-image-requirements/253962679005)):

- **Print-on-demand** — licensed stock mockups are allowed.
- **Digital downloads** — include a visual preview or excerpt of the files buyers receive.
- **Customised / made-to-order** — use photos of real finished items; the first image must show the finished customised item.
- **Patterns, recipes, seeds** — include at least one real, unedited photo of a finished result. AI images can't be the only finished-result images.

**How this repo handles it:** every listing runs the AI & image compliance gate (`skill/references/playbooks/ai-image-compliance.md`). It blocks the three prohibited categories, requires the disclosure line for AI-created items, and adds the required photo/preview step to the publish checklist. Unknown AI status never becomes a false claim — the tool won't say "no AI" or "100% handmade" unless you confirm it, and it prints a disclosure reminder on every listing.

**California SB 1050** (effective 1 January 2027): images or videos featuring AI-generated synthetic performers may require a clear disclosure for California buyers. The gate flags this in image and video briefs.

*Policy details change. This repository tracks them with a monthly CI freshness check, but it is not legal advice — verify against Etsy's linked policies and consult your own counsel for edge cases.*

---

## Scope and Limits

This system does not:

- Claim an SEO rewrite will fix a hero-image problem.
- Claim a tag rewrite will rescue a listing with a 0.3% conversion rate.
- Promise a #1 ranking.
- Create images, videos, or mockups (it writes briefs only).

When the problem is not SEO, it says so and points to concrete next steps backed by real data.

This is an Etsy SEO tool, and it does Etsy SEO well. If Etsy SEO is the only problem, expect a meaningful traffic lift — typically 20–40% impression improvement on rewritten listings within 30 days. If the problem lies elsewhere (weak photos, pricing, reviews, or a saturated niche), the system will say so and route you to what would actually work.

---

## Installation

### Option 1: Claude / Cowork (full automation, recommended)

```bash
git clone https://github.com/moiz-za/etsy-seller-seo-system.git
cd etsy-seller-seo-system
mkdir -p ~/.claude/skills/etsy-seller
cp -r skill/. ~/.claude/skills/etsy-seller/
cp -r state-templates ~/.claude/skills/etsy-seller/
```

> Prefer a one-step install? Download `etsy-seller.skill` from the [latest release](https://github.com/moiz-za/etsy-seller-seo-system/releases/latest) and unzip it into `~/.claude/skills/etsy-seller/` — the archive bundles the skill and the state templates.

Restart Claude. On the first listing input, the skill creates `~/etsy-listings/` and begins tracking. No file management is required.

### Option 2: ChatGPT / Perplexity / Gemini

Upload `portable/Etsy_Listing_System_Instructions.md` as a knowledge file to your Custom GPT, Space, or Gem, and enable web browsing.

See [INSTALL.md](./INSTALL.md) for detailed steps per tool.

---

## How It Works

```
Paste listing (title + tags + description)  or  short new-product description
                    │
                    ▼
          Auto-Detect: REWRITE vs CREATE
                    │          (no mode selection, no prompts)
                    ▼
        Live Research — Etsy autocomplete
        + top-10 competitor SERP scraping
                    │
                    ▼
    Competition Difficulty Assessment
    + Trademark / Policy Check (stoplist + 2026 policies)
                    │
                    ▼
      Listing Build: title → 13 tags → attributes
      → description → Pinterest block → pre-publish checklist
                    │
                    ▼
   Caveman-mode output + diff view (rewrites) + state saved
   to ~/etsy-listings/
```

That is the whole interaction: no mode selection, no shop prompts, no setup forms.

---

## Free vs Paid

Most paid Etsy SEO tools cost $9–$50 per month. This system is designed to run entirely on free tiers.

### The free path

1. Sign up at [claude.ai](https://claude.ai), [chatgpt.com](https://chatgpt.com), or [gemini.google.com](https://gemini.google.com).
2. Open [`portable/Etsy_Listing_System_Instructions.md`](./portable/Etsy_Listing_System_Instructions.md) and copy the entire contents.
3. Start a new chat and paste the document as your first message.
4. Reply with: *"OK, follow this system. Here's my listing: [paste your listing]"*.

### Free-tier support

| Tool | Free tier works? | Notes |
|---|---|---|
| **Claude.ai (free)** | Yes | Daily message cap; web search enabled. Paste the portable doc as the first message. |
| **ChatGPT (free)** | Yes | Browsing available on the free tier. Same paste-first-message pattern. |
| **Gemini (free)** | Yes | Web search available; handles long instructions well. |
| **Perplexity (free)** | Partial | Basic search works, but the URL-fetch dependency in keyword research is less reliable on the free tier. |

### What the free path keeps

- All SEO rules (title, tags, attributes, description).
- Live Etsy autocomplete and competitor SERP research (with web browsing enabled).
- Trademark stoplist scan.
- Honest scope diagnosis.
- Per-intent description hooks, indexing spread check, Pinterest content, and the pre-publish checklist.
- All operational playbooks.

### What the free path gives up

- **Cross-session memory** — re-paste the session-state snapshot at the start of each new chat (about 30 seconds).
- **Automatic folder management** — no local `~/etsy-listings/` database; state lives in the chat thread.
- **Daily message limits** — free tiers cap daily usage.

### When the paid path makes sense

For 30+ listings or multiple shops, the paid Claude path removes manual copy-paste friction:

- **Claude Code** (terminal) — requires Claude Pro/Max or API credits.
- **Cowork** (Claude desktop app) — requires Claude Pro/Max.

Copy the `skill/` folder to `~/.claude/skills/etsy-seller/` and the system handles state automatically.

The skill content is identical on both paths. For 1–5 listings, the free path is sufficient.

---

## Comparison with Other Etsy SEO Tools

| Feature | Typical Etsy SEO tools | This system |
|---|---|---|
| Keyword research | Static keyword lists | Live Etsy autocomplete + SERP scraping |
| Tag character limits | Not enforced | Verified at 20 characters or fewer |
| Etsy algorithm | Advice from 2018–2022 | 2026 NLP-aware, natural language |
| Diagnostics | Prescriptive tag advice | Identifies when the problem is not SEO |
| State across sessions | None or paid SaaS | Local markdown files |
| Cost | $9–$50/month | $0, runs inside your AI tool |
| Setup | Account, login, onboarding | Drop a folder into `~/.claude/skills/` |

---

## Who It's For

- Etsy sellers whose listings are not getting impressions and want to know why.
- Sellers launching new listings who want them optimized from day one.
- SEO consultants managing listings for multiple clients (one thread per shop).
- Multi-shop sellers who want a single workflow across shops.

---

## Repository Structure

```
etsy-seller-seo-system/
├── README.md                   ← you're here
├── INSTALL.md                  ← step-by-step setup per AI tool
├── CHANGELOG.md                ← version history
├── LICENSE                     ← MIT
├── NOTICE                      ← trademark attribution
├── CODE_OF_CONDUCT.md          ← community expectations
├── CONTRIBUTING.md             ← contribution guide
├── SECURITY.md                 ← vulnerability reporting
├── etsy-seller.skill           ← packaged skill (attached to releases)
│
├── .github/                    ← CI workflows + issue/PR templates
├── .githooks/                  ← pre-push leak guard
├── scripts/                    ← policy-sync, archive build, freshness check
│
├── skill/                      ← drop into ~/.claude/skills/etsy-seller/
│   ├── SKILL.md                ← the orchestrator (2 modes + auto-detect)
│   ├── scripts/
│   │   ├── bootstrap.py        ← silent state init on first run
│   │   ├── sync_etsy_policy.py ← dual-repo sync + archive build
│   │   └── README.md
│   └── references/
│       ├── data-model/SCHEMA.md ← state file formats
│       ├── listing-guide.md     ← title/tag/attribute/description rules
│       ├── seo-guide.md         ← 2026 Etsy algorithm details
│       ├── policies.md          ← Etsy policies (2026)
│       ├── operations.md        ← fees, Star Seller, cases, diagnostics
│       ├── pinterest-guide.md   ← Pinterest strategy
│       └── playbooks/           ← system laws + operational playbooks
│
├── portable/                    ← single self-contained doc for non-Claude tools
│   └── Etsy_Listing_System_Instructions.md
│
└── state-templates/             ← markdown templates auto-copied on first run
    └── etsy-listings/
        ├── keyword-map.md
        ├── refresh-schedule.md
        ├── listings/_TEMPLATE_listing.md
        └── sqr-imports/README.md
```

---

## Related Projects

### Companion repository

Designed to work alongside [`svg-design-intelligence-system`](https://github.com/moiz-za/svg-design-intelligence-system), which handles market research, buyer psychology, IP risk screening, and prompt engineering to create original SVG digital products before publishing.

- **ESVG-DIS System** creates the right *product*.
- **Etsy Seller SEO System** creates the right *listing*.

Neither depends on the other; use either independently or together.

### SellWren

[SellWren](https://sellwren.com) is a free Etsy seller toolkit from the same team that applies this system's checks as point-and-click tools, plus a live shop dashboard on the official Etsy API.

| This repo (AI skill) | SellWren free tool |
|---|---|
| 13-tag verification (13 tags, 20 characters or fewer, phrase overlap) | **Tag Verifier** |
| Title checks (primary keyword in first 40 chars, 6–14 words, no subjective words) | **Title Builder** |
| Trademark stoplist scan | **IP Scanner** |
| 9-block description format | **Description Builder** |

- **Free tools:** [sellwren.com/tools](https://sellwren.com/tools) — no account, nothing stored.
- **Live dashboard demo:** [sellwren.com/demo-dashboard](https://sellwren.com/demo-dashboard) — income, winners, listing health, and profit math.
- **SellWren for Desktop** (one-time license, local data) is in development; join the waitlist at [sellwren.com](https://sellwren.com).

The skill and SellWren share the same rulebooks and 2026 Etsy policy alignment. Use the skill for deep research and listing creation, and SellWren for daily monitoring and quick checks.

---

## FAQ

**Is there a free path?**
Yes. Paste `portable/Etsy_Listing_System_Instructions.md` into any free-tier chat (Claude.ai, ChatGPT, Gemini). All SEO rules, live research (with web browsing), trademark and AI/image compliance scanning, and scope diagnosis are included. See [Free vs Paid](#free-vs-paid).

**Do I need API keys or a paid SaaS account?**
No. The system runs inside your AI tool — no API keys, subscriptions, or hosted service.

**How do I rewrite an existing listing?**
Paste the current title, all 13 tags, and the full description. The system detects a rewrite, runs the research, and returns an optimized version with a diff view.

**How do I create a new listing?**
Describe the product briefly, for example: *"Funny cat mom SVG bundle, 20 designs, SVG/PNG/EPS, commercial use included."* The system detects a new listing and builds it from scratch.

**Does it work on free tiers?**
Claude.ai, ChatGPT, and Gemini work on free tiers. Perplexity works partially; the URL-fetch dependency in keyword research is less reliable there.

**How does cross-session memory work on the free path?**
Re-paste the session-state snapshot at the start of each new chat (about 30 seconds). On paid Claude, this is automatic via `~/etsy-listings/`.

**What if my problem is not SEO?**
The system says so and points to concrete next steps, rather than rewriting tags that will not help.

**Can I use it for multiple shops?**
Yes. Use a separate chat thread per shop; each thread is its own database.

**Does this tool generate AI listings for me?**
No. It is a human-in-the-loop assistant: you bring the product, photos, and creative decisions; it optimizes the listing and checks it against Etsy policy. Batch mode processes your rows for review — it is not an auto-publish pipeline, because Etsy prohibits bot-generated listings.

**What happens if my product is a pattern, recipe, or instructions?**
The gate checks that the instructions are your own work and that your photos include a real finished result. AI-generated instructions are blocked, and AI images can't be the only evidence of the finished result.

**Is this affiliated with Etsy?**
No. This project is not affiliated with, endorsed by, or sponsored by Etsy, Inc.

---

## Community

- **Contributing guide:** [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Code of Conduct:** [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- **Security policy:** [SECURITY.md](./SECURITY.md) — report vulnerabilities privately, never in a public issue.
- **Questions and ideas:** [GitHub Discussions](https://github.com/moiz-za/etsy-seller-seo-system/discussions)
- **Bug reports and feature requests:** [GitHub Issues](https://github.com/moiz-za/etsy-seller-seo-system/issues)

If this system saves you time, [star the repo](https://github.com/moiz-za/etsy-seller-seo-system/stargazers) — it helps other Etsy sellers find it.

Maintainers pushing from a local clone should enable the leak-guard hook once:

```bash
git config core.hooksPath .githooks
```

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| **2.2.1** | October 2026 | 2026 operations sweep: Payment account/payouts, Purchase Protection, tariffs & DDP, EU PPWR/EPR, policy-violations appeals, review-rating calc |
| **2.2.0** | October 2026 | Etsy AI & image policy (22 Oct 2026): new Law 6 gate, unedited-photo rules, AI disclosure, prohibited AI categories, public policy section |
| 2.1.2 | October 2026 | Sync & consistency: install-path fix, April 2026 title guidance, CI hardening, rule sync |
| 2.1.1 | September 2026 | Archive fix, maintainer-script path sanitization, SellWren links, leak guard |
| 2.1.0 | July 2026 | Caveman Output Mode + 5 Immutable System Laws across skill and portable editions |
| 2.0.2 | July 2026 | Etsy August 2026 Creativity Standards update, `.skill` packaging fix, dual-layout bootstrap |
| 2.0.1 | May 2026 | Free-tier documentation + GitHub language stats fix |
| 2.0.0 | May 2026 | Major restructure: flat listing DB, 2-mode auto-detect, dropped shop concept |
| 1.1.0 | May 2026 | Automation scripts, per-intent description hooks, SEO myths debunked |

See the full [CHANGELOG.md](./CHANGELOG.md) for details.

---

## Author and Maintainer

Engineered and maintained by **Moiz Zoaib Ali**.

- **Personal website:** [moiz.solutions](https://moiz.solutions)
- **AI tools directory:** [tools.moiz.solutions](https://tools.moiz.solutions)
- **Free Etsy seller tools:** [SellWren](https://sellwren.com)
- **GitHub:** [@moiz-za](https://github.com/moiz-za)

---

## License

MIT. Copyright (c) 2026 Moiz Zoaib Ali. Use freely, modify, and share. No warranty. Not affiliated with Etsy, Inc. See [NOTICE](./NOTICE) for trademark attribution.
