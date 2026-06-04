# Uploaded Raw File Download Authorization Audit Review

Status: source-first review only.

Phase marker: uploaded raw file download authorization audit review v0.

## Purpose

The guarded raw file download path is now scan-first, locally rate-limited, and filename-safe for attachment headers.

The repeated remaining boundary is authorization:

```text
local_v0_no_auth_not_production
```

This review decides the next smallest product gate before pretending to solve production authorization.

## Primary Sources

- OWASP File Upload Cheat Sheet: uploaded files should be accessed through application controls, only authorized users should use upload services, read access needs proper controls, and download services need request limits.
- OWASP Authorization Cheat Sheet: permissions should be validated on every request for the specific object or functionality; authorization failures should exit safely and be logged.
- OWASP Logging Cheat Sheet: application logging should be included for security events, audit trails can reconstruct actions, and logs should avoid sensitive values while still supporting security and operations.
- OWASP Logging Vocabulary Cheat Sheet: event records should have consistent event names and enough structured context to support investigation, while privacy-sensitive fields should be treated carefully.

Source URLs:

```text
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html
```

## Local Repository Evidence

Current guarded download route:

```text
GET /documents/upload-raw-files/{raw_file_id}/download
```

Current local boundaries:

```text
scan-first download: implemented
latest clean scan result: required
local fixed-window rate limit: implemented
attachment filename safety: implemented
authorization_boundary: local_v0_no_auth_not_production
```

Current gap:

```text
The route can explain why a request was allowed or blocked through response status and headers, but it does not persist an audit trail for allowed/blocked download decisions.
```

## Decision

Do not add a fake production authorization system yet.

Do not claim user identity, tenant isolation, RBAC, ABAC, signed URLs, session enforcement, or production authorization.

Next gate should be a small persistence boundary:

```text
raw_file_download_events
```

The event table should record the local v0 download decision for each guarded raw file download attempt.

Planned fields:

```text
id
raw_file_id
latest_scan_result_id
download_result
blocked_reason
http_status_code
authorization_boundary
rate_limit_boundary
filename_boundary
client_host_boundary
created_at
metadata_json
```

Suggested values:

```text
download_result: allowed | blocked
blocked_reason: missing_clean_scan | latest_scan_not_clean | quarantine_status_blocked | rate_limited | raw_file_missing
authorization_boundary: local_v0_no_auth_not_production
rate_limit_boundary: local_v0_in_memory_fixed_window_not_distributed
filename_boundary: local_v0_content_disposition_filename_safety_not_production
client_host_boundary: local_request_client_host_not_identity
```

## Why Audit Before Production Auth

NoiseProof is still a local portfolio artifact.

Adding real identity or tenant authorization without a real deployment, user model, session boundary, or threat model would create false confidence.

Persisting download decision events is smaller and more inspectable:

```text
request -> scan check -> rate-limit check -> download decision -> audit event
```

It lets a reviewer see whether the system can explain:

```text
who/what boundary was used
which raw file was requested
which scan result was considered latest
whether the response was allowed or blocked
why it was blocked
which local v0 boundaries were active
```

## Non-goals

This review adds no endpoint code.

This is not endpoint code.

This review adds no schema.

This is not schema.

This review adds no migration.

This review adds no API response behavior.

This review adds no hosted deployment evidence.

This is not hosted deployment evidence.

This review adds no production authorization.

This is not production authorization.

This review adds no user identity.

This is not user identity.

This review adds no RBAC, ABAC, tenant isolation, sessions, JWT verification, OAuth, signed URL, or cloud IAM integration.

This review adds no malware detection proof.

This review adds no external reviewer feedback.

This is not customer validation, Braincrew acceptance, production readiness, robust file serving, robust file-type detection, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Acceptance For Next Gate

The next implementation gate should be accepted only if:

```text
db migration exists for raw_file_download_events
init schema includes raw_file_download_events
repository can create and list download events
guarded download route records allowed and blocked attempts
tests cover missing scan, rate-limited, and allowed download events
README and runbook still say production authorization is not implemented
```

## Next Gate

```text
uploaded raw file download audit schema v0
```
