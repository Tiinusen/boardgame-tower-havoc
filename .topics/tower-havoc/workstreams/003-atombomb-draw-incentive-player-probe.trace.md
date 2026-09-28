# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: tiinex.decision.v1
  - Created At: 2026-09-28 16:04:09
  - Trace: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Origin:
    - [relative](../cards/001-9-1-atombomb-global-events.decision.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-28 16:15:58
  - Authors: Steward
  - Why: Observe participant-side strategic incentives independently from Keeper adjudication and Steward design acceptance.
  - Summary: Synthetic Player agency probe for draw incentives after adding one immediate Atombomb Event.
  - Status: ready/local

---

# Atombomb Draw-Incentive Player Probe

## Objective

Player is an explicitly required participant in this current work because the new one-copy Atombomb changes the strategic risk/reward of spending actions on card-draw attempts and should be probed from participant agency without self-adjudication.

Act as one synthetic Tower Havoc seat under the current rules and return player-chosen Action Intents for a small fixed set of public-state scenarios. The purpose is to expose strategic incentives and surprises, not to decide whether the design is good or balanced.

## Done Criteria

- use the current action/draw rule: a draw attempt costs 1 action, succeeds on D6 1 or 6, failed attempts may be retried by spending more actions, and a successful draw closes further draw attempts that turn;
- assume the current deck concept is the 34-card Dud-free deck plus exactly one immediate Atombomb Event, with unknown shuffled order unless a scenario states otherwise;
- produce player intent/strategy responses for at least six public-state scenarios spanning: being far behind in tower progress; being clearly ahead; a close race; low Ready Ammo; a large bank of Available Actions; and Bell-related pressure;
- for each scenario, choose a legal intended action sequence or pass/draw choice and give a short player-strategy reason;
- do not self-resolve dice, draws, legality disputes, Event outcomes, attacks, Bell attempts, or match victory; those belong to Keeper/runtime resolution;
- do not inspect hidden deck order or opponent hidden hands;
- label all output as a SYNTHETIC player strategy probe, not playtest Evidence and not a design verdict;
- return the synthetic Action Intent material and one qualified Player-to-Steward Handoff Package.

## Scope

Player agency/strategy only. No Keeper adjudication, canonical rule mutation, project acceptance, card artwork, remote publication, or statistical balance claim.

## Dependencies

- `../cards/001-9-1-atombomb-global-events.decision.trace.md`
- `../rules/001-2-1-draw-and-action-costs.decision.trace.md`
- `../roles/001-4-player.role.trace.md`
- `../runtime/001-match-provenance-runtime.topic.trace.md`

## Seat Boundary

Treat the holder as exactly one synthetic seat per scenario. Other players exist only through the public scenario state supplied by this Task; do not choose their actions.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: gecTeS1rJJiKmsaFaip-83oOzczV57Ob5KXhP7CTi_Q