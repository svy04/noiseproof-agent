# Raw File Download Operator-token Guard

Status: accepted.

Phase marker: raw file download operator-token guard v0.

## Purpose

Add a small opt-in local guard before raw uploaded bytes can be downloaded.

If `NOISEPROOF_RAW_FILE_DOWNLOAD_OPERATOR_TOKEN` is configured, `GET /documents/upload-raw-files/{raw_file_id}/download` requires this header before the scan, approval, and rate-limit gates run:

```text
X-NoiseProof-Operator-Token
```

## Implemented Surface

```text
Settings.raw_file_download_operator_token
NOISEPROOF_RAW_FILE_DOWNLOAD_OPERATOR_TOKEN
X-NoiseProof-Operator-Token
GET /documents/upload-raw-files/{raw_file_id}/download
raw_file_download_events
```

When the token is missing or invalid, the endpoint returns:

```text
403
operator token required before raw file download
```

It records a blocked download event with:

```text
blocked_reason = operator_token_missing_or_invalid
authorization_boundary = local_v0_operator_token_header_not_production
```

## Boundary

This is a local v0 operator-token guard.

It is not production authorization.

It is not authenticated user identity.

It is not role-based access control.

It is not session auth.

It is not OAuth, OIDC, signed URL support, or tenant isolation.

It does not replace scan-first gating, active download approval, rate limiting, audit events, storage controls, or hosted deployment hardening.

Default local behavior stays unchanged when the token is not configured.

## Allowed Claim

NoiseProof can optionally require a configured local operator token before raw-file download attempts proceed to scan, approval, and rate-limit gates.

## Non-claims

This is not production auth.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production malware scanning evidence.

This is not product-complete.

## Test Evidence

Targeted route test:

```text
tests/test_routes.py::test_document_upload_raw_file_download_requires_configured_operator_token_before_scan_gate
```

Targeted docs test:

```text
tests/test_docs.py::test_raw_file_download_operator_token_guard_documents_opt_in_boundary
```

Focused regression check:

```text
uv run pytest -q tests/test_routes.py -k "raw_file_download or download_readiness or download_approval"
```

Full verification should still run before completion:

```text
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
```
