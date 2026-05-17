# Refresh Schedule

**Schema version:** 2.0
**Last updated:** (auto-updated by skill)

This is when each listing in your database is due for its next refresh. Etsy gradually demotes listings that go untouched for 90+ days; the skill helps you maintain a refresh cadence to prevent this decay.

---

## Cadence rules

- **Minor refresh:** every 90 days. One tag swap, one attribute update, or hero alt text refresh.
- **Full review:** every 180 days. Re-run Phase 4 keyword research; rewrite if needed.

**Priority levels** are computed against today's date:
- **P1** = overdue (next minor refresh date already passed)
- **P2** = within 30 days
- **P3** = within 90 days
- **Recent** = touched in last 90 days; skip

---

## Schedule

| Listing ID | Last full edit | Last minor edit | Next minor | Next full review | Priority | Notes |
|---|---|---|---|---|---|---|

*Example row format (gets removed once you have real listings):*

| L001 | YYYY-MM-DD | YYYY-MM-DD | YYYY-MM-DD | YYYY-MM-DD | P3 | _Initial creation_ |

---

## Notes

- The skill updates dates on every listing touch.
- To find what to refresh this week, ask the skill: "What's due for refresh?" → it scans this file and returns the P1 + P2 listings.
