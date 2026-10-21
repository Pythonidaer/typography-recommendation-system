"""Audit proposed attribute source availability; do not estimate mood or suitability.
Usage: python scripts/audit_attribute_inventory.py PINNED_FAMILIES_CSV
The input must match the previously audited source SHA-256.
"""
import csv
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from report_instance_trait_coverage import coverage

ROOT=Path(__file__).resolve().parents[1]


def summarize(rows, tag_groups):
    families=set()
    valid=defaultdict(set)
    invalid=[]
    for line,row in enumerate(rows,1):
        if len(row)!=4:
            raise ValueError(f'Malformed source row {line}')
        family,location,tag,raw=row
        families.add(family)
        try:
            weight=float(raw)
        except ValueError:
            weight=float('nan')
        if not math.isfinite(weight) or not 0<weight<=100:
            invalid.append(line)
            continue
        valid[tag].add(family)
    groups={}
    for name,tags in tag_groups.items():
        assignments=[valid[t] for t in tags]
        union=set().union(*assignments)
        intersection=set.intersection(*assignments) if assignments else set()
        histogram=Counter(sum(f in members for members in assignments) for f in families)
        groups[name]={'source_tags':tags,'families_with_any_assignment':len(union),
                      'families_with_every_listed_tag':len(intersection),
                      'families_without_any_assignment':sorted(families-union),
                      'tag_assignment_count_histogram':{str(k):v for k,v in sorted(histogram.items())}}
    return {'denominator_families':len(families),'excluded_invalid_weight_lines':invalid,
            'groups':groups,'per_source_tag':{t:len(valid[t]) for t in sorted(set().union(*map(set,tag_groups.values())))}}


def audit(path):
    prior=json.loads((ROOT/'research/source-audit/google-fonts-tags.json').read_text())
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=prior['sources']['families.csv']['sha256']:
        raise ValueError('Input does not match the pinned source hash.')
    inventory=json.loads((ROOT/'research/attribute-inventory.json').read_text())
    retained=[x['tag'] for x in inventory['retained_source_labels']]
    six_ids={'calm','playful','cheerful','energetic','elegant','rugged'}
    six_tags=sorted({t for c in inventory['candidates'] if c['id'] in six_ids for t in c['source_tag_candidates']})
    result=summarize(list(csv.reader(raw.decode().splitlines())),{'original_six_candidate_source_tags':six_tags,'all_retained_expressive_source_tags':retained})
    result.update(upstream_revision=prior['upstream_revision'],source=prior['sources']['families.csv'],inventory_version=inventory['version'],status='source_availability_not_validated_attribute_coverage',checked_on='2026-10-21',denominator='Distinct exact family names in pinned tag CSV, not live catalogue or all styles.',limitations=['Any assignment includes unresolved scope and raw values of any valid strength. It does not establish a strong trait.','Related source labels stay separate; unions measure data availability, not combined mood scores.','Every listed tag does not mean every proposed attribute is assessed. Missing is unknown.','The five-family sample cannot establish category, script, or catalogue fairness.'])
    manifest=json.loads((ROOT/'research/specimens/batch-1/manifest.json').read_text())
    pilot=[]
    for item in manifest['instances']:
        instance=item['instance']
        record=json.loads((ROOT/'research/fonts'/f'{instance["family_id"]}.json').read_text())
        candidates=[]
        for candidate in inventory['candidates']:
            candidates.append({'candidate_id':candidate['id'],'mapping_relation':candidate['mapping_relation'],
                               'source_checks':[coverage(record,instance,t) for t in candidate['source_tag_candidates']],
                               'assessment_score':None})
        pilot.append({'instance_id':instance['id'],'candidates':candidates})
    result['pilot_instance_checks']=pilot
    return result


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit(__doc__)
    result=audit(sys.argv[1])
    (ROOT/'research/source-audit/attribute-inventory-coverage.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['pilot_instance_checks','limitations','per_source_tag']},indent=2))
