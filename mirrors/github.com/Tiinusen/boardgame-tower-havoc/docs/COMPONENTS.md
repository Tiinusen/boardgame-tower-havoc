> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Tower Havoc — Components

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

## Visible state

- State: provisional/PLAYTEST
- Component Rule ID: components.player-state
- Stack Wells: Ready Ammo; Production; Available Actions
- Stack Well Geometry: one coin-sized well per fungible resource; tokens stack vertically
- Quick Reference: printed directly on the board; no card slot
- Tower Section: three permanent floor rows; each row has 2 Build slots plus Reinforcement slots labelled 2, 3, 4, 5
- Build Representation: two Action-face coins placed on a floor's Build slots represent the paid build cost and give each placed marker permanent meaning
- Reinforcement Representation: one Action-face coin on the matching numbered slot records protection against that attack value
- Bell Section: one Bell construction slot; Ring the Bell is an action and needs no separate slot
- Removed Zones: player-card slot; active-card slot; quick-reference-card slot; card-draw-attempt slot; Ring-the-Bell slot
- Decision: use this fixed layout for every faction board; only decorative faction treatment may vary.

## Mechanical equivalence

- State: accepted
- Component Rule ID: components.mechanical-equivalence
- Decision: Every faction tower-floor variant must preserve the same outer bounding box, footprint, floor-to-floor contact area, stacking height, alignment behavior, practical stability envelope, reinforcement interface locations, and accessibility. Cosmetic variation must not create a gameplay advantage.
