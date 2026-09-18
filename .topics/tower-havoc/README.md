# Tower Havoc semantic map

`.topics/tower-havoc/**` is the canonical semantic source of the game. The repository root README and generated files are reception/projection surfaces, not competing rule authority.

## Main lineage

Filename lineage is local to each directory. The important current branches are therefore read per directory rather than as one repository-global number tree:

- `001-tower-havoc.project.trace.md` — Project root in `.topics/tower-havoc/`
- `001-1-*` and `001-2-*` — direct same-directory children of the Project root
- `rules/001-*` — current playable rules and rule Conditions
- `cards/001-*` — deck/card family definitions
- `components/001-*` — bill of materials and physical state model
- `edition/001-*` — edition-independent boundary and Dieselpunk presentation
- `factions/001-*` — Classic/Faction modes
- `digital/001-*` — TTS task and presentation surface
- `physical/001-*` — physical/CAD task
- `playtest/001-*` — playtest task/baseline/surface; future Evidence belongs here
- `presentation/001-*` — generated rulebook/reference/data presentation surfaces
- `runtime/001-*` — match-provenance runtime exploration
- `sources/001-*` — preserved original source material

## Filename lineage convention

Filename lineage is a **directory-local navigation convention**, not semantic identity and not a replacement for the artifact's declared `Parent`.

- Every directory owns its own filename-lineage namespace.
- A trace artifact whose semantic Parent is absent from that same directory receives the next free local major: `001`, `002`, `003`, ...
- A trace artifact whose semantic Parent is present in that directory receives the next free child slot under the Parent's local filename lineage: `001-1`, `001-2`, ...
- The rule applies recursively: a child of `001-1` in the same directory becomes `001-1-1`, then `001-1-2`, and so on.
- Moving an artifact to another directory recalculates only its filename lineage in the destination directory. Its semantic `Parent` remains whatever the artifact explicitly declares.
- Directory placement, filename lineage, and semantic Parent are therefore three distinct surfaces.

Example:

```text
rules/
├── 001-core-rules.topic.trace.md
├── 001-1-action-economy.decision.trace.md
├── 001-2-ammunition.decision.trace.md
└── 001-3-attack.decision.trace.md
    └── 001-3-1-hit-resolution.condition.trace.md
```

If the `attack` artifact were moved alone into an empty `combat/` directory while keeping its semantic Parent in `rules/`, its filename would become local major `001-attack...`, because its Parent is no longer in the same directory.

## Artifact-role discipline

This model intentionally does not make everything a Topic:

- Project = the game project boundary
- Topic = durable semantic game domains
- Decision = current governing rules/design outcomes
- Condition = explicit rule gates/branches
- Task = work to perform (TTS, CAD, playtesting)
- Presentation Surface = generated/interactive views of canonical material
- Preservation = historical source material kept for later judgment
- Evidence = deliberately absent until real playtest observations exist

## Match provenance runtime

The `runtime/001-*` branch explores playing Tower Havoc directly through artifact lineage. Project-local gameplay schema notes live under `.topics/.schemas/tower-havoc/`. These runtime schemas are intentionally local to Tower Havoc and do not claim generic Tiinex game semantics.
