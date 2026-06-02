# Retrieval-run-linked Report Runtime Smoke

Phase marker: retrieval-run-linked Report runtime smoke v0.

## Scope

This is local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /retrieval-runs/{retrieval_run_id}/report
```

It is not hosted deployment evidence.

## Environment

Observed local database state:

```text
docker compose ps: healthy
Applied migrations: 13
Pending migrations: 0
```

FastAPI was started locally on:

```text
http://127.0.0.1:8033
```

## Live HTTP Sequence

Observed sequence:

```text
GET /health -> 200
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
POST /retrieval-runs/{retrieval_run_id}/report before gate -> 409
POST /retrieval-runs/{retrieval_run_id}/noise-gate -> 201
POST /retrieval-runs/{retrieval_run_id}/report after gate -> 201
GET /reports -> 200
```

Observed smoke payload:

```json
{
  "health_status": "ok",
  "document_id": "1444594a-554c-43dc-a305-06138eb426b5",
  "chunk_id": "a57c1179-eaa1-4b75-8b67-94368f6b71b8",
  "retrieval_run_id": "5f20334f-e296-4219-82e7-f55def6d0597",
  "ledger_entry_count": 1,
  "gate_id": "54bb168c-f90f-4de8-8bb3-d0d791313cca",
  "gate_decision": "needs_revision",
  "pre_report_status": 409,
  "report_status": "needs_revision",
  "report_gate_decision": "needs_revision",
  "report_evidence_entry_count": 1,
  "report_retrieval_run_id": "5f20334f-e296-4219-82e7-f55def6d0597",
  "report_input_noise_gate_record_id": "54bb168c-f90f-4de8-8bb3-d0d791313cca",
  "report_input_evidence_id": "a4198f15-8b40-4f97-97b8-69b0376efb8d",
  "listed_report_count": 17,
  "listed_first_retrieval_run_id": "5f20334f-e296-4219-82e7-f55def6d0597"
}
```

## Interpretation

The smoke confirms:

- the endpoint refuses to create a report record before a linked Noise Gate exists
- the report record keeps the same `retrieval_run_id` in `stage_input_manifest`
- the report record references the linked Noise Gate record id
- the report record references the linked Evidence Ledger row id

The observed report status was `needs_revision`, which is acceptable because the sample evidence is single-source and the gate did not allow an unrestricted final answer.

## Boundary

This smoke adds no hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, embeddings, semantic retrieval, LLM judgment, free-form final report generation, automatic failure-case creation, financial advice behavior, or product-complete claim.

