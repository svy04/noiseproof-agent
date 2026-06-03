# External Review Issue Body Scan Execution Endpoint Refresh

Status: owner-authored issue edit only.

Phase marker: external review issue body scan execution endpoint refresh v0.

## Purpose

This gate updates the live public external review issue body so reviewers can reach the raw upload scan execution endpoint runtime smoke proof from issue #1.

It is request infrastructure only.

It does not add runtime behavior.

It does not count as external reviewer feedback.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after edit:

```json
{
  "updatedAt": "2026-06-03T03:42:56Z",
  "has_scan_execution_proof": true,
  "has_scan_execution_request_refresh": true,
  "starts_with_request": true,
  "first_codepoint": 35,
  "comment_count": 1
}
```

## Added Links

Scan execution endpoint runtime proof:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
```

Request refresh artifact:

```text
docs/review/external-reviewer-scan-execution-endpoint-request-refresh.md
```

## Added Boundary

The issue body now states that the scan execution endpoint runtime proof is:

```text
local Docker DB plus live FastAPI HTTP for POST /documents/upload-raw-files/{raw_file_id}/scan
default scanner-unavailable -> failed / scan_error
raw_bytes_key_leaked -> false
temporary_scan_path_key_leaked -> false
download_url_key_leaked -> false
real_clamav_runtime_verified -> false
malware_scanning_evidence -> false
not hosted deployment evidence
not external reviewer feedback
not real ClamAV execution
not signature database evidence
not malware scanning
not a download endpoint
```

## Boundary

This is an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not real ClamAV execution.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not malware scanning.

This is not a download endpoint.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Gate

```text
external feedback current-state scan execution endpoint issue verification v0
```
