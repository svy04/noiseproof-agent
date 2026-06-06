# Report Markdown Local Inspection Paths Runtime Smoke

Status: implemented.

Phase marker: report markdown local inspection paths runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that persisted report markdown exports render the `Local Inspection Paths` section from stored Report records.

This smoke verifies the read surface introduced by `docs/review/report-markdown-local-inspection-paths.md` against the runtime API and database path.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
compose_project=noiseproof-phase648
POSTGRES_PORT=55447
api_host=127.0.0.1
api_port=8045
db_container=noiseproof-phase648-db-1
db_health=healthy
pg_isready=accepting connections
```

## Migration State

```text
Applied migrations: 23
Pending migrations: 0
```

## Runtime Flow

```text
GET /health -> ok
POST /documents -> document_id=9413a77c-ebb6-4339-8af0-46332f9ae87c
POST /documents/{document_id}/chunks -> 3 chunks
POST /chunks/{chunk_id}/embeddings -> 2 caller-provided embeddings
POST /documents/{document_id}/semantic-retrieval-runs -> retrieval_run_id=cd347bea-cf43-42db-a653-8ffcae417026
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> stored_entry_count=2
POST /retrieval-runs/{retrieval_run_id}/noise-gate -> blocked
POST /retrieval-runs/{retrieval_run_id}/report -> blocked
GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK
content-type: text/markdown; charset=utf-8
GET /retrieval-runs -> latest_retrieval_mode=semantic_persisted
```

## Observed IDs

```text
retrieval_run_id=cd347bea-cf43-42db-a653-8ffcae417026
evidence_entry_ids=ed310565-1362-4100-b7e5-91d138d60e35,049992c5-1aa6-46b4-ab38-541aeb915f7b
noise_gate_record_id=aa58da63-5007-498b-a20a-f535409778a3
report_record_id=3437ed3a-3018-4cb0-ab65-8c73f8e70aae
report_workflow_trace_id=08a49fc0-66c4-4921-b604-2ad8af5785e9
latest_query_vector_source=caller_provided_vector
latest_is_semantic_retrieval_run=True
latest_persistence_boundary=semantic_retrieval_run_only_no_evidence_ledger
```

## Markdown Checks

```text
markdown_http_200=True
markdown_content_type_text_markdown=True
markdown_contains_local_inspection_paths=True
markdown_contains_current_report_markdown=True
markdown_contains_current_report_record_filter=True
markdown_contains_current_trace_path=True
markdown_contains_retrieval_runs_path=True
markdown_contains_evidence_ledgers_path=True
markdown_contains_noise_gates_path=True
markdown_contains_stage_input_links=True
markdown_contains_source_provenance=True
markdown_contains_handoff_false=True
```

## Cleanup

```text
api_process_stopped=true
docker compose -p noiseproof-phase648 down -v
api_8045_down=true
```

## Boundary

This is local runtime read-surface evidence only.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not new retrieval behavior.

It is not Evidence Ledger creation logic beyond the existing runtime path.

It is not Noise Gate creation logic beyond the existing runtime path.

It is not report generation logic beyond the existing runtime path.

It is not an LLM call.

It is not product-complete.

## Next Gate

```text
remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
