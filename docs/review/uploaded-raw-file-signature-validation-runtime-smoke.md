# Uploaded Raw File Signature Validation Runtime Smoke

Status: local Docker PostgreSQL plus live FastAPI HTTP proof.

Phase marker: uploaded raw file signature validation runtime smoke v0.

## Purpose

Verify that the local v0 raw file signature validation behavior works against a live FastAPI API container and local Docker PostgreSQL.

This smoke checks that `POST /documents/upload-raw-files`:

```text
accepts CSV bytes even when Content-Type is spoofed as application/pdf
blocks declared PDF bytes that do not start with %PDF-
does not return raw bytes in the blocked error detail
does not persist the blocked mismatch payload
```

## Environment

Compose command:

```text
docker compose --profile api up -d --build api
```

Migration status:

```text
Applied migrations: 18
Pending migrations: 0
```

## Smoke Output

```text
health 200 {'status': 'ok', 'service': 'noiseproof-agent-api', 'workflow_version': 'phase40-lineage-warning-code-dashboard'}
spoofed_csv_upload 201 b4c1895c-9747-4d83-add6-98fee5074271 csv application/pdf True True False
declared_pdf_mismatch 415 file signature mismatch csv local_v0_magic_prefix_allowlist_not_production raw_bytes_present False
mismatch_hash_persisted_recent 200 False
```

## Interpreted Checks

Spoofed CSV upload:

```text
status: 201
source_type: csv
declared_content_type: application/pdf
detected_signature_type: csv
signature_boundary: local_v0_magic_prefix_allowlist_not_production
response_has_raw_bytes: false
```

Declared PDF mismatch:

```text
status: 415
block_reason: file signature mismatch
detected_signature_type: csv
signature_boundary: local_v0_magic_prefix_allowlist_not_production
raw_bytes_present: False
mismatch_hash_persisted_recent: False
```

## What This Proves

The live local API applies the local v0 signature check before raw upload persistence.

The live local API does not trust `Content-Type` as proof of file type.

The live local API can block a declared PDF when the prefix is not PDF-like.

The live local API does not expose raw bytes in the blocked response.

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

This is not robust file-type detection.

This is not a full allowlist policy.

This is not malware scanning evidence.

This is not production authorization.

This is not production file upload security.

This is not hosted deployment evidence.

This is not endpoint malicious-detection runtime proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external reviewer signature-validation request refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
