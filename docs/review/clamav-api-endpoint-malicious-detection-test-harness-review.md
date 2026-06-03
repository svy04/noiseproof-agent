# ClamAV API Endpoint Malicious-detection Test Harness Review

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection test harness review v0

## Goal

Choose a safe future harness for proving the raw-file scan endpoint can surface a malicious/test-signature verdict through the API, without committing a test payload, bypassing local security controls, or turning a blocked runtime attempt into malware-detection evidence.

## Current Inputs

The current proof chain is intentionally split:

```text
clean-file endpoint proof exists
api_endpoint_verified_with_real_clamav: true
clean-file scan_verdict: clean
malicious_detection_verified: false
EICAR-through-API proof remains pending
payload_committed_to_repo: false
```

The previous malicious/test-signature runtime attempt was blocked before the endpoint request:

```text
runtime smoke not completed
host command was rejected before endpoint request
do not bypass OS security controls
```

## Selected Harness Shape

Use a review-first, opt-in harness before attempting another runtime smoke.

The future harness should be disabled by default and should require both:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
```

The input is an owner-provided runtime-only test signature. It must not be stored in git, test fixtures, docs, generated reports, shell history examples, or CI configuration.

```text
owner-provided runtime-only test signature
payload_committed_to_repo: false
```

## Harness Result States

The future harness should return one of these states:

| state | meaning |
|---|---|
| `not_configured` | Required opt-in variables were not provided. |
| `blocked_by_environment` | OS, endpoint, container, or scanner controls prevented the request or scan. |
| `verified_infected` | The endpoint returned an infected verdict from real ClamAV through the API boundary. |
| `unexpected_clean` | The endpoint completed but did not detect the test signature. |
| `scan_error` | The endpoint reached the scanner path but returned a scan error. |

`verified_infected only if` all of these are true:

```text
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw payload not printed
temporary input deleted or never written
```

## Safety Rules

```text
do not store the test signature payload or an encoded form in the repository
do not bypass OS security controls
do not publish unauthenticated clamd to the host
do not run the malicious/test-signature smoke in CI by default
do not print raw payload bytes in logs
do not call this production malware scanning evidence
```

If the host or security layer rejects the test-signature input again, the correct result is:

```text
blocked_by_environment
```

The correct next action is to record the block, not to bypass controls.

## Non-claims

This is review-only.

This artifact is not malware detection proof.

It is not:

- EICAR-through-API proof
- production malware scanning evidence
- hosted deployment evidence
- external reviewer feedback
- customer validation
- Braincrew acceptance
- product-complete claim

## Next Gate

ClamAV API endpoint malicious-detection test harness v0
