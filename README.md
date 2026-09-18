# Tower Havoc

**Tower Havoc** is a 2–6 player competitive tower-building and artillery board game. The first visual edition is **Dieselpunk Edition**.

## Source of truth

The canonical game definition lives in **`.topics/tower-havoc/**`** as typed Tiinex artifacts. Start at:

- `.topics/tower-havoc/001-tower-havoc.project.trace.md`
- `.topics/tower-havoc/README.md`

The ordinary `docs/`, `data/`, `cad/FUSION360_BRIEF.md`, and `tts/ONE_HOUR_PLAYTEST.md` files are generated projections for humans/tools. Regenerate them with:

```bash
python scripts/generate_from_topics.py
```

This is deliberate: rules live as Decisions, explicit gates live as Conditions, prototype work lives as Tasks, views live as Presentation Surfaces, and future real play observations will live as Evidence instead of being mixed into rule prose.

## Fast path to a playtest

1. Read `docs/RULEBOOK.md`.
2. Read `tts/ONE_HOUR_PLAYTEST.md`.
3. Use generic TTS blocks/tokens first.
4. Use the generated 40-card manifest/assets.
5. Record the exact first-session baseline and observations.

## Status

Pre-playtest MVP. Several balance constants remain explicitly `PLAYTEST`.

## Authorship

Game design and rules: **Olle Tiinus**. Future concrete contributions should be credited when they exist and are accepted.

## Artifact-native match runtime

The repository now contains a draft local gameplay schema family under `.topics/.schemas/tower-havoc/`. It is designed so a match can eventually be played and replayed as provenance: ruleset -> match -> seats -> turn order -> action intents -> random results -> adjudicated resolutions -> generated state -> match result. See `runtime/GITHUB_MATCH_RUNTIME.md`.
### Gameplay schema inheritance

Project-local `towerhavoc.*` schemas are grouped as one Tower Havoc Schema Family, but each schema inherits from the nearest matching Tiinex semantic family rather than from a Tower Havoc umbrella schema. See `.topics/.schemas/tower-havoc/README.md`.

## Experimental match-lineage inspection

This review carrier also includes `examples/match-lineage-demo/`, a synthetic full-match artifact tree used to inspect the proposed gameplay provenance schemas. It is example material, not canonical playtest evidence. Candidate Human Runtime and automatic rule-resolution schema notes live under `runtime/experiments/`.


## Tiinex filename lineage

Canonical trace filenames under `.topics/tower-havoc/**` use directory-local numeric lineage. See `.topics/tower-havoc/README.md`; semantic `Parent` remains authoritative.
