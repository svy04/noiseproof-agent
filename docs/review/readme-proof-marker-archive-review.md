# README Proof-marker Archive Review

Status: review-only gate.

Phase marker: readme proof-marker archive review v0.

Label: README proof-marker archive review.

This review decides whether the hidden proof-marker archive left inside `README.md` during Phase 103 should remain there or be extracted into a dedicated review artifact.

## Problem

Phase 103 made the rendered README easier to scan, but it preserved legacy README proof markers in a hidden HTML comment so older source-level proof checks could keep passing while the rendered page stopped showing a chronological wall.

hidden README archive is a temporary compatibility bridge.

That bridge is acceptable for one transition, but it is not the clean final shape. The rendered README is shorter, yet the source file still carries a large hidden archive. That makes future README edits noisier and blurs the line between public first-pass narrative and proof-marker compatibility storage.

## Decision

Extract the hidden README proof-marker archive next.

The extraction should:

- move legacy proof markers into a dedicated review artifact
- keep README rendered content short and source content clean
- update tests to read proof markers from that artifact where appropriate
- preserve the external-reader fast path and explicit non-claims
- avoid deleting provenance without another inspectable source

## Boundary

Do not extract the archive in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
readme proof-marker archive extraction v0
```
