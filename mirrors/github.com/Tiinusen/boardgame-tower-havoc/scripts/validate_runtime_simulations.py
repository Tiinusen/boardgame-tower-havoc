#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'.topics/tower-havoc/runtime/simulations'
expected_dirs=[
'01-basic-build-bell','02-reinforcement-block','03-middle-floor-collapse','04-planned-ammo-matures',
'05-sabotage-opens-shot','06-ceasefire-rejects-attack','07-bell-ineligible-then-success','08-hidden-deck-commit-reveal',
'09-incremental-lineage-match']
errs=[]
if not (S/'001-runtime-simulation-corpus.topic.trace.md').exists():errs.append('missing corpus Topic')
for d in expected_dirs:
    p=S/d
    if not p.exists():errs.append('missing '+d);continue
    if not (p/'001-ruleset.ruleset.trace.md').exists():errs.append(d+': missing local-major ruleset')
    if not (p/'002-match.match.trace.md').exists():errs.append(d+': missing local-major match')
    if not list((p/'setup').glob('*-initial-state.trace.md')):errs.append(d+': missing initial state')
    if not (p/'terminal'/'001-result.trace.md').exists():errs.append(d+': missing terminal result')
# all synthetic artifacts explicitly say synthetic somewhere in title/body lineage except schema/runtime decision
topic_names={'001-runtime-simulation-corpus.topic.trace.md','002-incremental-lineage-stress.topic.trace.md'}
for p in S.rglob('*.trace.md'):
    t=p.read_text(encoding='utf-8')
    if p.name not in topic_names and 'TH-SIM-' not in t:
        errs.append(str(p.relative_to(ROOT))+': missing TH-SIM scenario identity')
# critical runtime branch coverage
schemas=set()
for p in S.rglob('*.trace.md'):
    t=p.read_text(encoding='utf-8')
    for line in t.splitlines():
        if line.strip().startswith('- Current Schema:'):
            value=line.split(':',1)[1].strip()
            if value.startswith('[') and '](' in value:
                value=value[1:value.index('](')]
            schemas.add(value)
            break
for s in ['towerhavoc.match.v1','towerhavoc.action.intent.v1','towerhavoc.action.resolution.v1','towerhavoc.rule.resolution.v1','towerhavoc.random.request.v1','towerhavoc.random.result.v1','towerhavoc.state.v1','towerhavoc.match.result.v1','towerhavoc.hidden.commitment.v1','towerhavoc.hidden.reveal.v1']:
    if s not in schemas:errs.append('schema not exercised: '+s)
if errs:
    print('FAIL')
    for e in errs:print('-',e)
    sys.exit(1)
print(f'OK: {len(expected_dirs)} synthetic runtime simulations present with core schema coverage')
