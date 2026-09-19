#!/usr/bin/env python3
from pathlib import Path
import json, math
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
AS=ROOT/'tts'/'assets'; AS.mkdir(parents=True,exist_ok=True)
cards=json.loads((ROOT/'data'/'cards.json').read_text(encoding='utf-8'))['cards']
const=json.loads((ROOT/'data'/'prototype-constants.json').read_text(encoding='utf-8'))
try:
    title_font=ImageFont.truetype('DejaVuSans-Bold.ttf',34)
    body_font=ImageFont.truetype('DejaVuSans.ttf',23)
    small_font=ImageFont.truetype('DejaVuSans.ttf',18)
    tiny_font=ImageFont.truetype('DejaVuSans.ttf',15)
    back_font=ImageFont.truetype('DejaVuSans-Bold.ttf',52)
    coin_font=ImageFont.truetype('DejaVuSans-Bold.ttf',64)
except Exception:
    title_font=body_font=small_font=tiny_font=back_font=coin_font=ImageFont.load_default()

def wrapped(draw,text,font,width):
    words=text.split(); lines=[]; line=''
    for w in words:
        trial=(line+' '+w).strip()
        if draw.textbbox((0,0),trial,font=font)[2] <= width: line=trial
        else:
            if line: lines.append(line)
            line=w
    if line: lines.append(line)
    return lines

def card_image(card,w=600,h=840):
    im=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(im)
    d.rectangle((16,16,w-16,h-16),outline='black',width=4)
    d.text((36,36),card['name'],fill='black',font=title_font)
    d.text((36,92),card['type'].upper(),fill='black',font=small_font)
    y=150
    for line in wrapped(d,card['effect'],body_font,w-72):
        d.text((36,y),line,fill='black',font=body_font); y+=32
    y=max(y+30,600)
    d.text((36,y),'Timing: '+card['timing'],fill='black',font=small_font)
    d.text((36,h-62),card['id'],fill='black',font=small_font)
    return im

cols=8; rows=math.ceil(len(cards)/cols); cw,ch=600,840
sheet=Image.new('RGB',(cols*cw,rows*ch),'white')
for i,c in enumerate(cards): sheet.paste(card_image(c),(i%cols*cw,i//cols*ch))
sheet.save(AS/'cards-front-8x5.png',optimize=True)
back=Image.new('RGB',(cw,ch),'white'); d=ImageDraw.Draw(back); d.rectangle((16,16,cw-16,ch-16),outline='black',width=6); d.text((85,330),'TOWER HAVOC',fill='black',font=back_font); d.text((170,405),'PLAYTEST',fill='black',font=title_font); back.save(AS/'cards-back.png',optimize=True)

# Shared double-sided coin face textures.
def coin_face(label,sub):
    s=512; im=Image.new('RGB',(s,s),'white'); d=ImageDraw.Draw(im)
    d.ellipse((22,22,s-22,s-22),outline='black',width=12)
    bb=d.textbbox((0,0),label,font=coin_font); d.text(((s-(bb[2]-bb[0]))/2,170),label,fill='black',font=coin_font)
    bb2=d.textbbox((0,0),sub,font=small_font); d.text(((s-(bb2[2]-bb2[0]))/2,285),sub,fill='black',font=small_font)
    return im
coin_face('ACTION','BANK / BUILD / REINFORCE').save(AS/'coin-action.png',optimize=True)
coin_face('AMMO','READY / PRODUCTION').save(AS/'coin-ammo.png',optimize=True)

# Compact stacked player board. Printed positions are guidance/state locations, not hidden automation.
W,H=1800,1000
mat=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(mat)
d.rectangle((18,18,W-18,H-18),outline='black',width=5)
d.text((50,32),'TOWER HAVOC — COMPACT PLAYTEST BOARD',fill='black',font=title_font)

# Resource stack wells.
def well(cx,cy,r,label,helper):
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline='black',width=5)
    bb=d.textbbox((0,0),label,font=small_font); d.text((cx-(bb[2]-bb[0])/2,cy-r-34),label,fill='black',font=small_font)
    for i,ln in enumerate(wrapped(d,helper,tiny_font,2*r+40)):
        d.text((cx-r,cy+r+12+i*20),ln,fill='black',font=tiny_font)
well(180,230,82,'ACTION BANK','Action face up; stack vertically')
well(430,230,82,'READY AMMO','Ammo face up; spend to attack')
well(680,230,82,'PRODUCTION','Ammo face up; matures next own turn')

# Quick-reference card slot.
d.rectangle((870,115,1715,365),outline='black',width=4)
d.text((900,135),'FACTION / MODE QUICK REFERENCE',fill='black',font=small_font)
d.text((900,185),'Place the current faction or Classic quick-reference card here.',fill='black',font=tiny_font)

# Tower build rows: two build circles + four printed reinforcement positions.
d.text((55,455),'TOWER CONSTRUCTION',fill='black',font=title_font)
start_y=540
for floor in [3,2,1]:
    y=start_y+(3-floor)*135
    d.text((65,y+24),f'FLOOR {floor}',fill='black',font=small_font)
    d.text((205,y-16),'BUILD',fill='black',font=tiny_font)
    for j in range(2):
        cx=270+j*110; cy=y+38; r=40
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline='black',width=4)
        d.text((cx-8,cy-12),str(j+1),fill='black',font=small_font)
    d.text((485,y-16),'REINFORCEMENT',fill='black',font=tiny_font)
    for j,val in enumerate([2,3,4,5]):
        cx=570+j*110; cy=y+38; r=40
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline='black',width=4)
        d.text((cx-8,cy-12),str(val),fill='black',font=small_font)

