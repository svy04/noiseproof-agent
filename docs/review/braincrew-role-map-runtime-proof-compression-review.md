# Braincrew Role-map Runtime Proof Compression Review

Status: review-only gate.

Phase marker: braincrew role-map runtime proof compression review v0.

Label: Braincrew role-map runtime proof compression review.

This review decides whether `docs/application/braincrew-role-map.md` should compress its runtime proof section for reviewer scanability.

## Problem

The Runtime Proof Surfaces section is too long.

It contains valuable evidence boundaries, but it now reads like a chronological proof ledger. That makes the FDE-first mapping less immediate: the role fit is visible, then the reader hits a long runtime proof wall before reaching DeepDocurator alignment and the application message.

## Decision

Compress the Braincrew role map next.

The compression should:

- keep the FDE-first mapping and Product Engineer secondary mapping intact
- preserve the external-reader proof path as the first runtime proof entry
- group runtime evidence into short proof categories instead of long narrative paragraphs
- keep links to fresh DB smoke, failure-case proof index, application-ready review, and proof-marker archive
- preserve boundaries around hosted deployment, automatic failure-case creation, and complete workflow failure causality

## Boundary

Do not compress the Braincrew role map in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, free-form final answer generation, or hiring outcome claim.

This preserves FDE-first mapping.
This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
braincrew role-map runtime proof compression v0
```
