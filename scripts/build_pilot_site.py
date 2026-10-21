"""Build the pinned, self-hosted font assets for the editorial walkthrough."""
import concurrent.futures
import hashlib
import json
import urllib.parse
import urllib.request
from io import BytesIO
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

REVISION='45e3d5269e4a17d823f6d84470bc084dc5ae46f6'
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'site/assets'
FONTS=[
 ('chakra','Chakra Petch','ofl/chakrapetch','ChakraPetch-Regular.ttf','OFL.txt','chakra-petch-license.txt'),
 ('plex','IBM Plex Sans','ofl/ibmplexsans','IBMPlexSans[wdth,wght].ttf','OFL.txt','ibm-plex-license.txt'),
 ('elite','Special Elite','apache/specialelite','SpecialElite-Regular.ttf','LICENSE.txt','special-elite-license.txt'),
 ('rock','Rock Salt','apache/rocksalt','RockSalt-Regular.ttf','LICENSE.txt','rock-salt-license.txt'),
 ('ops','Black Ops One','ofl/blackopsone','BlackOpsOne-Regular.ttf','OFL.txt','black-ops-license.txt'),
 ('merri','Merriweather','ofl/merriweather','Merriweather[opsz,wdth,wght].ttf','OFL.txt','merriweather-license.txt'),
 ('dot','DotGothic16','ofl/dotgothic16','DotGothic16-Regular.ttf','OFL.txt','dotgothic16-license.txt'),
 ('notojp','Noto Sans JP','ofl/notosansjp','NotoSansJP[wght].ttf','OFL.txt','notosansjp-license.txt'),
]

def download(path):
    url='https://raw.githubusercontent.com/google/fonts/'+REVISION+'/'+urllib.parse.quote(path,safe='/')
    last=None
    for _ in range(3):
        try:
            with urllib.request.urlopen(url,timeout=60) as response:
                return response.read(),url
        except Exception as error:
            last=error
    raise RuntimeError(f'Could not download {path}') from last

def build(item):
    id,name,directory,filename,license_name,license_output=item
    raw,url=download(directory+'/'+filename)
    font=TTFont(BytesIO(raw))
    axes={}
    if 'fvar' in font:
        axes={a.axisTag:(400 if a.axisTag=='wght' else a.defaultValue) for a in font['fvar'].axes}
        font=instantiateVariableFont(font,axes,inplace=True)
    output=id+'.ttf'
    font.flavor=None
    font.save(OUT/output)
    points=sorted(font.getBestCmap())
    ranges=[]
    for point in points:
        if ranges and point==ranges[-1][1]+1:
            ranges[-1][1]=point
        else:
            ranges.append([point,point])
    font.close()
    license_bytes,license_url=download(directory+'/'+license_name)
    (OUT/license_output).write_bytes(license_bytes)
    file_hash=hashlib.sha256((OUT/output).read_bytes()).hexdigest()
    css="@font-face{font-family:'"+name+"';font-style:normal;font-weight:400;font-display:swap;src:url('./"+output+"') format('truetype')}"
    record={'ranges':ranges,'file':output,'sha256':file_hash}
    source={'id':id,'family':name,'source_url':url,'source_sha256':hashlib.sha256(raw).hexdigest(),'axis_settings':axes,'file':output,'sha256':file_hash,'license_url':license_url,'license_sha256':hashlib.sha256(license_bytes).hexdigest()}
    return id,css,record,source

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(build,FONTS))
    (OUT/'fonts.css').write_text('\n'.join(r[1] for r in results)+'\n')
    (OUT/'coverage.json').write_text(json.dumps({r[0]:r[2] for r in results},separators=(',',':'))+'\n')
    (OUT/'font-sources.json').write_text(json.dumps({'revision':REVISION,'files':[r[3] for r in results]},indent=2)+'\n')
    print('Built 8 pinned regular font files, licenses, character maps, and source hashes.')

if __name__=='__main__':
    main()
