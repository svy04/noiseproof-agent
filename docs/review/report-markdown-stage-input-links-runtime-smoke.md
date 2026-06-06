# Report Markdown Stage Input Links Runtime Smoke

Status: implemented.

Phase marker: report markdown stage input links runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that persisted report markdown exports render the `Stage Input Links` section from stored report `stage_input_manifest` values.

This smoke verifies the read surface introduced by `docs/review/report-markdown-stage-input-links.md` against the runtime API and database path.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
compose_project=noiseproof-phase645
POSTGRES_PORT=55446
api_host=127.0.0.1
api_port=8044
db_container=noiseproof-phase645-db-1
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
POST /documents -> document_id=6aef4700-840e-4d91-9bc6-9f33678dde0f
POST /documents/{document_id}/chunks -> 3 chunks
POST /chunks/{chunk_id}/embeddings -> 2 caller-provided embeddings
POST /documents/{document_id}/semantic-retrieval-runs -> retrieval_run_id=59fb5a9f-f6f1-426e-8281-1b2605a8f152
missing_embedding_chunk_ids_count=1
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> stored_entry_count=2
POST /retrieval-runs/{retrieval_run_id}/noise-gate -> blocked
POST /retrieval-runs/{retrieval_run_id}/report -> blocked
GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK
content-type: text/markdown; charset=utf-8
```

## Observed IDs

```text
retrieval_run_id=59fb5a9f-f6f1-426e-8281-1b2605a8f152
evidence_entry_ids=9eb939b5-04d8-4073-a5ca-122b37ff232b,073b003a-61e1-45ac-b9df-ecbec7165b4b
noise_gate_record_id=00bea177-1892-4bc3-b36b-b158d8eefa18
report_record_id=1ca7666b-7622-4574-a22d-7838f72cc879
stage_input_retrieval_run_id=59fb5a9f-f6f1-426e-8281-1b2605a8f152
stage_input_noise_gate_record_id=00bea177-1892-4bc3-b36b-b158d8eefa18
```

## Markdown Checks

```text
markdown_http_200=True
markdown_content_type_text_markdown=True
markdown_contains_stage_input_links=True
markdown_contains_retrieval_run_id=True
markdown_contains_evidence_entry_id_count=2
markdown_contains_noise_gate_record_id=True
markdown_contains_source_provenance=True
markdown_contains_handoff_false=True
```

## Cleanup

```text
api_process_stopped=true
docker compose -p noiseproof-phase645 down -v
api_8044_down=true
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
