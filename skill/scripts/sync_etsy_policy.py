#!/usr/bin/env python3
"""
Automated Etsy Policy & Engine Dual-Repo Sync Script
Synchronizes rulebooks bidirectionally between:
  - svg-design-intelligence-system (integration/etsy-seo-engine/)
  - etsy-seller-seo-system (skill/references/)
"""

import os
import sys
import shutil
import hashlib
import json
import zipfile
from pathlib import Path

# Paths
REPO_ESVG = Path('/Users/moiz/Documents/GitHub/svg-design-intelligence-system')
REPO_SELLER = Path('/Users/moiz/Documents/GitHub/etsy-seller-seo-system')

DIR_ESVG = REPO_ESVG / 'integration' / 'etsy-seo-engine'
DIR_SELLER = REPO_SELLER / 'skill' / 'references'

FILES_TO_SYNC = ['listing-guide.md', 'seo-guide.md', 'policies.md']
PLAYBOOKS = [
    'ab-testing.md', 'action-layer-pointers.md', 'conversion-floor.md',
    'listing-health-score.md', 'platform-fit-check.md', 'price-positioning.md',
    'regional-handling.md', 'search-intent-classification.md',
    'trademark-stoplist.md', 'video-brief.md'
]

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
    if not DIR_ESVG.exists():
        print(f"❌ ESVG directory not found: {DIR_ESVG}")
        return False
    if not DIR_SELLER.exists():
        print(f"⚠️ Standalone etsy-seller-seo-system repo not found at {DIR_SELLER}. Skipping cross-repo sync.")
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

def rebuild_packages():
    print("📦 Rebuilding skill archives and re-syncing global plugins...")

    # Rebuild ESVG skill archive
    output_esvg = REPO_ESVG / 'esvg-dis.skill'
    if output_esvg.exists():
        output_esvg.unlink()

    SKIP_NAMES = {'.DS_Store', '__pycache__', 'Thumbs.db', '.gitkeep'}
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

    # Sync ESVG Plugin
    plugin_dir = Path.home() / '.gemini' / 'config' / 'plugins' / 'esvg-dis-plugin'
    skill_target = plugin_dir / 'skills' / 'esvg-dis'
    if plugin_dir.exists():
        shutil.rmtree(plugin_dir)
    plugin_dir.mkdir(parents=True, exist_ok=True)
    skill_target.mkdir(parents=True, exist_ok=True)

    plugin_json = {
        'name': 'esvg-dis-plugin',
        'version': '1.1.0',
        'description': 'Etsy SVG Design Intelligence System (ESVG-DIS)',
        'author': {'name': 'Moiz'},
        'license': 'MIT'
    }
    with open(plugin_dir / 'plugin.json', 'w') as f:
        json.dump(plugin_json, f, indent=2)

    shutil.copy(REPO_ESVG / 'skill' / 'SKILL.md', skill_target / 'SKILL.md')
    for d in ['workflow', 'knowledge', 'prompts', 'integration', 'playbooks', 'state-templates', 'examples', 'documentation']:
        sp = REPO_ESVG / d
        tp = skill_target / d
        if sp.exists():
            shutil.copytree(sp, tp, ignore=shutil.ignore_patterns('.DS_Store', '__pycache__'))

    print("✅ esvg-dis.skill and global plugin updated successfully!")

if __name__ == '__main__':
    sync_files()
