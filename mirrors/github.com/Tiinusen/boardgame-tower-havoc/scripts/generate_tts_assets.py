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


# Approved visual runtime materialization.
# These bytes are source material under art/approved/** and must not be regenerated heuristically.
import shutil

approved=ROOT/'art'/'approved'
board_src=approved/'player-boards'
board_dst=AS/'player-boards'
board_dst.mkdir(parents=True,exist_ok=True)
for p in sorted(board_src.glob('*.png')):
    shutil.copy2(p,board_dst/p.name)

shutil.copy2(approved/'coins'/'action-side.png',AS/'coin-action.png')
shutil.copy2(approved/'coins'/'ammo-side.png',AS/'coin-ammo.png')

ref_src=approved/'card-references'
ref_dst=AS/'card-design-references'
ref_dst.mkdir(parents=True,exist_ok=True)
for p in sorted(ref_src.glob('*.png')):
    shutil.copy2(p,ref_dst/p.name)

# Remove obsolete first-playtest presentation assets if they survive from an older checkout.
for stale in [AS/'player-mat.png',AS/'classic-quick-reference-card.png',AS/'reference-card.png']:
    if stale.exists():
        stale.unlink()

print(f'Generated placeholder TTS card deck for {len(cards)} cards and materialized approved board/coin/card-reference assets.')
