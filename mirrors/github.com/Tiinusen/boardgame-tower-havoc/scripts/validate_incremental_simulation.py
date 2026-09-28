#!/usr/bin/env python3
from pathlib import Path
import shutil, subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parents[1]
SCENARIO=ROOT/'.topics/tower-havoc/runtime/simulations/09-incremental-lineage-match'
GEN=ROOT/'scripts/run_incremental_lineage_simulation.py'
errs=[]

files=sorted(p.relative_to(SCENARIO).as_posix() for p in SCENARIO.rglob('*.trace.md'))
if len(files)!=56:
    errs.append(f'expected 56 committed scenario artifacts, found {len(files)}')

with tempfile.TemporaryDirectory(prefix='tower-havoc-incremental-') as td:
    target=Path(td)
    cp=subprocess.run(
        [sys.executable,str(GEN),'--source-root',str(ROOT),'--target-root',str(target)],
        text=True,capture_output=True
    )
    if cp.returncode!=0:
        errs.append('generator failed: '+(cp.stderr.strip() or cp.stdout.strip()))
    else:
        regen=target/'.topics/tower-havoc/runtime/simulations/09-incremental-lineage-match'
        regen_files=sorted(p.relative_to(regen).as_posix() for p in regen.rglob('*.trace.md'))
        if regen_files!=files:
            errs.append('regenerated file set differs from committed file set')
        else:
            for rel in files:
                if (SCENARIO/rel).read_bytes()!=(regen/rel).read_bytes():
                    errs.append('byte mismatch after deterministic incremental regeneration: '+rel)
                    break

# Structural anti-retrospection checks.
attack_req=SCENARIO/'turns/turn-002/001-2-1-attack.random-request.trace.md'
attack_runtime=SCENARIO/'turns/turn-002/001-2-1-1-machine.runtime.trace.md'
bell_req=SCENARIO/'turns/turn-004/001-2-1-bell.random-request.trace.md'
bell_runtime=SCENARIO/'turns/turn-004/001-2-1-1-machine.runtime.trace.md'
for req,run in [(attack_req,attack_runtime),(bell_req,bell_runtime)]:
    if not req.exists() or not run.exists():
        errs.append('missing random request/runtime pair')
    else:
        # Created At values are deterministic and must show request preceding source runtime.
        def created(p):
            import re
            t=p.read_text(encoding='utf-8').split('- Current',1)[1].split('---',1)[0]
            return re.search(r'^\s+- Created At: (.+)$',t,re.M).group(1)
        if not created(req)<created(run):
            errs.append(f'random source runtime does not follow request: {req.name}')

if errs:
    print('FAIL')
    for e in errs:print('-',e)
    sys.exit(1)
print('OK: TH-SIM-09 regenerates byte-for-byte from incremental emission; random requests precede source runtimes')
