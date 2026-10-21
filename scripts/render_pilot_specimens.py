"""Render fixed-font research specimens, not a product interface or reader test.
Usage: python scripts/render_pilot_specimens.py FONT_DIRECTORY OUTPUT_DIRECTORY [LABEL_FONT]
Requires Pillow and fontTools. Source binaries must match pilot-character-checks.json.
"""
import hashlib
import json
import tempfile
from pathlib import Path
import sys
import PIL
from PIL import Image, ImageDraw, ImageFont
import fontTools
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
SCALE = 2
WIDTH = 480
CONTENT_WIDTH = 360
GUTTER = 60
INK = '#202124'
LABEL_FONT = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
ROLES = {
 'heading': ('Heading specimens', 'A place by the river', 40, 1.2),
 'paragraph': ('Paragraph specimens', 'The path follows the river past a row of houses. A footbridge connects the two streets near the station.', 20, 1.5),
 'characters': ('Character specimens', 'Il1 O0 rn m 8B {} [] () , . : ;', 24, 1.5),
}

def wrap(text, font):
    lines, current = [], ''
    for word in text.split():
        candidate = (current + ' ' + word).strip()
        if current and font.getlength(candidate) > CONTENT_WIDTH * SCALE:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def render(binary_root, output, label_path=LABEL_FONT):
    protocol = json.loads((ROOT / 'research/protocols/mood-comparison-draft.json').read_text())
    checks = json.loads((ROOT / 'research/source-audit/pilot-character-checks.json').read_text())
    expected = {f['id']: f for f in checks['families']}
    output.mkdir(parents=True, exist_ok=True)
    label = ImageFont.truetype(str(label_path), 13 * SCALE)
    title = ImageFont.truetype(str(label_path), 22 * SCALE)
    records = []
    with tempfile.TemporaryDirectory() as temporary:
        for index, instance in enumerate(protocol['instances'], 1):
            slug = instance['family_id']
            path = binary_root / (slug + '.ttf')
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != expected[slug]['sha256']:
                raise ValueError('Source hash mismatch: ' + slug)
            font = TTFont(path)
            required = set(''.join(role[1] for role in ROLES.values()))
            missing = sorted(c for c in required if ord(c) not in font.getBestCmap())
            if missing:
                raise ValueError(f'{slug} missing characters: {missing}')
            if 'fvar' in font:
                axis_names = {a.axisTag for a in font['fvar'].axes}
                if axis_names != set(instance['axis_settings']):
                    raise ValueError('Unpinned axis: ' + slug)
                font = instantiateVariableFont(font, instance['axis_settings'], inplace=False)
            static_path = Path(temporary) / (slug + '.ttf')
            font.save(static_path)
            font.close()
            records.append({'sample': index, 'instance': instance, 'source_sha256': digest,
                            'source_url': expected[slug]['source_url'], 'static_path': static_path})
        sheets = []
        for role, (heading, text, size, leading) in ROLES.items():
            y = 130 * SCALE
            layouts = []
            for record in records:
                font = ImageFont.truetype(str(record['static_path']), size * SCALE,
                                          layout_engine=ImageFont.Layout.RAQM)
                lines = wrap(text, font)
                baseline = y + 40 * SCALE
                line_step = round(size * leading * SCALE)
                row_bottom = baseline + line_step * len(lines)
                layouts.append((record, font, lines, y, baseline, line_step))
                y = row_bottom + 40 * SCALE
            image = Image.new('RGB', (WIDTH * SCALE, y + 20 * SCALE), 'white')
            draw = ImageDraw.Draw(image)
            draw.text((GUTTER*SCALE, 30*SCALE), heading, font=title, fill=INK)
            draw.text((GUTTER*SCALE, 68*SCALE), 'Same text and settings; five font instances.', font=label, fill=INK)
            draw.text((GUTTER*SCALE, 91*SCALE), 'Research specimens. No scores or test results.', font=label, fill=INK)
            sample_data = []
            for record, font, lines, top, baseline, step in layouts:
                draw.line((GUTTER*SCALE, top, (WIDTH-GUTTER)*SCALE, top), fill='#d8dadd', width=1)
                draw.text((GUTTER*SCALE, top+10*SCALE), 'Sample ' + str(record['sample']), font=label, fill=INK)
                boxes = []
                for n, line in enumerate(lines):
                    point = (GUTTER*SCALE, baseline+n*step)
                    box = draw.textbbox(point, line, font=font, anchor='la')
                    if box[0] < 0 or box[2] > WIDTH*SCALE or box[3] > image.height:
                        raise ValueError(f'Clipped text: {role}/{record["sample"]}')
                    draw.text(point, line, font=font, anchor='la', fill=INK)
                    boxes.append(box)
                sample_data.append({'sample':record['sample'], 'instance_id':record['instance']['id'],
                                    'lines':lines, 'glyph_bounds_image_px':boxes})
            filename = role + '-specimens.png'
            # Preserve the exact specified colors and antialiased glyphs.
            image.save(output / filename, optimize=True)
            sheets.append({'id':role, 'file':filename, 'text':text,
                           'reference_font_size_px':size, 'line_height_ratio':leading,
                           'image_size_px':list(image.size), 'samples':sample_data,
                           'sha256':hashlib.sha256((output/filename).read_bytes()).hexdigest()})
    manifest = {
        'status':'raster_specimens_rendered_no_participant_testing', 'created_at':'2026-10-21',
        'upstream_revision':checks['upstream_revision'],
        'renderer':{'pillow':PIL.__version__,'fonttools':fontTools.__version__,
                    'layout':'RAQM','label_font':str(label_path),
                    'label_font_sha256':hashlib.sha256(label_path.read_bytes()).hexdigest()},
        'reference_canvas_width_px':WIDTH, 'content_width_reference_px':CONTENT_WIDTH,
        'raster_scale':SCALE, 'foreground':INK, 'background':'#ffffff',
        'instances':[{k:v for k,v in record.items() if k!='static_path'} for record in records],
        'sheets':sheets,
        'limits':['Raster research artifacts, not verified browser/CSS rendering.',
                  'Equal nominal size does not match perceived size.',
                  'Labels are neutral; font identity remains available in the key.',
                  'Fixed sample order is for inspection, not a randomized participant trial.',
                  'No mood, comfort, legibility, readability, or pairing judgments collected.'],
    }
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'sheets':[{s['file']:s['image_size_px']} for s in sheets],
                      'source_hashes_verified':len(records)}))

if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        raise SystemExit(__doc__)
    render(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]) if len(sys.argv)==4 else LABEL_FONT)
