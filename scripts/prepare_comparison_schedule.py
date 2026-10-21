"""Prepare a balanced 5-trial block for 4 choices from 5 pilot instances.
This creates a research schedule, not responses or a participant interface.
"""
import json
from pathlib import Path
from collections import Counter
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'research/specimens/batch-1/manifest.json').read_text())
ids = [r['instance']['id'] for r in manifest['instances']]
if len(ids)!=5 or len(set(ids))!=5:
    raise ValueError('This block requires exactly 5 unique instances')
trials = [{'id':f'trial-{omit+1}', 'omitted_instance':ids[omit],
           'positions':{name:ids[(omit+k)%5] for k,name in enumerate(
               ['top_left','top_right','bottom_left','bottom_right'],1)}}
          for omit in range(5)]
exposures = Counter(v for t in trials for v in t['positions'].values())
pairs = Counter(tuple(sorted(pair)) for t in trials for pair in combinations(t['positions'].values(),2))
assert set(exposures.values())=={4}
assert len(pairs)==10 and set(pairs.values())=={3}
for position in trials[0]['positions']:
    assert set(t['positions'][position] for t in trials)==set(ids)
result = {
    'version':'0.1','status':'proposed_not_run',
    'scope':'One attribute and one text role per block; attribute remains unassigned.',
    'attribute_id':None,'role':None,'participant_id':None,
    'trial_order':'canonical; permute and record before a real session',
    'trials':trials,
    'balance_checks':{'presentations_per_instance':4,'co_presentations_per_pair':3,
                      'presentations_per_instance_in_each_position':1},
    'outcomes':['selected_option','none_fit','too_similar','skip'],
    'responses':[],
    'limitations':['Balanced exposure does not remove every presentation or context bias.',
                  'Interrupted or partial blocks may lose the planned balance.',
                  'Four-option winners do not order unselected options.',
                  'An eventual UI must use verified live text or record image display scale.',
                  'Do not run all mood/role combinations by default; start with one short block.'],
}
output = ROOT/'research/protocols/four-option-schedule.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print('5 trials: equal exposure, all 10 pair counts, and position balance verified')
