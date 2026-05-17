# Etsy Seller System

> Honest, evidence-driven Etsy SEO optimization for AI tools. Paste a listing → get back an optimized one. No shop registration, no setup forms, no nonsense.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0-blue.svg)]()
[![Schema](https://img.shields.io/badge/schema-2.0-blue.svg)]()
[![Policy](https://img.shields.io/badge/Etsy_policy-May_2026-green.svg)]()

---

## What this is

An Etsy SEO assistant that runs inside Claude (or pasted into ChatGPT, Perplexity, Gemini). You give it your listing — either an existing one that isn't getting traffic, or a short description of a new product — and it gives you back an optimized version: title, tags, description, attributes, Pinterest content, all built from **live Etsy search data** (real autocomplete + real competitor SERP scraping).

**The honest version of what most "Etsy SEO tools" pretend to be.**

---

## What it actually does (the short list)

- ✅ Pulls **live Etsy autocomplete** for what buyers are actually typing right now
- ✅ Scrapes the **top 10 competitor listings** for your keyword to learn what's winning
- ✅ Assesses **competition difficulty** — tells you if your keyword is realistic or hopeless
- ✅ Builds a **title** with your primary keyword in the first 40 characters (the part shown on mobile)
- ✅ Verifies all 13 tags are **under Etsy's silent 20-character limit** (the #1 cause of "I published but nothing happened")
- ✅ Catches **trademarked words** before your listing gets taken down
- ✅ Checks **Etsy's current policies** every session (policies change)
- ✅ Uses **NLP-aware natural-language writing** (no keyword chains — Etsy 2026 penalizes those)
- ✅ Generates **Pinterest content** for compound external SEO
- ✅ Remembers your listings **across sessions** (on Claude) so it doesn't suggest duplicate keywords

## What it explicitly will NOT do

- ❌ Won't pretend an SEO rewrite will fix a hero-image problem
- ❌ Won't claim a tag rewrite will save a listing with a 0.3% conversion rate
- ❌ Won't promise you'll rank #1
- ❌ Won't create images, videos, or mockups for you (writes briefs only)

When your problem isn't SEO, **it says so**, then points you to concrete next steps with real data (competitor hero-image patterns, price ranges, free tools, etc.).

---

## Quick start

### Option A — Claude / Cowork (full automation, recommended)

```bash
# Clone or download this repo, then:
cp -r skill ~/.claude/skills/etsy-seller
```

Restart Claude. Done. On your first listing input, the skill auto-creates `~/etsy-listings/` and starts tracking everything. You never have to manage files.

### Option B — ChatGPT / Perplexity / Gemini

Upload `portable/Etsy_Listing_System_Instructions.md` as a knowledge file to your Custom GPT / Space / Gem. Enable web browsing. Done.

See [INSTALL.md](INSTALL.md) for detailed steps per tool.

---

## Using this for free (no paid account)

Most paid Etsy SEO tools lock everything behind a $9–$50/month subscription. This system is built so you don't have to pay anyone — not Anthropic, not OpenAI, not me. There's a free path that takes 5 minutes to set up and costs $0.

### The free path

1. Sign up free at [claude.ai](https://claude.ai), [chatgpt.com](https://chatgpt.com), or [gemini.google.com](https://gemini.google.com)
2. Open [`portable/Etsy_Listing_System_Instructions.md`](portable/Etsy_Listing_System_Instructions.md) from this repo and copy the entire contents
3. Start a new chat in your AI tool, paste the doc as your first message
4. Reply with: *"OK, follow this system. Here's my listing: [paste your listing]"*

The AI follows the instructions and produces an optimized listing. That's it.

### What works on free tiers

| Tool | Free tier works? | Notes |
|---|---|---|
| **Claude.ai (free)** | ✅ Yes | Daily message cap; web search enabled. Paste portable doc as first message. |
| **ChatGPT (free)** | ✅ Yes | Has browsing on free tier. Same paste-first-message pattern. |
| **Gemini (free)** | ✅ Yes | Web search available; handles long instructions well. |
| **Perplexity (free)** | ⚠️ Partial | Basic search works but the URL-fetch dependency in keyword research is less reliable on free tier. |

### What you keep on the free path

- ✅ All SEO rules (title / tags / attributes / description)
- ✅ Live Etsy autocomplete + competitor SERP research (if web browsing is enabled)
- ✅ Trademark stoplist scan — protects your listing from takedown
- ✅ Honest scope diagnosis — tells you when your problem isn't SEO
- ✅ Per-intent description hooks, indexing spread check, Pinterest content, pre-publish checklist
- ✅ All 10 operational playbooks

### What you lose on the free path

- ❌ Cross-session memory — re-paste your session-state snapshot at the start of every new chat (it's a 30-second copy-paste)
- ❌ Automatic folder management — no local `~/etsy-listings/` database; everything lives in the chat thread
- ⚠️ Daily message limits — free tiers cap how much you can do per day

### When the paid path makes sense

If you're optimizing 30+ listings or running multiple shops, the paid Claude path saves real time:

- **Claude Code** (terminal) — needs Claude Pro/Max or API credits
- **Cowork** (Claude desktop app) — needs Claude Pro/Max

Copy the `skill/` folder to `~/.claude/skills/etsy-seller/` and the system handles everything automatically: silent folder creation, cross-session memory, no copy-paste between sessions.

**The skill content is identical on both paths.** The paid path just removes the manual copy-paste friction. If you're optimizing 1–5 listings, the free path is more than enough.

---

## How you use it (the simplest possible flow)

**Rewriting an existing listing that isn't getting traffic:**

> Paste your current title, all 13 tags, and full description. The skill auto-detects this is a rewrite, does the research, and returns an optimized version.

**Creating a new listing:**

> Type a short description: *"Funny cat mom SVG bundle, 20 designs, SVG/PNG/EPS, commercial use included"*. The skill auto-detects this is a new listing, does the research, and builds everything from scratch.

That's the whole interaction. No mode selection. No "which shop?" prompts. No setup forms.

---

## What's in the box

```
etsy-seller-system/
├── README.md                              ← you're here
├── INSTALL.md                             ← step-by-step setup per AI tool
├── CHANGELOG.md                           ← version history
├── LICENSE                                ← MIT
│
├── skill/                                 ← drop into ~/.claude/skills/etsy-seller/
│   ├── SKILL.md                           ← the orchestrator (2 modes + auto-detect)
│   ├── scripts/
│   │   └── bootstrap.py                   ← silent state init on first run
│   └── references/
│       ├── data-model/SCHEMA.md           ← state file formats
│       ├── listing-guide.md               ← title/tag/attribute/description rules
│       ├── seo-guide.md                   ← 2026 Etsy algorithm details
│       ├── policies.md                    ← Etsy policies (May 2026)
│       ├── operations.md                  ← fees, Star Seller, cases, diagnostics
│       ├── pinterest-guide.md             ← Pinterest strategy
│       └── playbooks/                     ← 10 operational playbooks
│
├── portable/                              ← single self-contained doc for non-Claude tools
│   └── Etsy_Listing_System_Instructions.md
│
└── state-templates/                       ← markdown templates auto-copied on first run
    └── etsy-listings/
        ├── keyword-map.md
        ├── refresh-schedule.md
        ├── listings/_TEMPLATE_listing.md
        └── sqr-imports/README.md
```

---

## Who this is for

- **Etsy sellers** whose listings aren't getting impressions and want to know why
- **Anyone launching new listings** who wants them optimized from day one
- **SEO consultants** managing listings for multiple clients (multi-shop = multi-thread in your AI tool)
- **Sellers running multiple shops** who want one tool that handles all of them

---

## What makes it different from other Etsy SEO tools

| Feature | Most Etsy SEO tools | This system |
|---|---|---|
| Keyword research | Static keyword lists, guesses | Live Etsy autocomplete + SERP scraping |
| Tag char limits | Doesn't enforce | Verified ≤20 chars on every tag |
| Etsy algorithm | Old advice from 2018–2022 | May 2026 NLP-aware, natural language |
| Diagnostic honesty | "Use these tags and you'll explode" | "Your problem isn't SEO — here's what is" |
| State across sessions | None or paid SaaS | Free local markdown files |
| Cost | $9–$50/month | $0 — runs inside your AI tool |
| Setup | Account + login + onboarding | Drop folder into ~/.claude/skills/ |

---

## Realistic expectations

This is an SEO tool. It does SEO well. If your only problem is bad SEO, this can produce a meaningful traffic lift — typically 20–40% impression improvement on rewritten listings within 30 days.

If your problem isn't SEO — weak photos, wrong price, no reviews, saturated niche — this tool will tell you that honestly and route you to what would actually work. That honesty matters more than another set of rewritten tags.

---

## Contributing

This system is opinionated and built around the May 2026 Etsy algorithm. If Etsy changes its rules (and it will), this needs updates. Welcome contributions:

- Updates to `skill/references/seo-guide.md` for algorithm changes
- Updates to `skill/references/policies.md` for policy changes
- Additions to `skill/references/playbooks/trademark-stoplist.md` for newly trademarked franchises
- New playbooks for genuinely new operational patterns

Avoid:
- Adding new "modes" — the system is intentionally 2-mode
- Re-introducing shop concept / multi-shop architecture
- Anything that violates the scope-honesty principle (no fake-fixes)

See [CHANGELOG.md](CHANGELOG.md) for what's changed across versions.

---

## License

MIT — use freely, modify, share. No warranty. Not affiliated with Etsy.

---

## Acknowledgments

Built with stubborn opinions about Etsy SEO and zero tolerance for advice that doesn't work.
