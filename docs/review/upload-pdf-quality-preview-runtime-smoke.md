# Upload PDF Quality Preview Runtime Smoke

Phase marker: upload PDF quality preview runtime smoke v0.

Status: verified.

Purpose: record local Docker PostgreSQL plus live FastAPI HTTP evidence that `POST /documents/upload-pdf-quality-preview` preserves the preview-only PDF quality boundary for born-digital and encrypted PDF uploads.

Runtime environment:

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase715
POSTGRES_PORT=55453
DATABASE_URL=postgresql://noiseproof:noiseproof@127.0.0.1:55453/noiseproof
FastAPI URL: http://127.0.0.1:8114
```

Database preparation:

```text
docker compose -p noiseproof-phase715 up -d db
db_health=healthy
uv run python -m app.migration_runner --status
Applied migrations: 0
Pending migrations: 23
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
Applied migrations: 23
Pending migrations: 0
```

HTTP smoke:

```text
GET /health -> 200
health_body={"service": "noiseproof-agent-api", "status": "ok", "workflow_version": "phase40-lineage-warning-code-dashboard"}
documents_before=0
phase715-born-digital.pdf_status=200
phase715-encrypted.pdf_status=200
documents_after=0
document_count_delta=0
digital_quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim
digital_persistence_boundary=preview_only_not_persisted
digital_text_extraction=True
digital_robust_pdf_extraction=False
digital_failure_case_candidate=None
encrypted_quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim
encrypted_persistence_boundary=preview_only_not_persisted
encrypted_encrypted=True
encrypted_password_required=True
encrypted_robust_pdf_extraction=False
encrypted_failure_type=pdf_encrypted_requires_password
quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim
persistence_boundary=preview_only_not_persisted
```

Cleanup:

```text
stopping_pid=84436
docker compose -p noiseproof-phase715 down
docker compose -p noiseproof-phase715 ps -> no running services
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not document persistence evidence for this preview route.

This is not retrieval behavior.

This is not Evidence Ledger generation.

This is not decryption evidence.

This is not robust PDF extraction evidence.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not product-complete.

Next recommended gate: remote verification for this runtime-smoke documentation after push, or another source-first product gate selected from current repository state.
