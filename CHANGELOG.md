# Changelog

## 0.4 — artifact-native game model

- Replaced the development-only Tiinex tree with a canonical game model rooted in `tiinex.project.v1`.
- Applied differentiated artifact roles: Project, Topic, Decision, Condition, Task, Presentation Surface, and Preservation.
- Represented the complete current rule/card/component/edition/faction/prototype baseline inside `.topics`.
- Added explicit Conditions for attack-hit resolution and bell eligibility.
- Added Presentation Surface artifacts for rulebook, quick reference, machine manifests, TTS table, and playtest observation checklist.
- Added a Preservation artifact for the original Sänka Torn draft.
- Made `docs/`, `data/`, CAD brief, and TTS quickstart generated projections from `.topics`.
- Added `scripts/generate_from_topics.py` as the projection step.
- Kept playtest Evidence absent until real observations exist.

## v0.6 — semantic schema inheritance

- Re-parented all 13 project-local `towerhavoc.*` gameplay schemas to the nearest existing Tiinex semantic family instead of flattening them directly under `tiinex.root.v1`.
- Added explicit parent-specialization and body-structure inheritance overrides to every local gameplay schema.
- Kept the Tower Havoc Schema Family as a domain grouping/discovery surface rather than an inheritance umbrella.
- Added a direct parent map and validation that fails if a local gameplay schema is accidentally flattened back to Root.

## v0.5 — artifact-native match schemas

- added 13 project-local `towerhavoc.*` gameplay schemas
- added Tiinex Schema Family artifact under the Tower Havoc runtime branch
- landed event-sourced match-authority R&D decision
- added GitHub Issue/Actions runtime task and implementation note
- added hidden-state commitment/reveal semantics so full provenance need not expose cards during play
- added local gameplay-schema validator

## Review carrier — match-lineage demo

- Added a Windows-safe synthetic match lineage under `examples/match-lineage-demo/`.
- Added non-canonical schema candidates under `runtime/experiments/` for Human Runtime and automatic Tower Havoc rule resolution.
- These additions are review material and do not claim real playtest evidence or canonical Tiinex Docs authority.

## Review carrier 003 — directory-local filename lineage

- Corrected `.topics/tower-havoc/**` trace filenames so each directory owns an independent numeric filename-lineage namespace.
- Same-directory Parent relationships now use child suffixes (`001-1`, `001-2`, ...); artifacts whose Parent is outside the directory use local majors (`001`, `002`, ...).
- Rebuilt the synthetic match-lineage demo to demonstrate the same rule across setup and per-turn directories.
- Added `scripts/validate_filename_lineage.py` to prevent accidental drift back to repository-global filename numbering.
- Updated relative references, generated projections, and continuity integrity after the rename.
