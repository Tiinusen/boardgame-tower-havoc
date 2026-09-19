#!/usr/bin/env python3
from pathlib import Path
import re, json, csv
ROOT=Path(__file__).resolve().parents[1]
TOP=ROOT/'.topics'/'tower-havoc'
GEN='> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**\n> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.\n\n'

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def sec(rel,name):
    t=read(rel); m=re.search(rf'^## {re.escape(name)}\s*$\n(.*?)(?=^## |^---$|\Z)',t,re.M|re.S); return m.group(1).strip() if m else ''
def field(rel,section,label):
    s=sec(rel,section); m=re.search(rf'^- {re.escape(label)}:\s*(.*)$',s,re.M); return m.group(1).strip() if m else ''
def table(rel,section):
    lines=sec(rel,section).splitlines(); groups=[]; i=0
    while i < len(lines):
        if lines[i].startswith('|') and i+1<len(lines) and re.match(r'^\|?\s*:?-+',lines[i+1]):
            block=[]
            while i<len(lines) and lines[i].startswith('|'): block.append(lines[i]); i+=1
            hdr=[x.strip() for x in block[0].strip('|').split('|')]
            rows=[]
            for ln in block[2:]: rows.append(dict(zip(hdr,[x.strip() for x in ln.strip('|').split('|')])))
            groups.append(rows); continue
        i+=1
    return groups

def decision_text(rel):
    s=sec(rel,'Decision'); m=re.search(r'^- Decision:\s*(.*)$',s,re.M); return m.group(1).strip() if m else s
def numbers(text): return [int(x) for x in re.findall(r'\d+', text or '')]
def first_number(text, default=None):
    xs=numbers(text); return xs[0] if xs else default
def last_number(text, default=None):
    xs=numbers(text); return xs[-1] if xs else default

P={
'setup':'.topics/tower-havoc/rules/001-1-setup.decision.trace.md',
'actions':'.topics/tower-havoc/rules/001-2-1-draw-and-action-costs.decision.trace.md',
'ammo':'.topics/tower-havoc/rules/001-3-1-ammunition-and-attack-cost.decision.trace.md',
'turn':'.topics/tower-havoc/rules/001-4-1-action-first-turn-start.decision.trace.md',
'build':'.topics/tower-havoc/rules/001-5-1-two-action-floor-build.decision.trace.md',
'attack':'.topics/tower-havoc/rules/001-6-2-action-and-ammo-attack-cost.decision.trace.md',
'hit':'.topics/tower-havoc/rules/001-6-1-hit-resolution.condition.trace.md',
'rein':'.topics/tower-havoc/rules/001-7-reinforcement.decision.trace.md',
'collapse':'.topics/tower-havoc/rules/001-8-collapse.decision.trace.md',
'victory':'.topics/tower-havoc/rules/001-9-2-bell-construction.decision.trace.md',
'bell':'.topics/tower-havoc/rules/001-9-1-1-bell-ready.condition.trace.md',
'deck':'.topics/tower-havoc/cards/001-1-1-dud-free-deck.decision.trace.md',
'events':'.topics/tower-havoc/cards/001-9-global-events.decision.trace.md',
'recycle':'.topics/tower-havoc/cards/001-10-1-dud-free-recycle.decision.trace.md',
'components':'.topics/tower-havoc/components/001-1-1-compact-coin-inventory.decision.trace.md',
'layout':'.topics/tower-havoc/components/001-2-1-stacked-player-board.decision.trace.md',
'geometry':'.topics/tower-havoc/components/001-3-mechanical-equivalence.decision.trace.md',
'edition':'.topics/tower-havoc/edition/001-1-edition-independence.decision.trace.md',
'visual':'.topics/tower-havoc/edition/001-2-dieselpunk-visual-direction.decision.trace.md',
'cannon':'.topics/tower-havoc/edition/001-3-light-field-cannon.decision.trace.md',
'classic':'.topics/tower-havoc/factions/001-1-classic-mode.decision.trace.md',
'factions':'.topics/tower-havoc/factions/001-2-faction-mode.decision.trace.md',
'tts':'.topics/tower-havoc/digital/001-1-1-post-playtest-tts-baseline.decision.trace.md',
'cad':'.topics/tower-havoc/physical/001-1-fusion360-master-geometry.decision.trace.md',
'play':'.topics/tower-havoc/playtest/001-1-1-second-session-baseline.decision.trace.md',
'play_surface':'.topics/tower-havoc/playtest/001-2-playtest-observation-surface.presentation.trace.md',
'tts_task':'.topics/tower-havoc/digital/001-tabletop-simulator-prototype.task.trace.md',
'tts_surface':'.topics/tower-havoc/digital/001-2-1-post-playtest-tts-surface.presentation.trace.md',
'cad_task':'.topics/tower-havoc/physical/001-physical-prototype-and-cad.task.trace.md'
}
# Rulebook
rulebook=GEN+'# Tower Havoc — Rulebook\n\n**Edition:** Dieselpunk Edition  \n**Status:** post-first-playtest PLAYTEST  \n**Players:** 2–6\n\n'
rulebook+='## Goal\n\nBuild a three-floor tower, construct its bell, survive the required orbit, then make a legal bell attempt. '+decision_text(P['victory'])+'\n\n'
rulebook+='## Setup\n\n'+sec(P['setup'],'Decision')+'\n\n'
rulebook+='## Start of your turn\n\n'+sec(P['turn'],'Decision')+'\n\n'
rulebook+='## Actions and ammunition\n\n'+sec(P['actions'],'Decision')+'\n\n'+sec(P['ammo'],'Decision')+'\n\n'
rulebook+='## Building\n\n'+sec(P['build'],'Decision')+'\n\n'
rulebook+='## Attacking\n\n'+sec(P['attack'],'Decision')+'\n\n'+sec(P['hit'],'Condition Statement')+'\n\n'+sec(P['hit'],'Branch Outcomes')+'\n\n'
rulebook+='## Reinforcement\n\n'+sec(P['rein'],'Decision')+'\n\n'
rulebook+='## Collapse\n\n'+sec(P['collapse'],'Decision')+'\n\n'
rulebook+='## Cards and events\n\n'+sec(P['deck'],'Decision')+'\n\n'+sec(P['events'],'Decision')+'\n\n'+sec(P['recycle'],'Decision')+'\n\n'
rulebook+='## Victory\n\n'+sec(P['victory'],'Decision')+'\n\n'+sec(P['bell'],'Condition Statement')+'\n\n'
rulebook+='## Next-session PLAYTEST baseline\n\n'+sec(P['play'],'Decision')+'\n'
(ROOT/'docs'/'RULEBOOK.md').write_text(rulebook,encoding='utf-8')

