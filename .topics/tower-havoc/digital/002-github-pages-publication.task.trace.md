# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.project.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/coordination/project/tiinex.project.v1.schema.md)
  - Created At: 2026-09-18 01:31:00
  - Trace: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Origin:
    - [relative](../001-tower-havoc.project.trace.md)
- Current
  - Current Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 12:50:14
  - Authors: Olle Tiinus; ChatGPT
  - Why: The first real TTS playtest showed repository permalink asset URLs were not a reliable TTS delivery mechanism.
  - Summary: Publish source mirrors plus stable TTS asset URLs via GitHub Pages.

---

# Publish Tower Havoc mirrors and TTS assets through GitHub Pages

## Objective

Create one repository-owned public publication flow that exposes inspectable Tower Havoc artifact material and stable HTTP TTS asset paths without making GitHub Pages semantic authority.

## Done Criteria

A push to the working source branch regenerates project projections/assets, validates the repository, builds a public artifact, publishes an inspectable `public` branch, deploys the same material to GitHub Pages, includes a source-repository mirror, and serves `tts/assets/**` as direct Pages files suitable for Tabletop Simulator.

## Scope

Adapt the portable static/mirror publication pattern from `Tiinex/docs/.github/workflows/publish-public.yml` at docs commit `f5a9543318283344d8f3d08649d885f1a5f28639`. Publish the Tower Havoc `.topics` material, generated docs/data, root README/rights notice, and TTS assets. Keep build output derived and disposable; source authority remains the repository lineage.

## Dependencies

Requires GitHub Actions and GitHub Pages to be enabled for the repository. TTS consumes the resulting public Pages asset URLs but does not become a dependency of canonical game semantics.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc](../001-tower-havoc.project.trace.md)
  - Value: 7YEXIYUxtC4y0Woyo5xmZ0g1mp44NQQoum3NfGmMeoQ

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:-Cg7yVEC_8DLcCDNjdLpEQUxqkAP0_Gx0P58GuQXytI
