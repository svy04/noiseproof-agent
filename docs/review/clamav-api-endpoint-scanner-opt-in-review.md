# ClamAV API Endpoint Scanner Opt-in Review

Status: implemented

Phase marker: ClamAV API endpoint scanner opt-in review v0

Review type: review-only

## Goal

Select the smallest safe API change for using the existing clamd service adapter from the raw-file scan endpoint without changing the default scanner behavior.

## Current Code Boundary

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
current code: NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter
default remains NOISEPROOF_SCANNER=unavailable
scanner_not_configured
```

The current `clamav` setting uses the subprocess-style `ClamAvScannerAdapter`. That path is still useful for local machines with a `clamscan` binary, but it is not the right Compose-network integration path for the optional `clamav` service.

## Decision

Add a future explicit `clamd` scanner option rather than silently changing the meaning of `clamav`.

```text
next code gate: NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter
CLAMD_HOST=clamav
CLAMD_PORT=3310
```

The default must stay unavailable:

```text
default remains NOISEPROOF_SCANNER=unavailable
```

This keeps production-looking claims gated behind an explicit runtime setting.

## Why This Boundary

- It preserves the existing `clamav` subprocess adapter behavior.
- It lets the Docker Compose `api` service reach the internal `clamav` service by service name.
- It avoids publishing unauthenticated clamd TCP to the host.
- It keeps missing or disabled scanners as `scanner_not_configured` / `scan_error`, never `clean`.
- It creates a narrow next implementation target that can be unit-tested without needing real malware scanning evidence.

## Non-claims

This review adds no endpoint code and no runtime scan proof.

It is not endpoint runtime proof with real ClamAV.

It is not malware scanning evidence.

It is not:

- scanner default switch
- hosted deployment evidence
- file signature validation
- production malware scanning evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- product-complete claim

## Next Gate

ClamAV API endpoint scanner opt-in implementation v0
