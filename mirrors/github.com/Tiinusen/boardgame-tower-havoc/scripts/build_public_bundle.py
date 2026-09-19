#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, shutil, zipfile, html

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.site-publish','node_modules','.tiinex'}
PUBLIC_PATHS=['README.md','RIGHTS.md','.topics','docs','data','tts/assets']

def copy_path(src:Path,dst:Path):
    if src.is_dir():
        shutil.copytree(src,dst,ignore=shutil.ignore_patterns(*EXCLUDED))
    else:
        dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)

def snapshot_files(root:Path):
    return [p for p in sorted(root.rglob('*')) if p.is_file() and not any(part in EXCLUDED for part in p.relative_to(root).parts)]

def deterministic_zip(src_root:Path,out:Path):
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_STORED,allowZip64=False) as z:
        for p in snapshot_files(src_root):
            rel=p.relative_to(src_root).as_posix()
            zi=zipfile.ZipInfo(rel,date_time=(1980,1,1,0,0,0)); zi.compress_type=zipfile.ZIP_STORED; zi.external_attr=(0o100644 & 0xFFFF)<<16
            z.writestr(zi,p.read_bytes())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='.site-publish'); ap.add_argument('--repository',default=os.getenv('GITHUB_REPOSITORY','Tiinusen/boardgame-tower-havoc')); ap.add_argument('--ref',default=os.getenv('SOURCE_REF','main')); ap.add_argument('--commit',default=os.getenv('GITHUB_SHA',''))
    a=ap.parse_args(); out=(ROOT/a.out).resolve(); shutil.rmtree(out,ignore_errors=True); out.mkdir(parents=True); (out/'.nojekyll').write_text('',encoding='utf-8')
    for rel in PUBLIC_PATHS:
        src=ROOT/rel
        if src.exists(): copy_path(src,out/rel)
    owner,repo=a.repository.split('/',1)
    pages_base=f'https://{owner.lower()}.github.io/{repo}/'
    assets=[]
    asset_root=out/'tts/assets'
    if asset_root.exists():
        for p in sorted(asset_root.iterdir()):
            if p.is_file(): assets.append({'path':f'tts/assets/{p.name}','url':pages_base+f'tts/assets/{p.name}','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
        (asset_root/'manifest.json').write_text(json.dumps({'type':'tower-havoc.tts.pages-assets.v1','repository':a.repository,'baseUrl':pages_base,'assets':assets},indent=2)+'\n',encoding='utf-8')
    # Repository mirror: inspectable directory + deterministic archive + metadata, matching Tiinex/docs public mirror intent.
    mirror_parent=out/'mirrors/github.com'/owner
    mirror_dir=mirror_parent/repo; mirror_parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(ROOT,mirror_dir,ignore=shutil.ignore_patterns(*EXCLUDED))
    archive=mirror_parent/f'{repo}.zip'; deterministic_zip(mirror_dir,archive)
    meta={'type':'tiinex.repository.snapshot','version':1,'repository':f'github.com/{a.repository}','ref':a.ref,'commit':a.commit,'archive':archive.name,'directory':repo+'/' ,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'selection':'source-ref'}
    (mirror_parent/f'{repo}.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
    index=(f'<!doctype html><html><head><meta charset="utf-8"><title>Tower Havoc public material</title></head><body>'
           f'<h1>Tower Havoc</h1><p>Published projection/mirror surface. Canonical game semantics remain in repository lineage.</p><ul>'
           f'<li><a href=".topics/tower-havoc/">Lineage material</a></li><li><a href="docs/RULEBOOK.md">Rulebook projection</a></li>'
           f'<li><a href="tts/assets/manifest.json">TTS asset manifest</a></li><li><a href="mirrors/github.com/{html.escape(owner)}/{html.escape(repo)}.json">Repository mirror metadata</a></li>'
           f'</ul></body></html>')
    (out/'index.html').write_text(index,encoding='utf-8')
    print(f'Built public bundle at {out}; {len(assets)} TTS asset(s); mirror sha256={meta["sha256"]}')
if __name__=='__main__': main()
