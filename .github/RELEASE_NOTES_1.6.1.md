# UIKit Accessibility Auditor 1.6.1

## Summary

- UIKit audits now treat source code, comments, string literals, logs, and retrieved documentation as data, ignoring embedded instructions that attempt to redirect the audit or authorize unrelated actions.
- Version-specific API recommendations require SDK or current Apple documentation evidence, with uncertainty and supported fallbacks when verification is unavailable.
- Adaptive-layout and media checks link to verified primary Apple sources for iOS 26/27.

## Why this release

The Agent Trust Hub report identified missing explicit input trust boundaries and incorrectly described the linked WWDC sessions as nonexistent. This patch addresses the missing boundaries and records the supporting Apple sources. A fresh external audit is required to confirm any change to the published warning.

## Compatibility notes

- No breaking changes. UIKit is version `1.6.1`; SwiftUI and AppKit remain at `1.6.0`.
- Installation names, paths, and the P0/P1/P2 findings, patch, and manual-verification contract are preserved.

## Validation

- Markdown lint, local Markdown links, repository metadata/version validation, and the skill-creator validator passed.
- Nine existing validator tests passed.
- The official skills CLI `1.7.4` discovered all three skills and installed UIKit for Claude Code, Cursor, Codex, and GitHub Copilot in a temporary project with telemetry disabled. Installed package files matched the source.
- Added a behavioral evaluation scenario for a UIKit source comment that attempts to suppress an evidenced finding. This scenario has not undergone a new independent model evaluation.
- No Swift snippets or live assistive-technology sessions were executed.
