const assert=require('node:assert/strict');
const P=require('../site/engine.js'),coverage=require('../site/assets/coverage.json');
const base={purpose:'portfolio',reading:'balanced',primaryLanguage:'english',additionalLanguage:'',additionalScope:'',count:3,fontType:'none',style:'none',retro:0,rough:0,accent:'detail',textToCheck:''};
assert.equal(P.catalog.length,80);assert.equal(new Set(P.catalog.map(f=>f.id)).size,80);
for(const f of P.catalog){assert.ok(coverage[f.id]);assert.ok(f.categories.length);assert.ok(f.metadata_url.includes('45e3d5269e4a17d823f6d84470bc084dc5ae46f6'));assert.equal(f.mood_scores,null);assert.equal(f.reading_performance,null);assert.equal(f.pairing_scores,null);assert.equal(coverage[f.id].character_count,coverage[f.id].ranges.reduce((n,[a,b])=>n+b-a+1,0));}
for(const count of [1,2,3])for(const additionalLanguage of ['','japanese']){
 const b={...base,count,additionalLanguage,additionalScope:additionalLanguage?'heading':''},r=P.recommend(b,coverage);assert.ok(!r.error,JSON.stringify(r));assert.equal(r.families.length,count);assert.equal(new Set(r.families.map(f=>f.id)).size,count);
 if(additionalLanguage)assert.ok(r.families[0].scripts.includes('japanese'));
 for(let i=0;i<count;i++)for(const f of P.replacements(i,b,r.families,coverage)){assert.ok(!r.families.some(x=>x.id===f.id));if(additionalLanguage&&i===0)assert.ok(f.scripts.includes('japanese'))}
}
for(const count of [1,2,3]){const r=P.recommend({...base,primaryLanguage:'japanese',count},coverage);assert.ok(!r.error);assert.ok(r.families.every(f=>f.scripts.includes('japanese')))}
assert.ok(P.recommend({...base,count:4},coverage).error);
assert.ok(P.recommend({...base,textToCheck:'\u{10ffff}'},coverage).error);
assert.equal(P.hasText('dot','日本語',coverage),true);assert.equal(P.hasText('plex','日本語',coverage),false);
const heading={...base,count:2,additionalLanguage:'japanese',additionalScope:'heading',style:'digital'};
assert.equal(P.recommend(heading,coverage).families[0].id,'dot');
const noto=P.catalog.find(f=>f.id==='notojp');assert.equal(P.priority(noto,'body',heading),P.priority(noto,'body',base));assert.equal(P.showsJapaneseSample(noto),true);
assert.ok(P.recommend({...base,primaryLanguage:'other'},coverage).error);assert.ok(P.recommend({...base,additionalLanguage:'other'},coverage).error);assert.ok(P.languageError({...base,additionalLanguage:'english'}));assert.ok(P.languageError({...base,additionalLanguage:'japanese'}));
const thai={...base,count:2,additionalLanguage:'thai',additionalScope:'heading'};assert.equal(P.recommend(thai,coverage).families[0].id,'chakra');assert.ok(P.recommend({...thai,additionalScope:'both'},coverage).error);
assert.equal(P.hasText('chakra','กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ',coverage),true);
const restored=P.normalizeBrief({language:'heading',count:'2',retro:'3',rough:'1',japaneseText:'見出し'});assert.equal(restored.additionalScope,'heading');assert.equal(restored.additionalLanguage,'japanese');assert.equal(restored.textToCheck,'見出し');for(const key of ['count','retro','rough'])assert.equal(typeof restored[key],'number');
for(const fontType of ['SERIF','SANS_SERIF','MONOSPACE','HANDWRITING','DISPLAY']){
 const brief={...base,count:2,fontType},r=P.recommend(brief,coverage);assert.ok(P.typeMatches(r.families[0],fontType));
 for(const f of P.catalog)for(const role of ['heading','body','accent'])assert.equal(P.priority(f,role,brief),P.priorityDetails(f,role,brief).reduce((n,x)=>n+x.points,0));
}
console.log('80 unique source-reviewed candidates; category preferences; script/text constraints; exact family counts; transparent rule points; replacements; draft migration; and unknown metric checks passed.');

const one={...base,count:1,additionalLanguage:'japanese',additionalScope:'both',fontType:'DISPLAY',style:'digital'};
assert.equal(P.recommend({...one,singleRole:'all'},coverage).families[0].id,'notojp');
assert.equal(P.recommend({...one,singleRole:'heading'},coverage).families[0].id,'dot');
assert.ok(P.recommend({...one,singleRole:''},coverage).error);
assert.ok(P.briefNotices({...one,singleRole:'all'},coverage).some(s=>s.includes('Only 1 family')));
assert.ok(P.briefNotices({...one,singleRole:'all'},coverage).some(s=>s.includes('look you selected')));
assert.deepEqual(P.briefNotices(one,null),[]);
assert.equal(P.normalizeBrief({count:1}).singleRole,'all');
assert.ok(P.catalog.find(f=>f.id==='anton').styles.includes('poster'));
console.log('Single-family scope, legacy interpretation, pool warnings, and poster associations passed.');
