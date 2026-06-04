# Uploaded Raw File Download Filename Safety Runtime Smoke v0

Phase marker: uploaded raw file download filename safety runtime smoke v0.

## Goal

Verify the local v0 guarded raw file download filename-safety boundary against the running Docker-backed FastAPI API.

This smoke checks only the `Content-Disposition` attachment filename behavior after the existing scan-first download guard allows a file to be returned.

## Runtime context

```text
Docker API rebuild command:
docker compose --profile api up -d --build api

Health:
GET /health -> 200
workflow_version -> phase40-lineage-warning-code-dashboard
```

Running containers:

```text
noiseproof-agent-api
noiseproof-agent-db
noiseproof-agent-clamav
```

This is local Docker runtime evidence only.

## Smoke input

Uploaded raw file:

```text
filename: ..\nested/%0d%0aInjected: yes/very-long-<180 a characters>.csv
content_type: text/csv
source_type: csv
content: ticker,revenue\nALPHA,120\n
```

Scan state:

```text
caller-provided manual clean scan metadata
scanner_name: manual-clean-filename-smoke
scan_status: completed
scan_verdict: clean
```

The scan row is metadata-only. This smoke does not prove malware detection.

## Observed output

```text
health 200 {'status': 'ok', 'service': 'noiseproof-agent-api', 'workflow_version': 'phase40-lineage-warning-code-dashboard'}
upload 201
raw_file_id 73b313a1-170b-41b8-b54b-889b923e5f5a
upload_boundary raw_upload_quarantine_db_bytea_guarded_download_endpoint raw_bytes_present False
scan_result 201 clean
download 200 True
filename_boundary local_v0_content_disposition_filename_safety_not_production
content_disposition attachment; filename="very-long-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.csv"
safe_filename very-long-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.csv
safe_filename_length 120
safe_checks {'no_path': True, 'no_dotdot': True, 'no_crlf': True, 'no_injected': True, 'ends_csv': True, 'lte_120': True}
```

## What this proves

The local Docker-backed API can:

```text
store a safe CSV raw upload in quarantine
avoid exposing raw_bytes in the upload metadata response
record caller-provided clean scan metadata
return the raw bytes only through the guarded download endpoint
expose X-NoiseProof-Download-Filename-Boundary
derive a 120-character safe attachment filename
remove path-shaped, CRLF-shaped, dotdot-shaped, and injected-label filename content from the attachment filename
preserve the .csv suffix after truncation
```

## What this does not prove

This is not production authorization.
It is not hosted deployment evidence.
It is not malware detection proof.
It is not product-complete evidence.

This is not:

```text
production authorization
distributed rate limiting
production malware scanning evidence
endpoint malicious-detection runtime proof
hosted deployment evidence
robust file serving
robust file-type detection
external reviewer feedback
customer validation
Braincrew acceptance
product-complete evidence
```

## Next recommended gate

```text
external reviewer filename-safety request refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
