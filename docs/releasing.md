# Releasing

Use this process for each release.

## 1) Prepare

- Ensure `main` is up to date.
- Ensure working tree is clean.
- Confirm all changed skills follow `docs/skill-canonical-standard.md`.
- Ensure Docs Checks workflow is green (`.github/workflows/docs-checks.yml`).

## 2) Update changelog

- Add release section in `CHANGELOG.md`.
- Move completed items from `[Unreleased]` into the new version.

## 3) Tag and publish

- Create annotated tag:
  - `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
- Push tag:
  - `git push origin vX.Y.Z`
- Create GitHub release using `.github/RELEASE_TEMPLATE.md`.
- Optionally keep a versioned release draft in `.github/RELEASE_NOTES_X.Y.Z.md`.

## 4) Post-release

- Re-open `[Unreleased]` for next cycle.
- Verify skills index/import status if distributed via skills.sh.
