## Summary

- Expanded SKILL.md frontmatter descriptions for all three accessibility auditor skills to improve discoverability in Dispatch, Claude Code, and other skill runtimes.
- Clarified scope, trigger scenarios, and expected output (P0/P1/P2 findings with patch-ready fixes and manual verification steps).
- No changes to audit behavior, output contract, or checklists.

## Why this release

Dispatch flagged that the SwiftUI skill description was too sparse for proactive recommendations. This patch makes all three platform auditors easier to discover and route correctly without changing how they audit code.

## Compatibility notes

- No breaking changes.
- Skill behavior and output contract are unchanged; skill frontmatter versions remain `1.3.0`.
- Existing skill names and install paths remain valid.

## Test plan

- [x] Validate all local Markdown links with `scripts/check_markdown_local_links.py`.
- [x] Confirm updated descriptions follow `docs/skill-canonical-standard.md`.
- [x] Confirm no audit guidance or checklist content changed.
