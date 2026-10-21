"""Regression checks for data problems that must remain visible in audit reports."""
import tempfile
import unittest
from pathlib import Path
from audit_font_tags import audit


class AuditTests(unittest.TestCase):
    def test_reports_duplicates_invalid_values_and_malformed_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            families, definitions, ui = [root / n for n in ('families.csv', 'defs.csv', 'ui')]
            families.write_text('Test,,/Expressive/Calm,50\nTest,,/Expressive/Calm,50\nOther,wght@400,/Expressive/Calm,0\nBroken,,row\n')
            definitions.write_text('/Expressive/Calm,0,100,calm\n')
            ui.write_text('tag_names: "/Script/Upright"')
            result = audit(families, definitions, ui)
            self.assertEqual(len(result['duplicate_keys']), 1)
            self.assertEqual(result['invalid_score_lines'], [3])
            self.assertEqual(result['malformed_row_lines'], [4])
            self.assertEqual(result['tags']['/Expressive/Calm']['families_location_only'], 1)
            self.assertEqual(result['literal_ui_tags_without_exact_definition_or_rows'], ['/Script/Upright'])

    def test_preserves_unknown_tags_and_rejects_nonfinite_or_malformed_locations(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            families, definitions, ui = [root / n for n in ('families.csv', 'defs.csv', 'ui')]
            families.write_text('Test,wght@nan,/Unknown/Tag,50\nOther,wght@400,/Expressive/Calm,nan\n')
            definitions.write_text('/Expressive/Calm,0,100,calm\n')
            ui.write_text('')
            result = audit(families, definitions, ui)
            self.assertEqual(result['invalid_score_lines'], [2])
            self.assertEqual(result['malformed_location_lines'], [1])
            self.assertEqual(result['data_tags_missing_definitions'], ['/Unknown/Tag'])


if __name__ == '__main__':
    unittest.main()
