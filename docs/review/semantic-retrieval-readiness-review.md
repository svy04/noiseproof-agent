# Semantic Retrieval Readiness Review

Status: source-first review.

Phase marker: semantic retrieval readiness review v0.

This review decides the smallest safe path toward semantic retrieval without implementing embeddings in this gate.

## Primary Sources Checked

pgvector:

```text
https://github.com/pgvector/pgvector
```

Relevant observations:

- pgvector stores vectors inside Postgres with the rest of the data.
- pgvector supports exact and approximate nearest neighbor search.
- pgvector supports cosine distance.
- pgvector supports HNSW and IVFFlat indexes.

Sentence Transformers:

```text
https://sbert.net/docs/quickstart.html
```

Relevant observations:

- Sentence Transformers exposes `SentenceTransformer.encode` for producing embeddings from text.
- It can provide a local embedding path before any hosted LLM or external embedding API is introduced.

PostgreSQL `pg_trgm`:

```text
https://www.postgresql.org/docs/current/static/pgtrgm.html
```

Relevant observations:

- `pg_trgm` supports trigram-based text similarity inside Postgres.
- It is a useful lexical/similarity fallback and comparison baseline, but it is not semantic retrieval.

## Current State

NoiseProof currently has lexical retrieval over persisted `document_chunks`.

The current linked proof chain is:

```text
document_chunks
retrieval_runs.metadata_json.candidate_chunk_ids
retrieval-run-linked Evidence Ledger rows
retrieval-run-linked Noise Gate records
retrieval-run-linked Report records
```

## Decision

Do not implement embeddings in this gate.

Search marker: do not implement embeddings in this gate.

Do not jump directly to HNSW, IVFFlat, or hybrid ranking before the data model boundary is explicit.

The selected next product gate is:

```text
next product gate: embedding schema review v0
```

That review should decide:

- whether embeddings live directly on `document_chunks`
- whether embeddings live in a separate `chunk_embeddings` table
- which dimension is selected for the first local embedding model
- how to record `embedding_model`, `embedding_dimension`, and `embedding_created_at`
- whether semantic retrieval is compared against lexical retrieval before replacing it

## Candidate Implementation Shape

Likely smallest implementation path after schema review:

```text
document_chunks
  -> chunk_embeddings
  -> semantic retrieval preview
  -> lexical vs semantic comparison
  -> retrieval_runs with retrieval_mode metadata
```

## Explicit Non-claims

This is not semantic retrieval implementation.

This is not embeddings.

This is not vector index creation.

This is not HNSW or IVFFlat runtime evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not financial advice.

This is not product-complete.

## Boundary

This review only selects the next safe planning gate.

It adds no runtime behavior, schema, migration, endpoint, embedding model dependency, vector column, vector index, external API call, LLM call, semantic retrieval, report-generation behavior, or dashboard behavior.
