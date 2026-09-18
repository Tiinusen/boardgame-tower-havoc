# Tower Havoc Match Lineage Demo

Synthetic match used only to inspect the proposed gameplay provenance schemas.

This revision deliberately demonstrates the **directory-local filename-lineage convention**:

- `match/setup/` owns one local namespace;
- every turn directory owns another local namespace;
- semantic `Parent` remains explicit inside each artifact;
- moving an artifact between these directories would cause its filename lineage to be recalculated for the destination without changing Parent semantics.

`tiinex.human.runtime.v1` and `towerhavoc.rule.resolution.v1` are hypothetical in this demo. The demo ruleset starts both players with 9 banked actions only to keep the example short; this is not a proposed game rule.

Open `TREE.txt` first.
