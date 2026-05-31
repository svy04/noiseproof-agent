# README Proof-marker Archive Application Refresh Review

Status: review-only gate.

Phase marker: readme proof-marker archive application refresh review v0.

Label: README proof-marker archive application refresh review.

This review decides whether application-facing documents should mention the extracted proof-marker archive after the legacy README markers moved to `docs/review/readme-proof-marker-archive.md`.

## Problem

The README source is now cleaner, and the legacy proof markers live in a dedicated review artifact. However, the application-facing documents still point readers mainly to the README, `docs/GOAL.md`, and external-reader proof path.

application-facing docs do not yet mention the extracted proof-marker archive.

That is acceptable for the immediate extraction, but reviewers who want exact legacy marker continuity should have a visible path to the archive without needing to infer it from tests.

## Decision

Refresh application-facing docs next.

The refresh should:

- link `docs/review/readme-proof-marker-archive.md` from the portfolio/application proof path
- explain that the archive is source-level provenance, not product runtime evidence
- keep the primary external-reader path short
- preserve non-claims around hosted deployment, automatic failure-case creation, and complete workflow failure causality

## Boundary

Do not refresh application-facing docs in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
readme proof-marker archive application refresh v0
```
