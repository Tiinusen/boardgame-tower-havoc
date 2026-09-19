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

## Review carrier 004 — synthetic runtime simulation corpus

- Added eight typed synthetic match simulations under `.topics/tower-havoc/runtime/simulations/` as replay/conformance examples rather than playtest Evidence.
- Added draft/local `towerhavoc.rule.resolution.v1` for deterministic automatic game effects that do not originate from a player Action Intent.
- Exercised human-style generic Runtime and Machine Runtime randomness sources without making Tower Havoc depend on a digital-only execution model.
- Added `scripts/validate_runtime_simulations.py` and extended gameplay-schema validation.
- Preserved all-rights-reserved licensing status; no reuse license is granted by the simulation corpus.


## Working update — explicit Tower Havoc roles

- Added a canonical `roles/` branch under `.topics/tower-havoc/`.
- Added reusable `tiinex.party.role.v1` endpoints for Steward, Cartographer, Keeper, and Player.
- Kept all four Roles as siblings under one Roles Topic rather than encoding collaboration/delegation as Role Parent ancestry.
- Used the current canonical `Holder Relationship -> Assignment Modes` field and kept Role identity distinct from holder/session/seat identity.
- Bound Steward to project-level direction/acceptance, Cartographer to design/continuity materialization, Keeper to match adjudication/audit/simulation, and Player to seat-level strategy/intent.
- Added explicit boundaries preventing synthetic simulation from becoming playtest Evidence, Keeper mismatches from becoming automatic cheating accusations, and Role references from becoming holder/delegation/publication authority.

## Working update — README surface reduction

- Removed every nested `README.md`; repository root `README.md` is now the only README surface.
- Tiinex artifacts, schemas, generated projections, and directory structure carry their own semantics without parallel README maintenance.
- This reduces documentation drift and avoids treating directory-local summaries as competing semantic authority.

## Working update — canonical c14n-v2 integrity repair

- Re-sealed project-local Tower Havoc schemas and trace artifacts using the current Tiinex `sha256-base64url-c14n-v2` canonicalization rather than the earlier local approximation.
- Rebound every local Parent-target integrity value after Parent digests changed.
- Semantic bodies, Parent declarations, filenames, and directory-local filename lineage were preserved; this pass repairs integrity metadata only.


## Working update — incremental match-lineage stress

- Added `002-incremental-lineage-stress.topic.trace.md` as a new simulation-stress Topic without rewriting the earlier eight-scenario corpus semantics.
- Added `09-incremental-lineage-match/`, a 56-artifact three-seat synthetic match emitted artifact-by-artifact while the harness executes.
- Added `scripts/run_incremental_lineage_simulation.py`; each emitted child requires an already-verifying Parent and random fixture values are consumed only after the corresponding Random Request artifact verifies.
- Added byte-for-byte regeneration validation plus current Tiinex c14n-v2/local-Parent integrity validation and a single-README-surface validator.
- The fixture exercises turn-start/turn-end rule resolution, planned-ammo maturation, three-floor building, reinforcement, a blocked random attack, a full orbit, and successful bell resolution.

## Working update — first real TTS playtest response

- Preserved the first real TTS session observations as `tiinex.evidence.v1` without inventing unreported duration/player-count/session statistics.
- Added successor PLAYTEST Decisions for draw attempts, action-first turn start, flat two-action floor construction, 1 Action + 1 Ammo attacks, bell construction/maturity, Dud removal, deck recycle, compact component inventory, and stacked player-board layout.
- Added playtest baseline.002 rather than rewriting baseline.001.
- Updated generated TTS assets to a compact board, Action/Ammo coin faces, and Classic mode quick-reference card; nested README generation remains disabled.
- Added a GitHub Pages/public-branch publication flow adapted from Tiinex/docs static/mirror publication semantics, including stable `tts/assets/**` delivery and a repository mirror.
- Added an ammunition successor so generated projections no longer repeat the historical zero-action attack cost from baseline.001.

## Working update — Pilot-mediated card generation

- Added a project-local `Pilot` Role for bounded human-mediated external execution, exact-byte Evidence capture, and lineage-correct return Handoffs.
- Added a Tower Havoc card-generation process adapted from the generic Tiinex Business Pilot/Human-Mediated External Execution and the proven Playthings visual-production flow, without importing Playthings domain semantics.
- Preserved the first manually generated six-card batch byte-exactly in execution lineage and recorded the 5:7 versus 4:7 review disposition.
- Added Pilot Card Generation Tranche 1 with seven independent Handoff routes: six Tactic routes and one Ammunition Shortage Event production-reference probe.
