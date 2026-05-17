#!/usr/bin/env python3
"""
bootstrap.py — One-time state initialization for the etsy-seller skill (v2.0).

Detects whether the user's state folder exists at ~/etsy-listings/.
If not, creates it with empty markdown templates from the bundled state-templates.

Idempotent — safe to call on every skill invocation. Returns early if state already exists.

Usage:
    python3 bootstrap.py [--state-dir PATH] [--templates-dir PATH] [--quiet]

Default paths:
    state-dir:     ~/etsy-listings
    templates-dir: <skill-dir>/../../state-templates/etsy-listings (auto-detected)
"""
import argparse
import os
import shutil
import sys
from pathlib import Path


def find_default_templates_dir(script_dir: Path) -> Path:
    """The state-templates folder is at the package root, two levels above this script."""
    # script_dir = .../skill/scripts/
    # templates  = .../state-templates/etsy-listings/
    return script_dir.parent.parent / "state-templates" / "etsy-listings"


def find_default_state_dir() -> Path:
    return Path.home() / "etsy-listings"


def state_exists(state_dir: Path) -> bool:
    """State is considered to exist if keyword-map.md is present."""
    return (state_dir / "keyword-map.md").exists()


def bootstrap(state_dir: Path, templates_dir: Path, verbose: bool = True) -> dict:
    """Create state structure from templates. Idempotent."""
    result = {
        "state_dir": str(state_dir),
        "templates_dir": str(templates_dir),
        "already_existed": False,
        "files_created": [],
        "errors": [],
    }

    if state_exists(state_dir):
        result["already_existed"] = True
        if verbose:
            print(f"[bootstrap] State already exists at {state_dir} — no action.")
        return result

    if not templates_dir.exists():
        result["errors"].append(f"Templates dir not found: {templates_dir}")
        return result

    state_dir.mkdir(parents=True, exist_ok=True)
    if verbose:
        print(f"[bootstrap] Created state dir: {state_dir}")

    # Copy every entry from the template folder
    for entry in templates_dir.iterdir():
        target = state_dir / entry.name
        if target.exists():
            continue
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
        result["files_created"].append(str(target.relative_to(state_dir)))
        if verbose:
            print(f"[bootstrap] Copied: {entry.name}")

    if verbose:
        print(f"[bootstrap] Done. {len(result['files_created'])} entries created.")
        print(f"[bootstrap] Your listings database is ready at: {state_dir}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Bootstrap etsy-seller skill state (v2.0).")
    parser.add_argument("--state-dir", type=Path, default=None,
                        help="Where to create state (default: ~/etsy-listings)")
    parser.add_argument("--templates-dir", type=Path, default=None,
                        help="Source templates (default: ../../state-templates/etsy-listings)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    state_dir = args.state_dir or find_default_state_dir()
    templates_dir = args.templates_dir or find_default_templates_dir(script_dir)

    result = bootstrap(state_dir, templates_dir, verbose=not args.quiet)

    if result["errors"]:
        print(f"[bootstrap] Completed with {len(result['errors'])} error(s):", file=sys.stderr)
        for err in result["errors"]:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
