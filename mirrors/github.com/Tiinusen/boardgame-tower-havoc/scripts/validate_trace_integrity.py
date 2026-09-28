#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, re, sys

ROOT=Path(__file__).resolve().parents[1]
TARGETS=list((ROOT/'.topics/tower-havoc').rglob('*.trace.md')) + list((ROOT/'.topics/.schemas/tower-havoc').glob('*.schema.md'))
METHOD='sha256-base64url-c14n-v2'
errs=[]

def normalize(md):
    md=md.replace('\r\n','\n').replace('\r','\n')
    return '\n'.join(line.rstrip(' \t') for line in md.split('\n')).rstrip()

def strip_link(v):
    m=re.match(r'^\[([^\]]+)\]\([^)]+\)$',v.strip())
    return (m.group(1) if m else v).strip()

def entries(md):
    norm=normalize(md); lines=norm.split('\n')
    try: ih=lines.index('# Continuity Integrity')
    except ValueError: return lines,[]
    out=[]; cur=None
    def finish():
        nonlocal cur
        if cur is not None: out.append(cur); cur=None
    for i in range(ih+1,len(lines)):
        line=lines[i]
        if re.match(r'^#\s+',line): finish(); break
        m=re.match(r'^-\s+(.+?)\s*$',line)
        if m:
            finish(); cur={'method':strip_link(m.group(1)),'towards':'','vals':[]}; continue
        if cur is None: continue
        m=re.match(r'^\s+-\s+Towards:\s*(.*?)\s*$',line)
        if m: cur['towards']=strip_link(m.group(1))
        m=re.match(r'^(\s+-\s+Value:)([ \t]*)(.*)$',line)
        if m: cur['vals'].append((i,m.group(1),m.group(2),m.group(3).strip()))
    finish()
    return lines,out

def self_digest(path):
    md=path.read_text(encoding='utf-8')
    lines,es=entries(md)
    ss=[e for e in es if e['method']==METHOD and e['towards']=='self']
    if len(ss)!=1 or len(ss[0]['vals'])!=1:
        return None,None,'ambiguous self entry'
    i,label,spacing,decl=ss[0]['vals'][0]
    c=lines[:]; c[i]=label+spacing
    comp=base64.urlsafe_b64encode(hashlib.sha256('\n'.join(c).encode()).digest()).decode().rstrip('=')
    return decl,comp,''

def local_parent(path):
    text=path.read_text(encoding='utf-8')
    if '- Parent' not in text.split('- Current',1)[0]: return None
    m=re.search(r'^\s+- Trace: \[[^\]]+\]\(([^)]+)\)\s*$',text.split('- Current',1)[0],re.M)
    if not m:return None
    ref=m.group(1).strip()
    if '://' in ref or '::' in ref:return None
    p=(path.parent/ref).resolve()
    return p if p.exists() else None

self_cache={}
for p in TARGETS:
    decl,comp,reason=self_digest(p)
    self_cache[p.resolve()]=(decl,comp)
    if reason or decl!=comp:
        errs.append(f'{p.relative_to(ROOT)}: self c14n-v2 mismatch ({reason or "digest-mismatch"})')

for p in (ROOT/'.topics/tower-havoc').rglob('*.trace.md'):
    par=local_parent(p)
    if not par or par.resolve() not in self_cache: continue
    expected=self_cache[par.resolve()][0]
    _,es=entries(p.read_text(encoding='utf-8'))
    nonself=[e for e in es if e['method']==METHOD and e['towards']!='self']
    if len(nonself)!=1 or len(nonself[0]['vals'])!=1:
        errs.append(f'{p.relative_to(ROOT)}: local Parent integrity entry ambiguous')
        continue
    actual=nonself[0]['vals'][0][3]
    if actual!=expected:
        errs.append(f'{p.relative_to(ROOT)}: Parent-target digest does not match {par.relative_to(ROOT)}')

if errs:
    print('FAIL')
    for e in errs: print('-',e)
    sys.exit(1)
print(f'OK: {len(TARGETS)} Tower Havoc schemas/trace artifacts verify c14n-v2; local Parent targets agree')
