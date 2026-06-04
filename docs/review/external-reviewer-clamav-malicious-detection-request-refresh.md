# External Reviewer ClamAV Malicious-detection Request Refresh

Status: implemented

Phase marker: external reviewer clamav malicious-detection request refresh v0

## Goal

Point external reviewers to the first local ClamAV API endpoint malicious-detection owner-runtime smoke without implying production malware scanning or external validation.

## Proof Linked

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
```

Reviewer-facing surfaces now link to the proof:

```text
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/braincrew-role-map.md
docs/application/portfolio-index.md
```

## Proof Markers

```text
harness_status: verified_infected
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw_payload_logged: false
```

## Boundary

```text
not live issue body edit
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
not product-complete
```

This refresh changes reviewer navigation only. It adds no runtime behavior, schema, migration, API endpoint, live issue body edit, external reviewer feedback, hosted deployment evidence, production malware scanning evidence, customer validation, Braincrew acceptance, or product-complete claim.

## Follow-up Issue-body Refresh

The live issue body refresh is recorded here:

```text
docs/review/external-review-issue-body-clamav-malicious-detection-refresh.md
```
