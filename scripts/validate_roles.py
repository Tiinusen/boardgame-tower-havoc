#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
roles = root / ".topics" / "tower-havoc" / "roles"

expected = {
    "001-roles.topic.trace.md": "tiinex.topic.v1",
    "001-1-steward.role.trace.md": "tiinex.party.role.v1",
    "001-2-cartographer.role.trace.md": "tiinex.party.role.v1",
    "001-3-keeper.role.trace.md": "tiinex.party.role.v1",
    "001-4-player.role.trace.md": "tiinex.party.role.v1",
}

canonical_modes = [
    "explicit-session",
    "explicit-user-session",
    "explicit-role-invocation",
    "handoff",
    "explicit-participation",
]
order = {v: i for i, v in enumerate(canonical_modes)}

errors = []
for name, schema in expected.items():
    p = roles / name
    if not p.exists():
        errors.append(f"missing: {p.relative_to(root)}")
        continue
    txt = p.read_text(encoding="utf-8")
    if schema not in txt:
        errors.append(f"{name}: missing schema {schema}")
    if schema == "tiinex.party.role.v1":
        for section in [
            "## Role Identity",
            "## Role Boundary",
            "## Authority And Responsibility Boundary",
            "## Holder Relationship",
            "## Interpretation Limits",
        ]:
            if section not in txt:
                errors.append(f"{name}: missing {section}")
        m = re.search(r"^- Assignment Modes: (.+)$", txt, re.M)
        if not m:
            errors.append(f"{name}: missing Assignment Modes")
        else:
            vals = [x.strip() for x in m.group(1).split(",")]
            if any(v not in order for v in vals):
                errors.append(f"{name}: invalid Assignment Modes {vals}")
            elif vals != sorted(vals, key=lambda x: order[x]):
                errors.append(f"{name}: Assignment Modes not in canonical order: {vals}")

if errors:
    print("ROLE VALIDATION: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("ROLE VALIDATION: OK")
print(f"- role artifacts: 4")
print("- roles topic: 1")
print("- canonical assignment mode serialization: OK")
