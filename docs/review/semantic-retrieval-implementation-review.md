# Semantic Retrieval Implementation Review

Phase marker: semantic retrieval implementation review v0.

Status: review-only.

## Purpose

Select the smallest safe semantic retrieval implementation boundary after the caller-provided chunk embedding endpoint runtime proof.

This review does not implement semantic retrieval. It chooses the next implementation gate and keeps embedding generation, vector index behavior, and answer quality claims out of scope.

## Primary Sources Checked

pgvector:

```text
https://github.com/pgvector/pgvector
```

Relevant observations:

- pgvector can store vectors in Postgres next to existing relational records.
- pgvector supports cosine distance through vector distance operators.
- pgvector supports exact nearest-neighbor ordering before approximate indexes are needed.
- HNSW and IVFFlat are index options, not required for the first small semantic retrieval proof.

Sentence Transformers semantic search:

```text
https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
```

Relevant observations:

- Semantic search compares a query embedding with corpus embeddings.
- NoiseProof can use this concept without adding model generation in the first semantic retrieval gate by requiring a caller-provided query vector.

PostgreSQL `pg_trgm`:

```text
https://www.postgresql.org/docs/current/static/pgtrgm.html
```

Relevant observations:

- `pg_trgm` remains useful as a lexical similarity baseline.
- `pg_trgm` is not semantic retrieval and should not be used to claim vector search quality.

## Current State

NoiseProof already has:

```text
document_chunks
chunk_embeddings
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
retrieval_runs.metadata_json.candidate_chunk_ids
retrieval-run-linked Evidence Ledger / Noise Gate / Report handoff
```

The embedding endpoint accepts caller-provided vectors only and records:

```text
caller_provided_embedding_only_no_generation
```

## Decision

The next implementation should be:

```text
next product gate: semantic retrieval preview endpoint v0
```

The selected boundary is:

```text
POST /documents/{document_id}/semantic-retrieval-preview
```

Input should include:

```text
question
query_embedding
embedding_model
embedding_dimension
limit
```

The implementation should use:

```text
document_chunks
chunk_embeddings
chunk_embeddings.embedding <=> query_embedding
exact cosine ranking first
```

The response should include candidate chunks and a comparison boundary against the current lexical retrieval path, but it should not persist a `retrieval_runs` row in the first preview gate.

Only after preview behavior is inspected should a later persistence gate write semantic retrieval candidates into:

```text
retrieval_runs.metadata_json.candidate_chunk_ids
```

## Why Preview Before Persistence

Semantic retrieval can look impressive while silently producing weak or misleading candidates.

Before it becomes part of the Evidence Ledger handoff, NoiseProof needs a visible preview that shows:

- which chunks were selected
- which embedding rows were used
- which chunks were missing embeddings
- whether the query vector dimension matched stored embeddings
- whether lexical and semantic candidates disagree
- whether source recency and citation metadata are still visible

## Selected Query Boundary

Use caller-provided query vector first.

This keeps the next gate inspectable because it avoids:

- embedding model installation
- hosted embedding API calls
- LLM calls
- hidden model-version drift
- semantic quality claims before comparison data exists

## Initial Ranking Rule

Use exact cosine ranking first.

Do not add a vector index until the repo has enough persisted embeddings and runtime evidence to justify index behavior.

Search marker:

```text
exact cosine ranking first
```

## Explicit Non-claims

This is no embedding generation.

This is no HNSW or IVFFlat index.

This is no vector search quality claim.

This is no persisted semantic retrieval run.

This is no Evidence Ledger generation.

This is no LLM calls.

This is no hosted deployment evidence.

This is no external reviewer feedback.

This is no Braincrew acceptance.

This is not product-complete.

## Boundary

This review adds no runtime behavior, route code, repository code, schema, migration, model dependency, embedding generator, HNSW index, IVFFlat index, Evidence Ledger generation, Noise Gate generation, report generation, dashboard behavior, hosted deployment evidence, or external reviewer feedback.
