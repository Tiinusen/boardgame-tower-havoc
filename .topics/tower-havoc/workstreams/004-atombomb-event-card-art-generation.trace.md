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
  - Created At: 2026-09-28 16:15:59
  - Authors: Steward
  - Why: Generate production-facing Atombomb card art through the qualified Pilot boundary while preserving exact source provenance.
  - Summary: Pilot human-mediated production-art route for the accepted Atombomb Event card.
  - Status: ready/local

---

# Atombomb Event Card Art Generation

## Objective

Pilot is an explicitly required participant in this current work because the accepted Atombomb Event needs one human-mediated production-art generation route with exact source-byte provenance and a qualified return package.

Guide the human through one same-conversation image-generation route using the approved Event card reference. Keep generation guidance epistemic and minimal: the reference image carries the established visual system, while the user-visible text states only the card identity, exact production copy, and enough illustrative intent to distinguish the subject.

## Exact Human-Visible Generation Text

Present the approved Event reference image and this exact text to the human for the next user turn:

```text
Use the attached Tower Havoc EVENT card as the visual reference.

Create one isolated 5:7 portrait card for:

EVENT
Atombomb

Destroy all tower floors and all reinforcements belonging to every player.

Resolve immediately.

Use an illustration of a catastrophic dieselpunk superweapon blast overwhelming fortified towers. Keep the rules text clearly legible and output only the card, without a surrounding mockup or background.
```

## Terminal Approval Phrase

Before generation, also give the human this exact phrase to send only when the current generated image is accepted:

```text
Approved. No more image generation. Create and return the Tiinex handoff package from the current approved output.
```

Generic approval, silence, or emoji does not trigger return-only state.

## Done Criteria

- the human submits the generation request as a user turn in the same Pilot conversation with the approved Event reference attached;
- no `PLAYTEST`, prototype/draft status, lineage/process language, or other development meta-subtext appears on the card face;
- the visible gameplay copy remains exactly equivalent to the accepted Atombomb effect and immediate timing; do not add Bell, hand, ammo, action, production, or other effects;
- if the human wants a correction, guide only the bounded correction they request; do not redesign gameplay or visual-system semantics;
- once the exact terminal approval phrase is received, enter return-only state before tool selection: preserve exact current source bytes → truthful execution Evidence → Pilot-to-Steward return Handoff → manufacture qualified Handoff Package → expose a human-visible package link/attachment → show exact routing text → stop;
- a raw `/mnt/data/...` path is not successful human-visible package delivery;
- exact returned/downloaded source bytes are preserved before crop, resize, normalization, deck-sheet packing, or other deterministic derivatives;
- return one qualified Pilot-to-Steward Handoff Package or an exact fail-visible blocker.

## Scope

One Atombomb Event-card generation route only. No sibling card generation, gameplay redesign, final Steward acceptance, remote publication, rights change, or deterministic image post-processing before exact source preservation.

## Dependencies

- `../cards/001-9-1-atombomb-global-events.decision.trace.md`
- `../art/001-3-card-visual-system.decision.trace.md`
- `../art/approved/card-references/event-front-reference.png`
- `../art/001-5-pilot-mediated-card-generation.topic.trace.md`
- `../roles/001-5-pilot.role.trace.md`

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-9-1-atombomb-global-events.decision.trace.md](../cards/001-9-1-atombomb-global-events.decision.trace.md)
  - Value: 1b5UA56LeOHMixichDk6Jr5f6NG0CCLmL01pln9Yxdo

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: mHEDynH710cerFUE476vR1hgiizbHzy-DpjptuNUyYs