#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
SCOPE=ROOT/'.topics'/'tower-havoc'
NAME=re.compile(r'^(\d{3}(?:-\d+)*)-(.+)\.trace\.md$')
errs=[]

def parent_path(p):
    t=p.read_text(encoding='utf-8')
    m=re.search(r'^- Parent\s*$([\s\S]*?)(?=^- Current\s*$)',t,re.M)
    if not m:return None
    q=re.search(r'^\s*- Trace:\s*(?:\[[^\]]*\]\()?([^\)\n]+)\)?\s*$',m.group(1),re.M)
    if not q:return None
    ref=q.group(1).strip()
    if '://' in ref:return None
    return (p.parent/ref).resolve()

for d in sorted({p.parent for p in SCOPE.rglob('*.trace.md')}):
    files=sorted(d.glob('*.trace.md'))
    if not files: continue
    info={}
    for p in files:
        m=NAME.match(p.name)
        if not m:
            errs.append(f'{p.relative_to(ROOT)}: filename does not start with local 3-digit major lineage')
            continue
        info[p.resolve()]=(m.group(1),parent_path(p))
    local=set(info)
    roots=[]; children={}
    seen_labels={}
    for p,(lab,par) in info.items():
        if lab in seen_labels: errs.append(f'{d.relative_to(ROOT)}: duplicate local lineage {lab}')
        seen_labels[lab]=p
        if par in local:
            plab=info[par][0]
            expected_prefix=plab+'-'
            if not lab.startswith(expected_prefix) or lab.count('-') != plab.count('-')+1:
                errs.append(f'{Path(p).relative_to(ROOT)}: same-directory Parent {plab} requires direct child lineage {plab}-N, got {lab}')
            else:
                try: suffix=int(lab.rsplit('-',1)[1])
                except: suffix=-1
                children.setdefault(par,[]).append(suffix)
        else:
            roots.append(lab)
            if '-' in lab:
                errs.append(f'{Path(p).relative_to(ROOT)}: Parent is outside directory, so artifact must use a local major, got {lab}')
    majors=sorted(int(x) for x in roots if re.fullmatch(r'\d{3}',x))
    if majors != list(range(1,len(majors)+1)):
        errs.append(f'{d.relative_to(ROOT)}: local majors must be contiguous from 001; found {majors}')
    for par,sufs in children.items():
        ss=sorted(sufs)
        if ss != list(range(1,len(ss)+1)):
            errs.append(f'{d.relative_to(ROOT)}: children of {info[par][0]} must be contiguous from -1; found {ss}')
if errs:
    print('FAIL')
    for e in errs: print('-',e)
    sys.exit(1)
print('OK: Tower Havoc trace filenames follow directory-local lineage convention')
