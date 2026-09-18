# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Current
  - Current Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Authors: Olle Tiinus
  - Why: Make the game itself reconstructable from explicit semantic artifacts rather than generated docs or remembered conversation.
  - Summary: Canonical Tower Havoc game project and lineage authority.

---
# Tower Havoc

## Project Identity

- Description: Tower Havoc is a 2–6 player competitive board game project built around bankable actions, ammunition, three-level towers, visible fortification, artillery attacks, tactical cards, global events, and a delayed bell victory condition.
- Boundary: This Project owns the current game-design and prototype continuity for Tower Havoc. Edition art, final manufacturing, commercial publication, legal clearance, and later publisher agreements are outside the current pre-playtest boundary unless separately represented.

## Project Purpose And Scope

- Description: Develop one mechanically coherent board game that can be tested quickly in Tabletop Simulator, then validated physically, while keeping the game definition reconstructable from Tiinex artifacts rather than from chat history or generated prose.
- Boundary: `.topics/tower-havoc/**` is the semantic source of truth for game rules and design state. Repository documents, data manifests, CAD briefs, and TTS helper material are projections or implementation artifacts unless they explicitly declare otherwise.

## Parties And Resources

- Relevant Parties: Olle Tiinus is the current game designer and rules author. Future collaborators are credited for concrete contributions when those contributions exist and are accepted.
- Relevant Resources: the Tower Havoc rule lineage, original Sänka Torn draft, generated rulebook/data projections, Tabletop Simulator prototype assets, future Fusion 360 work, and future playtest evidence.

## Coordination State

- Description: pre-playtest MVP. Core mechanics, card manifest, component model, first edition direction, and first-session baseline are represented. Several balance values remain explicitly provisional.
- Boundary: No playtest Evidence is claimed yet. Provisional values remain PLAYTEST until observed sessions support later Decisions.

## Milestones And Outcomes

- Description: first digital playtest; evidence-backed balance revision; ugly physical prototype; shared mechanical CAD master; later presentation/production refinement if the game proves worth continuing.
- Boundary: A generated document or successful validator run is not itself evidence that the game is balanced, fun, commercially viable, or production-ready.

## Interpretation Limits

- Does Not Prove: commercial readiness, patent freedom, trademark clearance, market demand, publisher interest, final balance, or manufacturing fitness.
- Must Not Be Treated As: a commercial release, a publisher contract, a final legal/IP clearance, or evidence that untested mechanics are balanced.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ
