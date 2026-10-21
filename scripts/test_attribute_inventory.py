"""Synthetic data only: verify source-availability counts, not mood judgments."""
import unittest
from audit_attribute_inventory import summarize, audit


class InventoryAuditTests(unittest.TestCase):
    def test_union_is_not_complete_coverage_and_duplicates_are_not_families(self):
        rows=[['A','','Calm','10'],['A','wght@900','Calm','90'],['B','','Playful','20'],['C','','Other','30']]
        report=summarize(rows,{'set':['Calm','Playful']})
        self.assertEqual(report['denominator_families'],3)
        group=report['groups']['set']
        self.assertEqual(group['families_with_any_assignment'],2)
        self.assertEqual(group['families_with_every_listed_tag'],0)
        self.assertEqual(group['families_without_any_assignment'],['C'])
        self.assertEqual(group['tag_assignment_count_histogram'],{'0':1,'1':2})

    def test_invalid_weights_are_quarantined_and_missing_is_not_zero(self):
        rows=[['A','','Calm','0'],['B','','Calm','nan'],['C','','Calm','101'],['D','','Calm','1']]
        report=summarize(rows,{'set':['Calm','Unknown']})
        self.assertEqual(report['excluded_invalid_weight_lines'],[1,2,3])
        self.assertEqual(report['per_source_tag']['Calm'],1)
        self.assertEqual(report['per_source_tag']['Unknown'],0)
        self.assertNotIn('score',report)

    def test_pinned_source_required(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'wrong.csv';path.write_text('A,,Calm,10\n')
            with self.assertRaisesRegex(ValueError,'pinned source hash'):
                audit(path)


if __name__=='__main__':
    unittest.main()
