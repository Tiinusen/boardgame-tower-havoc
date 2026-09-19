#!/usr/bin/env python3
from pathlib import Path
import re, sys

root=Path(__file__).resolve().parents[1]
prod=root/'.topics/tower-havoc/art/card-production'
terminal='Approved. No more image generation. Create and return the Tiinex handoff package from the current approved output.'
expected=[
'002-1-cartographer-to-pilot-defensive-reroll.handoff.trace.md',
'002-2-cartographer-to-pilot-offensive-reroll-4.handoff.trace.md',
'002-3-cartographer-to-pilot-offensive-reroll-5.handoff.trace.md',
'002-4-cartographer-to-pilot-upper-hand.handoff.trace.md',
'002-5-cartographer-to-pilot-plunder.handoff.trace.md',
'002-6-cartographer-to-pilot-overtime.handoff.trace.md',
'002-7-cartographer-to-pilot-ammunition-shortage.handoff.trace.md',
]
errs=[]
for name in expected:
    p=prod/name
    if not p.exists(): errs.append('missing '+name); continue
    t=p.read_text(encoding='utf-8')
    checks=[
      ('handoff schema','tiinex.handoff.v1'),
      ('from Cartographer','- From: Cartographer'),
      ('to Pilot','- To: Pilot'),
      ('human-mediated mode','- Interaction Mode: human-mediated-external-execution'),
      ('one attempt','- Max Execution Attempts: 1'),
      ('sibling stop','- Sibling Route Continuation: forbidden'),
      ('terminal phrase',terminal),
      ('exact request section','## Exact Human-Visible Generation Request'),
    ]
    for label,needle in checks:
        if needle not in t: errs.append(f'{name}: missing {label}')
    if 'ammunition-shortage' in name:
        if '../../../../art/approved/card-references/event-front-reference.png' not in t:
            errs.append(f'{name}: wrong Event reference')
    else:
        if '001-generated-offensive-reroll-2.png' not in t:
            errs.append(f'{name}: wrong Tactic reference')
for f in ['001-generated-sabotage.png','001-generated-offensive-reroll-2.png','001-generated-offensive-reroll-3.png','001-generated-defensive-reroll.png','001-generated-offensive-reroll-4.png','001-generated-offensive-reroll-5.png']:
    if not (prod/f).is_file(): errs.append('missing preserved source '+f)
if errs:
    print('PILOT CARD ROUTE VALIDATION: FAIL')
    for e in errs: print('-',e)
    sys.exit(1)
print('OK: 7 independent Pilot card-generation routes use exact declared references, one human-mediated attempt, terminal return, and sibling isolation')
