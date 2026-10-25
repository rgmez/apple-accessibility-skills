## Summary

- Reduced false positives: inspect native semantics, distinguish missing context from confirmed defects, and allow no-finding responses without speculative patches.
- Added framework-specific Apple references for display preferences, custom controls, gesture alternatives, subtitle previews, and optional VoiceOver automation.
- Added CI checks for skill metadata and versions, with nine validator regression tests.

## Why this release

The auditors now require evidence for findings and demonstrated core-task impact for P0 severity. Examples no longer assume an icon-only control lacks a useful label or that visible row content proves a broken accessibility tree.

Conditional references cover Show Borders, Reduce Bright Effects, animated-image preferences, live display changes, scalable custom fonts, macOS Keyboard navigation, Larger Text declaration criteria, and the restoration of active captions after subtitle previews.

## Compatibility and migration

- Skill names and installation paths remain unchanged; all three skills are version `1.6.0`.
- Frontmatter consumers must read `metadata.version` instead of the former top-level `version`. Runtime distribution information is now the string-valued `metadata.supported-runtimes`, replacing the former `compatibility` list.
- Newer APIs remain gated by their documented platform and SDK availability. `XCUIVoiceOverService` is optional and was marked beta in the documentation reviewed on 2026-10-25.
- Local validation requires Python 3.9 or later and `python3 -m pip install -r requirements-dev.txt`. CI installs these dependencies automatically.

## Validation

- Passed Markdown lint, local Markdown link checks, and `git diff --check`.
- All three skills passed the skill-creator validator and the repository metadata/version validator.
- Nine validator regression tests passed.
- An independent evaluator answered five realistic audit requests without seeing their acceptance criteria; the sampled recommendations met those criteria. See `examples/audit-evaluation.md`.
- No consuming app, Swift snippets, or live assistive-technology sessions were executed. Runtime accessibility still needs verification in the app being audited.
