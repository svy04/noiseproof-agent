# External Reviewer Report Handoff Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer report handoff request refresh v0.

This refresh points reviewer-facing request surfaces to the latest retrieval-run-linked Report proof path.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate.

## Latest Proof To Inspect

retrieval-run-linked Evidence Ledger proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
```

retrieval-run-linked Noise Gate proof:

```text
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
POST /retrieval-runs/{retrieval_run_id}/noise-gate
```

retrieval-run-linked Report proof:

```text
docs/review/retrieval-run-linked-report-runtime-smoke.md
POST /retrieval-runs/{retrieval_run_id}/report
```

Observed report handoff markers:

```text
pre_report_status: 409
input_noise_gate_record_id
input_evidence_ledger_entry_ids
```

## Reviewer Surfaces Refreshed

- `docs/review/external-reader-proof-path.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `CONTRIBUTING.md`

## Allowed Claim

External reviewers can now reach the latest local runtime proof for the retrieval-run-to-Evidence-Ledger-to-Noise-Gate-to-Report handoff from the standard review entry surfaces.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not production RAG evidence.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, LLM call, embeddings, semantic retrieval, free-form final report generation, financial advice behavior, automatic failure-case creation, or product-complete claim.

The next evidence gate remains:

```text
external reviewer feedback v0
```
