# README External Proof Path Refresh Review

Status: review-only gate.

Phase marker: readme external proof path refresh review v0.

Label: README external proof path refresh review.

This review decides whether `README.md` should surface the compact external-reader proof path near the top of the repository.

## Current State

The compact proof path exists:

- `docs/review/external-reader-proof-path.md`

It is already surfaced in:

- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

`README.md` currently lists the phase in implementation status, but does not yet give a top-level fast path for an external reviewer.

## Decision

Add a short fast-path block to `README.md` next.

It should:

- link `docs/review/external-reader-proof-path.md`
- say it is a 5-minute repository-native path
- keep implemented/planned/unproven claims separated
- repeat the core boundaries: not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality

## Boundary

Do not edit README fast path in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
readme external proof path refresh v0
```
