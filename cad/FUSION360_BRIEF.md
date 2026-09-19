> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Fusion 360 Brief — Tower Havoc

- State: accepted
- CAD Rule ID: cad.master
- Decision: Begin physical modeling from one parametric mechanically neutral tower-floor master. Preserve shared bounding box, footprint, stacking/contact area, height, alignment, stability envelope, reinforcement interfaces, and access. Create cosmetic faction variants only after the master survives physical stacking tests.
- Reinforcement Interface Options: slots; holes; pegs; clips; magnets; adjacent marker positions
- First Prototype Priority: visibility and easy removal over realism

## Shared mechanical invariants

- State: accepted
- Component Rule ID: components.mechanical-equivalence
- Decision: Every faction tower-floor variant must preserve the same outer bounding box, footprint, floor-to-floor contact area, stacking height, alignment behavior, practical stability envelope, reinforcement interface locations, and accessibility. Cosmetic variation must not create a gameplay advantage.

## Components

- State: provisional/PLAYTEST
- Component Manifest ID: components.mvp.v2

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Compact player board | 6 | printed/TTS board | coin-sized stack wells plus tower-construction rows and faction/mode quick-reference slot |
| Faction or mode quick-reference card | 6 | printed/TTS card | one per player; Classic uses a Classic-mode card instead of a separate generic reference card |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Shared bell | 1 | obvious bell object | theatrical ring object; per-player bell construction state lives on each board |
| Action/Ammo coin | 144 | double-sided coin/token | Action face on one side; Ammo face on the other; one shared physical vocabulary for Action Bank, Ready Ammo, Production, build/reinforcement markers, and bell construction |
| Card | 34 | generated prototype deck | next PLAYTEST deck manifest comes from card lineage |
