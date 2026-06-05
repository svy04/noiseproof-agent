# External Reviewer Persisted Report Markdown Export Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer persisted report markdown export request refresh v0.

This refresh points reviewer-facing request surfaces to the persisted Report markdown export proof.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate.

## Latest Proof To Inspect

persisted Report markdown export proof:

```text
docs/review/persisted-report-markdown-export.md
GET /reports/{report_record_id}/markdown
```

persisted Report markdown export remote verification:

```text
docs/review/persisted-report-markdown-export-remote-verification.md
CI run 27022884406 -> api-smoke -> success
External Feedback Screen run 27022884394 -> screen -> success
```

Observed export markers:

```text
deterministic text/markdown export
existing persisted report_records rows only
unknown report ids return 404 Report record not found
claim
source ids
evidence spans
confidence
limitations
contradictions
next data needed
stage input manifest
warnings
```

## Reviewer Surfaces Refreshed

- `docs/review/external-reader-proof-path.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `CONTRIBUTING.md`

## Allowed Claim

External reviewers can now reach the latest persisted Report markdown export proof from the standard review entry surfaces.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not free-form report generation.

This is not a new report-generation path.

This is not an LLM call.

This is not retrieval.

This is not Evidence Ledger creation.

This is not Noise Gate behavior.

This is not Report record creation.

This is not financial advice.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, LLM call, embeddings, semantic retrieval, financial advice behavior, or product-complete claim.

The next evidence gate remains:

```text
external reviewer feedback v0
```
