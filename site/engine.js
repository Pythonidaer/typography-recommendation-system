(function(root){
const catalog=[
{id:'chakra',name:'Chakra Petch',css:'Chakra Petch',scripts:['latin','thai'],styles:['digital','geometric'],body:false,fact:'Squared letterforms and tapered corners connect it to angular, technical lettering.',tradeoff:'The orderly shapes may feel too tidy for a worn or handmade direction.',source:'ofl/chakrapetch'},
{id:'plex',name:'IBM Plex Sans',css:'IBM Plex Sans',scripts:['latin'],styles:['neutral','modern'],body:true,fact:'IBM describes Plex for print, web, and mobile interfaces. Sans offers a consistent supporting family.',tradeoff:'It contributes less decorative character than the display candidates.',source:'ofl/ibmplexsans'},
{id:'elite',name:'Special Elite',css:'Special Elite',scripts:['latin'],styles:['typewriter','rough'],body:false,fact:'Its design draws on vintage typewriters and uneven ink.',tradeoff:'It can suggest an old document more than an unsettling atmosphere.',source:'apache/specialelite'},
{id:'rock',name:'Rock Salt',css:'Rock Salt',scripts:['latin'],styles:['handwritten','rough'],body:false,fact:'Its letters were drawn with felt-tip markers.',tradeoff:'The handwriting may feel casual or personal rather than ominous.',source:'apache/rocksalt'},
{id:'ops',name:'Black Ops One',css:'Black Ops One',scripts:['latin'],styles:['industrial','rough'],body:false,fact:'Its heavy cut-out letterforms draw on military stencil lettering.',tradeoff:'The military association can pull a design away from a handmade direction.',source:'ofl/blackopsone'},
{id:'merri',name:'Merriweather',css:'Merriweather',scripts:['latin'],styles:['editorial','print'],body:true,fact:'Its designer describes a serif family intended for reading on screens.',tradeoff:'Its book-like character is a different direction from pixel or stencil lettering.',source:'ofl/merriweather'},
{id:'dot',name:'DotGothic16',css:'DotGothic16',scripts:['latin','japanese'],styles:['digital','retro'],body:false,fact:'Its design recalls 16-by-16 bitmap lettering from older games and screens. The supplied file contains Japanese characters.',tradeoff:'The pixel construction may be more literal than a subtle retro reference.',source:'ofl/dotgothic16'},
{id:'notojp',name:'Noto Sans JP',css:'Noto Sans JP',scripts:['latin','japanese'],styles:['neutral','modern'],body:true,fact:'This Japanese sans-serif family covers hiragana, katakana, kanji, and Latin characters.',tradeoff:'It offers less distinctive retro character than the display candidates.',source:'ofl/notosansjp'}
];
function hasText(id,text,coverage){const ranges=coverage&&coverage[id]&&coverage[id].ranges;if(!ranges)return false;return [...text].every(c=>/\s/.test(c)||ranges.some(([a,b])=>{const cp=c.codePointAt(0);return cp>=a&&cp<=b}))}
function rolePool(role,b,coverage){return catalog.filter(f=>{
const jp=b.language==='both'||(b.language==='heading'&&role==='heading')||(b.count===1&&b.language!=='english');
if(jp&&!f.scripts.includes('japanese'))return false;
if((role==='body'||role==='all')&&!f.body)return false;
if(!coverage||!coverage[f.id])return false;
if(b.japaneseText&&jp&&!hasText(f.id,b.japaneseText,coverage))return false;
return true;
})}
function priority(f,role,b){let p=0;
// Version 0.1 editorial rules: source-linked associations, not personality measurements.
if(role==='body'||role==='all'){
 if(f.id==='plex')p+=12;
 if(f.id==='notojp'&&b.language!=='english')p+=24;
 if(f.id==='merri'&&b.style==='editorial')p+=18;
 if(f.id==='merri'&&b.reading==='long')p+=4;
}else{
 if(b.style!=='none'&&f.styles.includes(b.style)&&!(role==='accent'&&b.accent==='contrast'))p+=20;
 if(role==='accent'&&b.accent==='contrast'&&f.styles.includes('rough')&&Number(b.rough)>0)p+=20;
 if(f.styles.some(t=>['digital','retro','print','typewriter'].includes(t)))p+=Number(b.retro)*2;
 if(f.styles.includes('rough'))p+=Number(b.rough)*(role==='accent'?5:2);
 if(role==='heading'&&f.id==='chakra')p+=8;
 if(role==='heading'&&f.id==='dot'&&b.language!=='english')p+=8;
 if(role==='accent'&&f.id==='elite')p+=3;
}
return p}
function recommend(b,coverage){
if(![1,2,3].includes(b.count))return {error:'Choose 1, 2, or 3 families.'};
if(!['english','heading','both'].includes(b.language))return {error:'Choose the required languages.'};
const roles=b.count===1?['all']:b.count===2?['heading','body']:['heading','body','accent'];
const picked=[];
for(const role of roles){
 const eligible=rolePool(role,b,coverage).filter(f=>!picked.some(x=>x.id===f.id));
 eligible.sort((a,c)=>priority(c,role,b)-priority(a,role,b)||a.name.localeCompare(c.name));
 if(!eligible.length)return {error:b.language==='both'?'This pilot has only 2 Japanese-capable families. Try 1 or 2 families, or limit Japanese to headings.':'This small pool cannot meet every requirement. Check the language text or try fewer families.'};
 picked.push({...eligible[0],role});
}
return {families:picked,ruleVersion:'editorial-pilot-0.1'};
}
function replacements(index,b,picked,coverage){const role=picked[index].role;return rolePool(role,b,coverage).filter(f=>!picked.some(x=>x.id===f.id)).sort((a,c)=>priority(c,role,b)-priority(a,role,b)||a.name.localeCompare(c.name))}
const api={catalog,hasText,rolePool,recommend,replacements};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.FontPilot=api;
})(typeof window!=='undefined'?window:globalThis);
