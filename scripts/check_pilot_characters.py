"""Inspect one normal font file per pilot family; this is not a reading test.
Usage: python scripts/check_pilot_characters.py BINARY_DIRECTORY OUTPUT_JSON
Requires fontTools. Files must be named <record-id>.ttf and come from the pinned URLs.
"""
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import quote
from fontTools.ttLib import TTFont

REVISION = '45e3d5269e4a17d823f6d84470bc084dc5ae46f6'
FILES = {
    'notosans': 'NotoSans[wdth,wght].ttf',
    'merriweather': 'Merriweather[opsz,wdth,wght].ttf',
    'robotomono': 'RobotoMono[wght].ttf',
    'caveat': 'Caveat[wght].ttf',
    'abrilfatface': 'AbrilFatface-Regular.ttf',
}
SAMPLES = {
    'printable_ascii': ''.join(chr(c) for c in range(32, 127)),
    'english_ui_example': 'Choose your fonts. Save changes. 12:45 PM $19.99',
    'character_distinction_sample': 'Il1 O0 rn m {} [] () , . : ;',
    'extended_example': 'Café naïve résumé — “Hello” € £ ©',
}

def inspect(root):
    results = []
    for slug, filename in FILES.items():
        path = root / (slug + '.ttf')
        font = TTFont(path)
        cmap = font.getBestCmap() or {}
        samples = {}
        for name, text in SAMPLES.items():
            missing = sorted({c for c in text if ord(c) not in cmap})
            samples[name] = {'text': text, 'mapped': not missing,
                             'missing': [{'character': c, 'codepoint': f'U+{ord(c):04X}'} for c in missing]}
        axes = []
        if 'fvar' in font:
            axes = [{'tag': a.axisTag, 'min': a.minValue, 'default': a.defaultValue,
                     'max': a.maxValue} for a in font['fvar'].axes]
        results.append({
            'id': slug,
            'source_url': f'https://raw.githubusercontent.com/google/fonts/{REVISION}/ofl/{slug}/' + quote(filename),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'file_bytes': path.stat().st_size,
            'axes': axes,
            'samples': samples,
        })
        font.close()
    return {'upstream_revision': REVISION, 'checked_on': '2026-10-21',
            'scope': 'Unicode cmap presence in 1 normal file per family; no shaping, visual distinction, language completeness, italic-file, or reading-performance tests',
            'families': results}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    result = inspect(Path(sys.argv[1]))
    Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for family in result['families']:
        print(family['id'], {k:v['mapped'] for k,v in family['samples'].items()})
