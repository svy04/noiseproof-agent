# Uploaded Raw File Download Rate Limit Local

Status: local API behavior only.

Phase marker: uploaded raw file download rate limit local v0.

## Purpose

This gate implements the smallest local v0 download rate-limit boundary selected in:

```text
docs/review/uploaded-raw-file-download-rate-limit-review.md
```

The goal is to stop repeated guarded raw file download attempts from being unlimited in the local service while keeping the production boundary visible.

## Implemented Behavior

Endpoint:

```text
GET /documents/upload-raw-files/{raw_file_id}/download
```

New local v0 behavior:

```text
per-process in-memory fixed window
keyed by raw_file_id and client host
5 attempts per 60 seconds
blocked no-scan attempts count toward the local limit
successful clean-download attempts count toward the local limit
limit is scoped by raw_file_id/client-host key
exceeded attempts return HTTP 429
429 response contains no raw bytes
```

Exceeded response:

```json
{
  "detail": "raw file download rate limit exceeded"
}
```

Rate-limit boundary header:

```text
X-NoiseProof-Download-Rate-Limit-Boundary: local_v0_in_memory_fixed_window_not_production
```

Authorization boundary remains:

```text
X-NoiseProof-Authorization-Boundary: local_v0_no_auth_not_production
```

## Code Paths

```text
apps/api/app/routes/documents.py
apps/api/tests/test_routes.py
```

Implementation symbols:

```text
DOWNLOAD_RATE_LIMIT_ATTEMPTS
DOWNLOAD_RATE_LIMIT_WINDOW_SECONDS
DOWNLOAD_RATE_LIMIT_BOUNDARY
_download_attempt_windows
_consume_download_attempt
```

## Test Evidence

Focused tests:

```powershell
uv run pytest -q tests/test_routes.py -k "raw_file_download"
```

Observed:

```text
3 passed, 120 deselected, 1 warning
```

The new regression test verifies:

```text
5 same-file blocked attempts return 409
6th same-file attempt returns 429
429 body contains no raw_bytes
429 response includes local_v0_in_memory_fixed_window_not_production
authorization boundary remains local_v0_no_auth_not_production
different raw_file_id is not limited by the first file's attempts
```

## Source-first Basis

Primary source:

```text
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
```

This implementation follows the review decision to add request limiting around file download handling without pretending to solve production authorization.

## Boundary

This is local API behavior only.

This is an in-memory per-process fixed-window limit.

This is not distributed rate limiting.

This is not production authorization.

This is not user-level quota enforcement.

This is not bot detection.

This is not WAF integration.

This is not hosted deployment evidence.

This is not production malware scanning evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file download rate limit runtime smoke v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
