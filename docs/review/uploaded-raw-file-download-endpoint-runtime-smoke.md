# Guarded Raw File Download Endpoint Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: guarded raw file download endpoint runtime smoke v0.

## Purpose

Verify the guarded raw file download endpoint against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke checks that raw bytes are returned only when the latest scan result is `completed / clean`.

## Environment

```text
docker compose --profile api up -d --build api
GET /health -> 200
```

Migration runner:

```text
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
Applied migrations: 18
Pending migrations: 0
```

The run applied:

```text
019_uploaded_raw_file_guarded_download_boundary.sql
```

## Observed HTTP Flow

Health:

```text
health 200 {"status":"ok","service":"noiseproof-agent-api","workflow_version":"phase40-lineage-warning-code-dashboard"}
```

Upload:

```text
upload 201
persistence_boundary: raw_upload_quarantine_db_bytea_guarded_download_endpoint
filename: ../../sample.csv
storage_key: generated value without original filename path
raw_file_storage: true
raw_bytes not present in metadata response
```

Download before any scan result:

```text
download_no_scan 409
detail: latest clean scan result required before raw file download
```

Caller-provided clean scan metadata:

```text
clean_result 201
scanner_name: runtime-clean-metadata
scan_status: completed
scan_verdict: clean
```

Download after latest clean scan result:

```text
download_clean 200 True
X-Content-Type-Options: nosniff
X-NoiseProof-Download-Boundary: scan_first_latest_clean_result_required
X-NoiseProof-Authorization-Boundary: local_v0_no_auth_not_production
Content-Disposition: attachment; filename="sample.csv"
```

Later failed scan metadata:

```text
failed_result 201
scanner_name: runtime-failed-metadata
scan_status: failed
scan_verdict: scan_error
error_message: later runtime failure
```

Download after latest failed scan result:

```text
download_after_failed 409
detail: latest clean scan result required before raw file download
```

## What This Proves

The local HTTP route can:

```text
block downloads before scan evidence exists
return raw bytes after the latest scan result is completed / clean
block downloads again when a later scan_error result becomes latest
sanitize a path-like original filename into attachment filename="sample.csv"
keep metadata upload/list responses without raw_bytes
```

## Boundary

This is local runtime smoke evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not production authorization.

This is not enforced download rate limiting.

This is not file signature validation.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, autonomous workflow execution, and not product-complete.
