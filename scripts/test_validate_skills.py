"""Regression cases for metadata that a Markdown linter cannot validate."""
import tempfile
import unittest
from pathlib import Path

import yaml

from validate_skills import SECTIONS, validate_repository, validate_skill


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = self.root / "skills" / "sample-auditor" / "SKILL.md"
        self.path.parent.mkdir(parents=True)
        self.path.with_name("checklist.md").write_text("Manual checks\n")
        self.metadata = {
            "name": "sample-auditor", "description": "Audit a sample interface.",
            "metadata": {"version": "1.6.0"},
        }

    def write_skill(self, data=None, version="1.6.0"):
        body = "\n\n".join(f"## {s}\n\n" + (version if s == "Version" else "Guidance") for s in SECTIONS)
        self.path.write_text("---\n" + yaml.safe_dump(data or self.metadata) + "---\n[checklist.md](checklist.md)\n\n" + body + "\n")

    def test_standard_metadata_and_string_compatibility_pass(self):
        self.metadata["compatibility"] = "Requires a runnable Apple-platform app for runtime checks."
        self.write_skill()
        self.assertEqual(validate_skill(self.path), [])

    def test_legacy_top_level_version_and_runtime_list_fail(self):
        self.metadata["version"] = "1.6.0"
        self.metadata["compatibility"] = ["codex", "claude"]
        self.write_skill()
        errors = validate_skill(self.path)
        self.assertTrue(any("Unsupported top-level" in e for e in errors))
        self.assertTrue(any("compatibility must" in e for e in errors))

    def test_metadata_values_must_be_strings(self):
        self.metadata["metadata"]["version"] = 1.6
        self.write_skill()
        self.assertTrue(any("string-to-string" in e for e in validate_skill(self.path)))

    def test_duplicate_yaml_keys_are_rejected(self):
        self.write_skill()
        self.path.write_text(self.path.read_text().replace("name: sample-auditor", "name: sample-auditor\nname: other-auditor"))
        self.assertTrue(any("Duplicate YAML key" in e for e in validate_skill(self.path)))

    def test_malformed_yaml_returns_diagnostic(self):
        self.path.write_text("---\nname: [unterminated\n---\n")
        self.assertTrue(any("Invalid YAML" in e for e in validate_skill(self.path)))

    def test_version_drift_is_rejected(self):
        self.write_skill(version="1.5.0")
        self.assertTrue(any("must match" in e for e in validate_skill(self.path)))

    def test_missing_description_and_checklist_are_rejected(self):
        self.metadata["description"] = "  "
        self.write_skill()
        self.path.with_name("checklist.md").unlink()
        errors = validate_skill(self.path)
        self.assertTrue(any("Description must" in e for e in errors))
        self.assertTrue(any("checklist" in e for e in errors))

    def test_wrong_name_is_rejected(self):
        self.metadata["name"] = "other-auditor"
        self.write_skill()
        self.assertTrue(any("directory" in e for e in validate_skill(self.path)))

    def test_empty_repository_fails_instead_of_passing_silently(self):
        self.assertEqual(validate_repository(self.root), ["No skills found"])


if __name__ == "__main__":
    unittest.main()
