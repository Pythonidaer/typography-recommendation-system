const assert=require('node:assert/strict');
const P=require('../site/engine.js'),coverage=require('../site/assets/coverage.json');
const base={purpose:'portfolio',reading:'scan',language:'english',count:3,style:'digital',retro:3,rough:3,accent:'contrast',japaneseText:''};
for(const count of [1,2,3])for(const language of ['english','heading']){
 const b={...base,count,language},r=P.recommend(b,coverage);assert.ok(!r.error,JSON.stringify(r));assert.equal(r.families.length,count);assert.equal(new Set(r.families.map(f=>f.id)).size,count);
 if(language==='heading')assert.ok(r.families[0].scripts.includes('japanese'));
 for(let i=0;i<count;i++)for(const f of P.replacements(i,b,r.families,coverage)){assert.ok(!r.families.some(x=>x.id===f.id));if(language==='heading'&&i===0)assert.ok(f.scripts.includes('japanese'))}
}
assert.ok(P.recommend({...base,language:'both',count:3},coverage).error);
for(const count of [1,2])assert.ok(P.recommend({...base,language:'both',count},coverage).families.every(f=>f.scripts.includes('japanese')));
assert.ok(P.recommend({...base,count:4},coverage).error);
assert.ok(P.recommend({...base,language:'heading',japaneseText:'日本語\u{10ffff}'},coverage).error);
assert.equal(P.hasText('dot','日本語',coverage),true);
assert.equal(P.hasText('plex','日本語',coverage),false);
assert.ok(P.recommend(base,coverage).families.some(f=>f.id==='elite'));
console.log('Count, unique families, Japanese coverage, replacement constraints, unsupported text, and limited-pool failure checks passed.');

// Heading-only Japanese must not add a preference to the body slot.
const headingBrief={...base,count:2,language:'heading',reading:'balanced',rough:1};
assert.deepEqual(P.recommend(headingBrief,coverage).families.map(f=>f.id),['dot','plex']);
assert.ok(P.replacements(1,headingBrief,P.recommend(headingBrief,coverage).families,coverage).some(f=>f.id==='notojp'));
assert.equal(P.showsJapaneseSample(P.catalog.find(f=>f.id==='notojp')),true);
assert.equal(P.showsJapaneseSample(P.catalog.find(f=>f.id==='plex')),false);
assert.ok(P.japaneseTextError({...headingBrief,japaneseText:'sample heading'}));
assert.equal(P.japaneseTextError({...headingBrief,japaneseText:'見出し Web'}),null);
assert.equal(P.japaneseTextError({...headingBrief,japaneseText:''}),null);
const restored=P.normalizeBrief({...headingBrief,count:'2',retro:'3',rough:'1'});
assert.equal(typeof restored.count,'number');assert.equal(typeof restored.retro,'number');assert.equal(typeof restored.rough,'number');
assert.deepEqual(P.recommend(restored,coverage).families.map(f=>f.id),['dot','plex']);
console.log('Heading-only ranking, Japanese specimen eligibility, input guidance, and restored numeric values passed.');
