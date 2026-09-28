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
  - Created At: 2026-09-28 16:15:55
  - Authors: Steward
  - Why: Parallelize independent post-Atombomb work while preserving Steward acceptance and exact semantic lineage.
  - Summary: Bounded Cartographer integration of the accepted Atombomb into deck lineage and deterministic projections.
  - Status: ready/local

---

# Atombomb Deck And Projection Integration

## Objective

Cartographer is an explicitly required participant in this current work because the accepted Atombomb rule must be materialized across Tower Havoc source and projections without transferring Steward acceptance.

Materialize the accepted one-copy Atombomb Event into the current Dud-free deck and every derived gameplay/runtime surface that depends on deck or Event composition, while preserving semantic lineage and failing visibly if the historical deck parent cannot be qualified by the current bootstrap.

## Done Criteria

- the current deck lineage has a truthful successor representing 35 cards: the existing 34-card Dud-free composition plus exactly one Atombomb Event;
- the deck successor preserves `001-1-1-dud-free-deck.decision.trace.md` as its semantic Parent when current Tooling can qualify that historical parent;
- if current Tooling cannot author that exact successor because of historical schema/integrity authority, return the exact blocker and do not reparent the deck Decision merely for convenience;
- the accepted seven-Event Atombomb Decision is consumed without widening Atombomb into Bell, hand, Ready Ammo, Production, Available Actions, or other state not named by the Steward Decision;
- `data/cards.*`, card-art generation planning, component quantities, TTS deck material, generated documentation/manifests, and other deterministic projections agree with the qualified canonical deck/Event state;
- no Dud cards return and no development-only metadata is introduced into production-facing card copy;
- all relevant project-local validators are run and exact failures are returned rather than bypassed;
- return one qualified Cartographer-to-Steward Handoff Package with changed-source summary, validation state, and unresolved blockers if any.

## Scope

Local Tower Havoc artifact/projection/source mutation required for the accepted Atombomb deck revision. This branch does not generate card artwork, redesign card-draw rules, tune balance, repair Tiinex Core/VS Code, publish remotely, or change licensing/rights.

## Dependencies

- `../cards/001-9-1-atombomb-global-events.decision.trace.md`
- `../cards/001-1-1-dud-free-deck.decision.trace.md`
- `../cards/001-5-1-retire-duds.decision.trace.md`
- `../art/001-3-card-visual-system.decision.trace.md`
- `../roles/001-2-cartographer.role.trace.md`

## Authority Boundary

Steward has accepted Atombomb inclusion, Event family, quantity, and bounded effect. Cartographer may materialize the resulting local lineage and deterministic projections, but may not invent additional gameplay effects or treat a tooling blockage as permission to rewrite semantic Parent continuity.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: daaGDpkAAJwUrAQUJzW0oDVf0wDqE8yF_F9cFUu_bZ4