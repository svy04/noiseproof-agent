# Uploaded Raw File Download Rate Limit Runtime Smoke

Status: local Docker PostgreSQL plus live FastAPI HTTP evidence.

Phase marker: uploaded raw file download rate limit runtime smoke v0.

## Purpose

This gate verifies the local v0 guarded raw file download rate limit against the running Docker-backed API.

It checks the behavior implemented in:

```text
docs/review/uploaded-raw-file-download-rate-limit-local.md
```

## Environment

```text
docker compose --profile api up -d --build api
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
Applied migrations: 18
Pending migrations: 0
```

HTTP target:

```text
http://localhost:8000
```

## Observed HTTP Smoke

```text
health 200 {'status': 'ok', 'service': 'noiseproof-agent-api', 'workflow_version': 'phase40-lineage-warning-code-dashboard'}
upload_rate_file 201 74943645-cbff-4f7f-887a-60988bd8a26e raw_upload_quarantine_db_bytea_guarded_download_endpoint False
blocked_statuses [409, 409, 409, 409, 409]
limited 429 {'detail': 'raw file download rate limit exceeded'} local_v0_in_memory_fixed_window_not_production local_v0_no_auth_not_production False
clean_result 201 clean
clean_download 200 True local_v0_in_memory_fixed_window_not_production local_v0_no_auth_not_production nosniff attachment; filename="clean-download.csv"
```

## Verified Claims

The local smoke verifies:

```text
same raw_file_id no-scan download attempts return 409 for the first 5 attempts
6th same raw_file_id attempt returns 429
429 response includes local_v0_in_memory_fixed_window_not_production
429 response includes local_v0_no_auth_not_production
429 response does not include raw_bytes
separate clean raw file can still download successfully
clean download response includes local_v0_in_memory_fixed_window_not_production
clean download response includes local_v0_no_auth_not_production
clean download response includes nosniff
clean download uses a safe attachment filename
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

This is not hosted deployment evidence.

This is not distributed rate limiting.

This is not production authorization.

This is not user-level quota enforcement.

This is not bot detection.

This is not WAF integration.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external reviewer rate-limit request refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
