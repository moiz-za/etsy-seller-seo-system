# Contributing to the Etsy Seller SEO System

Thanks for wanting to improve this project. This system is opinionated and built
around the 2026 Etsy algorithm. If Etsy changes its rules (and it will), this
needs updates — so contributions are genuinely welcome.

By participating, you agree to follow our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Ways to contribute

- **Report a bug** — use the [bug report template](https://github.com/moiz-za/etsy-seller-seo-system/issues/new?template=bug_report.yml).
- **Suggest a feature** — use the [feature request template](https://github.com/moiz-za/etsy-seller-seo-system/issues/new?template=feature_request.yml).
- **Ask a question / share results** — use [GitHub Discussions](https://github.com/moiz-za/etsy-seller-seo-system/discussions).
- **Send a change** — open a pull request (see below).
- **Report a security issue** — do **not** open a public issue; follow [SECURITY.md](./SECURITY.md).

### What we especially want

- Updates to `skill/references/seo-guide.md` for algorithm changes
- Updates to `skill/references/policies.md` for Etsy policy changes
- Additions to `skill/references/playbooks/trademark-stoplist.md` for newly
  trademarked franchises
- New playbooks for genuinely new operational patterns

### What we will decline

- Adding new "modes" — the system is intentionally 2-mode
- Re-introducing the shop concept / multi-shop architecture
- Anything that violates the scope-honesty principle (no fake-fixes)
- Unverified claims presented as Etsy policy without a source

## Development setup

This is a prompt/skill and documentation project; there is no build step. You
need:

- `git`
- Python 3 (only for the optional policy-sync script)

```bash
git clone https://github.com/moiz-za/etsy-seller-seo-system.git
cd etsy-seller-seo-system

# Enable the local leak guard once per clone (recommended)
git config core.hooksPath .githooks
```

The leak guard blocks commits that contain private shop data or personal machine
paths. CI runs the same scan on every push and pull request.

## Repository structure

| Path | What lives here |
|------|-----------------|
| `skill/` | The Claude/Cowork skill: `SKILL.md`, references, playbooks, scripts |
| `portable/` | Single-file prompt edition for ChatGPT / Perplexity / Gemini |
| `state-templates/` | Starter files copied into a seller's local state |
| `scripts/` | Policy-sync helper + archive build |
| `.github/` | Workflows, issue/PR templates |

If you edit anything under `skill/`, rebuild the packaged archive before
committing and update cross-references if a path changes:

```bash
python3 scripts/sync_etsy_policy.py --build   # rebuilds etsy-seller.skill
```

Commit the rebuilt `etsy-seller.skill` alongside your change — the **Archive
Check** CI job fails if the committed archive differs from the source tree.

## Policy freshness

`skill/references/policies.md` starts with a verified-on stamp:

```
**Policy baseline: 22 October 2026.**
```

The **Policy Freshness** workflow checks that date on the first day of every
month and opens a `policy-freshness` issue when it is more than 120 days old.

To re-verify the baseline by hand:

```bash
python3 scripts/check_policy_freshness.py            # prints PASS / STALE
python3 scripts/check_policy_freshness.py --today 2027-06-01   # test the stale path
```

When Etsy changes a policy:

1. Update `skill/references/policies.md` (and the affected reference/playbook).
2. Mirror behaviour changes in `skill/SKILL.md` and the portable edition.
3. Add a `CHANGELOG.md` entry and bump the version.
4. Move the `Policy baseline` date to the verification date.
5. Run `python3 scripts/sync_etsy_policy.py --build` and commit both files.

## Style and conventions

- Keep the system's existing voice: direct, evidence-driven, honest about limits.
- Exactly **13 tags**, each **≤ 20 characters**; max 2 tags may share a 2-word
  phrase cluster.
- **No emojis** in skill output (description text or section headers).
- Cite live data or explicitly tag reasoning fallbacks — no invented facts.
- Prefer small, focused changes over large rewrites.

### Commit messages

Use a conventional prefix matching the existing history:

- `fix:` bug fixes
- `docs:` documentation and prompt text
- `feat:` new capabilities
- `chore:` tooling, packaging, housekeeping

## Pull requests

1. Fork the repo and create a branch from `main`.
2. Make your change and run any relevant checks.
3. Fill out the pull request template.
4. Link the issue your PR addresses, if any.
5. Be responsive to review feedback.

A maintainer will review as soon as possible. Please keep PRs scoped to a single
concern so they are quick to review.

## Reporting security issues

See [SECURITY.md](./SECURITY.md). Never disclose a vulnerability in a public
issue, discussion, or pull request.
