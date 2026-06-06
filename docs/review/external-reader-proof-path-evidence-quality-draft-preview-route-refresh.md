# External-reader Proof Path Evidence Quality Draft Preview Route Refresh

Status: implemented.

Phase marker: external-reader proof path evidence quality draft preview route refresh v0.

This route refresh aligns the repository-native reviewer path with the latest Evidence Ledger quality-risk failure-case draft preview proof.

## What Changed

The external-reader proof path now surfaces the Evidence quality draft preview proof chain before the earlier ops-count route:

```text
docs/review/evidence-quality-risk-failure-case-draft-preview.md
docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke.md
docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke-remote-verification.md
```

The external reviewer link map now includes the same proof chain under `Latest Evidence Quality Draft Preview Proof`.

## Review Markers

The route points reviewers to these inspectable markers:

```text
POST /evidence-ledgers/{entry_id}/failure-case-draft-preview
preview_only_not_persisted
evidence_quality_risk
weakly_supported
low_confidence
missing_source_date
failure_case_count_delta -> 0
clean_preview_status -> 409
missing_preview_status -> 404
```

## Boundary

This is route alignment only.

It is not new runtime evidence.
It is not a live issue body edit.
It is not automatic failure-case creation.
It is not final truth adjudication.
It is not retrieval quality evidence.
It is not Evidence Ledger quality evidence.
It is not embedding generation.
It is not an LLM call.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: remote verification for this route refresh after push, external review issue-body refresh only if the public issue should point to this latest product handoff proof, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
