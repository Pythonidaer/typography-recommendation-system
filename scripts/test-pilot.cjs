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
assert.ok(P.recommend({...base,language:'heading',japaneseText:'\u{10ffff}'},coverage).error);
assert.equal(P.hasText('dot','日本語',coverage),true);
assert.equal(P.hasText('plex','日本語',coverage),false);
assert.ok(P.recommend(base,coverage).families.some(f=>f.id==='elite'));
console.log('Count, unique families, Japanese coverage, replacement constraints, unsupported text, and limited-pool failure checks passed.');
