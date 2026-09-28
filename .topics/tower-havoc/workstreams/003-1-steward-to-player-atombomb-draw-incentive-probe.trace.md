# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-28 16:15:58
  - Trace: [003-atombomb-draw-incentive-player-probe.trace.md](003-atombomb-draw-incentive-player-probe.trace.md)
  - Origin:
    - [relative](003-atombomb-draw-incentive-player-probe.trace.md)
- Current
  - Current Schema: [tiinex.handoff.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/handoff/tiinex.handoff.v1.schema.md)
  - Created At: 2026-09-28 16:18:09
  - Authors: Steward
  - Why: Probe participant-side incentives independently from Keeper adjudication and Steward acceptance.
  - Summary: Transfer bounded synthetic Player strategy/intents for Atombomb draw incentives.
  - Status: ready/local

---

# Steward To Player — Atombomb Draw-Incentive Probe

## Handoff Parties

- Purpose: transfer a bounded synthetic Player-agency probe for card-draw decisions after adding one immediate Atombomb Event.
- From: Steward
- From Kind: role
- From Reference: [Steward Role](../roles/001-1-steward.role.trace.md)
- To: Player
- To Kind: role
- To Reference: [Player Role](../roles/001-4-player.role.trace.md)

## Transfers

- player-strategy-probe
  - Transfer Kind: work-and-responsibility
  - Description: choose Player Action Intents/strategic sequences for the fixed public-state scenarios in the controlling Task, without adjudicating results or changing rules.
  - Controlling Artifact: [Atombomb Draw-Incentive Player Probe](003-atombomb-draw-incentive-player-probe.trace.md)
  - Boundary: one synthetic seat per scenario; Player chooses intents only and must not self-resolve randomness, Events, legality disputes, or victory.

## Required Context

- controlling-task
  - Material: Atombomb Draw-Incentive Player Probe Task.
  - Material Reference: [Controlling Task](003-atombomb-draw-incentive-player-probe.trace.md)
  - Purpose: exact scenarios, participant authority, seat boundary, and expected output.
  - Availability: available

- draw-rule
  - Material: current post-playtest action and draw economy.
  - Material Reference: [Draw And Action Costs](../rules/001-2-1-draw-and-action-costs.decision.trace.md)
  - Purpose: legal cost/success/retry boundary for draw-attempt intents.
  - Availability: available

- atombomb-event
  - Material: accepted Atombomb Event Decision.
  - Material Reference: [Atombomb Event Decision](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Purpose: known one-copy immediate reset risk/reward in the strategy probe.
  - Availability: available

## Reference Context

- player-role
  - Material: Tower Havoc Player Role.
  - Material Reference: [Player Role](../roles/001-4-player.role.trace.md)
  - Purpose: seat agency and self-adjudication boundary.
  - Availability: available

## Retained Responsibilities

- adjudication
  - Retained By: Keeper
  - Responsibility: legality/result adjudication remains outside this Player probe.
  - Boundary: Player may express intended sequences but may not convert them into resolved state.

- design-acceptance
  - Retained By: Steward
  - Retained By Reference: [Steward Role](../roles/001-1-steward.role.trace.md)
  - Responsibility: decide whether any observed incentive is desirable or warrants design change.

## Exclusions And Dependencies

- no-self-adjudication
  - Kind: excluded-scope
  - Description: do not resolve dice, card order/draw outcome, Event effects, attacks, Bell attempts, or match results.
  - Responsible Party Or Role: Player

- no-design-verdict
  - Kind: excluded-scope
  - Description: do not rate Atombomb or card draw as good/bad/balanced; return strategy choices and reasons only.
  - Responsible Party Or Role: Player

## Completion Expectation

- Signal Kind: return
- Signal Meaning: one qualified Player-to-Steward Handoff Package carrying SYNTHETIC Action Intent/strategy material for the declared scenarios and no self-adjudicated game-state changes.
- Return To: Steward
- Return To Reference: [Steward Role](../roles/001-1-steward.role.trace.md)

## Interpretation Limits

- Does Not Mean: a real person played a session, Player choices are optimal, or synthetic intent is empirical playtest Evidence.
- Must Not Be Used To Claim: Keeper adjudication, design acceptance, hidden deck knowledge, resolved randomness, or balance conclusions.
- Authority Limits: Player owns strategy/intent for its synthetic seat only.
- Transport Limits: the Handoff does not bind Player to any real-world identity or grant access to unavailable hidden state.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [003-atombomb-draw-incentive-player-probe.trace.md](003-atombomb-draw-incentive-player-probe.trace.md)
  - Value: gecTeS1rJJiKmsaFaip-83oOzczV57Ob5KXhP7CTi_Q

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: jUO0LiYoO7xYL0VY8gKlXhFyd_KyBmPdk1_ziloMYpQ