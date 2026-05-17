# SQR Imports

This folder stores raw Search Query Report (SQR) data pasted from Etsy Shop Stats.

## How to import SQR data

1. In Etsy: Shop Manager → Stats → click on the listing → "Search Terms" tab
2. Set window to last 30 days
3. Manually copy the table (Etsy does not offer CSV export)
4. In your AI chat: paste the table — the skill auto-detects the SQR shape and processes it

The skill will:
- Identify the listing it relates to (matches against existing keyword-map entries by title or asks if ambiguous)
- Compare the SQR queries against your current primary keyword
- Recommend a pivot if a different query is outperforming
- Write a new file here: `YYYY-MM-DD_L###.md`

## File naming

```
YYYY-MM-DD_L###.md
```

Example: `2026-06-14_L007.md` = SQR for listing L007 imported on June 14, 2026.

## Why keep old imports

The skill compares current SQR against earlier imports to detect:
- Keywords gaining traction (rising impressions)
- Keywords decaying (dropping impressions — often signals competitor entry)
- New query patterns appearing
- Lost queries (you fell off page 1)

Retain SQR files for 12 months minimum.
