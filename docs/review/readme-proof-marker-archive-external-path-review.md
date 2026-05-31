# README Proof-marker Archive External Path Review

Status: review-only gate.

Phase marker: readme proof-marker archive external path review v0.

Label: README proof-marker archive external path review.

This review decides whether the compact external-reader proof path should mention the extracted README proof-marker archive.

## Problem

The external-reader proof path should stay compact. Its job is to guide a reviewer through the current evidence chain in roughly five minutes, not to list every historical marker.

However, application-facing docs now expose `docs/review/readme-proof-marker-archive.md` as source-level provenance for legacy README proof markers. A reviewer using only `docs/review/external-reader-proof-path.md` may not discover that archive unless they continue into the portfolio index or application review.

## Decision

Add a compact optional note next.

The note should:

- keep the 5-minute path order unchanged
- link `docs/review/readme-proof-marker-archive.md` only as optional source-level provenance
- state that the archive is not product runtime evidence
- preserve boundaries around hosted deployment, automatic failure-case creation, and complete workflow failure causality

## Boundary

Do not update the external-reader proof path in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is source-level provenance.
This is not product runtime evidence.
This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
readme proof-marker archive external path refresh v0
```
