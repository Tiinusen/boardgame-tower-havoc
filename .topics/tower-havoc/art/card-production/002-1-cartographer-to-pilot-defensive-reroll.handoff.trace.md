# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/053d46ce082d4ec261b82abc44ecca403d61e240/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 16:12:00
  - Trace: [Pilot Card Generation Tranche 1](002-pilot-card-generation-tranche.task.trace.md)
  - Origin:
    - [relative](002-pilot-card-generation-tranche.task.trace.md)
- Current
  - Current Schema: [tiinex.handoff.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/handoff/tiinex.handoff.v1.schema.md)
  - Created At: 2026-09-19 16:13:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Retry the earlier 4:7 candidate as an exact 5:7 source without changing card semantics.
  - Summary: Qualified Pilot handoff route for one human-mediated `Defensive Reroll` card-front generation.
  - Status: ready/local

---

# Defensive Reroll — Cartographer To Pilot

## Handoff Parties

- Purpose: execute exactly one fresh-conversation human-mediated external generation route for `Defensive Reroll`, preserve the exact returned source/deviations, manufacture a Pilot-to-Cartographer return package, and stop
- From: Cartographer
- From Kind: role
- From Reference: [Cartographer Role](../../roles/001-2-cartographer.role.trace.md)
- To: Pilot
- To Kind: role
- To Reference: [Pilot Role](../../roles/001-5-pilot.role.trace.md)

## Transfers

- card-generation-route
  - Transfer Kind: work-and-responsibility
  - Description: present the declared reference image and exact human-visible generation request unchanged, guide one human-operated external generation, preserve the exact returned source bytes and execution facts, then return Evidence and a Pilot-to-Cartographer Handoff package
  - Controlling Artifact: [Pilot Card Generation Tranche 1](002-pilot-card-generation-tranche.task.trace.md)
  - Boundary: one card route only; do not continue into a sibling card or redesign the prompt

## Required Context

- visual-reference
  - Material: exact reviewed Offensive Reroll — 2 5:7 PNG
  - Material Reference: [Tactic production reference](001-generated-offensive-reroll-2.png)
  - Purpose: strict visual/layout authority for this bounded generation route
  - Availability: available

- pilot-role
  - Material: Tower Havoc Pilot Role
  - Material Reference: [Pilot Role](../../roles/001-5-pilot.role.trace.md)
  - Purpose: bounded external-execution recipient authority
  - Availability: available

- tranche-task
  - Material: current card-generation tranche Task
  - Material Reference: [Pilot Card Generation Tranche 1](002-pilot-card-generation-tranche.task.trace.md)
  - Purpose: scope, done criteria, route isolation, and retained review boundary
  - Availability: available

## Reference Context

- visual-process
  - Material: Tower Havoc Pilot-mediated card-generation process
  - Material Reference: [Pilot-Mediated Card Generation](../001-5-pilot-mediated-card-generation.topic.trace.md)
  - Purpose: exact-byte preservation, one-route-per-conversation, terminal return, and stable-promotion rules
  - Availability: available

## Retained Responsibilities

- design-review
  - Retained By: Cartographer
  - Responsibility: review returned source against current card semantics, text fidelity, visual family, geometry, and deterministic-processing suitability
  - Boundary: Pilot return is not Cartographer review PASS

- project-acceptance
  - Retained By: Steward
  - Responsibility: project-level acceptance of visual source when that acceptance is required
  - Boundary: Pilot and Cartographer must not manufacture Steward acceptance

## Exclusions And Dependencies

- no-direct-substitution
  - Kind: excluded-scope
  - Description: Pilot must guide the human-operated external generation rather than silently substituting a Pilot-held image-generation action
  - Responsible Party Or Role: Pilot

- no-gameplay-invention
  - Kind: excluded-scope
  - Description: do not invent, paraphrase, rebalance, or extend card gameplay text beyond the exact request
  - Responsible Party Or Role: Pilot

- no-source-transform-before-return
  - Kind: excluded-scope
  - Description: do not crop, resize, normalize, repaint, or recompress the returned source before byte preservation and return
  - Responsible Party Or Role: Pilot

## Completion Expectation

- Signal Kind: return
- Signal Meaning: one exact returned source PNG or truthful blocker, execution Evidence, and Pilot-to-Cartographer return Handoff package; then stop
- Return To: Cartographer
- Return To Reference: [Cartographer Role](../../roles/001-2-cartographer.role.trace.md)

## Exact Human-Visible Generation Request

Pilot MUST present this exact text unchanged in one fenced Markdown code block after identifying the declared reference image:

```text
Use the attached Tower Havoc TACTIC card as the strict visual reference.

Create ONE isolated production card front only.

CRITICAL OUTPUT GEOMETRY:
- exact 5:7 portrait card aspect ratio
- the complete card must fill the canvas edge-to-edge
- no margins outside the card
- no mockup
- no table or background
- no second card
- no contact sheet
- preserve the same outer proportions, frame geometry, header height, illustration region, text panel proportions, typography hierarchy and bottom emblem placement as the attached reference

The attached image is the production-layout reference.
Change only the requested card title, rules text, timing text and central illustration.
Do not redesign the card frame or alter its proportions.

TYPE: TACTIC
TITLE: Defensive Reroll

RULES TEXT:
Reroll one relevant roll made by the card owner. Exact eligible roll types remain PLAYTEST.

TIMING:
Reaction / PLAYTEST.

Do not resolve the PLAYTEST wording yourself and do not invent eligible roll types.
Illustration should depict emergency defensive coordination, engineers, spotters, or a last-second correction around a fortified tower.
Keep all text highly legible.
```

After the human chooses the current result for return, Pilot MUST instruct the human to send this exact terminal text in a separate fenced Markdown code block:

```text
Approved. No more image generation. Create and return the Tiinex handoff package from the current approved output.
```

That terminal text means return-only state. It does not itself create final Tower Havoc visual acceptance.

## Interaction Limit

- Interaction Mode: human-mediated-external-execution
- Execution Expected: yes
- Max Execution Attempts: 1
- Awaiting State: awaiting-human-execution-result
- Sibling Route Continuation: forbidden

## Interpretation Limits

- Does Not Mean: generated pixels are gameplay authority, the provider received unseen internal prompt bytes identical to the user-visible request, or a returned file is accepted product source merely because it exists.
- Must Not Be Used To Claim: final card acceptance, TTS deck-sheet PASS, print suitability, publication permission, or completion of sibling routes.
- Authority Limits: Cartographer retains design review and Steward retains project-level acceptance.
- Transport Limits: Handoff package/carriage proves the declared transport material and route, not external provider behavior beyond preserved observable evidence.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Pilot Card Generation Tranche 1](002-pilot-card-generation-tranche.task.trace.md)
  - Value: qwIpuIS9bY-6z5pHGrrZd24nJHbbGSfR6DBB66kA3mM

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:ZjtPyRLFAT6z6VEPrVmN-1fx8ereqXopbGj2iG34o6w
