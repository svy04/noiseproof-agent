# Ops Summary Semantic Retrieval Operational Counts

Status: implemented.

Phase marker: ops summary semantic retrieval operational counts v0.

## Purpose

Make implemented caller-provided vector semantic retrieval paths more inspectable from `/ops/summary`.

Phase 612 corrected the wording boundary. This phase adds explicit operational counters so a reviewer can see whether semantic retrieval runs and caller-provided embedding rows exist without reading raw table contents.

## Added Fields

```text
retrieval_run_count
semantic_retrieval_run_count
chunk_embedding_count
caller_provided_embedding_count
```

## Route-level Behavior

The route test creates a semantic retrieval fixture with two caller-provided embedding rows, runs one semantic retrieval, and verifies `/ops/summary`.

Observed test expectation:

```text
retrieval_run_count -> 1
semantic_retrieval_run_count -> 1
chunk_embedding_count -> 2
caller_provided_embedding_count -> 2
Semantic retrieval runs recorded: 1
caller-provided embedding row(s): 2
```

The summary note states that these are operational counts, not semantic retrieval quality evidence.

## Changed Surface

```text
GET /ops/summary
OpsSummaryOut
PostgresRepository.ops_summary()
test InMemoryRepository.ops_summary()
```

## Boundary

This is an operations summary count surface only.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not distributed tracing.

This is not free-form final report generation.

This is not product-complete.

## Verification

```text
tests/test_routes.py::test_ops_summary_counts_semantic_retrieval_and_caller_provided_embeddings
```

## Next Gate

```text
local Docker/FastAPI runtime smoke for these operational counts if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