# Cards
card_rels=[
'.topics/tower-havoc/cards/001-2-sabotage.decision.trace.md',
'.topics/tower-havoc/cards/001-3-offensive-reroll.decision.trace.md',
'.topics/tower-havoc/cards/001-4-defensive-reroll.decision.trace.md',
'.topics/tower-havoc/cards/001-6-upper-hand.decision.trace.md',
'.topics/tower-havoc/cards/001-7-plunder.decision.trace.md',
'.topics/tower-havoc/cards/001-8-overtime.decision.trace.md']
cards=[]
for rel in card_rels:
    name=field(rel,'Decision','Name'); typ=field(rel,'Decision','Type'); qty=int(field(rel,'Decision','Quantity')); eff=field(rel,'Decision','Effect'); timing=field(rel,'Decision','Timing'); fam=field(rel,'Decision','Card Family ID').split('.')[-1]
    if fam=='offensive-reroll':
        rows=table(rel,'Decision')[0]
        for row in rows:
            val=row['Printed Value']; n=int(row['Quantity'])
            for i in range(1,n+1): cards.append({'id':f'offensive-reroll-{val}-{i:02d}','family':f'offensive-reroll-{val}','name':f'Offensive Reroll — {val}','type':typ,'effect':eff.replace('the value printed on this card',val),'timing':timing,'source':rel})
    else:
        for i in range(1,qty+1): cards.append({'id':f'{fam}-{i:02d}','family':fam,'name':name,'type':typ,'effect':eff,'timing':timing,'source':rel})
for row in table(P['events'],'Decision')[0]:
    fam=re.sub(r'[^a-z0-9]+','-',row['Event'].lower()).strip('-')
    for i in range(1,int(row['Quantity'])+1): cards.append({'id':f'event-{fam}-{i:02d}','family':f'event-{fam}','name':row['Event'],'type':'event','effect':row['Effect'],'timing':row['Timing'],'source':P['events']})
