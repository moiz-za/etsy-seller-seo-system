#!/usr/bin/env python3
"""
Automated Etsy Policy & Engine Dual-Repo Sync Script
Synchronizes rulebooks bidirectionally between:
  - svg-design-intelligence-system (integration/etsy-seo-engine/)
  - etsy-seller-seo-system (skill/references/)

Maintainer utility — not needed for normal skill usage. Auto-detects both repos
when cloned side by side; override locations with ESVG_REPO / SELLER_REPO env vars.
"""

import argparse
import os
import sys
import shutil
import hashlib
import json
import zipfile
from pathlib import Path

SELLER_REPO_DIRNAME = 'etsy-seller-seo-system'
ESVG_REPO_DIRNAME = 'svg-design-intelligence-system'


def _walk_up(start: Path, predicate):
    current = start.resolve()
    for candidate in [current] + list(current.parents):
        if predicate(candidate):
            return candidate
    return None


def detect_repos(script_path: Path):
    """Locate both repo roots from the script's own location.

    A seller repo has skill/references/ and no integration/etsy-seo-engine/;
    an ESVG repo has integration/etsy-seo-engine/. If only one is found, the
    other is looked up as a sibling directory.
    """
    p = script_path.resolve().parent
    esvg = _walk_up(p, lambda c: (c / 'integration' / 'etsy-seo-engine').is_dir())
    seller = _walk_up(p, lambda c: (c / 'skill' / 'references').is_dir()
                      and not (c / 'integration' / 'etsy-seo-engine').is_dir())
    if esvg is None and seller is not None:
        esvg = seller.parent / ESVG_REPO_DIRNAME
    if seller is None and esvg is not None:
        seller = esvg.parent / SELLER_REPO_DIRNAME
    return esvg, seller


_SCRIPT_PATH = Path(__file__).resolve()
_ESVG_FOUND, _SELLER_FOUND = detect_repos(_SCRIPT_PATH)
REPO_SELLER = Path(os.environ.get('SELLER_REPO')) if os.environ.get('SELLER_REPO') else _SELLER_FOUND
REPO_ESVG = Path(os.environ.get('ESVG_REPO')) if os.environ.get('ESVG_REPO') else _ESVG_FOUND

DIR_ESVG = REPO_ESVG / 'integration' / 'etsy-seo-engine' if REPO_ESVG else None
DIR_SELLER = REPO_SELLER / 'skill' / 'references' if REPO_SELLER else None

FILES_TO_SYNC = ['listing-guide.md', 'seo-guide.md', 'policies.md']
PLAYBOOKS = [
    'ab-testing.md', 'action-layer-pointers.md', 'ai-image-compliance.md',
    'conversion-floor.md',
    'listing-health-score.md', 'platform-fit-check.md', 'price-positioning.md',
    'regional-handling.md', 'search-intent-classification.md',
    'trademark-stoplist.md', 'video-brief.md'
]

SKIP_NAMES = {'.DS_Store', '__pycache__', 'Thumbs.db', '.gitkeep'}


def get_hash(filepath):
    if not filepath.exists():
        return None
    return hashlib.md5(filepath.read_bytes()).hexdigest()


def get_mtime(filepath):
    if not filepath.exists():
        return 0
    return filepath.stat().st_mtime


def sync_files():
    print("🔄 --- AUTOMATED ETSY POLICY & ENGINE DUAL-REPO SYNC ---")
    if DIR_ESVG is None or not DIR_ESVG.exists():
        print(f"❌ ESVG repo not found (looked for sibling dir '{ESVG_REPO_DIRNAME}').")
        print("   Set ESVG_REPO env var or clone both repos side by side.")
        return False
    if DIR_SELLER is None or not DIR_SELLER.exists():
        print(f"⚠️ Standalone etsy-seller-seo-system repo not found (looked for sibling dir '{SELLER_REPO_DIRNAME}'). Skipping cross-repo sync.")
        return True

    synced_count = 0

    # Sync root files
    for filename in FILES_TO_SYNC:
        f_esvg = DIR_ESVG / filename
        f_seller = DIR_SELLER / filename

        h_esvg = get_hash(f_esvg)
        h_seller = get_hash(f_seller)

        if h_esvg != h_seller:
            m_esvg = get_mtime(f_esvg)
            m_seller = get_mtime(f_seller)

            if m_esvg > m_seller:
                print(f"  --> Copying newer {filename} from ESVG ➔ Etsy Seller SEO System")
                shutil.copy2(f_esvg, f_seller)
                synced_count += 1
            else:
                print(f"  <-- Copying newer {filename} from Etsy Seller SEO System ➔ ESVG")
                shutil.copy2(f_seller, f_esvg)
                synced_count += 1

    # Sync playbooks
    pb_esvg_dir = DIR_ESVG / 'playbooks'
    pb_seller_dir = DIR_SELLER / 'playbooks'

    pb_esvg_dir.mkdir(exist_ok=True)
    pb_seller_dir.mkdir(exist_ok=True)

    for filename in PLAYBOOKS:
        f_esvg = pb_esvg_dir / filename
        f_seller = pb_seller_dir / filename

        h_esvg = get_hash(f_esvg)
        h_seller = get_hash(f_seller)

        if h_esvg != h_seller:
            m_esvg = get_mtime(f_esvg)
            m_seller = get_mtime(f_seller)

            if m_esvg > m_seller:
                print(f"  --> Copying newer playbook {filename} from ESVG ➔ Etsy Seller SEO System")
                shutil.copy2(f_esvg, f_seller)
                synced_count += 1
            elif m_seller > m_esvg:
                print(f"  <-- Copying newer playbook {filename} from Etsy Seller SEO System ➔ ESVG")
                shutil.copy2(f_seller, f_esvg)
                synced_count += 1

    if synced_count == 0:
        print("✅ Both repositories are already 100% synchronized! Zero drift detected.")
    else:
        print(f"🎉 Successfully synchronized {synced_count} file(s) across both repositories!")
        rebuild_packages()

    return True


