# Architecture Current-state ClamAV Proof Boundary Refresh

Phase marker: architecture current-state ClamAV proof boundary refresh v0.

## Why this exists

`docs/review/architecture-current-state-refresh.md` was correct when it was written: endpoint malicious-detection runtime proof was still unproven then.

Later, `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md` recorded local Docker FastAPI plus ClamAV endpoint evidence for owner-provided runtime input. Current-facing architecture and reviewer surfaces should now say that the local endpoint malicious-detection proof exists, while preserving the stronger boundaries that are still unproven.

## Current proof now recognized

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
harness_status: verified_infected
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw_payload_logged: false
```

Current-state wording:

```text
local endpoint malicious-detection proof exists
```

## Refreshed boundary

The architecture current-state should now separate:

- implemented local ClamAV endpoint malicious-detection owner-runtime proof
- still-unproven production malware scanning evidence
- still-unproven hosted deployment evidence
- still-unproven external reviewer feedback
- still-unproven production authorization and production observability

## Updated current-facing surfaces

This refresh updates:

- `docs/architecture.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reviewer-link-map.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/runbook.md`
- `docs/GOAL.md`

## Boundary

This is documentation/current-state alignment only.

It is not live issue body edit.

It is not production malware scanning evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It adds no runtime behavior, schema, migration, API endpoint, scanner behavior, malware signature payload, raw upload, hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, production malware scanning evidence, production authorization, autonomous/LLM-backed agents, polished web app, or product-complete claim.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
