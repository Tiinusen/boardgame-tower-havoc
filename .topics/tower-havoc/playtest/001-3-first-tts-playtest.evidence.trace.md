# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-18 02:11:00
  - Trace: [Run and instrument Tower Havoc playtests](001-playtest-program.task.trace.md)
  - Origin:
    - [relative](001-playtest-program.task.trace.md)
- Current
  - Current Schema: [tiinex.evidence.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/evidence/tiinex.evidence.v1.schema.md)
  - Created At: 2026-09-19 12:50:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Preserve the first real TTS playtest observations before landing successor PLAYTEST decisions.
  - Summary: Evidence slice for the first real Tower Havoc TTS playtest.

---

# First TTS Playtest Observation Evidence

## Supported Claim Or Question

- Supported Claim Or Question: what the first real Tower Havoc TTS playtest exposed about asset delivery, player-board ergonomics, quick-reference correctness, card-draw incentive, and turn-flow clarity
- Evidence Role: supports the next PLAYTEST revisions without claiming final balance or physical-game conclusions
- Review Context: first real Tower Havoc playtest conducted in Tabletop Simulator

## Provenance

- Known Source: designer report supplied immediately after the completed TTS playtest
- Preservation Basis: substantive observations are embedded as a bounded summary in this Evidence artifact
- Provenance Limits: no raw TTS save, exact session timestamp, player count, duration, per-turn log, or verbatim participant transcript was supplied with this evidence slice

## Evidence Material

- Material Kind: preserved playtest observation summary
- Material:
  - GitHub repository permalink-style asset URLs were not usable directly by Tabletop Simulator, motivating a GitHub Pages publication surface for stable HTTP asset delivery.
  - The existing player mat was impractical; separate broad zones and handling several distinct token types created unnecessary manipulation.
  - A double-sided coin/token with Action on one face and Ammo on the other was proposed so Action Bank, Ready Ammo, Production, construction, and reinforcement can share one physical vocabulary while board zones carry meaning.
  - The revised board should use coin-sized stack wells for Action, Ready Ammo, and Production, plus a slot for the faction/mode quick-reference card. Dedicated player-card and active-card areas were judged unnecessary.
  - Tower construction should be represented by two Action-token slots per floor, with four adjacent reinforcement positions for values 2, 3, 4, and 5.
  - Bell construction should cost 1 action and take one full table orbit before it is ready to be rung.
  - The quick reference omitted card draw as an action and incorrectly showed attacks as costing 0 actions; the playtest correction is 1 action plus 1 Ready Ammo per attack.
  - Dud cards reduced the incentive to engage with the deck and should be removed from the next baseline.
  - Every own turn needs to state clearly that the first thing the player receives is 1 action regardless of later start-of-turn processing.
  - Card draw felt too passive and low-incentive. The proposed next baseline spends 1 action per draw attempt, succeeds only on D6 1 or 6, allows another paid attempt after failure, and stops further draw attempts that turn after the first success.
  - The table presentation felt visually sparse enough that richer generated graphics are useful for the next TTS iteration, without treating graphics as gameplay evidence.

## Preservation And Fidelity

- Preservation State: summarized playtest report preserved in markdown
- Fidelity Notes: preserves the substantive observations and requested rule/component changes supplied by the designer; wording is normalized for project artifacts
- Known Losses: exact participant wording, table-state screenshots, quantitative event counts, and tactile physical-game evidence are not preserved here

## Interpretation Limits

- Does Not Prove: final balance, final component dimensions, long-term card value, physical ergonomics, statistical strategy strength, or that every participant shared the same preference
- Must Not Be Treated As: final rule validation, universal TTS limitation proof, publisher acceptance, physical prototype evidence, or permission to infer unreported session details

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Run and instrument Tower Havoc playtests](001-playtest-program.task.trace.md)
  - Value: D34kCPLAaVs1DZB5tFHPq7jDTei_oPGIZA1RZrqsdG8

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:ZQ1yWXrcm61NaoHl9td3r22HaWFLOflqnKq1obItlAs
