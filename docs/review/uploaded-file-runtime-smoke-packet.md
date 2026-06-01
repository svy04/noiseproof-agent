# Uploaded File Runtime Smoke Packet

Phase marker: uploaded file runtime smoke packet v0.

## Purpose

This packet records a local runtime smoke for the uploaded-file proof path through a live FastAPI server and Docker PostgreSQL database.

It exists to show that the upload preview chain can be exercised over HTTP, and that the final failure-case draft still requires a manual handoff before persistence.

## Runtime context

Date: 2026-06-01

Local-only runtime:

- Docker DB service: `noiseproof-agent-db`
- PostgreSQL image: `pgvector/pgvector:pg16`
- DB port: `55432 -> 5432`
- FastAPI URL: `http://127.0.0.1:8030`
- Uploaded fixture: `examples/messy-market-data/sample-note.md`
- Question: `Which source supports enterprise demand growth?`

Commands used:

```powershell
docker compose up -d db
docker compose ps
cd apps/api
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8030
```

Migration runner status before HTTP smoke:

```text
Applied migrations: 10
Pending migrations: 0
```

## HTTP smoke path

The smoke path called these endpoints against the local server:

1. `GET /health`
2. `POST /documents/upload-preview`
3. `POST /documents/upload-chunk-preview`
4. `POST /documents/upload-retrieval-preview`
5. `POST /documents/upload-evidence-preview`
6. `POST /documents/upload-noise-gate-preview`
7. `POST /documents/upload-report-preview`
8. `POST /documents/upload-failure-case-draft-preview`
9. `POST /failure-cases`
10. `GET /failure-cases`

Representative upload command shape:

```powershell
curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-report-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Manual failure-case handoff shape:

```powershell
$draft = $draftResponse.Body.draft_preview.draft
$manualBody = $draft | ConvertTo-Json -Depth 12
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8030/failure-cases" -ContentType "application/json" -Body $manualBody
```

## Observed results

```text
GET /health -> 200
health.status -> ok
health.workflow_version -> phase40-lineage-warning-code-dashboard

POST /documents/upload-preview -> 200
upload.source_type -> markdown
upload.persistence_boundary -> preview_only_not_persisted

POST /documents/upload-chunk-preview -> 200
fixed-window chunk_count -> 4
heading-aware chunk_count -> 4
row-aware chunk_count -> 10

POST /documents/upload-retrieval-preview -> 200
retrieval.status -> completed
retrieval.result_count -> 3

POST /documents/upload-evidence-preview -> 200
evidence.summary.supported_count -> 0
evidence.summary.weakly_supported_count -> 2
evidence.summary.contradicted_count -> 1

POST /documents/upload-noise-gate-preview -> 200
gate.decision -> needs_revision

POST /documents/upload-report-preview -> 200
report.status -> needs_revision

POST /documents/upload-failure-case-draft-preview -> 200
draft_preview.human_confirmation_required -> true
draft_preview.draft.fix_status -> draft

POST /failure-cases -> 201
manual_failure_case_id -> 27621108-6ce2-468e-a003-37b7e81b53d3
manual_failure_case_fix_status -> draft

GET /failure-cases -> 200
listed_failure_cases_after_manual_handoff -> 2
```

The local DB was not reset before the smoke. The listed failure-case count therefore includes pre-existing local records plus the newly persisted manual handoff record above.

## What this proves

This proves that, in a local Docker DB plus live FastAPI server path, an uploaded markdown file can move through:

```text
upload preview
-> chunk preview
-> lexical retrieval preview
-> Evidence Ledger preview
-> Noise Gate preview
-> report preview
-> failure-case draft preview
-> manual failure-case persistence
```

The observed evidence is intentionally not overstated. The sample question produced weak support and contradiction signals, so the gate and report stayed in `needs_revision` rather than pretending to be final.

## What this does not prove

This packet is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance, production readiness, robust PDF extraction, persisted file upload parsing, semantic retrieval, embeddings, LLM output, automatic failure-case creation, automatic failure detection, root-cause automation, or complete workflow failure causality.

It is not automatic failure-case creation.

The failure case was persisted only through explicit manual submission to `POST /failure-cases`.

## Next gate

The next useful product gate should review whether uploaded files should remain preview-only or receive a persisted intake boundary.

```text
persisted uploaded file intake review v0
```

That gate should be a review first. It should not add file storage, retrieval persistence, or automatic failure-case creation without a narrow reason.
