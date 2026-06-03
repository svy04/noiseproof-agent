# ClamAV API Endpoint Scanner Opt-in Implementation

Status: implemented

Phase marker: ClamAV API endpoint scanner opt-in implementation v0

## Goal

Add the smallest explicit scanner selection path that lets the raw-file scan endpoint use the existing clamd TCP adapter when the API runs inside the Docker Compose network.

## Implemented Code Boundary

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter
NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter
default remains NOISEPROOF_SCANNER=unavailable
CLAMD_HOST=clamav
CLAMD_PORT=3310
```

`Settings` now exposes:

```text
clamd_host: str = "clamav"
clamd_port: int = 3310
```

`get_scanner_adapter()` now preserves the existing `clamav` subprocess adapter and adds a separate `clamd` branch that constructs:

```text
ClamdScannerAdapter(host=settings.clamd_host, port=settings.clamd_port)
```

## Verification

Local targeted checks:

```text
uv run pytest tests/test_routes.py -q -k get_scanner_adapter_selects_clamd_only_for_explicit_opt_in
```

This unit test verifies:

- unavailable remains `ScannerUnavailableAdapter`
- `NOISEPROOF_SCANNER=clamav` still returns `ClamAvScannerAdapter`
- `NOISEPROOF_SCANNER=CLAMD` returns `ClamdScannerAdapter`
- `CLAMD_HOST=clamav`
- `CLAMD_PORT=3310`

## Boundary

This is scanner selection code and unit-test evidence only.

It is not endpoint runtime proof with real ClamAV.

It is not malware scanning evidence.

It is not:

- scanner default switch
- production malware scanning evidence
- file signature validation
- hosted deployment evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- product-complete claim

## Next Gate

ClamAV API endpoint scanner opt-in runtime smoke v0
