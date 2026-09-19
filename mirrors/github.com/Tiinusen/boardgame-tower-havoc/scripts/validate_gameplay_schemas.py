#!/usr/bin/env python3
from pathlib import Path
import re, sys, hashlib, base64
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'.topics/.schemas/tower-havoc'
expected={
 'towerhavoc.ruleset.v1':('tiinex.instrument.v1',['Ruleset Identity','Canonical Rule Binding','Runtime Parameters','Adjudication Boundary','Interpretation Limits']),
 'towerhavoc.match.v1':('tiinex.event.session.v1',['Match Identity','Ruleset Binding','Participants And Seats','Runtime Policy','Lifecycle','Interpretation Limits']),
 'towerhavoc.match.seat.v1':('tiinex.party.role.v1',['Match Binding','Participant Binding','Faction Assignment','Seat State','Interpretation Limits']),
 'towerhavoc.turn-order.v1':('tiinex.decision.v1',['Match Binding','Eligible Seats','Ordering Method','Ordered Seats','Finality','Interpretation Limits']),
 'towerhavoc.turn.v1':('tiinex.event.window.v1',['Match Binding','Turn Identity','Opening State','Action Window','Closing State','Interpretation Limits']),
 'towerhavoc.action.intent.v1':('tiinex.task.v1',['Match And Turn Binding','Actor','Requested Action','Parameters','Intent State','Interpretation Limits']),
 'towerhavoc.action.resolution.v1':('tiinex.runtime.v1',['Match And Turn Binding','Intent Binding','Adjudication','Costs Applied','Randomness Binding','Outcome And State Delta','Resulting State','Adjudication Provenance','Interpretation Limits']),
 'towerhavoc.rule.resolution.v1':('tiinex.runtime.v1',['Match And Turn Binding','Trigger','Rules Applied','Outcome And State Delta','Resulting State','Execution Provenance','Interpretation Limits']),
 'towerhavoc.random.request.v1':('tiinex.task.v1',['Request Identity','Match Binding','Random Purpose','Outcome Space','Randomness Source Policy','Deterministic Mapping','Request State','Interpretation Limits']),
 'towerhavoc.random.result.v1':('tiinex.derivation.v1',['Request Binding','Source Material','Source Verification','Mapping','Result','Runtime Provenance','Interpretation Limits']),
 'towerhavoc.state.v1':('tiinex.runtime.v1',['Match Binding','State Identity','Public State','Hidden State Commitments','Derivation Binding','Verification State','Interpretation Limits']),
 'towerhavoc.hidden.commitment.v1':('tiinex.claim.v1',['Match Binding','Secret Scope','Commitment Method','Commitment','Custody And Delivery','Reveal Policy','Interpretation Limits']),
 'towerhavoc.hidden.reveal.v1':('tiinex.validation.report.v1',['Commitment Binding','Revealed Material','Verification','Reveal Timing','Interpretation Limits']),
 'towerhavoc.match.result.v1':('tiinex.runtime.v1',['Match Binding','Completion','Winner Or Outcome','Final State','Audit Closure','Interpretation Limits']),
}
def self_digest(text):
    text=text.replace('\r\n','\n').replace('\r','\n')
    text='\n'.join(re.sub(r'[ \t]+$','',ln) for ln in text.split('\n')).rstrip()
    lines=text.split('\n')
    try: ih=lines.index('# Continuity Integrity')
    except ValueError: return None,None
    entries=[]; cur=None
    def strip_link(v):
        m=re.match(r'^\[([^\]]+)\]\([^)]+\)$',v.strip())
        return (m.group(1) if m else v).strip()
    def finish():
        nonlocal cur
        if cur is not None:
            entries.append(cur); cur=None
    for i in range(ih+1,len(lines)):
        line=lines[i]
        if re.match(r'^#\s+',line):
            finish(); break
        m=re.match(r'^-\s+(.+?)\s*$',line)
        if m:
            finish(); cur={'method':strip_link(m.group(1)),'towards':'','vals':[]}; continue
        if cur is None: continue
        m=re.match(r'^\s+-\s+Towards:\s*(.*?)\s*$',line)
        if m: cur['towards']=strip_link(m.group(1))
        m=re.match(r'^(\s+-\s+Value:)([ \t]*)(.*)$',line)
        if m: cur['vals'].append((i,m.group(1),m.group(2),m.group(3).strip()))
    finish()
    selfs=[e for e in entries if e['method']=='sha256-base64url-c14n-v2' and e['towards']=='self']
    if len(selfs)!=1 or len(selfs[0]['vals'])!=1:return None,None
    i,label,spacing,recorded=selfs[0]['vals'][0]
    canonical=lines[:]
    canonical[i]=label+spacing
    digest=base64.urlsafe_b64encode(hashlib.sha256('\n'.join(canonical).encode()).digest()).decode().rstrip('=')
    return recorded,digest

errs=[]
for sid,(parent,sections) in expected.items():
    p=D/(sid+'.schema.md')
    if not p.exists(): errs.append(f'missing {p.relative_to(ROOT)}'); continue
    t=p.read_text(encoding='utf-8')
    envelope=t.split('- Current\n',1)[0]
    if f'Current Schema: [{sid}]' not in t: errs.append(f'{sid}: Current Schema mismatch')
    if f'Parent Schema: [{parent}]' not in envelope: errs.append(f'{sid}: expected direct semantic parent {parent}')
    if 'Parent Schema: [tiinex.root.v1]' in envelope: errs.append(f'{sid}: unexpectedly flattened directly under Root')
    if 'Inheritance Overrides' not in t: errs.append(f'{sid}: missing explicit body inheritance override')
    for s in sections:
        if f'`## {s}`' not in t and f'## {s}\n' not in t:
            errs.append(f'{sid}: missing declared section {s}')
    recorded,computed=self_digest(t)
    if not recorded: errs.append(f'{sid}: missing self integrity entry')
    elif recorded != computed: errs.append(f'{sid}: self integrity mismatch')
if errs:
    print('FAIL')
    print('\n'.join('- '+e for e in errs))
    sys.exit(1)
print(f'OK: {len(expected)} local gameplay schemas use expected Tiinex semantic parents, body overrides, and valid self integrity')
