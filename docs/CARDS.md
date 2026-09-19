> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Tower Havoc — Cards

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

## Sabotage

- State: accepted prototype baseline
- Card Family ID: cards.sabotage
- Name: Sabotage
- Type: tactic
- Quantity: 6
- Effect: Remove one reinforcement from any opponent floor.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Offensive Reroll

- State: accepted prototype baseline
- Card Family ID: cards.offensive-reroll
- Name: Offensive Reroll
- Type: tactic
- Quantity: 8
- Timing: Reaction
- Effect: When another player rolls the value printed on this card for an attack, force that attack die to be rerolled.

| Printed Value | Quantity |
|---:|---:|
| 2 | 2 |
| 3 | 2 |
| 4 | 2 |
| 5 | 2 |

## Defensive Reroll

- State: accepted prototype baseline
- Card Family ID: cards.defensive-reroll
- Name: Defensive Reroll
- Type: tactic
- Quantity: 4
- Effect: Reroll one relevant roll made by the card owner. Exact eligible roll types remain PLAYTEST.
- Timing: Reaction / PLAYTEST.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Upper Hand

- State: accepted prototype baseline
- Card Family ID: cards.upper-hand
- Name: Upper Hand
- Type: tactic
- Quantity: 2
- Effect: Take two random cards from one chosen opponent hand.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Plunder

- State: accepted prototype baseline
- Card Family ID: cards.plunder
- Name: Plunder
- Type: tactic
- Quantity: 4
- Effect: Choose an opponent and roll D6: 1–2 steal 1 Ready Ammo; 3–4 steal 2; 5–6 steal 3; never steal more than the target has.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Overtime

- State: accepted prototype baseline
- Card Family ID: cards.overtime
- Name: Overtime
- Type: tactic
- Quantity: 4
- Effect: Gain 1 action.
- Timing: Play on your turn.
- Decision: Use this family and quantity in the v0.1 prototype deck.

## Global Events

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

## Deck recycle

- State: provisional/PLAYTEST
- Rule ID: cards.recycle
- Decision: when the draw pile is exhausted, shuffle the discard pile to create a new draw pile. No hand purge occurs as part of deck exhaustion.
