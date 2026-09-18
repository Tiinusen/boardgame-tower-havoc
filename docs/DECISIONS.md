> **GENERATED PROJECTION — DO NOT EDIT AS CANONICAL SOURCE.**
> Source authority: `.topics/tower-havoc/**`. Regenerate with `python scripts/generate_from_topics.py`.

# Tower Havoc — Decision Index

| Source | Decision | State | Operative summary |
|---|---|---|---|
| `.topics/tower-havoc/001-1-lineage-is-canonical-game-source.decision.trace.md` | Continuity Context | accepted | `.topics/tower-havoc/**` is the canonical semantic source for the current game definition and its development continuity. `docs/**`, `data/**`, CAD briefs, TTS helper files, and similar consumable material should be generated or reconciled from that source wherever practical. Raw preserved source material may remain outside `.topics` when a Preservation artifact declares its boundary. |
| `.topics/tower-havoc/001-2-tower-havoc-title.decision.trace.md` | Continuity Context | accepted working/product title | Use Tower Havoc consistently in repository, prototype, and generated documentation. |
| `.topics/tower-havoc/cards/001-1-deck-composition.decision.trace.md` | Continuity Context | accepted prototype baseline | - State: accepted prototype baseline
- Rule ID: cards.deck
- Total Cards: 40

/ Family / Quantity / Type /
/---/---:/---/
/ Sabotage / 6 / tactic /
/ Offensive Reroll / 8 / tactic /
/ Defensive Reroll / 4 / tactic /
/ Dud / 6 / tactic /
/ Upper Hand / 2 / tactic /
/ Plunder / 4 / tactic /
/ Overtime / 4 / tactic /
/ Global Events / 6 / event / |
| `.topics/tower-havoc/cards/001-10-deck-recycle.decision.trace.md` | Continuity Context | accepted prototype baseline | When the draw pile is exhausted, every player discards Dud cards from hand. Combine those Duds with the discard pile, shuffle, and create a new draw pile. |
| `.topics/tower-havoc/cards/001-2-sabotage.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-3-offensive-reroll.decision.trace.md` | Continuity Context | accepted prototype baseline | - State: accepted prototype baseline
- Card Family ID: cards.offensive-reroll
- Name: Offensive Reroll
- Type: tactic
- Quantity: 8
- Timing: Reaction
- Effect: When another player rolls the value printed on this card for an attack, force that attack die to be rerolled.

/ Printed Value / Quantity /
/---:/---:/
/ 2 / 2 /
/ 3 / 2 /
/ 4 / 2 /
/ 5 / 2 / |
| `.topics/tower-havoc/cards/001-4-defensive-reroll.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-5-dud.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-6-upper-hand.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-7-plunder.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-8-overtime.decision.trace.md` | Continuity Context | accepted prototype baseline | Use this family and quantity in the v0.1 prototype deck. |
| `.topics/tower-havoc/cards/001-9-global-events.decision.trace.md` | Continuity Context | accepted prototype baseline | - State: accepted prototype baseline
- Rule ID: cards.events
- Type: event
- Quantity: 6
- Global Rule: Events affect all players rather than targeting a chosen opponent. Immediate resolution is preferred. A persistent Event remains face-up and expires when the player who drew it begins their next turn.

/ Event / Quantity / Effect / Timing /
/---/---:/---/---/
/ Ammunition Shortage / 1 / Every player loses 1 Ready Ammo if possible. / Resolve immediately. /
/ Production Boom / 1 / Every player who currently has any ammo in Production gains +1 Ready Ammo immediately; Production contents remain unchanged. / Resolve immediately. /
/ Panic Production / 1 / Every player immediately chooses: gain 2 Ready Ammo OR gain 1 action. / Resolve immediately. /
/ Damp Powder / 1 / No player may use Emergency Ammo until the drawer begins their next turn; Planned Ammo works normally. / Leave face-up until expiry. /
/ Ceasefire / 1 / No attacks until the drawer begins their next turn. / Leave face-up until expiry. /
/ Building Strike / 1 / All builds cost +1 action until the drawer begins their next turn. / Leave face-up until expiry. / |
| `.topics/tower-havoc/components/001-1-component-inventory.decision.trace.md` | Continuity Context | accepted MVP inventory | - State: accepted MVP inventory
- Component Manifest ID: components.mvp

