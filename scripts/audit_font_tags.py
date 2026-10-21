"""Audit pinned upstream tag files without inferring missing values or font traits.
Usage: python scripts/audit_font_tags.py FAMILIES_CSV TAG_METADATA_CSV UI_TEXTPROTO OUTPUT_JSON
"""
import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REVISION = '45e3d5269e4a17d823f6d84470bc084dc5ae46f6'

def audit(families_path, definitions_path, ui_path):
    paths = [Path(x) for x in (families_path, definitions_path, ui_path)]
    rows = list(csv.reader(paths[0].read_text(encoding='utf-8').splitlines()))
    definitions = list(csv.reader(paths[1].read_text(encoding='utf-8').splitlines()))
    definition_names = {row[0] for row in definitions}
    keys = Counter()
    tags = defaultdict(list)
    malformed = []
    invalid_scores = []
    malformed_locations = []
    for line, row in enumerate(rows, 1):
        if len(row) != 4:
            malformed.append(line)
            continue
        family, location, tag, raw = row
        try:
            score = float(raw)
        except ValueError:
            invalid_scores.append(line)
            continue
        if not math.isfinite(score) or not 0 < score <= 100:
            invalid_scores.append(line)
        if location:
            try:
                axes, values = location.split('@')
                ax, vals = axes.split(','), values.split(',')
                if len(ax) != len(vals) or len(set(ax)) != len(ax):
                    raise ValueError()
                for value in vals:
                    if not math.isfinite(float(value)):
                        raise ValueError()
            except ValueError:
                malformed_locations.append(line)
        keys[(family, location, tag)] += 1
        tags[tag].append((family, location, score))
    families = {row[0] for row in rows if len(row) == 4}
    located = {row[0] for row in rows if len(row) == 4 and row[1]}
    tag_stats = {}
    for tag, entries in sorted(tags.items()):
        unlocated = {f for f, loc, _ in entries if not loc}
        all_families = {f for f, _, _ in entries}
        tag_stats[tag] = {
            'rows': len(entries),
            'families_any_scope': len(all_families),
            'families_unlocated': len(unlocated),
            'families_location_only': len(all_families - unlocated),
            'observed_min': min(v for _, _, v in entries),
            'observed_max': max(v for _, _, v in entries),
        }
    ui_tags = set(re.findall(r'tag_names: "([^"]+)"', paths[2].read_text()))
    literal_ui_tags = {t for t in ui_tags if '*' not in t}
    known = definition_names | set(tags)
    duplicates = [{'family': f, 'location': loc, 'tag': tag, 'count': n}
                  for (f, loc, tag), n in sorted(keys.items()) if n > 1]
    groups = defaultdict(set)
    for family, _, tag, _ in (r for r in rows if len(r) == 4):
        groups[tag.split('/')[1]].add(family)
    return {
        'upstream_revision': REVISION,
        'checked_on': '2026-10-21',
        'denominator': 'Distinct exact family names present in families.csv, not live Google Fonts catalogue coverage',
        'sources': {name: {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'url': f'https://raw.githubusercontent.com/google/fonts/{REVISION}/' + upstream} for name, upstream, p in zip(['families.csv', 'tags_metadata.csv', 'tags_ui_details.textproto'], ['tags/all/families.csv', 'tags/tags_metadata.csv', 'tags/tags_ui_details.textproto'], paths)},
        'total_rows': len(rows), 'distinct_family_names': len(families),
        'distinct_tags_in_data': len(tags), 'tag_definitions': len(definitions),
        'unlocated_rows': sum(not r[1] for r in rows if len(r) == 4),
        'located_rows': sum(bool(r[1]) for r in rows if len(r) == 4),
        'families_with_located_rows': len(located),
        'tag_group_family_counts': {k: len(v) for k, v in sorted(groups.items())},
        'malformed_row_lines': malformed, 'invalid_score_lines': invalid_scores,
        'malformed_location_lines': malformed_locations, 'duplicate_keys': duplicates,
        'data_tags_missing_definitions': sorted(set(tags) - definition_names),
        'defined_tags_without_rows': sorted(definition_names - set(tags)),
        'literal_ui_tags_without_exact_definition_or_rows': sorted(literal_ui_tags - known),
        'tags': tag_stats,
    }

if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise SystemExit(__doc__)
    result = audit(*sys.argv[1:4])
    Path(sys.argv[4]).write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'tags'}, indent=2))
