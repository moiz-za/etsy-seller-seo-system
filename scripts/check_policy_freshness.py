#!/usr/bin/env python3
"""Check how old the Etsy policy baseline is.

Reads the ``**Policy baseline: 22 October 2026.**`` line from
``skill/references/policies.md`` and compares it with today (UTC).

Used by the monthly Policy Freshness workflow. Exits 0 regardless of the
result so the workflow can decide what to do; stale state is reported through
``stale`` / ``age_days`` / ``baseline`` step outputs when running in GitHub
Actions, and through stdout everywhere else.

Maintainer utility — not needed for normal skill usage.
"""

import argparse
import datetime as dt
import os
import pathlib
import re
import sys

BASELINE_RE = re.compile(
    r"\*\*Policy baseline:\s*(\d{1,2}\s+[A-Za-z]+\s+\d{4})\.?\*\*"
)
DATE_FORMATS = ("%d %B %Y", "%d %b %Y")


def read_baseline(policies_path: pathlib.Path) -> dt.date:
    if not policies_path.exists():
        raise SystemExit(f"ERROR: {policies_path} not found")
    match = BASELINE_RE.search(policies_path.read_text(encoding="utf-8"))
    if not match:
        raise SystemExit(
            "ERROR: no '**Policy baseline: <day> <month> <year>.**' line found in "
            f"{policies_path}"
        )
    raw = " ".join(match.group(1).split())
    for fmt in DATE_FORMATS:
        try:
            return dt.datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    raise SystemExit(f"ERROR: could not parse policy baseline date: {raw!r}")


def write_output(**values: str) -> None:
    target = os.environ.get("GITHUB_OUTPUT")
    if not target:
        return
    with open(target, "a", encoding="utf-8") as fh:
        for key, value in values.items():
            fh.write(f"{key}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--policies",
        default="skill/references/policies.md",
        help="Path to policies.md (default: skill/references/policies.md)",
    )
    parser.add_argument(
        "--max-age-days",
        type=int,
        default=120,
        help="Age in days at which the baseline is considered stale (default: 120)",
    )
    parser.add_argument(
        "--today",
        help="Override today's date (YYYY-MM-DD) for testing",
    )
    args = parser.parse_args()

    baseline = read_baseline(pathlib.Path(args.policies))
    today = (
        dt.date.fromisoformat(args.today)
        if args.today
        else dt.datetime.now(dt.timezone.utc).date()
    )
    age = (today - baseline).days
    stale = age > args.max_age_days

    write_output(
        baseline=baseline.isoformat(),
        age_days=str(age),
        stale="true" if stale else "false",
        max_age_days=str(args.max_age_days),
    )

    status = "STALE" if stale else "PASS"
    unit = "day" if age == 1 else "days"
    budget_unit = "day" if args.max_age_days == 1 else "days"
    print(
        f"{status}: policy baseline {baseline.isoformat()} is {age} {unit} old "
        f"(budget {args.max_age_days} {budget_unit})."
    )
    if stale:
        print("Review Etsy's policies and update skill/references/policies.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
