# Scripts

A single utility script that handles state initialization for the etsy-seller skill.

## `bootstrap.py`

**Purpose:** create `~/etsy-listings/` with empty markdown templates on the first skill invocation. Idempotent — does nothing on subsequent runs.

**Called from:** SKILL.md Phase 0 (auto-bootstrap), every run.

**Dependencies:** Python 3.8+. Pure stdlib — no openpyxl, no third-party packages.

**Manual usage (not normally needed):**

```bash
# Default — creates ~/etsy-listings/ if missing
python3 bootstrap.py

# Custom state location
python3 bootstrap.py --state-dir /custom/path

# Quiet mode (no stdout)
python3 bootstrap.py --quiet
```

## Why this is bash, not Python imports

The skill runs INSIDE an AI tool (Claude/Cowork). The AI executes shell commands to invoke this script. Keeping it as a standalone CLI makes it:
- Testable on its own
- Portable across AI tools that support bash
- Independent of the AI tool's Python runtime

Once state is bootstrapped, the AI uses its native Edit/Write tools to update markdown state files directly — no Python scripting needed for ongoing operations.

## What state files this creates

Reads from `state-templates/etsy-listings/` (sibling to `skill/`):

```
~/etsy-listings/
├── keyword-map.md
├── refresh-schedule.md
├── listings/
│   └── _TEMPLATE_listing.md     (the AI references this when creating new L###-*.md files)
└── sqr-imports/
    └── README.md                (instructions for SQR paste workflow)
```
