# Install Guide

Pick the section matching your AI tool. Each takes 2–5 minutes.

---

## Claude Code / Cowork (full automation, recommended)

### Steps

1. Get the files — clone the repo, or download `etsy-seller.skill` from the [latest release](https://github.com/moiz-za/etsy-seller-seo-system/releases/latest):

   ```bash
   git clone https://github.com/moiz-za/etsy-seller-seo-system.git
   cd etsy-seller-seo-system
   ```

2. Install the skill **and** the state templates into your Claude skills directory.
   (`state-templates/` is required — the skill copies it into `~/etsy-listings/` on first run.)

   **macOS / Linux (from the clone):**
   ```bash
   mkdir -p ~/.claude/skills/etsy-seller
   cp -r skill/. ~/.claude/skills/etsy-seller/
   cp -r state-templates ~/.claude/skills/etsy-seller/
   ```

   **macOS / Linux (from the release archive):**
   ```bash
   mkdir -p ~/.claude/skills/etsy-seller
   unzip etsy-seller.skill -d ~/.claude/skills/etsy-seller/
   ```

   **Windows (PowerShell, from the clone):**
   ```powershell
   New-Item -ItemType Directory -Force $env:USERPROFILE\.claude\skills\etsy-seller | Out-Null
   Copy-Item -Recurse skill\* $env:USERPROFILE\.claude\skills\etsy-seller
   Copy-Item -Recurse state-templates $env:USERPROFILE\.claude\skills\etsy-seller
   ```

3. Restart Claude or reload skills. In Cowork: settings → skills → refresh.

4. Verify install — start a new conversation and paste an existing Etsy listing:

   ```
   Title: Beautiful Handmade Cat Mom SVG Designs for Cricut and Silhouette
   
   Tags: cat svg, cat mom svg, cute cat, cricut cat svg, silhouette, 
   cat lover, cat designs cricut, cat mom design, cute cat svg design,
   cat clipart, cat mom cricut, cute cat mom, cat mom svg design
   
   Description: This listing is for a digital download of cat mom SVG designs...
   ```

   The skill should auto-detect this is a rewrite and produce an optimized version in 30–60 seconds.

### What lives where after install

| Path | Purpose | Managed by |
|---|---|---|
| `~/.claude/skills/etsy-seller/` | The skill itself (SKILL.md, scripts, references, state-templates) | You — update when new version releases |
| `~/etsy-listings/` | Your listing database | Skill — auto-created on first run, auto-updated thereafter |

The two are separate so you can update the skill without losing your listing history.

---

## ChatGPT — Custom GPT (recommended for ChatGPT users)

### Steps

1. ChatGPT → Explore → Create.

2. **Configure tab:**
   - **Name:** Etsy Seller System
   - **Description:** Evidence-driven Etsy SEO optimization for existing and new listings
   - **Instructions:** Paste this short prompt:

     ```
     You are an Etsy listing SEO optimization system. Follow the system 
     defined in the attached knowledge file. Auto-detect REWRITE or CREATE 
     from input shape — title+tags+description = rewrite; short product 
     context = create. Always run Phase 1 policy freshness check, Phase 4 
     live keyword research (Etsy autocomplete + SERP scrape), and Phase 7 
     indexing spread check. Be honest about scope — if the user's problem 
     isn't SEO, say so and route to the action layer pointers playbook.
     ```

   - **Capabilities:** enable **Web Browsing** (required for live keyword research)

3. **Upload knowledge file:**
   - Click "Upload files"
   - Upload `portable/Etsy_Listing_System_Instructions.md`

4. **Save** and test:
   - Start a conversation
   - Paste an existing listing or describe a new product
   - The GPT should auto-detect the action and produce the universal output block

### State management (manual)

ChatGPT can't write files to your computer. To maintain a listing database:
- At the end of every session, the GPT outputs a "SESSION STATE" markdown block
- Copy it. Save it anywhere (Notes, Drive, plain text file)
- At the start of your next session, paste it back in the first message
- The GPT loads it as context and continues from where you left off

If you're working on multiple shops, use separate ChatGPT conversations — each chat is its own database.

---

## Perplexity — Spaces

### Steps

1. **Create a new Space.** Perplexity → Spaces → New Space.

2. **Name it:** "Etsy Seller System"

3. **Add knowledge file:** Spaces settings → Files → Upload → `portable/Etsy_Listing_System_Instructions.md`

4. **Custom instructions:**
   ```
   Follow the Etsy SEO system defined in the uploaded file. Auto-detect 
   REWRITE vs CREATE from input shape. Use Perplexity search to perform 
   live keyword research — search Etsy autocomplete suggestions and 
   competitor listings for the target keyword.
   ```

5. **Save** and test.

### Limitations specific to Perplexity

- Perplexity is search-first, not fetch-first. The autocomplete endpoint won't work directly — Perplexity falls back to its search-based discovery (documented in the portable doc Phase 4A fallback path).
- Expect ~70% of the system's accuracy compared to tools that fetch URLs directly (Claude/Cowork).
- State management: same manual session-snapshot pattern as ChatGPT.

---

## Gemini — Gem

### Steps

1. **Create a new Gem.** gemini.google.com → Gems → New Gem.

2. **Custom instructions:** paste the full content of `portable/Etsy_Listing_System_Instructions.md`. Gemini Gems support large instruction blocks.

3. **Save** and test.

### State management

Same manual session-snapshot pattern as ChatGPT.

---

## Updating to a new version

When a new release of `etsy-seller-seo-system` comes out:

**Claude / Cowork users:**
1. Replace the contents of `~/.claude/skills/etsy-seller/` with the new `skill/` + `state-templates/` contents (or unzip the new `etsy-seller.skill` into it)
2. Your `~/etsy-listings/` state is preserved automatically
3. Check `CHANGELOG.md` for any schema version bumps — rare, but if schema changes you may need to migrate state files

**Upgrading to 2.2.0 (Etsy AI & image policy):** no state migration is needed. The new `AI & image compliance` block is optional and is written the next time the skill touches each listing. Re-copy `skill/` and `state-templates/` (or reinstall the `.skill`) to pick up the new Law 6 gate.

**Other tool users:**
1. Re-upload `portable/Etsy_Listing_System_Instructions.md` to your GPT/Space/Gem
2. Your saved session-state snapshots stay valid (we maintain backwards compatibility within a major version)

---

## Troubleshooting

**"The skill isn't running web search"** — make sure web browsing/search is enabled in your AI tool's settings. The skill needs Phase 1 (policy check) and Phase 4 (live keyword research) to actually search.

**"It's asking too many questions"** — the auto-detection might be failing for your input shape. Try being more explicit: paste your existing listing with clear `Title:`, `Tags:`, `Description:` labels, OR write a sentence describing your new product with formats inside.

**"State files keep getting recreated"** — `~/etsy-listings/` may have been deleted or renamed. Check the path. If you want a different location, edit the SKILL.md and bootstrap.py to use the path you want.

**"Duplicate primary keyword warning fired but I want both listings"** — that's fine, just choose option [b] (keep both). The skill respects your decision.

**"The output is missing the SESSION STATE block"** — only appears for non-Cowork tools. In Cowork, state is auto-written to disk, no snapshot needed.

**"It says my listing is in a Very High difficulty niche"** — the platform-fit-check playbook is doing its job. Read the suggestions; you can override and proceed if you want.

---

## Sharing this with others

The entire `etsy-seller-seo-system/` folder is self-contained and freely shareable.

1. Zip the folder, or share the GitHub repo link
2. Recipient follows this INSTALL.md for their AI tool
3. Recipient starts with their own fresh state

No accounts, no API keys, no subscriptions. The only requirement is web search access in the AI tool of choice.

---

## Next step: SellWren

If you'd rather have these rules as instant point-and-click tools — tag verifier, title builder, IP scanner, description builder, plus a live shop dashboard — try the free tools at [sellwren.com/tools](https://sellwren.com/tools). Same team, same rulebooks, no account needed. SellWren for Desktop (one-time license) is coming soon — waitlist at [sellwren.com](https://sellwren.com).
