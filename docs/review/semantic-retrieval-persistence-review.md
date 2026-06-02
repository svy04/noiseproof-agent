# Semantic Retrieval Persistence Review

Phase marker: semantic retrieval persistence review v0.

Status: review-only.

## Purpose

Decide how semantic retrieval candidates should become a persisted `retrieval_runs` row after the preview endpoint and runtime smoke have proven the preview boundary.

This review adds no endpoint code. It selects the next implementation boundary.

## Current Evidence

Semantic preview endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-preview
```

Runtime smoke artifact:

```text
docs/review/semantic-retrieval-preview-runtime-smoke.md
semantic_preview_runtime_smoke
```

Observed runtime behavior:

```text
POST /documents/{document_id}/semantic-retrieval-preview -> 200
dimension mismatch -> 400
retrieval_runs_unchanged -> true
candidate_chunk_ids present
missing_embedding_chunk_ids present
```

The preview endpoint remains preview-only.

## Decision

The next implementation gate should be:

```text
semantic retrieval persistence endpoint v0
```

Use a new explicit endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-runs
```

Do not overload `POST /documents/{document_id}/retrieval-runs`.

Marker:

```text
do not overload POST /documents/{document_id}/retrieval-runs
```

Reason:

```text
The lexical document retrieval endpoint accepts question + strategy + top_k.
Semantic persistence requires question + caller-provided query_embedding + embedding_model + embedding_dimension + limit.
Mixing both request shapes into one route would make persistence behavior harder to inspect.
```

## Persistence Target

Use the existing retrieval_runs table.

The endpoint should create one `retrieval_runs` row with:

```text
question = request question
strategy = semantic-cosine
status = completed or no_results
result_count = candidate count
hit_rate = result_count / limit
citation_coverage = 1.0 when candidates exist, otherwise 0.0
missing_evidence_count = 0 when candidates exist, otherwise 1
```

Store semantic-specific proof in `metadata_json`.

Required metadata:

```text
metadata_json.source_table = document_chunks
metadata_json.embedding_table = chunk_embeddings
metadata_json.retrieval_mode = semantic_persisted
metadata_json.preview_source = semantic_preview_runtime_smoke
metadata_json.candidate_chunk_ids
metadata_json.candidate_embedding_ids
metadata_json.missing_embedding_chunk_ids
metadata_json.embedding_model
metadata_json.embedding_dimension
metadata_json.query_vector_source = caller_provided_vector
metadata_json.ranking_boundary = exact_cosine_caller_provided_query_vector
metadata_json.persistence_boundary = semantic_retrieval_run_only_no_evidence_ledger
metadata_json.no_embedding_generation = true
metadata_json.no_evidence_ledger_generation = true
metadata_json.not_financial_advice = true
```

The response can reuse `RetrievalRunResponse` shape by mapping semantic candidates into retrieval candidates:

```text
source_id = chunk_id
source_type = chunk source_type
chunk_strategy = chunk_strategy
chunk_index = chunk_index
text = chunk_text
score = 1.0 - cosine_distance
matched_terms = []
metadata.chunk_id
metadata.embedding_id
metadata.distance
metadata.embedding_model
metadata.distance_metric
metadata.source_table = document_chunks
metadata.embedding_table = chunk_embeddings
```

## Why Not a New Table

Do not add a `semantic_retrieval_candidates` table in the next gate.

The existing project already uses `retrieval_runs.metadata_json.candidate_chunk_ids` as the bridge into the retrieval-run-linked Evidence Ledger, Noise Gate, and Report handoff.

Adding a second candidate table before that handoff is proven necessary would make the proof path harder to read.

## Required Failure Behavior

The next implementation should:

- reject query vector dimension mismatch with `400`
- return `no_results` when no `document_chunks` exist
- return `no_results` when no matching `chunk_embeddings` exist
- keep missing embedding chunk ids in metadata and warnings
- never create Evidence Ledger entries
- never call an embedding model
- never call an LLM
- never answer buy/sell or target-price questions

## Explicit Non-claims

This is not endpoint code.

This is not retrieval runtime evidence.

This is not embedding generation.

This is not HNSW or IVFFlat index behavior.

This is not vector search quality evidence.

This is not Evidence Ledger generation.

This is not Critic / Noise Gate behavior.

This is not final report generation.

This is not financial advice.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

Recommended next gate:

```text
semantic retrieval persistence endpoint v0
```

That gate should implement only `POST /documents/{document_id}/semantic-retrieval-runs`, persist a `retrieval_runs` row, and keep the preview endpoint unchanged.
