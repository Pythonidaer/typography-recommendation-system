(function(root){
const catalog=typeof module!=='undefined'&&module.exports?require('./assets/catalog.js'):root.PilotCatalog;
const categoryNames={SANS_SERIF:'Sans serif',SERIF:'Serif',MONOSPACE:'Monospace',HANDWRITING:'Handwriting',DISPLAY:'Display'};
const languages={english:{name:'English',script:'latin'},japanese:{name:'Japanese',script:'japanese'},thai:{name:'Thai',script:'thai'}};
function normalizeBrief(b){
 const {language,japaneseText,...rest}=b;
 const legacyJapanese=language==='heading'||language==='both';
 return {...rest,fontType:b.fontType||'none',primaryLanguage:b.primaryLanguage||'english',additionalLanguage:b.additionalLanguage??(legacyJapanese?'japanese':''),additionalScope:b.additionalScope??(language==='both'?'both':language==='heading'?'heading':''),textToCheck:b.textToCheck??japaneseText??'',count:Number(b.count),retro:Number(b.retro),rough:Number(b.rough)};
}
function languageError(raw){const b=normalizeBrief(raw);
 if(!languages[b.primaryLanguage]||(b.additionalLanguage&&!languages[b.additionalLanguage]))return 'This pilot cannot yet recommend fonts for that language. Choose a supported language to explore the current samples.';
 if(b.additionalLanguage===b.primaryLanguage)return 'Choose a different additional language, or choose None.';
 if(b.additionalLanguage&&!['heading','both'].includes(b.additionalScope))return 'Choose where the additional language will appear.';
 return null;
}
function requiredScripts(role,raw){const b=normalizeBrief(raw),ids=[b.primaryLanguage];
 if(b.additionalLanguage&&(b.additionalScope==='both'||role==='heading'||role==='all'))ids.push(b.additionalLanguage);
 return [...new Set(ids.map(id=>languages[id]?.script).filter(Boolean))];
}
function showsJapaneseSample(f){return f.scripts.includes('japanese')}
function hasText(id,text,coverage){const ranges=coverage&&coverage[id]&&coverage[id].ranges;if(!ranges)return false;return [...text].every(c=>/\s/.test(c)||ranges.some(([a,b])=>{const cp=c.codePointAt(0);return cp>=a&&cp<=b}))}
function rolePool(role,raw,coverage){const b=normalizeBrief(raw);if(languageError(b))return [];const scripts=requiredScripts(role,b);return catalog.filter(f=>{
if(!scripts.every(script=>f.scripts.includes(script)))return false;
if((role==='body'||role==='all')&&!f.body)return false;
if(!coverage||!coverage[f.id])return false;
const checkText=!b.additionalLanguage||b.additionalScope==='both'||role==='heading'||role==='all';
if(b.textToCheck&&checkText&&!hasText(f.id,b.textToCheck,coverage))return false;
return true;
})}
function typeMatches(f,type){return type==='MONOSPACE'?f.monospace===true:f.categories.includes(type)}
function priorityDetails(f,role,raw){const b=normalizeBrief(raw),details=[];const add=(reason,points)=>{if(points)details.push({reason,points})};
if(role==='body'||role==='all'){
 if(f.body===true)add('Supporting-text shortlist',12);
 if(b.style!=='none'&&f.styles.includes(b.style))add('Requested lettering association',6);
 if(role==='all'&&typeMatches(f,b.fontType))add('Requested heading type',30);
}else{
 if(role==='heading'&&typeMatches(f,b.fontType))add('Requested heading type',30);
 if(b.style!=='none'&&f.styles.includes(b.style)&&!(role==='accent'&&b.accent==='contrast'))add('Requested lettering association',20);
 if(role==='accent'&&b.accent==='contrast'&&f.styles.includes('rough')&&Number(b.rough)>0)add('Contrasting rough accent',20);
 if(f.styles.some(t=>['digital','retro','print','typewriter'].includes(t)))add('Retro preference × 2',Number(b.retro)*2);
 if(f.styles.includes('rough'))add('Rough preference × '+(role==='accent'?5:2),Number(b.rough)*(role==='accent'?5:2));
}
return details;
}
function priority(f,role,b){return priorityDetails(f,role,b).reduce((sum,x)=>sum+x.points,0)}
function recommend(b,coverage){
b=normalizeBrief(b);
const issue=languageError(b);if(issue)return {error:issue};
if(![1,2,3].includes(b.count))return {error:'Choose 1, 2, or 3 families.'};
const roles=b.count===1?['all']:b.count===2?['heading','body']:['heading','body','accent'];
const picked=[];
for(const role of roles){
 const eligible=rolePool(role,b,coverage).filter(f=>!picked.some(x=>x.id===f.id));
 eligible.sort((a,c)=>priority(c,role,b)-priority(a,role,b)||a.name.localeCompare(c.name));
 if(!eligible.length)return {error:'This small pool does not have enough distinct families for these languages and text roles. Try fewer families or change where the additional language appears.'};
 picked.push({...eligible[0],role});
}
return {families:picked,ruleVersion:'editorial-pilot-0.3'};
}
function replacements(index,b,picked,coverage){b=normalizeBrief(b);const role=picked[index].role;return rolePool(role,b,coverage).filter(f=>!picked.some(x=>x.id===f.id)).sort((a,c)=>priority(c,role,b)-priority(a,role,b)||a.name.localeCompare(c.name))}
const api={categoryNames,typeMatches,priority,priorityDetails,normalizeBrief,languages,languageError,requiredScripts,showsJapaneseSample,catalog,hasText,rolePool,recommend,replacements};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.FontPilot=api;
})(typeof window!=='undefined'?window:globalThis);