assert len(cards)==first_number(field(P['deck'],'Decision','Total Cards')), (len(cards), field(P['deck'],'Decision','Total Cards'))
(ROOT/'data').mkdir(exist_ok=True)
(ROOT/'data'/'cards.json').write_text(json.dumps({'schema':'tower-havoc.generated.cards.v0.1','generated_from':'.topics/tower-havoc/**','count':len(cards),'cards':cards},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with (ROOT/'data'/'cards.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','family','name','type','effect','timing','source']); w.writeheader(); w.writerows(cards)
carddoc=GEN+'# Tower Havoc — Cards\n\n'+sec(P['deck'],'Decision')+'\n\n'
for rel in card_rels: carddoc+='## '+field(rel,'Decision','Name')+'\n\n'+sec(rel,'Decision')+'\n\n'
carddoc+='## Global Events\n\n'+sec(P['events'],'Decision')+'\n\n## Deck recycle\n\n'+sec(P['recycle'],'Decision')+'\n'
(ROOT/'docs'/'CARDS.md').write_text(carddoc,encoding='utf-8')

# Components
rows=table(P['components'],'Decision')[0]
with (ROOT/'data'/'components.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['Component','Quantity','Prototype Substitute','Constraint']); w.writeheader(); w.writerows(rows)
(ROOT/'docs'/'COMPONENTS.md').write_text(GEN+'# Tower Havoc — Components\n\n'+sec(P['components'],'Decision')+'\n\n## Visible state\n\n'+sec(P['layout'],'Decision')+'\n\n## Mechanical equivalence\n\n'+sec(P['geometry'],'Decision')+'\n',encoding='utf-8')

# Factions / edition / CAD
(ROOT/'docs'/'FACTIONS.md').write_text(GEN+'# Tower Havoc — Optional Faction Module\n\n'+sec(P['classic'],'Decision')+'\n\n'+sec(P['factions'],'Decision')+'\n',encoding='utf-8')
(ROOT/'docs'/'EDITION_BIBLE.md').write_text(GEN+'# Tower Havoc — Edition Model\n\n'+sec(P['edition'],'Decision')+'\n\n## Dieselpunk Edition\n\n'+sec(P['visual'],'Decision')+'\n\n## Weapon\n\n'+sec(P['cannon'],'Decision')+'\n',encoding='utf-8')
(ROOT/'cad'/'FUSION360_BRIEF.md').write_text(GEN+'# Fusion 360 Brief — Tower Havoc\n\n'+sec(P['cad'],'Decision')+'\n\n## Shared mechanical invariants\n\n'+sec(P['geometry'],'Decision')+'\n\n## Components\n\n'+sec(P['components'],'Decision')+'\n',encoding='utf-8')
(ROOT/'tts'/'ONE_HOUR_PLAYTEST.md').write_text(GEN+'# Tower Havoc — One-Hour TTS Playtest Path\n\n## Prototype baseline\n\n'+sec(P['tts'],'Decision')+'\n\n## First-session ruleset\n\n'+sec(P['play'],'Decision')+'\n\nUse generic objects first. Import/regenerate the generated card deck only after the table has the visible Action Bank, Ready Ammo, Production, tower floors, reinforcement values 2–5, D6, and bell/goal object.\n',encoding='utf-8')

# Constants normalized from lineage. Values are parsed from the owning artifacts rather than duplicated here.
player_range=numbers(field(P['setup'],'Decision','Players'))
build_cost=first_number(field(P['build'],'Decision','Build Cost Per Floor'))
build_costs=[build_cost,build_cost,build_cost]
rein_values=numbers(field(P['rein'],'Decision','Allowed Values'))
miss_values=numbers(field(P['hit'],'Condition Statement','Plain-Language Meaning'))[:2]
emergency=numbers(field(P['ammo'],'Decision','Emergency Production'))
planned=numbers(field(P['ammo'],'Decision','Planned Production'))
constants={
 'schema':'tower-havoc.generated.constants.v0.2','generated_from':'.topics/tower-havoc/**',
 'players':{'min':player_range[0],'max':player_range[-1]},
 'tower':{'levels':first_number(field(P['build'],'Decision','Tower Floors Per Player')),'reinforcement_values':rein_values},
 'actions_per_turn':first_number(field(P['actions'],'Decision','Actions Gained Per Own Turn')),
 'draw':{
   'action_cost':first_number(field(P['actions'],'Decision','Draw Attempt Cost')),
   'success_rolls':numbers(field(P['actions'],'Decision','Draw Attempt Success')),
   'failure_rolls':numbers(field(P['actions'],'Decision','Draw Attempt Failure'))[:4],
   'success_limit':field(P['actions'],'Decision','Draw Success Limit'),
 },
 'starting':{
   'ready_ammo':first_number(field(P['setup'],'Decision','Starting Ready Ammo')),
   'production_ammo':first_number(field(P['setup'],'Decision','Starting Production Ammo')),
   'banked_actions':first_number(field(P['setup'],'Decision','Starting Banked Actions')),
   'built_floors':first_number(field(P['setup'],'Decision','Starting Built Floors')),
 },
 'emergency_ammo':{'action_cost':emergency[0],'ready_gain':emergency[-1]},
 'planned_ammo':{'action_cost':planned[0],'production_gain':planned[-1],'matures':field(P['ammo'],'Decision','Planned Maturity')},
 'attack':{
   'ammo_cost':first_number(field(P['attack'],'Decision','Ready Ammo Cost')),
   'action_cost':first_number(field(P['attack'],'Decision','Action Cost')),
   'automatic_misses':miss_values,
   'hittable_values':rein_values,
   'first_session_max_per_turn':first_number(field(P['attack'],'Decision','Attack Limit')),
   'long_term_rule':field(P['attack'],'Decision','Long-Term Multi-Attack Rule'),
 },
 'reinforcement':{'action_cost':first_number(field(P['rein'],'Decision','Cost')),'values':rein_values},
 'building':{'same_turn_costs':build_costs,'state':field(P['build'],'Decision','State')},
 'bell':{
   'construction_action_cost':first_number(field(P['actions'],'Decision','Bell Construction Cost')),
   'construction_time':field(P['victory'],'Decision','Bell Construction Time'),
   'action_cost':first_number(field(P['actions'],'Decision','Bell Attempt Cost')),
   'success_rolls':[last_number(field(P['victory'],'Decision','Bell Attempt Success'))],
   'first_session_max_attempts_per_turn':first_number(field(P['victory'],'Decision','Bell Attempt Limit')),
   'state':field(P['victory'],'Decision','State'),
 },
 'deck_count':first_number(field(P['deck'],'Decision','Total Cards')),
 'sources':P
}
(ROOT/'data'/'prototype-constants.json').write_text(json.dumps(constants,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Additional generated helper projections.
# CAD parameter worksheet: dimensions remain intentionally unresolved; the parameter names derive from the mechanical-invariant decision.
param_rows=[
 {'parameter':'floor_width','value':'','unit':'mm','status':'TBD','purpose':'shared outer width; mechanical equivalence source','source':P['geometry']},
 {'parameter':'floor_depth','value':'','unit':'mm','status':'TBD','purpose':'shared outer depth; mechanical equivalence source','source':P['geometry']},
 {'parameter':'floor_height','value':'','unit':'mm','status':'TBD','purpose':'shared per-floor stacking height','source':P['geometry']},
 {'parameter':'contact_width','value':'','unit':'mm','status':'TBD','purpose':'shared floor-to-floor contact area','source':P['geometry']},
 {'parameter':'contact_depth','value':'','unit':'mm','status':'TBD','purpose':'shared floor-to-floor contact area','source':P['geometry']},
 {'parameter':'reinforcement_interface_size','value':'','unit':'mm','status':'TBD','purpose':'shared value-marker interface','source':P['cad']},
 {'parameter':'reinforcement_clearance','value':'','unit':'mm','status':'TBD','purpose':'allow marker add/remove while stacked','source':P['cad']},
 {'parameter':'board_width','value':'','unit':'mm','status':'TBD','purpose':'compact player-board physical envelope','source':P['layout']},
 {'parameter':'board_depth','value':'','unit':'mm','status':'TBD','purpose':'compact player-board physical envelope','source':P['layout']},
 {'parameter':'coin_diameter','value':'','unit':'mm','status':'TBD','purpose':'shared Action/Ammo coin diameter and stack-well sizing','source':P['layout']},
 {'parameter':'coin_slot_clearance','value':'','unit':'mm','status':'TBD','purpose':'clearance around stack wells and construction/reinforcement positions','source':P['layout']},
]
with (ROOT/'cad'/'PARAMETERS.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['parameter','value','unit','status','purpose','source']); w.writeheader(); w.writerows(param_rows)
# Playtest working surfaces. Real observations are working material until deliberately preserved as Evidence.
play_surface=sec(P['play_surface'],'Content Boundary')
(ROOT/'playtest'/'NEXT_SESSION.md').write_text(GEN+'# Next playtest\n\n## Baseline\n\n'+sec(P['play'],'Decision')+'\n\n## Observation boundary\n\n'+play_surface+'\n\nDo not rebalance mid-match unless continuation becomes impossible. Preserve what actually happened before deciding what should change.\n',encoding='utf-8')
(ROOT/'playtest'/'SESSION_TEMPLATE.md').write_text(GEN+'# Playtest session template\n\n## Session identity\n\n- Date:\n- Players:\n- Mode:\n- Baseline/variant:\n- Duration:\n- Table rounds:\n- Winner:\n\n## Observations\n\n'+play_surface+'\n\n## Player feedback\n\n- Most exposed moment:\n- Saving actions attractive?\n- Planned Ammo worth waiting for?\n- Wanted to attack but chose not to? Why?\n- Reinforcement felt optional/useful/mandatory?\n- Cards created decisions or noise?\n- Bell created tension or delay?\n- What would you try differently next match?\n\n## Evidence promotion\n\nThis working note is not automatically `tiinex.evidence.v1`. Preserve/session-bind it deliberately after the real session when it is used as evidence for a question or decision.\n',encoding='utf-8')

# TTS setup metadata and README are projections from the digital task/surface plus card manifest.
cols=8
rows_count=(len(cards)+cols-1)//cols
(ROOT/'tts'/'CUSTOM_DECK_SETTINGS.json').write_text(json.dumps({'Face':'assets/cards-front-8x5.png','Back':'assets/cards-back.png','Width':cols,'Height':rows_count,'Number':len(cards),'UniqueBack':False,'GeneratedFrom':[P['deck'],P['tts_surface']]},indent=2)+'\n',encoding='utf-8')
# Comprehensive generated game spec and decisions index
spec=GEN+'# Tower Havoc — Generated Game Specification\n\nThis projection combines current semantic branches for implementation/prototyping. It intentionally keeps rationale in `.topics` rather than duplicating all of it here.\n\n'
for title,key in [('Setup','setup'),('Action economy','actions'),('Ammunition','ammo'),('Turn structure','turn'),('Building','build'),('Attack','attack'),('Reinforcement','rein'),('Collapse','collapse'),('Victory','victory')]: spec+=f'## {title}\n\n'+sec(P[key],'Decision')+'\n\n'
spec+='## Cards\n\n'+sec(P['deck'],'Decision')+'\n\n'+sec(P['events'],'Decision')+'\n\n## Components\n\n'+sec(P['components'],'Decision')+'\n\n## Edition\n\n'+sec(P['visual'],'Decision')+'\n\n## Factions\n\n'+sec(P['factions'],'Decision')+'\n\n## First-session baseline\n\n'+sec(P['play'],'Decision')+'\n'
(ROOT/'docs'/'GAME_SPEC.md').write_text(spec,encoding='utf-8')

decisions=[]
for p in sorted(TOP.rglob('*.decision.trace.md')):
    rel=p.relative_to(ROOT).as_posix(); title=re.search(r'^# (.+)$',p.read_text(encoding='utf-8'),re.M).group(1); d=sec(rel,'Decision'); state=(re.search(r'^- State:\s*(.*)$',d,re.M) or [None,''])[1]; decisions.append((rel,title,state,decision_text(rel)))
out=GEN+'# Tower Havoc — Decision Index\n\n| Source | Decision | State | Operative summary |\n|---|---|---|---|\n'
for rel,title,state,d in decisions: out+=f'| `{rel}` | {title} | {state} | {d.replace("|","/")} |\n'
(ROOT/'docs'/'DECISIONS.md').write_text(out,encoding='utf-8')
print(f'generated {len(cards)} cards, {len(rows)} component rows, {len(decisions)} decisions')

# Regenerate placeholder TTS images from the generated manifests as part of the same projection pass.
import subprocess, sys
subprocess.run([sys.executable, str(ROOT/'scripts'/'generate_tts_assets.py')], check=True)
