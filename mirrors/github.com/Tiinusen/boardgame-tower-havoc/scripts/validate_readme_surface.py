#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
readmes=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('README.md'))
if readmes!=['README.md']:
    print('FAIL: only repository-root README.md is allowed; found',readmes)
    sys.exit(1)
print('OK: repository-root README.md is the only README surface')