# Bell build state.
d.rectangle((1110,455,1720,665),outline='black',width=3)
d.text((1140,480),'BELL BUILD',fill='black',font=small_font)
d.ellipse((1510,485,1590,565),outline='black',width=4)
d.text((1140,540),'Build after 3 floors: 1 Action',fill='black',font=tiny_font)
d.text((1140,575),'Survive one full orbit, then ring attempt: 1 Action',fill='black',font=tiny_font)

# High-value helper text.
d.rectangle((1110,700,1720,930),outline='black',width=3)
helpers=[
 'TURN START: +1 Action first.',
 'DRAW: pay 1 Action; roll D6. 1/6 = draw.',
 'Failed draw may retry for another Action.',
 'After a successful draw: no more draws this turn.',
 'ATTACK: 1 Action + 1 Ready Ammo.',
]
y=725
for h in helpers:
    d.text((1140,y),h,fill='black',font=tiny_font); y+=36
mat.save(AS/'player-mat.png',optimize=True)

# Classic mode quick-reference card; faction variants can later reuse the same footprint.
ref=Image.new('RGB',(850,1200),'white'); d=ImageDraw.Draw(ref); d.rectangle((15,15,835,1185),outline='black',width=4)
d.text((38,35),'TOWER HAVOC — CLASSIC',fill='black',font=title_font)
d.text((38,82),'QUICK REFERENCE',fill='black',font=small_font)
lines=[
 f"Turn start: gain {const['actions_per_turn']} Action FIRST; expire your Event; Production → Ready",
 f"Emergency Ammo: {const['emergency_ammo']['action_cost']} Action → {const['emergency_ammo']['ready_gain']} Ready Ammo",
 f"Planned Ammo: {const['planned_ammo']['action_cost']} Action → {const['planned_ammo']['production_gain']} Production Ammo",
 f"Build floor: {const['building']['same_turn_costs'][0]} Actions",
 f"Reinforce: {const['reinforcement']['action_cost']} Action; values {', '.join(map(str,const['reinforcement']['values']))}",
 f"Attack: {const['attack']['action_cost']} Action + {const['attack']['ammo_cost']} Ready Ammo",
 f"Attack die: {', '.join(map(str,const['attack']['automatic_misses']))} miss; {', '.join(map(str,const['attack']['hittable_values']))} hit unless reinforced",
 f"Draw attempt: {const['draw']['action_cost']} Action; D6 {', '.join(map(str,const['draw']['success_rolls']))} = draw; failures may retry",
 "After first successful draw: no more draw attempts this turn",
 f"Build bell: {const['bell']['construction_action_cost']} Action after 3 floors; wait one orbit",
 f"Ring bell: {const['bell']['action_cost']} Action; success on {', '.join(map(str,const['bell']['success_rolls']))}",
]
y=125
for txt in lines:
    for ln in wrapped(d,txt,body_font,770): d.text((40,y),ln,fill='black',font=body_font); y+=35
    y+=12
d.text((40,1125),'Generated projection — source: .topics/tower-havoc/**',fill='black',font=small_font)
ref.save(AS/'classic-quick-reference-card.png',optimize=True)
# Remove the old generic-reference artifact if it exists.
old=AS/'reference-card.png'
if old.exists(): old.unlink()
print(f'Generated TTS playtest assets for {len(cards)} cards plus compact board/coin/reference assets.')
