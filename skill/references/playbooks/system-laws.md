# Playbook — Immutable System Laws & Execution Discipline

This playbook establishes the non-bypassable **5 Immutable System Laws** governing the Etsy Seller SEO System. All AI agents, reasoning models, and portable single-file instructions MUST adhere strictly to these laws during workflow execution.

---

## 📜 The 5 Immutable System Laws

### ⚖️ Law 1: Immutable Operational Integrity
- **Directive:** Every workflow execution MUST process all operational steps (Intake, Mode Auto-Detection, Keyword Research, SERP Scraping, Competition Difficulty Assessment, Title/Tag/Attribute/Description Construction, and Pinterest Marketing Block) sequentially without skipping or shortcutting.
- **Rule:** No operational state or check may ever be simulated, glossed over, or silently ignored. Internal reasoning must process every check sequentially even when rendering a concise Caveman Mode output summary.

### 🔍 Law 2: Zero-Hallucination Evidence Traceability
- **Directive:** All research metrics, search difficulty assessments, competitor listings, autocomplete suggestions, and trademark statuses must be grounded in empirical data or explicitly tagged.
- **Rule:** If live web search is unavailable or offline, qualitative estimates MUST be explicitly tagged with `[Data Source: Reasoning Engine Fallback]`. Never invent numbers, fake competitor stats, or fabricate autocomplete search volume.

### 🏷️ Law 3: Mandatory 20-Character Tag Limit & Overlap Rules
- **Directive:** Every tag MUST be strictly verified against Etsy's silent character limit and overlap guardrails.
- **Rule:**
  - Exactly 13 tags (never leave tag slots blank).
  - Every tag MUST be **≤ 20 characters** (including spaces). Tags >20 chars are silently rejected by Etsy.
  - **Phrase Overlap Limit:** No exact 2+ word phrase may repeat across more than 2 tags (maximum 2 tags may share a 2-word phrase cluster).
  - Zero emojis or special symbols in tags.
  - Output character count verification per tag (`[Tag] ([X] chars ✅)`).

### 🦣 Law 4: Caveman Output Protocol & Token Efficiency
- **Directive:** Output responses MUST be concise, high-density, bullet-first, and zero-fluff ("Caveman Mode") to minimize token consumption while maintaining 100% analytical depth in local session memory (`~/etsy-listings/`).
- **Rule:** Strip conversational preamble, repetitive introductions, and excessive prose by default. Full raw SERP breakdowns or multi-column data matrices MUST remain preserved in state memory and rendered only when explicitly requested by the user (`"expand"`, `"full report"`, `"show details"`).

### 📝 Law 5: Strict Listing Format & No-Emoji Mandate
- **Directive:** All listing packages MUST strictly follow the canonical listing structure (`listing-guide.md`).
- **Rule:**
  - **Title Formula:** `[Primary Keyword] [Style Descriptor] | [Format]` with primary keyword in the **first 40 characters**.
  - **Title Word Limit:** 6 to 12 words (ABSOLUTE MAXIMUM: 14 words; reject titles with 15+ words).
  - **Prohibited Subjective Words Stoplist (ZERO ALLOWED):** `cute`, `adorable`, `beautiful`, `perfect`, `stunning`, `amazing`, `incredible`, `pretty`, `awesome`, `gorgeous`, `lovely`, `sweet`, `unique`, `best`, `top`, `wonderful`, `charming`.
  - **No-Emoji Mandate:** Zero emojis allowed in description text or section headers (prevents spam signals and ensures screen-reader accessibility).
  - **Mandatory Sections:** Meta zone (first 160 chars), Included Formats, Compatibility, Usage License, Etsy 2026 AI Creation Disclosure, Hero Alt Text, and Pinterest Marketing Block.

---

## ⛔ Non-Compliance Audit Signals
Any execution exhibiting the following defects violates the System Laws and MUST be corrected immediately:
- ❌ Outputting tags over 20 characters in length.
- ❌ Outputting subjective filler words (`cute`, `stunning`, `perfect`) in titles.
- ❌ Using emojis in listing description text or section headers.
- ❌ Omitting the Etsy AI Creation Disclosure settings.
- ❌ Outputting bloated, conversational prose when Caveman Mode is active.
