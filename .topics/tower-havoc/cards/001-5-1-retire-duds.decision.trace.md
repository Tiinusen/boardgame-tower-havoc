# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 01:49:00
  - Trace: [Dud card family](001-5-dud.decision.trace.md)
  - Origin:
    - [relative](001-5-dud.decision.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:07
  - Authors: Olle Tiinus; ChatGPT
  - Why: Preserve the original Dud experiment while explicitly removing it from the next playable baseline.
  - Summary: Dud quantity becomes zero for the next PLAYTEST deck.

---

# Retire Dud cards from next baseline

## Decision

- State: retired from next PLAYTEST baseline
- Card Family ID: cards.dud
- Name: Dud
- Type: tactic
- Quantity: 0
- Effect: none; no Dud instances are generated for the next baseline
- Timing: not-applicable
- Decision: remove Dud cards from the playable deck rather than replacing them immediately.

## Basis

The first TTS playtest found that Duds suppressed the incentive to spend actions interacting with the deck. Evidence: `../playtest/001-3-first-tts-playtest.evidence.trace.md`.

## Consequences

The original six Dud cards remain preserved in lineage as the v0.1 baseline but are absent from generated next-session card manifests.

## Review Conditions

Do not fill the six-card gap merely to preserve a round number; test the dud-free deck first.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Dud card family](001-5-dud.decision.trace.md)
  - Value: kSH6U6CaZd0JEGt4LnWHkXfqRw9SmK-ZAaUYydpcLFQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:JraSMinXOijcsSyJWcl0zeTRNOu3C6bfFX4xa5Z1YmY