/ Component / Quantity / Prototype Substitute / Constraint /
/---/---:/---/---/
/ Player mat / 6 / paper/player colour zone / visibly separate Action Bank, Ready Ammo, Production /
/ Reference card / 6 / paper note / one quick reference per player /
/ Optional faction card / 6 / paper note / used only in Faction mode /
/ Tower floor / 18 / generic block / 3 per player; identical mechanical envelope /
/ Light field cannon / 6 / pawn/token / theme/readability only; no real projectile required /
/ D6 / 2 / standard die / one required plus one spare /
/ Bell / 1 / obvious goal token / physical bell preferred later /
/ Ammo token / 72 / cube/coin / shared supply /
/ Reinforcement marker / 72 / numbered token / values 2–5 x 3 floors x 6 players /
/ Action tracker / 6 sets / counter/dial / must support banked actions without a small fixed cap /
/ Card / 40 / generated prototype deck / deck manifest comes from card lineage / |
| `.topics/tower-havoc/components/001-2-visible-player-state.decision.trace.md` | Continuity Context | accepted | persistent state that matters later should be physically/digitally represented rather than remembered where practical. |
| `.topics/tower-havoc/components/001-3-mechanical-equivalence.decision.trace.md` | Continuity Context | accepted | Every faction tower-floor variant must preserve the same outer bounding box, footprint, floor-to-floor contact area, stacking height, alignment behavior, practical stability envelope, reinforcement interface locations, and accessibility. Cosmetic variation must not create a gameplay advantage. |
| `.topics/tower-havoc/digital/001-1-first-tts-baseline.decision.trace.md` | Continuity Context | accepted prototype baseline | the first TTS build optimizes for time-to-playtest rather than presentation quality. |
| `.topics/tower-havoc/edition/001-1-edition-independence.decision.trace.md` | Continuity Context | accepted | Tower Havoc mechanics are edition-independent. A new visual edition may change theme, architecture, weapon appearance, faction names, art style, and props while preserving the base rules and mechanical component interfaces. |
| `.topics/tower-havoc/edition/001-2-dieselpunk-visual-direction.decision.trace.md` | Continuity Context | accepted | The first edition presents one coherent dieselpunk industrial world. |
| `.topics/tower-havoc/edition/001-3-light-field-cannon.decision.trace.md` | Continuity Context | accepted | Dieselpunk Edition represents attacks with a light field cannon. The cannon is a thematic/readability component and does not physically fire a projectile; the D6 resolves the shot. |
| `.topics/tower-havoc/factions/001-1-classic-mode.decision.trace.md` | Continuity Context | accepted | In Classic mode every player set is mechanically identical. Use Classic mode for the first playtests and as the reference when judging whether the core game itself works. |
| `.topics/tower-havoc/factions/001-2-faction-mode.decision.trace.md` | Continuity Context | provisional/PLAYTEST | Faction mode may use these six small prototype abilities after Classic testing, while final names remain open. |
| `.topics/tower-havoc/physical/001-1-fusion360-master-geometry.decision.trace.md` | Continuity Context | accepted | Begin physical modeling from one parametric mechanically neutral tower-floor master. Preserve shared bounding box, footprint, stacking/contact area, height, alignment, stability envelope, reinforcement interfaces, and access. Create cosmetic faction variants only after the master survives physical stacking tests. |
| `.topics/tower-havoc/playtest/001-1-first-session-baseline.decision.trace.md` | Continuity Context | provisional/PLAYTEST | Use this complete baseline for the first session so later variants have a comparable starting point. |
| `.topics/tower-havoc/rules/001-1-setup.decision.trace.md` | Continuity Context | accepted | Each player takes one player set with three tower floors and the resources required by the selected game mode. Classic mode is the reference setup. |
| `.topics/tower-havoc/rules/001-2-action-economy.decision.trace.md` | Continuity Context | accepted | Unused actions remain banked across turns. Actions are the flexible capital of the game rather than a turn-local allowance. |
| `.topics/tower-havoc/rules/001-3-ammunition.decision.trace.md` | Continuity Context | accepted | Ready Ammo and Production Ammo are separate visible states. Ammunition is prepaid offensive capacity, not a second copy of the action currency. |
| `.topics/tower-havoc/rules/001-4-turn-structure.decision.trace.md` | Continuity Context | accepted | Start-of-turn processing is deliberately short and physically observable. |
| `.topics/tower-havoc/rules/001-5-building.decision.trace.md` | Continuity Context | provisional/PLAYTEST | A player may build multiple floors in one turn if enough banked actions are available; successive builds currently use the 2/3/4 cost curve. |
| `.topics/tower-havoc/rules/001-6-attack.decision.trace.md` | Continuity Context | accepted with frequency PLAYTEST | attacks consume ammunition and resolve against one chosen built floor. The first session uses a one-attack cap only as a conservative comparison baseline. |
| `.topics/tower-havoc/rules/001-7-reinforcement.decision.trace.md` | Continuity Context | accepted | full fortification is intentionally legal; the game uses tactical removal rather than an artificial protection cap. |
| `.topics/tower-havoc/rules/001-8-collapse.decision.trace.md` | Continuity Context | accepted | When a floor is destroyed, that floor and every floor above it are removed from the built tower. Removed tower pieces return to the owner's unbuilt reserve. Reinforcements on removed floors lose their protection and return to component supply. |
| `.topics/tower-havoc/rules/001-9-victory.decision.trace.md` | Continuity Context | accepted structure; probability PLAYTEST | A player cannot build the third floor and attempt victory in the same turn. The tower must survive a full table orbit before the first legal bell attempt. |
| `.topics/tower-havoc/runtime/001-2-event-sourced-match-authority.decision.trace.md` | Continuity Context | accepted-for-R&D | bind each match to a frozen `towerhavoc.ruleset.v1`; preserve player commands as `towerhavoc.action.intent.v1`; generate separate randomness request/result artifacts when needed; preserve authoritative adjudication as `towerhavoc.action.resolution.v1`; generate `towerhavoc.state.v1` checkpoints as replayable projections; close with `towerhavoc.match.result.v1`. Hidden deck/hand state uses commitment/reveal artifacts rather than public plaintext during play. |
