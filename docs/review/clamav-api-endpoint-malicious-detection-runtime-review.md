# ClamAV API Endpoint Malicious-detection Runtime Review

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection runtime review v0

Review type: review-only

## Goal

Decide the next safe proof gate for malicious/test-signature detection through the raw-file scan endpoint after clean-file endpoint proof succeeded.

## Current Accepted Evidence

```text
clean-file endpoint proof exists
POST /documents/upload-raw-files/{raw_file_id}/scan -> 201
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: clean
clamd_response: stream: OK
api_endpoint_verified_with_real_clamav: true
malicious_detection_verified: false
```

EICAR-through-API proof is still pending.

## Safety Boundary

The next malicious-detection proof must use the EICAR test signature carefully:

- do not store the EICAR payload in the repository
- do not commit an encoded EICAR payload either
- do not bypass OS security controls
- do not claim production malware scanning evidence from a test signature
- delete any temporary test input after the smoke
- record only the detection result and matched signature, not the full payload

## Recommended Next Gate

Use a narrow runtime smoke that proves only this:

```text
NOISEPROOF_SCANNER=clamd
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/{raw_file_id}/scan -> 201
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
temporary_input_deleted: true
payload_committed_to_repo: false
```

## Non-claims

This review is not malware detection proof.

It is not:

- endpoint malicious-detection runtime proof
- production malware scanning evidence
- hosted deployment evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- product-complete claim

## Next Gate

ClamAV API endpoint malicious-detection runtime smoke v0
