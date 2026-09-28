# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.task.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/task/tiinex.task.v1.schema.md)
  - Created At: 2026-09-19 12:50:14
  - Trace: [Publish Tower Havoc mirrors and TTS assets through GitHub Pages](002-github-pages-publication.task.trace.md)
  - Origin:
    - [relative](002-github-pages-publication.task.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-19 12:50:15
  - Authors: Olle Tiinus; ChatGPT
  - Why: Make the public Pages/mirror behavior explicit without treating the hosting layer as game truth.
  - Summary: Accepted publication boundary for Tower Havoc GitHub Pages and repository mirrors.

---

# GitHub Pages publication contract

## Decision

- State: accepted implementation direction
- Publication ID: digital.github-pages.v1
- Source Authority: repository source and `.topics/tower-havoc/**`
- Public Branch: `public`
- Pages Deploy Source: GitHub Actions artifact built from the same publication directory as the public branch
- Required Public Material: `.topics`; `docs`; `data`; `tts/assets`; root `README.md`; `RIGHTS.md`
- Repository Mirror: publish an inspectable directory snapshot plus deterministic ZIP and metadata under `mirrors/github.com/<owner>/<repo>`
- TTS Asset Path: preserve repository-relative `tts/assets/<asset>` under GitHub Pages so the public URL remains predictable
- Build Rule: regenerate projections and TTS assets, then run project validators before publication
- Decision: GitHub Pages is a delivery/presentation surface; published mirrors and assets never replace lineage or repository history as semantic authority.

## Basis

The first TTS playtest showed direct GitHub repository permalink asset loading was not suitable. The Tiinex/docs publisher already demonstrates the desired public-branch + Pages + mirror pattern.

## Consequences

The repository gains a portable publish workflow and a local bundle builder. TTS URLs may target Pages while all generated asset provenance still points back to `.topics`.

## Review Conditions

If GitHub Pages behavior or the upstream Tiinex/docs publication pattern changes materially, update the implementation while preserving this authority boundary.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Publish Tower Havoc mirrors and TTS assets through GitHub Pages](002-github-pages-publication.task.trace.md)
  - Value: -Cg7yVEC_8DLcCDNjdLpEQUxqkAP0_Gx0P58GuQXytI

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:Pqj1yVbGCTvVbsNc35lJuVABEYYIvmfkkXxrp4XAiKM
