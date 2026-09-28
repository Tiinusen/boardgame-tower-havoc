# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 10:40:00
  - Trace: [Match Provenance Runtime](001-match-provenance-runtime.topic.trace.md)
  - Origin:
    - [relative](001-match-provenance-runtime.topic.trace.md)
- Current
  - Current Schema: tiinex.decision.v1
  - Created At: 2026-09-18 11:35:00
  - Authors: ChatGPT
  - Why: The simulation corpus exposes deterministic state changes that are not authored by a player.
  - Summary: R&D decision to model automatic game-rule transitions separately from player intent.

---

# Automatic Rule Resolution Is Separate From Player Intent

Automatic game effects should have their own resolution artifact instead of fabricating a player command.

## Decision

- State: accepted-for-R&D
- Subject: automatic Tower Havoc gameplay transitions
- Decision: use `towerhavoc.rule.resolution.v1` when a deterministic rule changes or confirms match state without a player-authored Action Intent

## Basis

- Turn-start action gain, planned-ammo maturation, event expiry, and similar effects occur because the rules trigger them.
- Treating those effects as Action Intents would misstate who requested the transition.
- A Runtime-shaped resolution remains host-neutral: the same transition may be carried out by a human procedure, Discord bot, GitHub Action, or later engine.

## Consequences

- Player actions remain `action.intent -> [randomness] -> action.resolution -> state`.
- Automatic effects become `turn/setup trigger -> rule.resolution -> state`.
- The simulation corpus can distinguish command-driven and rule-driven transitions explicitly.

## Review Conditions

- Revisit if a generic Tiinex transition/execution artifact later owns this role more precisely than Runtime.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Match Provenance Runtime](001-match-provenance-runtime.topic.trace.md)
  - Value: YGNSdvw4OzdD1k3VWRmMhp0S5U4zHoX4LuaqKDsxe9s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: lNjuEU9BNhMEbn1MoQ05JW3SLIcB4YnhJkCRWg4K3bc
