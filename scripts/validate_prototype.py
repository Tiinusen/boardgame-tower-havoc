#!/usr/bin/env python3
from pathlib import Path
import json,csv,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
cards=json.loads((ROOT/'data'/'cards.json').read_text(encoding='utf-8'))
const=json.loads((ROOT/'data'/'prototype-constants.json').read_text(encoding='utf-8'))
if cards.get('count') != len(cards.get('cards',[])): errors.append('cards count field does not match card instances')
if cards.get('count') != const.get('deck_count'): errors.append('card manifest count does not match generated deck_count')
ids=[c.get('id') for c in cards.get('cards',[])]
if len(ids)!=len(set(ids)): errors.append('card ids must be unique')
for c in cards.get('cards',[]):
    src=ROOT/c.get('source','')
    if not src.is_file(): errors.append(f"missing card source trace: {c.get('source')}")
with (ROOT/'data'/'components.csv').open(encoding='utf-8',newline='') as f: comps=list(csv.DictReader(f))
by={r['Component']:r for r in comps}
def qty(name):
    try: return int(by[name]['Quantity'].split()[0])
    except Exception: errors.append(f'missing/invalid component quantity for {name}'); return -1
players=const['players']['max']; floors=const['tower']['levels']; vals=len(const['tower']['reinforcement_values'])
if qty('Tower floor') != players*floors: errors.append('tower-floor quantity does not match players × floors')
if qty('Reinforcement marker') != players*floors*vals: errors.append('reinforcement quantity does not match players × floors × values')
if qty('Card') != cards['count']: errors.append('component card quantity does not match card manifest')
for rel in const.get('sources',{}).values():
    if not (ROOT/rel).is_file(): errors.append(f'missing constants source trace: {rel}')
for p in [ROOT/'docs'/'RULEBOOK.md',ROOT/'docs'/'GAME_SPEC.md',ROOT/'docs'/'CARDS.md',ROOT/'docs'/'COMPONENTS.md',ROOT/'docs'/'FACTIONS.md',ROOT/'docs'/'EDITION_BIBLE.md',ROOT/'cad'/'FUSION360_BRIEF.md',ROOT/'tts'/'ONE_HOUR_PLAYTEST.md',ROOT/'playtest'/'FIRST_SESSION.md']:
    if not p.read_text(encoding='utf-8').startswith('> **GENERATED PROJECTION'): errors.append(f'{p.relative_to(ROOT)} is missing generated-projection boundary')
if errors:
    print('FAILED'); [print('-',e) for e in errors]; sys.exit(1)
print(f"OK: generated projections are internally consistent and traceable ({cards['count']} cards, {len(comps)} component rows).")
