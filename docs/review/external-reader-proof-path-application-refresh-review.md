# External-reader Proof Path Application Refresh Review

Status: review-only gate.

Phase marker: external-reader proof path application refresh review v0.

Label: External-reader proof path application refresh review.

This review decides whether the compact external-reader proof path should be surfaced in application-facing documents beyond the portfolio index.

## Current State

`docs/review/external-reader-proof-path.md` now provides a repository-native 5-minute path.

It is already surfaced in:

- `docs/application/portfolio-index.md`

It is not yet surfaced directly in:

- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

## Decision

Refresh those application-facing documents next.

The refresh should:

- link `docs/review/external-reader-proof-path.md`
- preserve the 5-minute proof path wording
- keep hosted deployment evidence unclaimed
- keep automatic failure-case creation unclaimed
- keep complete workflow failure causality unclaimed
- avoid changing runtime, schema, dashboard, or smoke evidence

## Boundary

Do not refresh application-facing docs in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
external-reader proof path application refresh v0
```
