# Application Current-claim Compression Review

Status: review-only gate.

Phase marker: application current-claim compression review v0.

Label: Application current-claim compression review.

This review decides whether the application-facing current claim blocks should be compressed for external-reader scanability.

## Problem

The application-facing current claims are too long.

`docs/application/portfolio-index.md` and `docs/review/application-ready-review.md` preserve a lot of useful boundary detail, but the current-claim paragraphs now read like phase history. That makes the proof surface harder to scan for a Braincrew-style reviewer who needs the short claim first and the evidence path second.

The issue is not correctness. The issue is reader load.

## Decision

Compress the application-facing current claims next.

The compression should:

- keep the strongest allowed claim visible in one short paragraph
- keep forbidden claims close to the allowed claim
- move detailed phase history to existing proof artifacts instead of repeating it inline
- keep links to the external-reader proof path and proof-marker archive
- keep every claim bounded as a portfolio artifact, not a product-complete declaration

## Boundary

Do not compress application claims in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not a product-complete declaration.
This is not product-complete declaration language.
This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
application current-claim compression v0
```
