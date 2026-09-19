#!/usr/bin/env python3
from pathlib import Path
import json, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[1]
errs=[]
wf=ROOT/'.github/workflows/publish-public.yml'
if not wf.is_file(): errs.append('missing publish workflow')
if not (ROOT/'scripts/build_public_bundle.py').is_file(): errs.append('missing public bundle builder')
with tempfile.TemporaryDirectory(prefix='tower-havoc-public-') as td:
    out=Path(td)/'site'
    cp=subprocess.run([sys.executable,str(ROOT/'scripts/build_public_bundle.py'),'--out',str(out),'--repository','Tiinusen/boardgame-tower-havoc','--ref','validation','--commit','0'*40],cwd=ROOT,text=True,capture_output=True)
    if cp.returncode: errs.append('public bundle build failed: '+(cp.stderr or cp.stdout))
    else:
        for rel in ['.nojekyll','.topics/tower-havoc','docs/RULEBOOK.md','tts/assets/player-mat.png','tts/assets/coin-action.png','tts/assets/coin-ammo.png','tts/assets/classic-quick-reference-card.png','tts/assets/manifest.json','mirrors/github.com/Tiinusen/boardgame-tower-havoc.json','mirrors/github.com/Tiinusen/boardgame-tower-havoc.zip']:
            if not (out/rel).exists(): errs.append('public bundle missing '+rel)
        mf=out/'tts/assets/manifest.json'
        if mf.exists():
            j=json.loads(mf.read_text());
            if not j.get('baseUrl','').startswith('https://tiinusen.github.io/boardgame-tower-havoc/'): errs.append('unexpected Pages base URL')
if errs:
    print('FAIL'); [print('-',e) for e in errs]; sys.exit(1)
print('OK: public bundle exposes lineage/docs, repository mirror, and stable GitHub Pages TTS asset paths')
