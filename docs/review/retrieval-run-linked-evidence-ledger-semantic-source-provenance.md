# Retrieval-run-linked Evidence Ledger Semantic Source Provenance

Status: implemented.

Phase marker: retrieval-run-linked Evidence Ledger semantic source provenance v0.

## Purpose

Preserve source retrieval provenance when a persisted semantic retrieval run is handed off into `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`.

The handoff already avoided LLM calls, embedding generation, and new semantic retrieval. This gate makes the source retrieval mode visible so a reviewer can distinguish:

- the source run was semantic and persisted
- the Evidence Ledger handoff performs no new semantic retrieval
- the Evidence Ledger entries are deterministic metadata records, not quality proof

## Implemented Surface

```text
POST /documents/{document_id}/semantic-retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
GET /agent-runs
```

## Added Provenance Fields

Evidence Ledger entry metadata now carries:

```text
source_retrieval_mode
source_query_vector_source
source_is_semantic_retrieval_run
source_retrieval_persistence_boundary
persistence_boundary
```

Agent run trace metadata now carries:

```text
source_retrieval_mode
source_query_vector_source
source_is_semantic_retrieval_run
source_retrieval_persistence_boundary
handoff_performs_semantic_retrieval
```

Expected values for the semantic source-run path:

```text
source_retrieval_mode -> semantic_persisted
source_query_vector_source -> caller_provided_vector
source_is_semantic_retrieval_run -> true
source_retrieval_persistence_boundary -> semantic_retrieval_run_only_no_evidence_ledger
persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
handoff_performs_semantic_retrieval -> false
```

## Regression Test

```text
tests/test_routes.py
test_semantic_retrieval_run_evidence_ledger_preserves_source_retrieval_provenance
```

The test creates a document with persisted chunks and caller-provided embeddings, runs `POST /documents/{document_id}/semantic-retrieval-runs`, then creates an Evidence Ledger through `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`.

It verifies the source retrieval provenance appears in:

```text
response warnings
stored Evidence Ledger entry metadata
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
GET /agent-runs trace_json
```

## Boundary

This is route-level source-provenance preservation.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not a live OpenAI provider call.

This is not Evidence Ledger quality evidence.

This is not final truth adjudication.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for retrieval-run-linked Evidence Ledger semantic source provenance if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