def rebuild_seller_package():
    """Rebuild etsy-seller.skill — skill/ + state-templates/ (zip install layout)."""
    if REPO_SELLER is None:
        return
    output = REPO_SELLER / 'etsy-seller.skill'
    if output.exists():
        output.unlink()

    # Deterministic archive: fixed timestamp + sorted entries, so the byte
    # output is reproducible and CI can verify the committed archive matches
    # the source tree.
    fixed_time = (1980, 1, 1, 0, 0, 0)

    def add_file(z, fp, arcname):
        info = zipfile.ZipInfo(arcname, date_time=fixed_time)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        with open(fp, 'rb') as fh:
            z.writestr(info, fh.read())

    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(REPO_SELLER / 'skill'):
            dirs.sort()
            for f in sorted(files):
                fp = Path(root) / f
                if f in SKIP_NAMES or f.endswith(('.pyc', '.pyo')):
                    continue
                add_file(z, fp, str(fp.relative_to(REPO_SELLER / 'skill')))
        for root, dirs, files in os.walk(REPO_SELLER / 'state-templates'):
            dirs.sort()
            for f in sorted(files):
                fp = Path(root) / f
                if f in SKIP_NAMES or f.endswith(('.pyc', '.pyo')):
                    continue
                add_file(z, fp, str(fp.relative_to(REPO_SELLER)))

    print(f"✅ Rebuilt etsy-seller.skill ({REPO_SELLER.name}: skill/ + state-templates/)")


def rebuild_esvg_package():
    """Rebuild esvg-dis.skill — full multi-folder layout matching the repo structure."""
    if REPO_ESVG is None:
        return
    output_esvg = REPO_ESVG / 'esvg-dis.skill'
    if output_esvg.exists():
        output_esvg.unlink()

    with zipfile.ZipFile(output_esvg, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(REPO_ESVG / 'skill' / 'SKILL.md', arcname='SKILL.md')
        if (REPO_ESVG / 'skill' / 'scripts' / 'bootstrap.py').exists():
            z.write(REPO_ESVG / 'skill' / 'scripts' / 'bootstrap.py', arcname='scripts/bootstrap.py')
        for d in ['workflow', 'knowledge', 'prompts', 'integration', 'playbooks', 'state-templates', 'examples']:
            dp = REPO_ESVG / d
            if not dp.exists():
                continue
            for root, dirs, files in os.walk(dp):
                for f in files:
                    if f in SKIP_NAMES or f.endswith(('.pyc', '.pyo')):
                        continue
                    fp = Path(root) / f
                    z.write(fp, arcname=str(fp.relative_to(REPO_ESVG)))

    print(f"✅ Rebuilt esvg-dis.skill ({REPO_ESVG.name}: full multi-folder layout)")


def rebuild_packages():
    print("📦 Rebuilding skill archives...")
    rebuild_seller_package()
    rebuild_esvg_package()


def main():
    parser = argparse.ArgumentParser(
        description="Etsy policy dual-repo sync + packaged-skill build.")
    parser.add_argument(
        '--build', action='store_true',
        help="Rebuild etsy-seller.skill from skill/ + state-templates/ without cross-repo sync.")
    args = parser.parse_args()
    if args.build:
        rebuild_seller_package()
    else:
        sync_files()


if __name__ == '__main__':
    main()
