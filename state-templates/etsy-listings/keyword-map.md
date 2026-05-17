# Keyword Map

**Schema version:** 2.0
**Last updated:** (auto-updated by skill)

This is the master index of every listing in your database with its primary keyword. The skill reads this file on every REWRITE or CREATE to check whether a candidate primary keyword overlaps with an existing listing's cluster.

When you have many listings, this file becomes a quick at-a-glance view of your portfolio's keyword coverage.

---

## Listings

| Listing ID | Short slug | Primary keyword | Cluster words | Secondary keywords | Difficulty | Assigned | Status |
|---|---|---|---|---|---|---|---|

*The skill appends rows here automatically after every REWRITE or CREATE. The example row below shows the format; it gets removed once you have real listings.*

| L001 | _example-slug_ | _example primary kw_ | _word1;word2;word3_ | _sec phrase 1;sec phrase 2_ | _Medium_ | _YYYY-MM-DD_ | _example_ |

---

## Notes

- Listing IDs (L001, L002, ...) are permanent. They survive title rewrites and re-keywording.
- Cluster words are semicolon-separated. Used for the keyword reuse check (Phase 5).
- The skill writes to this file using its Edit/Write tools — no Python scripting needed for ongoing updates.
- Status values: `active` / `archived` / `paused`.
