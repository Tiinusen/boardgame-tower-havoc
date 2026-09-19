# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-19 15:02:00
  - Trace: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Origin:
    - [relative](001-visual-asset-system.topic.trace.md)
- Current
  - Current Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-19 16:09:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Adopt the proven Pilot/Handoff external-execution pattern locally so Tower Havoc visual generation becomes explicit, replayable, and package-carried.
  - Summary: Tower Havoc process for one-route-per-conversation Pilot-mediated card-art generation with exact-byte Evidence and qualified return Handoffs.
  - Status: ready/local

---

# Pilot-Mediated Card Generation

## Current Read

Tower Havoc card-art production crosses a human-operated external image-generation boundary. The controlling card semantics and approved visual references already exist in Tower Havoc lineage, while the human can execute a cleaner provider interaction by opening a fresh conversation/project with only the declared reference and exact prompt.

Use Pilot to make that boundary explicit and replayable rather than carrying prompt intent only in chat memory.

## Reused Tiinex Pattern

This project-local process intentionally follows the proven Tiinex Business/Playthings pattern without importing Playthings domain semantics:

- generic Pilot boundary: prepare → guide → receive → report → return;
- exact human-visible input is preserved separately from unknown provider-internal prompt compilation;
- one shared Handoff package may advertise several independent qualified routes;
- one fresh Pilot conversation is used per route;
- exact returned source bytes are preserved before transforms;
- returned execution is Evidence, not automatic product acceptance;
- final source/derivative promotion is performed by the retained reviewing/acceptance authority;
- Handoff transport carries the durable work boundary instead of an ad-hoc prose prompt.

Reference implementations studied for this local adaptation:

- Tiinex Business Pilot Role — `Tiinex/business/.topics/roles/001-7-pilot-role.trace.md`
- Tiinex Business Human-Mediated External Execution — `Tiinex/business/.topics/processes/004-human-mediated-external-execution-process.trace.md`
- Playthings Visual Production And Asset Lifecycle — `Tiinex/verse-playthings/.topics/viewer/playthings/processes/001-playthings-visual-production-and-asset-lifecycle-process.trace.md`

These are process references only. Tower Havoc remains semantically bounded to its own domain artifacts and schemas.

## Tower Havoc Route Contract

For one card-generation route:

1. Cartographer authors a bounded Handoff to Pilot from the current card-production Task.
2. The Handoff declares exactly one reference image, exact card semantics/text, exact human-visible generation prompt, attempt policy, and return role.
3. Tooling manufactures a qualified Handoff package. Shared packages may carry several independent route Pointers.
4. A fresh Pilot conversation is grounded to exactly one route.
5. Pilot presents the declared reference and exact prompt; the human performs the external generation.
6. On a chosen current result, the human sends the terminal instruction exactly:

```text
Approved. No more image generation. Create and return the Tiinex handoff package from the current approved output.
```

7. Pilot enters return-only state: preserve exact result → truthful Evidence → Pilot-to-Cartographer Handoff → qualified package → stop.
8. Cartographer reviews the returned source for text/layout/geometry and deterministic-processing suitability.
9. Steward acceptance remains separate when project-level source approval matters.
10. Crop/resize/TTS normalization/deck-sheet packing happens only after source preservation and is recorded as derivative work.

## Multi-Route Boundary

A shared carrier may hold several sibling card-generation Handoff routes, but each Pilot conversation selects exactly one route. A route must not continue into a sibling card. A retry that exceeds the declared attempt policy requires a successor Handoff rather than silently overwriting the previous execution history.

## Retention And Promotion

Keep exact source bytes and concise execution Evidence while the route is active/reviewable. Rejected attempts are not promoted into stable runtime asset directories merely because they exist. Accepted visual source or deterministic derivative may later move to `art/approved/**` and `tts/assets/**` with hashes back to the originating lineage.

## Interpretation Limits

This process does not claim that user-visible prompt fidelity proves provider-internal byte identity, that a generated image is accepted merely because it returned, or that Playthings owns Tower Havoc graphics semantics. It is a local adoption of a reusable Tiinex execution/transport pattern.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Value: 8q2khIhd68nFOB_FcG1H0HwVVABGuVO4LMB_0qxtZwE

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:m1-yqFRzNZugWsURilEayPzNsMUMtobUPzg42OUGV8Q
