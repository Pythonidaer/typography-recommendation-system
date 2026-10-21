"""Validate raw attribute-comparison records. No score or recommendation is computed.
Usage: python scripts/validate_comparison_responses.py RESPONSES_JSON
Input is a JSON array. Synthetic records are rejected by the CLI; tests may allow them.
Requires jsonschema==4.23.0.
"""
import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'research/schemas/attribute-response.schema.json').read_text())
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR=Draft202012Validator(SCHEMA)


def validate_records(records, allow_synthetic=False):
    errors=[]
    if not isinstance(records,list):
        return ['Input must be a JSON array.']
    schedule=json.loads((ROOT/'research/protocols/four-option-schedule.json').read_text())
    trials={t['id']:set(t['positions'].values()) for t in schedule['trials']}
    manifest_hash=hashlib.sha256((ROOT/'research/specimens/batch-1/manifest.json').read_bytes()).hexdigest()
    seen_ids=set()
    seen_trials=set()
    sessions={}
    for index,record in enumerate(records):
        label=f'record {index+1}'
        structural=list(VALIDATOR.iter_errors(record))
        if structural:
            errors.extend(f'{label}: {e.json_path}: {e.message}' for e in structural)
            continue
        if record['record_status']=='synthetic' and not allow_synthetic:
            errors.append(f'{label}: Synthetic records cannot enter observation input.')
        if record['response_id'] in seen_ids:
            errors.append(f'{label}: Duplicate response ID.')
        seen_ids.add(record['response_id'])
        # Corrections should replace/version the prior entry, not count as another vote.
        key=(record['session_id'],record['trial_id'])
        if key in seen_trials:
            errors.append(f'{label}: Duplicate trial response in a session.')
        seen_trials.add(key)
        # One block compares one attribute and role under one presentation condition.
        session_metadata={k:record[k] for k in ['attribute','role','stimulus_manifest_sha256','record_status']}
        session_metadata['participant']={k:record['participant'][k] for k in ['id','kind','model_id']}
        session_metadata['presentation']={k:v for k,v in record['presentation'].items() if k!='notes'}
        signature=json.dumps(session_metadata,sort_keys=True)
        prior=sessions.setdefault(record['session_id'],signature)
        if prior!=signature:
            errors.append(f'{label}: Session metadata changed; use a separate session for a different condition, participant, role, or attribute.')
        if set(record['shown_order'])!=trials[record['trial_id']]:
            errors.append(f'{label}: Shown options do not match the scheduled trial.')
        if record['outcome']=='selected_option' and record['selected_instance_id'] not in record['shown_order']:
            errors.append(f'{label}: Selection was not among displayed options.')
        if record['stimulus_manifest_sha256']!=manifest_hash:
            errors.append(f'{label}: Stimulus manifest hash does not match the pilot artifact.')
        try:
            timestamp=datetime.fromisoformat(record['created_at'].replace('Z','+00:00'))
            if timestamp.tzinfo is None:
                raise ValueError('Missing timezone')
        except ValueError:
            errors.append(f'{label}: created_at needs an ISO timestamp with timezone.')
    return errors


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit(__doc__)
    records=json.loads(Path(sys.argv[1]).read_text())
    errors=validate_records(records)
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print(f'{len(records)} record(s) structurally validated. This does not validate judgments or establish scores.')
