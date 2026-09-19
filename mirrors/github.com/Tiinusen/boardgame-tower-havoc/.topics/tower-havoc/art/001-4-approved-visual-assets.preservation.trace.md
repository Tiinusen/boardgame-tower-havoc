# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-19 15:02:00
  - Trace: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Origin:
    - [relative](001-visual-asset-system.topic.trace.md)
- Current
  - Current Schema: [tiinex.preservation.v1](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.schemas/core/preservation/tiinex.preservation.v1.schema.md)
  - Created At: 2026-09-19 15:10:00
  - Authors: Olle Tiinus; ChatGPT
  - Why: Keep the exact approved image bytes judgeable and portable before further card-front generation.
  - Summary: Preservation bundle for the explicitly approved player-board, coin, and card-reference image bytes.

---

# Approved Visual Asset Preservation

## Preserved Material

- Material Description: exact approved PNG bytes for six faction boards, two normalized Action/Ammo coin sides, one common card-back reference, and three card-front design references
- Material Kind: preserved generated-image files
- Material Reference: repository-local `art/approved/**`

- `art/approved/card-references/card-back-reference.png` — 543988 bytes — sha256 `956ef2705b93d1df1c28241eca4d58230d71051812c9377bb362d2f7f5343c7e`
- `art/approved/card-references/event-front-reference.png` — 541287 bytes — sha256 `1d7571beefd631777986f6054e2cadf33dc8fb1920587aa5649ef04f0877da66`
- `art/approved/card-references/sabotage-front-reference.png` — 509060 bytes — sha256 `6215adb68f1f7dbf1b7016664e5868c75d6fec35fa903a9d47838e558aaece0d`
- `art/approved/card-references/tactic-front-reference.png` — 522340 bytes — sha256 `2c5aa90040747667c79f4a2f5081475325cdfa9b87bd1d81956619db4367ede3`
- `art/approved/coins/action-side.png` — 488738 bytes — sha256 `179bf99ba7ea6fd391c2ada2ebf4b8250ead35f56d8e54cf8522c9c3540b33e4`
- `art/approved/coins/ammo-side.png` — 470906 bytes — sha256 `8080ea3e0dfa041f968e30d8a98f543e2a65499f4cddb5eefad8b309a0339221`
- `art/approved/player-boards/ash-dominion.png` — 2708996 bytes — sha256 `7fdc0c34c97c96b3436622d1ed55f37ded7f5ca6a86ea8857c6da384523fd37b`
- `art/approved/player-boards/brass-union.png` — 2681606 bytes — sha256 `126c0049646a7a16f61e92928b46cda10361c5ebec270a9e20c8a62be4095da0`
- `art/approved/player-boards/ember-rail.png` — 2677725 bytes — sha256 `4ef0a5147d34d46649e2a51d19483ca4cf67423328a3368df950ab1eda0edf54`
- `art/approved/player-boards/horizon-guild.png` — 2685140 bytes — sha256 `4b05f5a5adddd07e3bc2168f3e6ea5c408ed14160950c8681679527851783abf`
- `art/approved/player-boards/ironclads.png` — 2943040 bytes — sha256 `b4b08670ae0078240e756213c915dadb7a0d8ec77cb4e9b06408e1c161a4012b`
- `art/approved/player-boards/storm-foundry.png` — 2742048 bytes — sha256 `03a9f236a25739f2219bdcd1d66229c46db289eede508b0d5ea01ce417e36693`

## Preservation Act

- Preservation Method: exact local PNG copies retained in the workspace after explicit design review
- Preservation Time Or State: accepted visual baseline for the next Tower Havoc TTS iteration
- Actor: project Steward approval with Cartographer materialization

## Provenance

- Known Source: image-generation outputs and subsequent deterministic coin crop/normalization produced during the Tower Havoc design session
- Provenance Limits: prompt/model-internal generation state is not embedded in the PNG files; only the reviewed output bytes are preserved here

## Fidelity And Loss

- Fidelity Notes: player-board and card-reference files are exact copies of the explicitly approved outputs; coin files are the explicitly approved 512 × 512 normalized crops
- Known Losses: montage context and generation UI metadata are not required for runtime use; card references are not yet normalized production card faces

## Custody Or Storage Boundary

- Storage Or Custody State: repository-local preserved visual source material intended to travel with the next complete Workspace carrier
- Reuse Boundary: governed by repository `RIGHTS.md`; preservation does not grant an open license

## Interpretation Limits

- Does Not Prove: gameplay correctness, final print quality, manufacturing suitability, balance, or that example card text in the visual references is canonical
- Not Yet Used As: empirical playtest Evidence or final individual card-face approval

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [Tower Havoc Visual Asset System](001-visual-asset-system.topic.trace.md)
  - Value: 8q2khIhd68nFOB_FcG1H0HwVVABGuVO4LMB_0qxtZwE

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/f5a9543318283344d8f3d08649d885f1a5f28639/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value:5TLfyzpjyAllk__vru_HjxnKlodYFJmoBD5DfJdqSCc
