# README Phase-history Compression Review

Status: review-only gate.

Phase marker: readme phase-history compression review v0.

Label: README phase-history compression review.

This review decides whether the long chronological phase paragraph in `README.md` should be compressed now that the external reviewer fast path exists.

## Problem

The README now has a useful fast path, but the first "What This Is" section still contains a very long phase-by-phase history paragraph.

phase-history paragraph is too long.

That paragraph is useful as raw provenance, but it makes the README harder to scan. The detailed phase trail is already preserved in:

- `docs/GOAL.md`
- `docs/application/portfolio-index.md`
- phase-specific `docs/review/*` artifacts

## Decision

Compress the README phase history next.

The compression should:

- keep the product thesis visible
- keep current major capability groups visible
- move the exhaustive phase trail out of the top narrative
- keep the external-reader proof path as the first verification route
- preserve implemented/planned/unverified boundaries

## Boundary

Do not compress README in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
readme phase-history compression v0
```
