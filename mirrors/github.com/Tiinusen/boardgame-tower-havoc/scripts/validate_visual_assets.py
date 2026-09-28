#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'data/visual-assets.json').read_text(encoding='utf-8'))
errs=[]

def check_pair(source_rel, runtime_rel, expected_size=None):
    s=ROOT/source_rel; r=ROOT/runtime_rel
    if not s.is_file(): errs.append('missing source '+source_rel); return
    if not r.is_file(): errs.append('missing runtime '+runtime_rel); return
    if s.read_bytes()!=r.read_bytes(): errs.append('runtime bytes differ from approved source: '+runtime_rel)
    if expected_size:
        if Image.open(s).size!=expected_size: errs.append(f'unexpected image size {source_rel}: {Image.open(s).size}')

for row in m['player_boards']:
    check_pair(row['source'],row['tts'],(1448,1086))
    if hashlib.sha256((ROOT/row['source']).read_bytes()).hexdigest()!=row['sha256']:
        errs.append('hash mismatch '+row['source'])
for side,row in m['coin'].items():
    check_pair(row['source'],row['tts'],(512,512))
    if hashlib.sha256((ROOT/row['source']).read_bytes()).hexdigest()!=row['sha256']:
        errs.append('hash mismatch '+row['source'])
for kind,row in m['card_references'].items():
    check_pair(row['source'],row['tts_reference'])
    if hashlib.sha256((ROOT/row['source']).read_bytes()).hexdigest()!=row['sha256']:
        errs.append('hash mismatch '+row['source'])

if (ROOT/'tts/assets/classic-quick-reference-card.png').exists():
    errs.append('obsolete separate quick-reference card still materialized')
if (ROOT/'tts/assets/player-mat.png').exists():
    errs.append('obsolete generic player-mat still materialized')
if errs:
    print('FAIL')
    for e in errs: print('-',e)
    sys.exit(1)
print('OK: 6 approved faction boards, 2 shared coin sides, and 4 card-design references are byte-bound and materialized')
