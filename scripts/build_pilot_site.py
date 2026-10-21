"""Build source-reviewed editorial candidates from their pinned family records."""
import argparse
import concurrent.futures
import hashlib
import json
import shutil
import urllib.parse
import urllib.request
from io import BytesIO
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

REVISION='45e3d5269e4a17d823f6d84470bc084dc5ae46f6'
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'site/assets'
LEGACY_LICENSES={'chakra':'chakra-petch-license.txt','plex':'ibm-plex-license.txt','elite':'special-elite-license.txt','rock':'rock-salt-license.txt','ops':'black-ops-license.txt','merri':'merriweather-license.txt','dot':'dotgothic16-license.txt','notojp':'notosansjp-license.txt'}

def download(path):
    url='https://raw.githubusercontent.com/google/fonts/'+REVISION+'/'+urllib.parse.quote(path,safe='/')
    last=None
    for _ in range(3):
        try:
            with urllib.request.urlopen(url,timeout=30) as response:
                return response.read(),url
        except Exception as error:
            last=error
    raise RuntimeError(f'Could not download {path}') from last

def load_candidates():
    manifest=json.loads((ROOT/'research/pilot-catalog.json').read_text())
    candidates=[]
    for id in manifest['family_ids']:
        record=json.loads((ROOT/'research/fonts'/f'{id}.json').read_text())
        f=record['editorial_pilot']
        assert f['reviewed_at'] and f['heading_candidate'] and f['revision']==REVISION
        candidates.append({**f,'record_id':id,'id':f.get('runtime_id',id)})
    assert len(candidates)==len({f['id'] for f in candidates})==80
    return candidates

REUSE={}

def build(f):
    id,name,directory,filename=f['id'],f['name'],f['source'],f['filename']
    url='https://raw.githubusercontent.com/google/fonts/'+REVISION+'/'+urllib.parse.quote(directory+'/'+filename,safe='/')
    previous=REUSE.get(id)
    cached_path=OUT/(id+'.ttf');license_path=OUT/(id+'-license.txt')
    reused=bool(previous and previous.get('source_url')==url and cached_path.exists() and license_path.exists() and hashlib.sha256(cached_path.read_bytes()).hexdigest()==previous.get('sha256') and hashlib.sha256(license_path.read_bytes()).hexdigest()==previous.get('license_sha256'))
    if reused:
        raw=None;source_hash=previous['source_sha256'];font=TTFont(cached_path);axes=previous['axis_settings']
    else:
        raw,url=download(directory+'/'+filename);source_hash=hashlib.sha256(raw).hexdigest();font=TTFont(BytesIO(raw));axes={}
    if not reused and 'fvar' in font:
        axes={a.axisTag:(min(max(400,a.minValue),a.maxValue) if a.axisTag=='wght' else a.defaultValue) for a in font['fvar'].axes}
        font=instantiateVariableFont(font,axes,inplace=True)
    output=id+'.ttf'
    font.flavor=None
    font.save(OUT/output)
    cmap=font.getBestCmap();points=sorted(cmap);ranges=[]
    for point in points:
        if ranges and point==ranges[-1][1]+1:ranges[-1][1]=point
        else:ranges.append([point,point])
    letters=list(range(65,91))+list(range(97,123))
    widths={font['hmtx'][cmap[cp]][0] for cp in letters if cp in cmap}
    mono=all(cp in cmap for cp in letters) and len(widths)==1
    font.close()
    license_name='LICENSE.txt' if directory.startswith('apache/') else 'OFL.txt'
    if reused:
        license_bytes=license_path.read_bytes();license_url=previous['license_url']
    else:license_bytes,license_url=download(directory+'/'+license_name)
    (OUT/(id+'-license.txt')).write_bytes(license_bytes)
    if id in LEGACY_LICENSES:shutil.copyfile(OUT/(id+'-license.txt'),OUT/LEGACY_LICENSES[id])
    file_hash=hashlib.sha256((OUT/output).read_bytes()).hexdigest()
    css="@font-face{font-family:'"+name+"';font-style:normal;font-weight:400;font-display:swap;src:url('./"+output+"') format('truetype')}"
    record={'ranges':ranges,'file':output,'sha256':file_hash,'character_count':len(points),'ascii_uniform_width':mono,'printable_ascii':all(cp in cmap for cp in range(32,127))}
    source={'id':id,'family':name,'source_url':url,'source_sha256':source_hash,'axis_settings':axes,'file':output,'sha256':file_hash,'license_url':license_url,'license_sha256':hashlib.sha256(license_bytes).hexdigest()}
    candidate={k:f[k] for k in ['id','record_id','name','source','fact','body','styles','subsets','reviewed_at','description_url','metadata_url','body_basis','description_available']}
    candidate.update({'css':name,'categories':f['category'],'category':f['category'][0],'scripts':[s for s in ['latin','japanese','thai'] if s in f['subsets']],'monospace':mono,'tradeoff':f.get('tradeoff','This is an editorial candidate. Its fit with your content and other selected families has not been tested.'),'mood_scores':None,'reading_performance':None,'pairing_scores':None})
    return id,css,record,source,candidate

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--reuse-font-files',action='store_true');args=parser.parse_args()
    if args.reuse_font_files and (OUT/'font-sources.json').exists():
        old=json.loads((OUT/'font-sources.json').read_text())
        if old['revision']==REVISION:REUSE.update({f['id']:f for f in old['files']})
    OUT.mkdir(parents=True,exist_ok=True)
    candidates=load_candidates();results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(build,f) for f in candidates]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
            if len(results)%5==0:print(f'Built {len(results)}/{len(candidates)} font assets',flush=True)
    order={f['id']:i for i,f in enumerate(candidates)}
    results.sort(key=lambda r:order[r[0]])
    (OUT/'fonts.css').write_text('\n'.join(r[1] for r in results)+'\n')
    (OUT/'coverage.json').write_text(json.dumps({r[0]:r[2] for r in results},separators=(',',':'))+'\n')
    (OUT/'font-sources.json').write_text(json.dumps({'revision':REVISION,'files':[r[3] for r in results]},indent=2)+'\n')
    catalog=json.dumps([r[4] for r in results],ensure_ascii=False,separators=(',',':'))
    (OUT/'catalog.js').write_text("(function(r){const data="+catalog+";if(typeof module!=='undefined'&&module.exports)module.exports=data;else r.PilotCatalog=data;})(typeof window!=='undefined'?window:globalThis);\n")
    print(f'Built {len(results)} pinned regular font files, licenses, character maps, and source hashes.')

if __name__=='__main__':main()
