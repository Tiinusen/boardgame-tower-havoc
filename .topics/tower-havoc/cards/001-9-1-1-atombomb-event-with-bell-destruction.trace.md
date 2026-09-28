# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: tiinex.decision.v1
  - Created At: 2026-09-28 16:04:09
  - Trace: [001-9-1-atombomb-global-events.decision.trace.md](001-9-1-atombomb-global-events.decision.trace.md)
  - Origin:
    - [relative](001-9-1-atombomb-global-events.decision.trace.md)
- Current
  - Current Schema: tiinex.decision.v1
  - Created At: 2026-09-28 18:07:30
  - Authors: Steward
  - Why: Keeper exposed an under-specified Bell lifecycle after total structural destruction, and Steward has now explicitly decided that Atombomb destroys the Bell too.
  - Summary: Make Bell destruction explicit in the one-copy Atombomb Event and preserve atomic global resolution.
  - Status: ready/local

---

# Atombomb Event With Bell Destruction

## Decision

- State: provisional/PLAYTEST
- Rule ID: cards.events.atombomb
- Type: Event
- Quantity: 1
- Timing: Resolve immediately.
- Production-facing rule text: `Destroy all tower floors, all reinforcements, and all built Bells.`
- Decision: supersede the prior Atombomb Bell boundary by making Bell destruction explicit. Atombomb destroys every player's built tower floors, reinforcements, and Bell construction/marker as one immediate global resolution.

## Bell Consequence

When Atombomb resolves:

- any built Bell is destroyed together with the tower;
- any Bell maturity/readiness or previously satisfied Bell survival state is lost;
- rebuilding three floors does not restore the old Bell;
- the player must construct a new Bell and satisfy the ordinary Bell readiness/survival sequence before another Bell attempt can become legal.

## Other State

Atombomb does not itself alter hands, Ready Ammo, Production, Available Actions, or unrelated persistent Events unless another qualified rule separately says so.

## Global Resolution Boundary

The Event is one global immediate resolution. Implementations may iterate players internally, but they must not expose intermediate per-player destruction as action/reaction windows or allow seat order to change the final result.

## Deck Consequence

The intended next Dud-free deck contains 35 cards: the carried 34-card Dud-free composition plus exactly one Atombomb Event. Deck-derived projections must not move to 35 until that deck successor is itself qualified.

## Evidence Boundary

The Bell consequence is a Steward design disposition prompted by the bounded Keeper synthetic audit and the explicit human clarification that the Bell is destroyed too. The synthetic audit remains synthetic and is not playtest Evidence or balance proof.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-atombomb-global-events.decision.trace.md](001-9-1-atombomb-global-events.decision.trace.md)
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: _jZsDCcoNgpgX6b1aaJSMzj9iw1XGY8YePQoZ8zypjk