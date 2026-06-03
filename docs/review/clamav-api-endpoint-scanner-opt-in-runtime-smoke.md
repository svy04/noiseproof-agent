# ClamAV API Endpoint Scanner Opt-in Runtime Smoke

Status: implemented

Phase marker: ClamAV API endpoint scanner opt-in runtime smoke v0

## Goal

Verify that the raw-file scan endpoint can use the real Docker Compose `clamav` service through the explicit `NOISEPROOF_SCANNER=clamd` opt-in path.

## Runtime Setup Observed

```text
NOISEPROOF_SCANNER=clamd
CLAMD_HOST=clamav
CLAMD_PORT=3310
docker compose --profile api --profile scanner up -d --build api clamav
compose_up_api_clamd_exit=0
```

Container environment and health:

```text
NOISEPROOF_SCANNER=clamd
CLAMD_HOST=clamav
CLAMD_PORT=3310
GET /health -> 200
```

## Endpoint Smoke Observed

Input fixture:

```text
examples/messy-market-data/sample-market.csv
```

Upload:

```text
POST /documents/upload-raw-files -> 201
raw_file_id: 22d866d7-682c-4483-b7cb-496e66131c32
storage_backend: postgres_bytea
quarantine_status: stored_quarantined
```

Scan:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan -> 201
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: clean
matched_signature: null
clamd_host: clamav
clamd_port: 3310
clamd_command: INSTREAM
clamd_response: stream: OK
bytes_streamed: 232
temporary_scan_path_present: true
response_boundary: metadata_only_no_raw_bytes_no_download_url
api_endpoint_verified_with_real_clamav: true
malicious_detection_verified: false
```

## Boundary

This is clean-file endpoint runtime proof with real ClamAV over the Compose network.

It is not malware detection proof.

It is not EICAR-through-API proof.

It is not:

- production malware scanning evidence
- hosted deployment evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- file download behavior
- product-complete claim

## Next Gate

ClamAV API endpoint malicious-detection runtime review v0
