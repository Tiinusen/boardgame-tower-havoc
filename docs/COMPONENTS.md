> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Tower Havoc — Components

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

## Visible state

- State: provisional/PLAYTEST
- Component Rule ID: components.player-state
- Stack Wells: Action Bank; Ready Ammo; Production
- Stack Well Geometry: each well uses the same coin-sized footprint and permits vertical stacking
- Quick Reference Slot: one faction or mode quick-reference card
- Tower Section: three floor rows; each row has 2 Build slots plus reinforcement positions labelled 2, 3, 4, and 5
- Reinforcement Representation: place one Action-face coin on the matching reinforcement position after paying the reinforcement action cost
- Bell Section: one Bell Build slot using an Action-face coin to show constructed/pending bell state
- Removed Zones: dedicated player-card slot; active-card slot; separate generic-reference-card slot
- Helper Text: concise turn start, draw attempt, attack cost, build cost, and bell sequence reminders may be printed where they reduce lookup
- Decision: use board location plus coin face to communicate persistent state, and stack fungible resources instead of spreading many tokens across large zones.

## Mechanical equivalence

- State: accepted
- Component Rule ID: components.mechanical-equivalence
- Decision: Every faction tower-floor variant must preserve the same outer bounding box, footprint, floor-to-floor contact area, stacking height, alignment behavior, practical stability envelope, reinforcement interface locations, and accessibility. Cosmetic variation must not create a gameplay advantage.
