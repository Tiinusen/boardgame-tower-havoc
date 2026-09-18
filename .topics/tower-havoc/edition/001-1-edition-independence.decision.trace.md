# Continuity Context

- Envelope Schema: [tiinex.root.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/tiinex.root.v1.schema.md)
- Parent
  - Parent Schema: [tiinex.topic.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/topic/tiinex.topic.v1.schema.md)
  - Created At: 2026-09-18 01:59:00
  - Trace: [001-4-edition-model.topic.trace](001-edition-model.topic.trace.md)
  - Origin:
    - [relative](001-edition-model.topic.trace.md)
- Current
  - Current Schema: [tiinex.decision.v1](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.schemas/core/decision/tiinex.decision.v1.schema.md)
  - Created At: 2026-09-18 02:00:00
  - Authors: Olle Tiinus
  - Why: Lock the separation between game mechanics and visual edition.
  - Summary: Edition-independent mechanical core

---
# Edition-independent mechanical core

This artifact records the operative Tower Havoc state for this bounded subject.

## Decision

- State: accepted
- Edition Rule ID: edition.core
- Decision: Tower Havoc mechanics are edition-independent. A new visual edition may change theme, architecture, weapon appearance, faction names, art style, and props while preserving the base rules and mechanical component interfaces.

## Basis

This allows the game to be re-skinned without forking balance or teaching different rules.

## Consequences

Generated rulebook mechanics should not depend on dieselpunk-specific language where a neutral rule term works. Edition documents may provide flavor separately.

---

# Continuity Integrity

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: [001-4-edition-model.topic.trace](001-edition-model.topic.trace.md)
  - Value: dki7AJfR9AZw143XWOg5ngTpvGn6K5E4G27QdTUTPKs

- [sha256-base64url-c14n-v2](https://github.com/Tiinex/docs/blob/3988951208eb9a8926e84ab42625d4b42fa00c2d/.topics/.validators/sha256-base64url-c14n-v2.validator.md)
  - Towards: self
  - Value: 6Xk9CAegm2Fq_2zmIjOr-ZvsXXaamBYc34zRvkDr6hw