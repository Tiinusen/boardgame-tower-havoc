# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:53:00
  - Trace: [001-9-global-events.decision.trace.md](001-9-global-events.decision.trace.md)
  - Origin:
    - [relative](001-9-global-events.decision.trace.md)
- Current
  - Current Schema: tiinex.decision.v1
  - Created At: 2026-09-28 16:04:09
  - Authors: Steward
  - Why: Accept the participant-proposed one-copy Atombomb concept as a bounded global reset Event.
  - Summary: PLAYTEST Event-set successor adding exactly one Atombomb that destroys all tower floors and reinforcements.
  - Status: ready/local

---

# Global Event Set With Atombomb

## Decision

- State: provisional/PLAYTEST
- Rule ID: cards.events
- Type: event
- Quantity: 7
- Global Rule: Events affect all players rather than targeting a chosen opponent. Immediate resolution is preferred. A persistent Event remains face-up and expires when the player who drew it begins their next turn.

| Event | Quantity | Effect | Timing |
|---|---:|---|---|
| Ammunition Shortage | 1 | Every player loses 1 Ready Ammo if possible. | Resolve immediately. |
| Production Boom | 1 | Every player who currently has any ammo in Production gains +1 Ready Ammo immediately; Production contents remain unchanged. | Resolve immediately. |
| Panic Production | 1 | Every player immediately chooses: gain 2 Ready Ammo OR gain 1 action. | Resolve immediately. |
| Damp Powder | 1 | No player may use Emergency Ammo until the drawer begins their next turn; Planned Ammo works normally. | Leave face-up until expiry. |
| Ceasefire | 1 | No attacks until the drawer begins their next turn. | Leave face-up until expiry. |
| Building Strike | 1 | All builds cost +1 action until the drawer begins their next turn. | Leave face-up until expiry. |
| Atombomb | 1 | Destroy all tower floors and all reinforcements belonging to every player. | Resolve immediately. |

- Decision: add exactly one Atombomb Event to the current next-playtest Event family.

## Basis

A project participant proposed one `Atombomb` card that wipes all towers and reinforcements. The Steward accepted that bounded concept for the next playable revision.

## Bell Boundary

This Decision does not add a direct Bell effect. Existing Bell eligibility and survival rules continue to govern Bell state and legal victory attempts after tower destruction. Any future rule that explicitly destroys or preserves a Bell marker as an additional Atombomb effect requires a separate Steward Decision.

## Consequences

The Event family increases from six to seven cards. Deck composition, manifests, TTS material, card-art production planning, and any generated component projections must consume this successor rather than the prior six-Event baseline.

## Provenance Limit

The participant proposal is known through the Steward conversation report. This artifact does not identify the participant, infer a permanent Role, manufacture observed playtest Evidence, or assign rights beyond the reported proposal.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-global-events.decision.trace.md](001-9-global-events.decision.trace.md)
  - Value: PHo5b4nMUcQzd_vLHhzPh6YprK_4kqxadU0lVpwSvDY

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo