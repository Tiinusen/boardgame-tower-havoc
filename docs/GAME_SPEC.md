> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Tower Havoc — Generated Game Specification

This projection combines current semantic branches for implementation/prototyping. It intentionally keeps rationale in `.topics` rather than duplicating all of it here.

## Setup

- State: accepted
- Rule ID: rules.setup
- Players: 2–6
- Starting Ready Ammo: 2 per player
- Starting Production Ammo: 0
- Starting Banked Actions: 0
- Starting Built Floors: 0
- Start Player: highest D6 roll
- Turn Direction: clockwise
- Decision: Each player takes one player set with three tower floors and the resources required by the selected game mode. Classic mode is the reference setup.

## Action economy

- State: provisional/PLAYTEST
- Rule ID: rules.actions
- Actions Gained Per Own Turn: 1
- General Action Bank Cap: none
- Pass Cost: 0
- Draw Attempt Cost: 1 action
- Draw Attempt Die: D6
- Draw Attempt Success: 1 or 6
- Draw Attempt Failure: 2, 3, 4, or 5; the player may spend another action to attempt again during the same turn
- Draw Success Limit: after the first successful draw, that player may not make another draw attempt during the same turn
- Reinforce Cost: 1 action
- Attack Cost: 1 action plus 1 Ready Ammo
- Bell Construction Cost: 1 action
- Bell Attempt Cost: 1 action
- Draw Phrase: `Ah, hmmm, mmmm`
- Decision: keep banked actions as strategic capital while making attacks and card access visibly compete for that same capital.

## Ammunition

- State: provisional/PLAYTEST
- Rule ID: rules.ammunition
- Emergency Production: 1 action -> 1 Ready Ammo immediately
- Planned Production: 1 action -> 2 Production Ammo
- Planned Maturity: all Production Ammo becomes Ready Ammo at the beginning of that player's next own turn
- Attack Ammo Cost: 1 Ready Ammo
- Attack Action Cost: 1 action
- Decision: Ready Ammo and Production Ammo remain separate visible states; an attack now spends both 1 action and 1 Ready Ammo under the next-session baseline.

## Turn structure

- State: provisional/PLAYTEST
- Rule ID: rules.turn
- Start Step 1: gain 1 action; every own turn begins with this gain before any other start-of-turn game effect resolves
- Start Step 2: expire any persistent global event owned by this player from the previous orbit
- Start Step 3: move all of this player's Production Ammo to Ready Ammo
- Action Phase: spend any legal combination of available actions/resources in any legal order
- End: remaining actions stay banked; play passes clockwise
- Decision: the action gain is the first explicit event of every own turn and is never skipped because another start-of-turn effect also resolves.

## Building

- State: provisional/PLAYTEST
- Rule ID: rules.building
- Tower Floors Per Player: 3
- Build Cost Per Floor: 2 actions
- Same-Turn Multi-Floor Building: allowed when enough banked actions are available
- Three-Floor Burst Total: 6 actions
- Board Representation: each floor row exposes two Build slots sized for the shared Action/Ammo coin; the slots communicate the two-action cost
- Partial Construction State: none; both actions are paid when the floor is built, and the physical tower remains the authoritative visible built-floor state
- Decision: use one flat two-action floor cost so construction is easier to read and manipulate while preserving banked-action burst play.

## Attack

- State: provisional/PLAYTEST
- Rule ID: rules.attack
- Weapon Metaphor: light field cannon
- Target: one specific built floor of one opponent
- Ready Ammo Cost: 1
- Action Cost: 1
- Total Cost: 1 action plus 1 Ready Ammo
- Attack Limit: maximum 1 attack per player turn for the next-session baseline
- Long-Term Multi-Attack Rule: unresolved/PLAYTEST
- Decision: an attack consumes both one action and one Ready Ammo before its D6 resolution.

## Reinforcement

- State: accepted
- Rule ID: rules.reinforcement
- Cost: 1 action per reinforcement
- Allowed Values: 2, 3, 4, 5
- Placement: one marker protects one value on one built floor
- Duplicate Value On Same Floor: not allowed/has no additional effect
- Full Protection: a floor protected on 2, 3, 4, and 5 is immune to normal fire
- Countermeasure: Sabotage may remove one reinforcement
- Decision: full fortification is intentionally legal; the game uses tactical removal rather than an artificial protection cap.

## Collapse

- State: accepted
- Rule ID: rules.collapse
- Decision: When a floor is destroyed, that floor and every floor above it are removed from the built tower. Removed tower pieces return to the owner's unbuilt reserve. Reinforcements on removed floors lose their protection and return to component supply.

## Victory

