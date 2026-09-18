#!/usr/bin/env python3
from pathlib import Path
import json, textwrap, math
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
AS=ROOT/'tts'/'assets'; AS.mkdir(parents=True,exist_ok=True)
cards=json.loads((ROOT/'data'/'cards.json').read_text(encoding='utf-8'))['cards']
const=json.loads((ROOT/'data'/'prototype-constants.json').read_text(encoding='utf-8'))
try:
    title_font=ImageFont.truetype('DejaVuSans-Bold.ttf',34)
    body_font=ImageFont.truetype('DejaVuSans.ttf',23)
    small_font=ImageFont.truetype('DejaVuSans.ttf',18)
    back_font=ImageFont.truetype('DejaVuSans-Bold.ttf',52)
except Exception:
    title_font=body_font=small_font=back_font=ImageFont.load_default()

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
back=Image.new('RGB',(cw,ch),'white'); d=ImageDraw.Draw(back); d.rectangle((16,16,cw-16,ch-16),outline='black',width=6); d.text((85,330),'TOWER HAVOC',fill='black',font=back_font); d.text((170,405),'PROTOTYPE',fill='black',font=title_font); back.save(AS/'cards-back.png',optimize=True)

# Player mat
mat=Image.new('RGB',(1800,1000),'white'); d=ImageDraw.Draw(mat); d.text((55,35),'TOWER HAVOC — PROTOTYPE PLAYER MAT',fill='black',font=title_font)
boxes=[('ACTION BANK',(60,120,540,430)),('READY AMMO',(660,120,1140,430)),('PRODUCTION',(1260,120,1740,430)),('CARDS / HAND',(60,530,760,930)),('ACTIVE / FACTION',(880,530,1740,930))]
for name,b in boxes: d.rectangle(b,outline='black',width=4); d.text((b[0]+24,b[1]+20),name,fill='black',font=title_font)
mat.save(AS/'player-mat.png',optimize=True)

# Reference card derived from constants.
ref=Image.new('RGB',(850,1200),'white'); d=ImageDraw.Draw(ref); d.rectangle((15,15,835,1185),outline='black',width=4); d.text((38,35),'TOWER HAVOC — QUICK REFERENCE',fill='black',font=title_font)
lines=[
 f"Start: expire your persistent Event; Production → Ready; gain {const['actions_per_turn']} action",
 f"Emergency Ammo: {const['emergency_ammo']['action_cost']} action → {const['emergency_ammo']['ready_gain']} Ready Ammo",
 f"Planned Ammo: {const['planned_ammo']['action_cost']} action → {const['planned_ammo']['production_gain']} Production Ammo",
 f"Build this turn: {' / '.join(map(str,const['building']['same_turn_costs']))} actions",
 f"Reinforce: {const['reinforcement']['action_cost']} action; values {', '.join(map(str,const['reinforcement']['values']))}",
 f"Attack: {const['attack']['ammo_cost']} Ready Ammo, {const['attack']['action_cost']} actions",
 f"Attack die: {', '.join(map(str,const['attack']['automatic_misses']))} miss; {', '.join(map(str,const['attack']['hittable_values']))} hit unless reinforced",
 f"Bell: tower must have {const['tower']['levels']} floors at start of your turn; current success roll {', '.join(map(str,const['bell']['success_rolls']))}",
]
y=115
for txt in lines:
    for ln in wrapped(d,txt,body_font,770): d.text((40,y),ln,fill='black',font=body_font); y+=35
    y+=18
d.text((40,1125),'Generated projection — source: .topics/tower-havoc/**',fill='black',font=small_font)
ref.save(AS/'reference-card.png',optimize=True)
print(f'Generated TTS placeholder assets for {len(cards)} cards.')
