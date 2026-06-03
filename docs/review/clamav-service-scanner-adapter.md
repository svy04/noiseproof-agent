# ClamAV Service Scanner Adapter

Status: implemented.

Phase marker: ClamAV service scanner adapter v0.

## Purpose

This gate adds `ClamdScannerAdapter`, a scanner adapter that speaks to clamd with the `INSTREAM` protocol.

It follows `docs/review/clamav-service-scanner-adapter-review.md`.

It does not connect the API endpoint to this adapter yet.

## Implemented

```text
packages/ingestion/scanning/clamd.py
packages/ingestion/scanning/__init__.py export
packages/ingestion/__init__.py export
unit tests for clean response
unit tests for infected FOUND response
unit tests for missing temporary path
unit tests for unavailable clamd service
unit tests for timeout
unit tests for unexpected response
```

The adapter:

```text
uses socket.create_connection
sends zINSTREAM
streams file bytes with clamd INSTREAM length-prefixed chunks
sends a zero-length terminating chunk
maps clean response to completed / clean
maps FOUND response to completed / infected
maps timeout -> failed / scan_error
maps clamd_unavailable -> failed / scan_error
maps clamd_unexpected_response -> failed / scan_error
does not include the raw temporary scan path in result metadata
```

## Boundary

This is adapter code plus fake-socket unit coverage.

This is not API endpoint integration.

This is not default scanner switch.

This is not endpoint runtime proof with real ClamAV.

This is not production malware scanning evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

The current host-local API process is not yet proven to share the internal Docker network with the `clamav` service. A later gate must decide how the API runtime reaches clamd without publishing unauthenticated clamd TCP to the host.

## Verification

```text
uv run pytest tests/test_raw_file_scanning.py -q -k clamd_adapter
```

Observed result:

```text
4 passed, 7 deselected
```

## Next Product Gate

```text
ClamAV API service network boundary review v0
```
