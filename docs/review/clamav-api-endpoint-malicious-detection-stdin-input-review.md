# ClamAV API Endpoint Malicious-detection Stdin Input Review

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection stdin input review v0

## Goal

Document why the next safe implementation step is a stdin-only owner input path before retrying the owner-provided malicious/test-signature runtime smoke.

## Current Boundary

The current next product gate remains:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

However, the owner-provided runtime smoke remains pending because no owner-provided test signature is present in the current environment.

The project should not create, encode, commit, print, or synthesize that input as a workaround.

## Decision

Add a stdin-only owner input path to the harness before attempting another runtime smoke.

Reason:

```text
stdin-only owner input path
keeps payload out of command arguments
keeps payload out of docs
keeps payload out of git
keeps payload out of CI configuration
keeps payload out of shell-history examples
```

The existing environment variable path remains available for owner-controlled runtime environments:

```text
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT remains supported
```

But documentation should prefer stdin for local manual proof attempts.

## Safety Rules

```text
do not use this review to supply a test signature
payload_committed_to_repo: false
raw_payload_logged: false
do not bypass OS security controls
not malware detection proof
```

If stdin input is not provided, the harness should continue to return:

```text
not_configured
```

## Non-claims

This is review-only.

It is not:

- malware detection proof
- EICAR-through-API proof
- production malware scanning evidence
- hosted deployment evidence
- external reviewer feedback
- customer validation
- product-complete claim

## Next Gate

ClamAV API endpoint malicious-detection stdin input harness v0
