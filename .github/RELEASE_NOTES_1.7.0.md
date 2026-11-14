# Apple Accessibility Skills 1.7.0

## Summary

- Correct SwiftUI adjustable-control guidance and distinguish linked-group API availability from newer text-navigation behavior.
- Give all three auditors consistent API verification and input trust boundaries, plus form recovery and modal focus checks.
- Keep reading, media, and optional automation details in contextual references, with five new behavioral evaluation scenarios.

## Why this release

Auditors should recommend valid platform APIs, preserve input after validation failures, and verify that modal transitions remain operable with keyboard and assistive technologies. Contextual references keep specialized implementation guidance available without loading it for unrelated screens.

## Compatibility notes

- No breaking changes. SwiftUI, UIKit, and AppKit skills are all version `1.7.0`.
- Installation names, package paths, and the P0/P1/P2 findings, patch, and manual-verification contract are preserved.
- `accessibilityLinkedGroup(id:in:)` is available from iOS/iPadOS 14 and macOS 11. Newer continuous text-navigation behavior must be verified separately on the supported OS.

## Validation

- Markdown lint, local Markdown links, repository metadata/version validation, and the skill-creator validator passed.
- All nine existing validator tests passed.
- Skills CLI `1.7.4` discovered all three skills and installed them for Claude Code, Cursor, Codex, and GitHub Copilot in a temporary project with telemetry disabled. Installed resources matched the source byte-for-byte; the CLI shares `.agents/skills` across Cursor, Codex, and GitHub Copilot.
- An independent evaluator answered all five new behavioral scenarios without seeing the acceptance criteria. The release reviewer verified the recommendations against those criteria; see [the evaluation record](../examples/audit-evaluation.md#evaluation-record--2026-11-14).
- Generated Swift patches were not compiled. No apps, Inspector sessions, or live assistive-technology sessions were executed; runtime checks remain necessary.