- State: provisional/PLAYTEST
- Rule ID: rules.victory
- Required Tower: 3 built floors
- Bell Construction Requirement: a player with all three floors built may spend 1 action to construct the bell
- Bell Construction Time: one full table orbit; the bell becomes ready only at the beginning of that player's next own turn if the three-floor tower still exists
- Bell Attempt Cost: 1 action
- Bell Attempt Success: D6 result 1
- Bell Attempt Limit: maximum 1 bell attempt per player turn for the next-session baseline
- Decision: completing the tower unlocks bell construction, not immediate victory. The constructed bell must survive one orbit with the complete tower before a ring attempt is legal.

## Cards

- State: provisional/PLAYTEST
- Rule ID: cards.deck
- Total Cards: 34

| Family | Quantity | Type |
|---|---:|---|
| Sabotage | 6 | tactic |
| Offensive Reroll | 8 | tactic |
| Defensive Reroll | 4 | tactic |
| Upper Hand | 2 | tactic |
| Plunder | 4 | tactic |
| Overtime | 4 | tactic |
| Global Events | 6 | event |

- Decision: remove all six Dud cards and test the remaining 34-card composition before adding replacements.

- State: accepted prototype baseline
- Rule ID: cards.events
- Type: event
- Quantity: 6
- Global Rule: Events affect all players rather than targeting a chosen opponent. Immediate resolution is preferred. A persistent Event remains face-up and expires when the player who drew it begins their next turn.

| Event | Quantity | Effect | Timing |
|---|---:|---|---|
| Ammunition Shortage | 1 | Every player loses 1 Ready Ammo if possible. | Resolve immediately. |
| Production Boom | 1 | Every player who currently has any ammo in Production gains +1 Ready Ammo immediately; Production contents remain unchanged. | Resolve immediately. |
| Panic Production | 1 | Every player immediately chooses: gain 2 Ready Ammo OR gain 1 action. | Resolve immediately. |
| Damp Powder | 1 | No player may use Emergency Ammo until the drawer begins their next turn; Planned Ammo works normally. | Leave face-up until expiry. |
| Ceasefire | 1 | No attacks until the drawer begins their next turn. | Leave face-up until expiry. |
| Building Strike | 1 | All builds cost +1 action until the drawer begins their next turn. | Leave face-up until expiry. |

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

## Edition

- State: accepted
- Edition ID: edition.dieselpunk
- Product Name: Tower Havoc — Dieselpunk Edition
- Preferred Cues: riveted steel and plate; field artillery; rough concrete; pipes; fuel; pressure vessels; mechanical assemblies; ammunition boxes; field workshops; practical engineering; robust silhouettes
- Avoid As Primary Language: unrelated historical-era mashups; cyberpunk neon/hacking/megacorp cues; real national flags; direct historical-army reproduction; cosmetic details that alter stackability or stability
- Decision: The first edition presents one coherent dieselpunk industrial world.

## Factions

- State: provisional/PLAYTEST
- Mode ID: mode.faction
- Final Faction Names: unresolved

| Archetype | Visual Direction | Prototype Ability |
|---|---|---|
| Fortifiers | heavy plate / bunker engineering | once per game, place one reinforcement without spending an action |
| Arsenal | ammunition / logistics | start with 4 Ready Ammo instead of 2 |
| Engineers | construction rigs / field workshops | first floor built in the match costs 1 less action |
| Scouts | optics / signal gear | start with 1 tactic card |
| Saboteurs | infiltration / tools | one single-use Sabotage effect |
| Veterans | disciplined gun crew | one single-use reroll of an own roll |

- Decision: Faction mode may use these six small prototype abilities after Classic testing, while final names remain open.

## First-session baseline

- State: provisional/PLAYTEST
- Session Baseline ID: playtest.baseline.003
- Recommended Players: 3–4
- Mode: Classic mechanics with visually distinct faction boards
- Deck: 34-card Dud-free prototype deck
- Floor Build Cost: 2 actions per floor
- Attack Cost: 1 action plus 1 Ready Ammo
- Attack Limit: maximum 1 attack per player turn
- Draw Attempt: 1 action; D6 1 or 6 draws one card; failure may be retried for another action; first success ends card drawing for that turn
- Turn Start: gain 1 action first, then resolve event expiry and Production maturity
- Bell Sequence: build bell for 1 action after completing the tower; survive one full orbit; then spend 1 action for a bell attempt
- Bell Success: D6 result 1
- Bell Attempt Limit: maximum 1 per player turn
- Player Surface: one of six approved faction boards; Ready Ammo, Production, and Available Actions use shared coin stack wells; three permanent floor rows; integrated quick reference; no separate quick-reference card
- Decision: use this baseline for the next real session after the individual card-face art is materialized.
