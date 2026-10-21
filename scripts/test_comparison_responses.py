"""Synthetic fixtures only. These are not participant records or study results."""
import copy
import hashlib
import json
import unittest
from validate_comparison_responses import ROOT, validate_records
from report_instance_trait_coverage import coverage


class ResponseTests(unittest.TestCase):
    def fixture(self):
        schedule=json.loads((ROOT/'research/protocols/four-option-schedule.json').read_text())
        order=list(schedule['trials'][0]['positions'].values())
        return {'schema_version':'0.1','record_kind':'attribute_comparison','record_status':'synthetic',
                'response_id':'synthetic-1','session_id':'synthetic-session',
                'participant':{'id':'synthetic-person','kind':'human','model_id':None,'prompt_sha256':None,'visual_input_sha256':None},
                'attribute':{'id':'calm','definition_version':'0.1','definition_review_state':'draft'},
                'role':'heading','trial_id':'trial-1','shown_order':order,
                'stimulus_manifest_sha256':hashlib.sha256((ROOT/'research/specimens/batch-1/manifest.json').read_bytes()).hexdigest(),
                'presentation':{'verified':False,'mode':'synthetic','condition_id':'synthetic-condition','display_width_px':None,'notes':'Unit-test fixture only.'},
                'outcome':'selected_option','selected_instance_id':order[0],'created_at':'2026-10-21T12:00:00Z'}

    def test_synthetic_rejected_by_default(self):
        self.assertTrue(validate_records([self.fixture()]))
        self.assertFalse(validate_records([self.fixture()],allow_synthetic=True))

    def test_outside_selection_and_wrong_trial_are_rejected(self):
        d=self.fixture();d['selected_instance_id']='not-displayed'
        self.assertTrue(validate_records([d],True))
        d=self.fixture();d['trial_id']='trial-2'
        self.assertTrue(validate_records([d],True))

    def test_skips_are_not_selections(self):
        for outcome in ['none_fit','too_similar','skip']:
            d=self.fixture();d['outcome']=outcome
            self.assertTrue(validate_records([d],True))
            d['selected_instance_id']=None
            self.assertFalse(validate_records([d],True))

    def test_observed_requires_reviewed_definition_and_verified_presentation(self):
        d=self.fixture();d['record_status']='observed'
        self.assertTrue(validate_records([d],True))
        d['attribute']['definition_review_state']='reviewed';d['presentation'].update(verified=True,mode='raster',display_width_px=480)
        self.assertFalse(validate_records([d],True))

    def test_ai_provenance_and_human_ai_separation(self):
        d=self.fixture();d['participant']['kind']='ai'
        self.assertTrue(validate_records([d],True))
        d['participant'].update(model_id='synthetic-model',prompt_sha256='0'*64,visual_input_sha256='1'*64)
        self.assertFalse(validate_records([d],True))
        d['participant']['kind']='human'
        self.assertTrue(validate_records([d],True))

    def test_duplicate_responses_and_changed_artifacts_rejected(self):
        d=self.fixture();self.assertTrue(validate_records([d,copy.deepcopy(d)],True))
        d['stimulus_manifest_sha256']='f'*64
        self.assertTrue(validate_records([d],True))

    def test_scores_and_preferences_do_not_enter_attribute_records(self):
        d=self.fixture();d['mood_score']=90
        self.assertTrue(validate_records([d],True))
        d=self.fixture();d['record_kind']='project_preference'
        self.assertTrue(validate_records([d],True))

    def test_session_conditions_remain_consistent(self):
        first=self.fixture();second=copy.deepcopy(first)
        trial=json.loads((ROOT/'research/protocols/four-option-schedule.json').read_text())['trials'][1]
        second.update(response_id='synthetic-2',trial_id=trial['id'],shown_order=list(trial['positions'].values()),selected_instance_id=list(trial['positions'].values())[0])
        self.assertFalse(validate_records([first,second],True))
        for item in [first,second]:
            item['participant'].update(kind='ai',model_id='synthetic-model',prompt_sha256='0'*64,visual_input_sha256='1'*64)
        second['participant']['visual_input_sha256']='2'*64
        self.assertFalse(validate_records([first,second],True))
        second['attribute']['id']='playful'
        self.assertTrue(validate_records([first,second],True))

    def test_timezone_required(self):
        d=self.fixture();d['created_at']='2026-10-21T12:00:00'
        self.assertTrue(validate_records([d],True))


class CoverageTests(unittest.TestCase):
    def record(self,location):
        return {'source_tags':[{'tag':'/Expressive/Calm','location':location,'source_row':1,'raw_weight':90}]}

    def test_other_weight_is_not_exact_and_missing_is_not_zero(self):
        instance={'axis_settings':{'wght':400,'wdth':100}}
        self.assertEqual(coverage(self.record('wdth,wght@100,900'),instance,'/Expressive/Calm')['status'],'only_other_coordinates_found')
        self.assertEqual(coverage(self.record('wght@400'),instance,'/Expressive/Calm')['status'],'partial_coordinates_need_scope_review')
        result=coverage(self.record(None),instance,'/Expressive/Calm')
        self.assertEqual(result['status'],'unlocated_assignment_needs_scope_review')
        self.assertIsNone(result['calibrated_score'])
        self.assertEqual(coverage({'source_tags':[]},instance,'/Expressive/Calm')['status'],'missing')


if __name__=='__main__':
    unittest.main()
