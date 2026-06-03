# External Review Request

Status: external review request packet.

Phase marker: external review request packet v0.

Label: External review request packet.

This artifact prepares the next evidence gate without claiming that the gate is complete.

The current next gate is:

```text
external reviewer feedback v0
```

This page exists so an outside reviewer can inspect the current bounded proof path and leave critique in a structured form.

Shortest reviewer brief:

```text
docs/review/external-reviewer-brief.md
```

Copy-paste outreach packet:

```text
docs/review/external-reviewer-outreach-packet.md
```

Direct reviewer link map:

```text
docs/review/external-reviewer-link-map.md
```

Root review guide:

```text
CONTRIBUTING.md
docs/review/external-review-root-guide.md
```

Live issue body verification:

```text
docs/review/external-review-issue-body-encoding-verification.md
docs/review/external-review-issue-body-root-guide-verification.md
docs/review/external-review-issue-body-link-map-verification.md
```

Issue template link-map refresh:

```text
docs/review/external-review-issue-template-link-map-refresh.md
```

Issue label verification:

```text
docs/review/external-review-issue-label-verification.md
```

uploaded-file intake manifest proof:

```text
docs/review/uploaded-file-intake-manifest-preview.md
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-application-refresh.md
```

Boundary: this proof is not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file intake manifest persistence proof:

```text
docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md
```

Boundary: this proof is manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file parsed document persistence proof:

```text
docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
docs/review/uploaded-file-parsed-document-persistence-application-refresh.md
```

Boundary: this proof is document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk persistence proof:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
docs/review/uploaded-file-chunk-persistence-application-refresh.md
```

Boundary: this proof is not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk handoff proof:

```text
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/upload-chunks`, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file retrieval persistence proof:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.

retrieval-run-linked Report proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

Boundary: this proof is explicit `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, and `POST /retrieval-runs/{retrieval_run_id}/report`; the report handoff records `pre_report_status: 409` and `input_noise_gate_record_id`, but it is not hosted deployment evidence, not external reviewer feedback, not LLM judgment, not embeddings, not semantic retrieval, not free-form final report generation, and not financial advice.

toy semantic retrieval quality report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
docs/review/semantic-retrieval-quality-report-application-refresh.md
```

Boundary: this report is toy fixture metric output with `q-what-missing` kept visible. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

uploaded raw file storage proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
docs/review/uploaded-raw-file-storage-application-refresh.md
```

Boundary: this proof is explicit `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage. It is not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

uploaded raw file scan result endpoint proof:

```text
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, preserves `scan_verdict -> scan_error`, records `response_has_raw_bytes -> false`, and remains not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

## Review Path

Please read in this order:

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/application/portfolio-index.md`
4. `docs/review/local-browser-screenshot-walkthrough.md`
5. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
6. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
7. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
8. `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
9. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
10. `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
11. `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
12. `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
13. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
14. `docs/evaluation/semantic-retrieval-quality-report.md`
15. `docs/application/braincrew-role-map.md`

Optional source-level provenance:

```text
docs/review/readme-proof-marker-archive.md
```

## Reviewer Questions

Please answer any of these with direct references to the artifacts you inspected:

```text
What would make this portfolio stronger?
What claim feels over-stated?
What is missing before you would trust this?
What evidence is easiest to inspect?
What evidence is too self-authored or too weak?
What role does this currently signal?
What role does it not yet prove?
What should be removed, compressed, or made more direct?
```

## Preferred Feedback Format

Use the GitHub issue template:

```text
.github/ISSUE_TEMPLATE/external-review-feedback.md
```

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Feedback intake criteria:

```text
docs/review/external-feedback-intake-criteria.md
```

Use `docs/review/external-reviewer-outreach-packet.md` when contacting an FDE/product engineer reviewer, RAG/data engineer reviewer, or founder/operator reviewer before they comment on issue #1.

Suggested sections:

```text
Reviewer role
Evidence inspected
Feedback
Claim boundary
Missing evidence
Hiring signal
Optional next action
```

## Allowed Claim

NoiseProof Agent now has a public, structured request packet for collecting external reviewer feedback on its portfolio proof path.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This is not production RAG evidence.

This is not a claim that the portfolio is application-ready for every role.

This does not prove that any reviewer has inspected the repository.

The public issue above is a request surface only. It becomes external reviewer feedback only after an outside reviewer leaves a substantive comment that references inspected evidence.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
