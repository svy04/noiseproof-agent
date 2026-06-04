# Uploaded Raw File Extension Allowlist Runtime Smoke

Status: local Docker PostgreSQL plus live FastAPI HTTP smoke.

Phase marker: uploaded raw file extension allowlist runtime smoke v0.

## Purpose

This smoke verifies that the local raw upload extension allowlist runs in the live FastAPI service before raw upload persistence.

It checks one allowed CSV upload and one blocked double-extension upload.

It does not claim hosted deployment evidence.

It does not claim robust file-type detection or production upload security.

## Environment

The API was rebuilt and started with:

```powershell
docker compose --profile api up -d --build api
```

Migration status:

```text
Applied migrations: 18
Pending migrations: 0
```

Container state included:

```text
noiseproof-agent-api Up 0.0.0.0:8000->8000/tcp
noiseproof-agent-db Up healthy 0.0.0.0:55432->5432/tcp
noiseproof-agent-clamav Up healthy
```

Health check:

```text
health 200 {'status': 'ok', 'service': 'noiseproof-agent-api', 'workflow_version': 'phase40-lineage-warning-code-dashboard'}
```

## Smoke Command

The first smoke attempt used the `requests` module. That module was unavailable in the API uv environment, so the smoke was rerun with `httpx` without adding a dependency.

```text
requests module was unavailable
ModuleNotFoundError: No module named 'requests'
```

The successful smoke used `httpx` to submit live multipart requests to:

```text
POST http://localhost:8000/documents/upload-raw-files
GET http://localhost:8000/documents/upload-raw-files
```

## Observed Output

```text
health 200 {'status': 'ok', 'service': 'noiseproof-agent-api', 'workflow_version': 'phase40-lineage-warning-code-dashboard'}
allowed_csv_upload 201 8f3f74ef-3685-487e-bcc0-625e28d09999 extension_boundary_present True extension_allowed_present True raw_bytes_present False
double_extension_upload 415 suspicious double extension local_v0_extension_allowlist_not_production extension .csv raw_bytes_present False
double_extension_hash_persisted_recent 200 False
```

## Interpretation

Allowed case:

```text
filename: sample.csv
source_type: csv
status: 201
extension_boundary_present True
extension_allowed_present True
raw_bytes_present False
```

Blocked case:

```text
filename: sample.exe.csv
source_type: csv
status: 415
block_reason: suspicious double extension
extension_boundary: local_v0_extension_allowlist_not_production
client_filename_extension: .csv
raw_bytes_present False
```

Persistence check:

```text
double_extension_hash_persisted_recent 200 False
```

This means the blocked double-extension upload did not appear in the recent raw upload list by content hash.

## Boundary

This is local Docker runtime smoke only.

This is not hosted deployment evidence.

This is not robust file-type detection.

This is not malware scanning evidence.

This is not production authorization.

This is not external reviewer feedback.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external reviewer extension-allowlist request refresh v0
```
