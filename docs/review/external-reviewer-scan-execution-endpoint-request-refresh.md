# External Reviewer Scan Execution Endpoint Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer scan execution endpoint request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the explicit raw upload scan execution endpoint runtime smoke proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Scan Execution Endpoint Runtime Proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md`

The proof is narrow:

```text
The local runtime smoke verifies Docker PostgreSQL plus live FastAPI HTTP for upload, explicit scan execution, and scan-result listing. The default scanner is scanner-unavailable, so the observed result is failed / scan_error. It reports real_clamav_runtime_verified -> false and malware_scanning_evidence -> false.
```

## Updated Request Surfaces

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Boundaries

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not malware scanning.

This is not real ClamAV execution.

This is not ClamAV installation evidence.

This is not ClamAV signature database evidence.

This is not a download endpoint.

This is not a live issue body edit.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Gate

The next bounded request gate can update or verify the live public issue body so issue #1 points reviewers to the scan execution endpoint runtime smoke proof:

```text
external review issue body scan execution endpoint refresh v0
```
