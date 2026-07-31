<div align="center">

# Etsy Seller SEO System

### by [Moiz Solutions](https://tools.moiz.solutions)

[![Version](https://img.shields.io/badge/version-2.1.0-blue?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Schema](https://img.shields.io/badge/schema-2.1-blue?style=flat-square)](skill/references/data-model/SCHEMA.md)
[![Policy](https://img.shields.io/badge/Etsy_policy-August_2026-green?style=flat-square)](skill/references/policies.md)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](#-contributing)
[![Status](https://img.shields.io/badge/status-stable-success?style=flat-square)]()

**Honest, evidence-driven Etsy SEO optimization for AI tools.** Paste a listing → get back an optimized one. No shop registration, no setup forms, no nonsense.

**The honest version of what most "Etsy SEO tools" pretend to be.**

**100% free-tier compatible** — runs inside Claude, ChatGPT, Perplexity, or Gemini. No paid SaaS, no API keys, no servers.

---

</div>

## 📖 Table of Contents

- [Features](#-features)
- [What It Won't Do](#-what-it-explicitly-wont-do)
- [Installation](#-installation)
- [How It Works](#-how-it-works)
- [Free vs Paid](#-free-vs-paid)
- [Comparison](#-comparison-other-etsy-seo-tools-vs-this-system)
- [Who It's For](#-who-its-for)
- [Realistic Expectations](#-realistic-expectations)
- [Repository Structure](#-repository-structure)
- [Companion Repository](#-companion-repository)
- [FAQ](#-faq)
- [Changelog](#-changelog)
- [Contributing](#-contributing)
- [Author & Maintainer](#-author--maintainer)
- [License](#-license)

---

## 🚀 Features

### 🦣 Caveman Output Mode
- Crisp, high-density, bullet-first output style — cuts token consumption by up to **70%**
- Full raw SERP breakdowns and keyword tracking stay in state and unlock on demand (`"expand"`, `"full report"`)

### 📜 5 Immutable System Laws
Non-bypassable execution discipline (`skill/references/playbooks/system-laws.md`):
1. **Zero state skips** — sequential mode workflows with difficulty assessment and output phases
2. **Zero hallucination** — live search data or explicit `[Data Source: Reasoning Engine Fallback]` tagging
3. **Strict listing rules** — exactly 13 tags, every tag ≤20 chars, max 2 tags share a phrase cluster
4. **Caveman output protocol** — concise by default, details on request
5. **Strict format mandate** — mandatory title formula, title word count, no-emoji rule, Etsy 2026 AI Disclosure

### 🔍 Live Research Engine
- **Real Etsy autocomplete** — what buyers are actually typing right now
- **Top 10 competitor SERP scraping** — learn what's winning for your keyword
- **Competition difficulty assessment** — tells you if your keyword is realistic or hopeless

### ✍️ Optimized Listing Output
- Mandatory title formula `[Primary Keyword] [Style Descriptor] | [Format]` in the first **40 characters** (mobile preview line included)
- **6–12 word title limit (max 14)** + explicit **Prohibited Subjective Words Stoplist** (`cute`, `beautiful`, etc.)
- All **13 tags verified ≤20 chars** with refined phrase-overlap rules (max 2 tags share a 2-word cluster)
- **Zero emojis** in description text or section headers — clean formatting + screen-reader accessibility
- **NLP-aware natural-language writing** — no keyword chains (Etsy 2026 penalizes those)

### 🛡️ Trademark & Policy Guard
- Catches **trademarked words** before your listing gets taken down
- Checks **Etsy's current 2026 policies** every session via the **Automated Dual-Repo Policy Sync Engine** (`skill/scripts/sync_etsy_policy.py`) — zero policy drift
- **Platform fit check** — reality check on saturated niches (>100K results) *before* building the listing

### 🧠 Honest Scope Diagnosis
- Tells you **when your problem isn't SEO** — and what it actually is
- Action layer pointers with real competitor data, price ranges, and free-tool recommendations
- **Diff view for rewrites** — shows exactly what changed from your original and why

### 📌 Pinterest Content
- Generates **Pinterest marketing content** with explicit 220–232 char count & adjust guidance
- Compound external SEO beyond Etsy's walls

### 💾 Cross-Session Memory
- Remembers your listings **across sessions** (on Claude) — no duplicate keyword suggestions
- Silent local database at `~/etsy-listings/` — keyword map, refresh schedule, listing state
- Keyword reuse soft warning with sibling-phrase suggestions

---

## 🚫 What It Explicitly Won't Do

- Won't pretend an SEO rewrite will fix a **hero-image problem**
- Won't claim a tag rewrite will save a listing with a **0.3% conversion rate**
- Won't promise you'll **rank #1**
- Won't create images, videos, or mockups for you (writes briefs only)

When your problem isn't SEO, **it says so**, then points you to concrete next steps with real data (competitor hero-image patterns, price ranges, free tools, etc.).

---

## 🔧 Installation

### Option 1: Claude / Cowork (full automation, recommended)

```bash
git clone https://github.com/moiz-za/etsy-seller-seo-system.git
cd etsy-seller-seo-system
cp -r skill ~/.claude/skills/etsy-seller
```

Restart Claude. On your first listing input, the skill auto-creates `~/etsy-listings/` and starts tracking everything. You never have to manage files.

### Option 2: ChatGPT / Perplexity / Gemini

Upload `portable/Etsy_Listing_System_Instructions.md` as a knowledge file to your Custom GPT / Space / Gem. Enable web browsing. Done.

See [INSTALL.md](./INSTALL.md) for detailed steps per tool.

---

## ⚙️ How It Works

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

That's the whole interaction. **No mode selection. No "which shop?" prompts. No setup forms.**

---

## 💰 Free vs Paid

Most paid Etsy SEO tools lock everything behind a **$9–$50/month subscription**. This system is built so you don't have to pay anyone — not Anthropic, not OpenAI, not me. There's a free path that takes 5 minutes to set up and costs **$0**.

### The free path

1. Sign up free at [claude.ai](https://claude.ai), [chatgpt.com](https://chatgpt.com), or [gemini.google.com](https://gemini.google.com)
2. Open [`portable/Etsy_Listing_System_Instructions.md`](./portable/Etsy_Listing_System_Instructions.md) and copy the entire contents
3. Start a new chat in your AI tool, paste the doc as your first message
4. Reply with: *"OK, follow this system. Here's my listing: [paste your listing]"*

The AI follows the instructions and produces an optimized listing. That's it.

### What works on free tiers

| Tool | Free tier works? | Notes |
|---|---|---|
| **Claude.ai (free)** | Yes | Daily message cap; web search enabled. Paste portable doc as first message. |
| **ChatGPT (free)** | Yes | Has browsing on free tier. Same paste-first-message pattern. |
| **Gemini (free)** | Yes | Web search available; handles long instructions well. |
| **Perplexity (free)** | Partial | Basic search works but the URL-fetch dependency in keyword research is less reliable on free tier. |

### What you keep on the free path

- All SEO rules (title / tags / attributes / description)
- Live Etsy autocomplete + competitor SERP research (if web browsing is enabled)
- Trademark stoplist scan — protects your listing from takedown
- Honest scope diagnosis — tells you when your problem isn't SEO
- Per-intent description hooks, indexing spread check, Pinterest content, pre-publish checklist
- All operational playbooks

### What you lose on the free path

- **Cross-session memory** — re-paste your session-state snapshot at the start of every new chat (a 30-second copy-paste)
- **Automatic folder management** — no local `~/etsy-listings/` database; everything lives in the chat thread
- **Daily message limits** — free tiers cap how much you can do per day

### When the paid path makes sense

If you're optimizing **30+ listings** or running multiple shops, the paid Claude path saves real time:

- **Claude Code** (terminal) — needs Claude Pro/Max or API credits
- **Cowork** (Claude desktop app) — needs Claude Pro/Max

Copy the `skill/` folder to `~/.claude/skills/etsy-seller/` and the system handles everything automatically: silent folder creation, cross-session memory, no copy-paste between sessions.

**The skill content is identical on both paths.** The paid path just removes the manual copy-paste friction. If you're optimizing 1–5 listings, the free path is more than enough.

---

## ⚖️ Comparison: Other Etsy SEO Tools vs This System

| Feature | Most Etsy SEO tools | This system |
|---|---|---|
| Keyword research | Static keyword lists, guesses | Live Etsy autocomplete + SERP scraping |
| Tag char limits | Doesn't enforce | Verified ≤20 chars on every tag |
| Etsy algorithm | Old advice from 2018–2022 | 2026 NLP-aware, natural language |
| Diagnostic honesty | "Use these tags and you'll explode" | "Your problem isn't SEO — here's what is" |
| State across sessions | None or paid SaaS | Free local markdown files |
| Cost | $9–$50/month | $0 — runs inside your AI tool |
| Setup | Account + login + onboarding | Drop folder into ~/.claude/skills/ |

---

## 🎯 Who It's For

- **Etsy sellers** whose listings aren't getting impressions and want to know why
- **Anyone launching new listings** who wants them optimized from day one
- **SEO consultants** managing listings for multiple clients (multi-shop = multi-thread in your AI tool)
- **Sellers running multiple shops** who want one tool that handles all of them

---

## 📈 Realistic Expectations

This is an SEO tool. It does SEO well. If your only problem is bad SEO, this can produce a meaningful traffic lift — typically **20–40% impression improvement** on rewritten listings within 30 days.

If your problem isn't SEO — weak photos, wrong price, no reviews, saturated niche — this tool will tell you that honestly and route you to what would actually work. That honesty matters more than another set of rewritten tags.

---

## 📦 Repository Structure

```
etsy-seller-seo-system/
├── README.md                   ← you're here
├── INSTALL.md                  ← step-by-step setup per AI tool
├── CHANGELOG.md                ← version history
├── LICENSE                     ← MIT
│
├── skill/                      ← drop into ~/.claude/skills/etsy-seller/
│   ├── SKILL.md                ← the orchestrator (2 modes + auto-detect)
│   ├── scripts/
│   │   ├── bootstrap.py        ← silent state init on first run
│   │   └── sync_etsy_policy.py ← dual-repo policy sync engine
│   └── references/
│       ├── data-model/SCHEMA.md ← state file formats
│       ├── listing-guide.md     ← title/tag/attribute/description rules
│       ├── seo-guide.md         ← 2026 Etsy algorithm details
│       ├── policies.md          ← Etsy policies (August 2026)
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

## 🤝 Companion Repository

Designed to work alongside [`svg-design-intelligence-system`](https://github.com/moiz-za/svg-design-intelligence-system) — that repo handles market research, buyer psychology, IP risk screening, and prompt engineering to create original SVG digital products *before* publishing.

- **ESVG-DIS System** creates the right *product*.
- **Etsy Seller SEO System** creates the right *listing*.

Neither depends on the other; use either independently or together.

---

## ❓ FAQ

**Q: Is there really a free path?**  
A: Yes. Paste `portable/Etsy_Listing_System_Instructions.md` into any free-tier chat (Claude.ai, ChatGPT, Gemini). You keep all SEO rules, live research (with web browsing), trademark scan, and honest diagnosis. See [Free vs Paid](#-free-vs-paid).

**Q: Do I need API keys or a paid SaaS account?**  
A: No. The system runs entirely inside your AI tool. No API keys, no subscriptions, no hosted service.

**Q: How do I rewrite an existing listing that isn't getting traffic?**  
A: Paste your current title, all 13 tags, and full description. The skill auto-detects a rewrite, does the research, and returns an optimized version with a diff view showing exactly what changed.

**Q: How do I create a new listing?**  
A: Type a short description — e.g. *"Funny cat mom SVG bundle, 20 designs, SVG/PNG/EPS, commercial use included"*. The skill auto-detects a new listing and builds everything from scratch.

**Q: Does it work on the free tier of my AI tool?**  
A: Claude.ai, ChatGPT, and Gemini work on free tiers. Perplexity works partially (URL-fetch dependency in keyword research is less reliable on free tier).

**Q: How does cross-session memory work on the free path?**  
A: Re-paste your session-state snapshot at the start of each new chat — a 30-second copy-paste. On Claude (paid), it's automatic via `~/etsy-listings/`.

**Q: What if my problem isn't SEO?**  
A: The system tells you honestly and points to real next steps — competitor hero-image patterns, price ranges, free tools — instead of selling you fake-fix tag rewrites.

**Q: Can I use it for multiple shops?**  
A: Yes. Multi-shop sellers use separate chat threads — each thread is its own database. No shop registry or cross-shop architecture required.

**Q: Is this affiliated with Etsy?**  
A: No. Not affiliated with Etsy, Inc.

---

## 📋 Changelog

Recent highlights:

| Version | Date | Summary |
|---------|------|---------|
| **2.1.0** | 2026-07 | Caveman Output Mode + 5 Immutable System Laws across skill and portable editions |
| 2.0.2 | 2026-07 | Etsy August 2026 Creativity Standards update, `.skill` packaging fix, dual-layout bootstrap |
| 2.0.1 | 2026-05 | Free-tier documentation + GitHub language stats fix |
| 2.0.0 | 2026-05 | Major restructure: flat listing DB, 2-mode auto-detect, dropped shop concept |
| 1.1.0 | 2026-05 | Automation scripts, per-intent description hooks, SEO myths debunked |

See full [CHANGELOG.md](./CHANGELOG.md) for details.

---

## 🤝 Contributing

This system is opinionated and built around the 2026 Etsy algorithm. If Etsy changes its rules (and it will), this needs updates. Welcome contributions:

- Updates to `skill/references/seo-guide.md` for algorithm changes
- Updates to `skill/references/policies.md` for policy changes
- Additions to `skill/references/playbooks/trademark-stoplist.md` for newly trademarked franchises
- New playbooks for genuinely new operational patterns

Avoid:
- Adding new "modes" — the system is intentionally 2-mode
- Re-introducing shop concept / multi-shop architecture
- Anything that violates the scope-honesty principle (no fake-fixes)

---

## 👤 Author & Maintainer

Engineered and maintained by **Moiz Zoaib Ali**:
- **Personal Website:** [moiz.solutions](https://moiz.solutions)
- **AI Tools Directory:** [tools.moiz.solutions](https://tools.moiz.solutions)
- **GitHub Profile:** [@moiz-za](https://github.com/moiz-za)

---

## 📄 License

MIT — Copyright (c) 2026 Moiz Zoaib Ali. Use freely, modify, share. No warranty. Not affiliated with Etsy.

---

<div align="center">

**Built by [Moiz Solutions](https://tools.moiz.solutions)** · Report issues on [GitHub](https://github.com/moiz-za/etsy-seller-seo-system/issues)

*Built with stubborn opinions about Etsy SEO and zero tolerance for advice that doesn't work.*

</div>
