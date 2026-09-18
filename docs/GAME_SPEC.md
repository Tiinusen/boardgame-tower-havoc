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

- State: accepted
- Rule ID: rules.actions
- Actions Gained Per Own Turn: 1
- General Action Bank Cap: none
- Pass Cost: 0
- Draw Card Cost: 1 action
- Reinforce Cost: 1 action
- Bell Attempt Cost: 1 action
- Draw Phrase: `Ah, hmmm, mmmm`
- Decision: Unused actions remain banked across turns. Actions are the flexible capital of the game rather than a turn-local allowance.

## Ammunition

- State: accepted
- Rule ID: rules.ammunition
- Emergency Production: 1 action -> 1 Ready Ammo immediately
- Planned Production: 1 action -> 2 Production Ammo
- Planned Maturity: all Production Ammo becomes Ready Ammo at the beginning of that player's next own turn
- Attack Cost: 1 Ready Ammo
- Attack Action Cost: 0
- Decision: Ready Ammo and Production Ammo are separate visible states. Ammunition is prepaid offensive capacity, not a second copy of the action currency.

## Turn structure

- State: accepted
- Rule ID: rules.turn
- Start Step 1: expire any persistent global event owned by this player from the previous orbit
- Start Step 2: move all of this player's Production Ammo to Ready Ammo
- Start Step 3: gain 1 action
- Action Phase: spend any legal combination of available actions/resources in any legal order
- End: remaining actions stay banked; play passes clockwise
- Decision: Start-of-turn processing is deliberately short and physically observable.

## Building

- State: provisional/PLAYTEST
- Rule ID: rules.building
- Tower Floors Per Player: 3
- Build Cost — first floor built this turn: 2 actions
- Build Cost — second floor built this turn: 3 actions
- Build Cost — third floor built this turn: 4 actions
- Three-Floor Burst Total: 9 actions
- Decision: A player may build multiple floors in one turn if enough banked actions are available; successive builds currently use the 2/3/4 cost curve.

## Attack

- State: accepted with frequency PLAYTEST
- Rule ID: rules.attack
- Weapon Metaphor: light field cannon
- Target: one specific built floor of one opponent
- Cost: 1 Ready Ammo
- Additional Action Cost: 0
- First-Session Attack Limit: maximum 1 attack per player turn
- Long-Term Multi-Attack Rule: unresolved/PLAYTEST
- Decision: attacks consume ammunition and resolve against one chosen built floor. The first session uses a one-attack cap only as a conservative comparison baseline.

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

- State: accepted structure; probability PLAYTEST
- Rule ID: rules.victory
- Required Tower: 3 built floors
- Exposure Requirement: the complete three-floor tower must already exist at the beginning of the player's own turn
- Bell Attempt Cost: 1 action
- First-Session Success: D6 result 1
- First-Session Attempt Limit: maximum 1 bell attempt per player turn
- Decision: A player cannot build the third floor and attempt victory in the same turn. The tower must survive a full table orbit before the first legal bell attempt.

## Cards

- State: accepted prototype baseline
- Rule ID: cards.deck
- Total Cards: 40

| Family | Quantity | Type |
|---|---:|---|
| Sabotage | 6 | tactic |
| Offensive Reroll | 8 | tactic |
| Defensive Reroll | 4 | tactic |
| Dud | 6 | tactic |
| Upper Hand | 2 | tactic |
| Plunder | 4 | tactic |
| Overtime | 4 | tactic |
| Global Events | 6 | event |

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

- State: accepted MVP inventory
- Component Manifest ID: components.mvp

| Component | Quantity | Prototype Substitute | Constraint |
|---|---:|---|---|
| Player mat | 6 | paper/player colour zone | visibly separate Action Bank, Ready Ammo, Production |
| Reference card | 6 | paper note | one quick reference per player |
| Optional faction card | 6 | paper note | used only in Faction mode |
| Tower floor | 18 | generic block | 3 per player; identical mechanical envelope |
| Light field cannon | 6 | pawn/token | theme/readability only; no real projectile required |
| D6 | 2 | standard die | one required plus one spare |
| Bell | 1 | obvious goal token | physical bell preferred later |
| Ammo token | 72 | cube/coin | shared supply |
| Reinforcement marker | 72 | numbered token | values 2–5 x 3 floors x 6 players |
| Action tracker | 6 sets | counter/dial | must support banked actions without a small fixed cap |
| Card | 40 | generated prototype deck | deck manifest comes from card lineage |

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
- Session Baseline ID: playtest.baseline.001
- Recommended Players: 3–4
- Mode: Classic
- Deck: 40-card prototype deck
- Build Curve: 2 / 3 / 4
- Attack Limit: maximum 1 attack per player turn
- Bell Attempt Limit: maximum 1 per player turn
- Bell Success: D6 result 1
- Decision: Use this complete baseline for the first session so later variants have a comparable starting point.
