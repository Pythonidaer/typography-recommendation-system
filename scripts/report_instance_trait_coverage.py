"""Report evidence locations for the rendered pilot instances. Never infer scores."""
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
TAGS = ['Calm','Loud','Playful','Vintage','Business']

def parse_location(location):
    axes, values = location.split('@')
    return dict(zip(axes.split(','), map(float, values.split(','))))


def coverage(record, instance, tag):
    rows = [r for r in record['source_tags'] if r['tag']==tag]
    selected_axes = instance['axis_settings']
    exact, partial, unlocated, other = [], [], [], []
    for row in rows:
        if row['location'] is None:
            unlocated.append(row['source_row'])
            continue
        coordinates = parse_location(row['location'])
        if coordinates == selected_axes:
            exact.append(row['source_row'])
        elif coordinates and coordinates.keys() <= selected_axes.keys() and all(
                selected_axes[k]==v for k,v in coordinates.items()):
            partial.append(row['source_row'])
        else:
            other.append(row['source_row'])
    status = ('exact_coordinates_found' if exact else
              'partial_coordinates_need_scope_review' if partial else
              'unlocated_assignment_needs_scope_review' if unlocated else
              'only_other_coordinates_found' if other else 'missing')
    return {'tag':tag,'status':status,'exact_coordinate_rows':exact,
            'partial_coordinate_rows':partial,'unlocated_rows':unlocated,
            'other_coordinate_rows':other,'calibrated_score':None,
            'note':'Coordinate coverage is not confirmation of style scope, mood validity, or preference fit.'}


if __name__=='__main__':
    manifest=json.loads((ROOT/'research/specimens/batch-1/manifest.json').read_text())
    results=[]
    for item in manifest['instances']:
        instance=item['instance']
        record=json.loads((ROOT/'research/fonts'/f'{instance["family_id"]}.json').read_text())
        results.append({'instance_id':instance['id'],'selected_axes':instance['axis_settings'],
                        'traits':[coverage(record,instance,'/Expressive/'+t) for t in TAGS]})
    result={'status':'evidence_location_audit_not_scores','checked_on':'2026-10-21',
            'dimensions':'Earlier five-trait diagnostic set; not an approved mood vocabulary.',
            'instances':results,'counts':dict(Counter(t['status'] for r in results for t in r['traits']))}
    output=ROOT/'research/source-audit/instance-trait-coverage.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['counts']))
