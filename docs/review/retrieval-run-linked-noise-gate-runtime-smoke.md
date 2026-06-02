# Retrieval-run-linked Noise Gate Runtime Smoke

Phase marker: retrieval-run-linked Noise Gate runtime smoke v0.

## Scope

This is local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /retrieval-runs/{retrieval_run_id}/noise-gate
```

It is not hosted deployment evidence.

## Environment

Observed local database state:

```text
docker compose config: passed
docker compose up -d db: db running
docker compose ps: healthy
Applied migrations: 13
Pending migrations: 0
```

FastAPI was started locally on:

```text
http://127.0.0.1:8032
```

## Live HTTP Sequence

Observed sequence:

```text
GET /health -> 200
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/noise-gate before ledger -> 409
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
POST /retrieval-runs/{retrieval_run_id}/noise-gate after ledger -> 201
GET /noise-gates -> 200
```

Observed smoke payload:

```json
{
  "health_status": "ok",
  "document_id": "11def8dc-0406-478a-8c7b-3f7914648952",
  "chunk_id": "2506f74c-55b2-49f4-a18f-d7b9740baee8",
  "retrieval_run_id": "34f42cec-62ba-4a95-9a55-b60d89078e35",
  "pre_gate_status": 409,
  "ledger_entry_count": 1,
  "ledger_retrieval_run_id": "34f42cec-62ba-4a95-9a55-b60d89078e35",
  "gate_decision": "needs_revision",
  "gate_evidence_entry_count": 1,
  "gate_retrieval_run_id": "34f42cec-62ba-4a95-9a55-b60d89078e35",
  "gate_input_evidence_id": "fc6bbfa8-ffb4-408b-a3e6-650413f56eff",
  "listed_gate_count": 14,
  "listed_first_retrieval_run_id": "34f42cec-62ba-4a95-9a55-b60d89078e35"
}
```

## Interpretation

The smoke confirms:

- the endpoint refuses to create a gate record before linked Evidence Ledger rows exist
- the Evidence Ledger row keeps the same `retrieval_run_id`
- the Noise Gate record keeps the same `retrieval_run_id` in `stage_input_manifest`
- the Noise Gate record references the linked Evidence Ledger row id in `input_evidence_ledger_entry_ids`

The observed decision was `needs_revision`, which is acceptable because the sample evidence is single-source and remains bounded.

## Boundary

This smoke adds no hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, embeddings, semantic retrieval, LLM judgment, report generation, automatic failure-case creation, financial advice behavior, or product-complete claim.

