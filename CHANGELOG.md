# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog.

## [Unreleased]

## [1.3.1] - 2026-06-24

### Changed
- Expanded SKILL.md frontmatter descriptions for SwiftUI, UIKit, and AppKit accessibility auditor skills to improve discoverability in Dispatch, Claude Code, and other skill runtimes.

## [1.3.0] - 2026-06-23

### Changed
- Updated SwiftUI, UIKit, and AppKit accessibility auditor skills with WWDC26 / SDK 2027 readiness checks for resizable layouts, Liquid Glass legibility, media subtitles, clearer labels, and non-touch interaction paths.

## [1.2.0] - 2026-05-23

### Changed
- Strengthened SwiftUI custom tappable view guidance to require an explicit accessibility activation path when `.onTapGesture` is used.
- Expanded SwiftUI and UIKit audit guidance to cover Voice Control, Switch Control, and keyboard activation checks.
- Strengthened AppKit custom control guidance to require an accessibility press/action path for custom `NSView` controls.
- Expanded AppKit audit guidance to cover Voice Control, Switch Control, and non-pointer activation checks.
- Reclassified the UIKit Dynamic Type example from `P0` to `P1` to better match the priority contract.

## [1.1.1] - 2026-03-22

### Added
- `docs/review-red-flags.md` with practical anti-patterns and reviewer questions.
- Docs quality automation:
  - `.github/workflows/docs-checks.yml`
  - `.markdownlint.json`
  - `scripts/check_markdown_local_links.py`

### Changed
- Reworked `README.md` with:
  - stronger positioning and practical quick-start flow
  - explicit non-goals
  - before/after accessibility example
  - cleaner, tool-agnostic usage language
- Updated skill and adapter wording from prompt-centric to request-centric phrasing.
- Expanded `CONTRIBUTING.md` with editorial rules and reject criteria.
- Improved release/process docs:
  - `.github/RELEASE_TEMPLATE.md`
  - `docs/releasing.md`
  - `docs/skill-canonical-standard.md`

## [1.1.0] - 2026-03-20

### Added
- Repository governance and release hygiene:
  - `CONTRIBUTING.md`
  - `.github/RELEASE_TEMPLATE.md`
  - `docs/releasing.md`
- Canonical skill authoring contract in `docs/skill-canonical-standard.md`.
- Tool adapter guides:
  - `docs/adapters/cursor.md`
  - `docs/adapters/claude.md`
  - `docs/adapters/codex.md`
- Routing guide in `AGENTS.md` with framework-based loading rules.

### Changed
- Hardened all platform skill files with shared contract updates:
  - added `version` and `compatibility` frontmatter
  - added shared `Guardrails` section
  - renamed output section to `Output contract`
  - added required `Verification protocol`
  - added explicit `Version` section
- Expanded `README.md` with:
  - installation by environment (skills.sh, Cursor, Claude, Codex)
  - post-install smoke verification flow
  - updated repository structure and process references

## [1.0.0] - 2026-03-20

### Added
- Initial release with three platform accessibility auditor skills:
  - `swiftui-accessibility-auditor`
  - `uikit-accessibility-auditor`
  - `appkit-accessibility-auditor`
- Platform checklists for manual validation.
- Examples folder with SwiftUI/UIKit/AppKit sample audits.
- skills.sh install instructions in repository README.
