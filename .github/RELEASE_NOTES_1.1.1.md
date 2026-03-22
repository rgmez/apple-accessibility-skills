## Summary

- Reworked repository docs to be more direct, practical, and tool-agnostic.
- Added docs quality automation (markdown lint + local markdown link checks).
- Added review anti-pattern guidance to make accessibility audits easier to evaluate in PRs.

## Highlights

### README quality jump

The root `README.md` now includes:
- stronger positioning and clearer intent
- `Quick rules`, `Quick Start (30s)`, and `Non-goals`
- a concrete before/after example for accessibility semantics
- cleaner usage language and simpler routing

### Better review guidance

Added:
- `docs/review-red-flags.md`

This gives teams a fast checklist of common accessibility review mistakes and focused reviewer questions.

### Docs CI

Added:
- `.github/workflows/docs-checks.yml`
- `.markdownlint.json`
- `scripts/check_markdown_local_links.py`

This keeps markdown quality and local link integrity checked on push/PR.

## Full change list

### Added
- `.github/workflows/docs-checks.yml`
- `.markdownlint.json`
- `scripts/check_markdown_local_links.py`
- `docs/review-red-flags.md`

### Changed
- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `docs/adapters/cursor.md`
- `docs/adapters/claude.md`
- `docs/adapters/codex.md`
- `docs/releasing.md`
- `docs/skill-canonical-standard.md`
- `.github/RELEASE_TEMPLATE.md`
- `skills/swiftui-accessibility-auditor/SKILL.md`
- `skills/uikit-accessibility-auditor/SKILL.md`
- `skills/appkit-accessibility-auditor/SKILL.md`

## Compatibility notes

- No breaking changes.
- Existing skill names and install paths remain valid.

## Suggested tag/title

- Tag: `v1.1.1`
- Title: `v1.1.1 - Docs polish, review guidance, and docs CI`
