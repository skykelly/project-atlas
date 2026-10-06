#!/usr/bin/env python3
"""Editorial guards and queue summary. No research, rewriting or publishing."""
import argparse,collections,json,pathlib,re,sys
BLOCK={
 'contrast':r'(?:이|가) 아니라|\bnot\s+.{1,80}\bit[’\x27]?s\b',
 'throat':r'이 사례가 보여주는 것은|중요한 질문은|here[’\x27]?s what|this is why',
 'cliche':r'진정한 경쟁력|결국 실행이 답|미래를 좌우한다|시너지를 창출한다',
}
WARN={'generic':r'중요하다|필요하다|가치가 있다|핵심은', 'passive':r'추진되고|수행되었다|구현되었다'}
def signals(s,rules):
 return {k:[{'line':s[:m.start()].count('\n')+1,'text':m.group()} for m in re.finditer(v,s,re.I)] for k,v in rules.items()}
def body(s):
 return re.sub(r'^---\n[\s\S]*?\n---\n','',s,count=1)
def numbers(s):
 # Exclude URLs, IDs and numbering in headings/lists; retain repeated numbers as a multiset.
 s=body(s);s=re.sub(r'https?://[^\s)]+','',s)
 s=re.sub(r'^#{1,6}\s+\d+(?:\.\d+)*\.?\s*','',s,flags=re.M)
 s=re.sub(r'^\d+\.\s+','',s,flags=re.M)
 return collections.Counter(re.findall(r'(?<![A-Za-z0-9])\d+(?:[,.]\d+)*(?:[~–-]\d+(?:[,.]\d+)*)?',s))
def links(s):return collections.Counter(re.findall(r'\]\(([^)]+)\)',s))
def metadata(s):return re.match(r'^---\n[\s\S]*?\n---\n',s).group() if s.startswith('---\n') else None
def table_shapes(s):
 result=[];rows=[]
 for line in s.splitlines()+['']:
  if line.startswith('|'):rows.append(line.count('|'))
  elif rows:result.append(rows);rows=[]
 return result
p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True)
c=sub.add_parser('check');c.add_argument('--before',required=True);c.add_argument('--after',required=True);c.add_argument('--paths',nargs='+',required=True)
q=sub.add_parser('status');q.add_argument('--progress',default='data/editorial/progress.json')
a=p.parse_args()
if a.command=='status':
 d=json.loads(pathlib.Path(a.progress).read_text());counts=collections.Counter(x['status'] for x in d['documents']);remaining=sum(v for k,v in counts.items() if k!='completed');print(json.dumps({'documents':len(d['documents']),'counts':dict(counts),'remaining_runs':sum((sum(x['status']!='completed' and x['kind']==k for x in d['documents'])+1)//2 for k in ['synthesis','evidence','guide'])},ensure_ascii=False));sys.exit(0)
reports=[];failed=False
for name in a.paths:
 before=(pathlib.Path(a.before)/name).read_text();after=(pathlib.Path(a.after)/name).read_text();errors=[]
 if metadata(before)!=metadata(after):errors.append('metadata_changed')
 if links(before)!=links(after):errors.append('links_changed')
 if numbers(before)!=numbers(after):errors.append('number_inventory_changed')
 if table_shapes(before)!=table_shapes(after):errors.append('table_shape_changed')
 blocks={k:v for k,v in signals(after,BLOCK).items() if v}
 if blocks:errors.append('blocked_expression')
 warns={k:v for k,v in signals(after,WARN).items() if v}
 reports.append({'path':name,'errors':errors,'blocked':blocks,'warnings':warns,'chars_before':len(before),'chars_after':len(after)});failed|=bool(errors)
print(json.dumps({'passed':not failed,'documents':reports},ensure_ascii=False,indent=2));sys.exit(1 if failed else 0)
