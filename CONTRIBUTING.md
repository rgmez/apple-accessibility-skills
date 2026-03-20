# Contributing

Thanks for contributing to `apple-accessibility-skills`.

## Scope

This repository maintains platform-specific accessibility audit skills for:
- SwiftUI
- UIKit
- AppKit

## Contribution Rules

- Keep recommendations minimal, localized, and patch-ready.
- Prioritize practical accessibility impact over style preference.
- Do not suggest speculative API usage.
- Preserve existing behavior unless accessibility requires a change.
- Keep output concise and easy to verify manually.

## Required Skill Quality

For every skill update:
- keep the required section order from `docs/skill-canonical-standard.md`
- keep findings prioritized as P0/P1/P2
- include explicit verification steps
- reference the related `checklist.md` as a required artifact

## Pull Request Checklist

- [ ] Changes align with `docs/skill-canonical-standard.md`
- [ ] No broad refactor introduced without blocker-level reason
- [ ] Output contract remains stable and clear
- [ ] Manual verification steps are still valid
- [ ] Links and references resolve

## Commit Style

Use descriptive, human commit messages:
- short title with intent
- optional body with why the change matters
