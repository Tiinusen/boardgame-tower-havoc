# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 15:06:00
  - Trace: [Produce Individual Card Fronts](../001-3-1-individual-card-front-production.task.trace.md)
  - Origin:
    - [relative](../001-3-1-individual-card-front-production.task.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 16:12:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Turn the proven manual generation approach into one qualified Pilot/Handoff tranche before producing the rest of the deck.
  - Summary: First Pilot-mediated card-generation tranche: six Tactic routes plus one Event production-reference probe.
  - Status: ready/local

---

# Pilot Card Generation Tranche 1

## Objective

Execute the first qualified Pilot-mediated Tower Havoc card-art tranche through independent human-operated external-generation routes, preserving exact references, exact user-visible prompts, returned bytes, deviations, and lineage-correct return packages.

## Done Criteria

- six remaining/retry Tactic routes have one returned source candidate or truthful blocked return: Defensive Reroll, Offensive Reroll — 4, Offensive Reroll — 5, Upper Hand, Plunder, Overtime;
- one Event production-reference probe for Ammunition Shortage has one returned source candidate or truthful blocked return;
- every route uses a fresh Pilot conversation and selects only its own qualified Handoff Pointer;
- every successful route preserves exact returned bytes before any transform;
- Pilot returns Evidence + Pilot-to-Cartographer Handoff package and does not continue into sibling cards;
- Cartographer reviews returned source before deterministic TTS normalization or stable promotion.

## Scope

- generation only for the seven declared routes in this tranche;
- one isolated card front per route;
- no montage/contact sheet/mockup/background;
- no card-rule invention or paraphrase;
- Tactic routes use `001-generated-offensive-reroll-2.png` as strict production-layout reference;
- the Ammunition Shortage probe uses the accepted Event front reference already preserved at `art/approved/card-references/event-front-reference.png`;
- no remaining five Event cards are generated until the first Event source is reviewed as a production reference.

## Dependencies

- `../001-3-1-individual-card-front-production.task.trace.md`
- `../001-3-card-visual-system.decision.trace.md`
- `001-1-pre-pilot-source-review.decision.trace.md`
- `../001-5-pilot-mediated-card-generation.topic.trace.md`
- `../../roles/001-5-pilot.role.trace.md`

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Produce Individual Card Fronts](../001-3-1-individual-card-front-production.task.trace.md)
  - Value: X87JAQyNubj8HT-nr9NjLDasdHTI3kFAWBYur5HYrP0

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:qwIpuIS9bY-6z5pHGrrZd24nJHbbGSfR6DBB66kA3mM
