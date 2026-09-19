# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:38:00
  - Trace: [Attack targeting and cost](001-6-attack.decision.trace.md)
  - Origin:
    - [relative](001-6-attack.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:04
  - Authors: Olle Tiinus; ChatGPT
  - Why: Land the intended attack cost as a successor rather than silently editing the first-session baseline.
  - Summary: PLAYTEST successor: attacks cost 1 action + 1 Ready Ammo.

---

# Attack costs action and ammunition

This artifact supersedes the first-session attack-cost baseline for the next PLAYTEST iteration.

## Decision

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

## Basis

The first TTS playtest exposed that the quick reference said 0 actions, while the intended played cost was 1 action plus 1 ammo. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

Quick reference, generated constants, simulation/runtime legality checks for new matches, and TTS helper text must use the two-resource cost. Historical frozen simulations retain the rulesets they explicitly bound.

## Review Conditions

Keep the one-attack cap provisional and revisit only after more playtest evidence.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Attack targeting and cost](001-6-attack.decision.trace.md)
  - Value: BwhmeXLyNLdZRv9Topm-QYDyca5lW4W7675bubMPu-s

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:f8bXfuIz-GpcZm7cHaPRBfVX9mdp5AP58HqHGAZ9W5A
