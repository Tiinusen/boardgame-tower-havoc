# GitHub Issue match runtime — R&D design

This is an implementation note, not canonical gameplay authority. The authoritative semantic roles are defined by `.topics/.schemas/tower-havoc/**` and the design decision under `.topics/tower-havoc/runtime/**`.

## Why this can work

GitHub can be a thin host:

1. an Issue represents the human-facing match room;
2. comments carry player-authored `towerhavoc.action.intent.v1`;
3. Actions validates the intent against the frozen ruleset and current reconstructed state;
4. if randomness is needed, the runtime seals a `towerhavoc.random.request.v1` before the random source is available;
5. a later step materializes `towerhavoc.random.result.v1`;
6. the runtime writes `towerhavoc.action.resolution.v1` and a regenerated `towerhavoc.state.v1`;
7. the Issue receives only a convenient human-readable projection.

The game therefore does not need to be "digitized" as a conventional app before it can be played digitally. Markdown artifacts + a validator/adjudicator are enough for the first experiment.

## Important trust correction

GitHub Actions by itself cannot guarantee that **nobody can cheat**. A repository administrator can normally change workflows, secrets, branch settings, or history. What we can make strong is **tamper visibility and outcome non-selectability**:

- protect the match branch / disallow force-pushes;
- pin the workflow/runtime version in every resolution;
- seal the random request before entropy exists;
- use a public external randomness beacon or multi-party commit/reveal;
- map entropy to game outcomes deterministically;
- commit the source proof and mapping result;
- optionally mirror/archive match commits externally.

With that design, the workflow cannot simply reroll until it likes the answer without leaving evidence or violating the precommitted source policy.

## Hidden cards are the interesting part

A fully public issue cannot safely publish deck order or private hands. The schema family therefore separates:

- public state: counts, towers, ammo, actions, visible discard/event state;
- hidden commitment: a digest over canonical hidden state;
- private delivery: future implementation concern, likely encrypted payload or another per-player private channel;
- reveal: optional/post-match verification against the original commitment.

For the **first runtime R&D**, open hands are acceptable if the goal is only to verify action/state provenance. Hidden-hand play can be added once the event model works.

## Minimum event chain

```text
ruleset
match
seat x N
turn-order
state-000
turn-001
  action-intent
  random-request?
  random-result?
  action-resolution
  state-001
  ...
match-result
```

## Replay property

A verifier should be able to start from the frozen ruleset and initial setup, apply each accepted action resolution in sequence, verify each random-result mapping, and reproduce the final state/result. A stored state snapshot is a cache; disagreement between snapshot and replay should fail closed.
