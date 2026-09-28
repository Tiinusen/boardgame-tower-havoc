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
- Component Manifest ID: components.mvp.v3

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Faction player board | 6 | approved TTS board art | identical gameplay layout; integrated quick reference; one visual variant per faction |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Shared bell | 1 | obvious bell object | theatrical ring object; per-player bell construction state lives on each board |
| Action/Ammo coin | 144 | shared double-sided coin/token | one common visual design; Action face and Ammo face; stack in resource wells |
| Card | 34 | current Dud-free draw deck | one common back and three visual front families |

- Removed Component: separate faction/mode quick-reference card
- Decision: integrate the quick reference into each player board and keep the rest of the compact shared-coin inventory.
