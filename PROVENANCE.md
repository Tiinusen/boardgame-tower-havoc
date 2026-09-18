# Provenance

Tower Havoc uses `.topics/tower-havoc/**` as its canonical semantic game model.

The current artifact-native model was reconstructed from the earlier rule/specification work and conversation decisions, then separated by semantic role using the current Tiinex Docs schema families. The structure follows the same general discipline visible in `Tiinex/business`: directory placement is for navigation, while declared Parent continuity and artifact type carry meaning.

The original uploaded `game.md` is preserved as `sources/original-sanka-torn-draft.md` and is bounded by `.topics/tower-havoc/sources/001-original-sanka-torn-draft.preservation.trace.md`. It is historical source material, not current rule authority.

No playtest Evidence has been fabricated. The playtest branch is prepared to receive real `tiinex.evidence.v1` artifacts after sessions occur.

Generated documents and data files carry a generated-projection header where practical and should be regenerated rather than edited as canonical sources.

## Local gameplay schema experiment (v0.5)

Tower Havoc now carries project-local schema notes for match execution. They are explicitly draft/local and are not claimed as generic Tiinex schemas. They separate player intent, randomness, adjudication, generated state, hidden-state commitments, and final result so a future host can be replaced without losing match provenance.
## Semantic schema inheritance correction (v0.6)

The Tower Havoc gameplay namespace remains project-local, but namespace membership is not used as schema inheritance. Each `towerhavoc.*` schema now declares the nearest existing Tiinex semantic parent that owns its primary role (for example Task for action/random requests, Event Session for a match, Event Window for a turn, Party Role for a seat, Derivation for random result mapping, and Validation Report for commitment reveal verification).

The local Schema Family artifact groups the domain and records extension policy. It does not replace those direct semantic parents.

## Filename lineage boundary

Numeric filename lineage under `.topics/tower-havoc/**` is directory-local navigation metadata. It is not semantic identity and must not be treated as a replacement for the artifact's declared `Parent`. Renaming or moving an artifact may therefore change its filename lineage while preserving semantic Parent continuity.
