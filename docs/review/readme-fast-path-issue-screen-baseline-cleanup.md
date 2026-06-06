# README Fast-path Issue Screen Baseline Cleanup

Status: implemented.

Purpose: remove stale `Latest issue-*` markers from the README External Reviewer Fast Path and keep the issue screen readability/BOM state as a baseline.

Marker:

```text
readme fast-path issue screen baseline cleanup v0
```

Updated README first-pass wording:

```text
Issue screen baseline:
issue #1 starts with ## Request
first codepoint 35
no leading BOM
candidate_count=0
draft_count=0
BOM-removal workflow runs remain archived as request-surface hygiene
not the current proof route
```

Why this gate exists:

- the README fast path now routes current proof inspection through retrieval-run-linked Evidence Ledger semantic source provenance;
- the previous `Latest issue readability state`, `Latest issue-feedback state`, and `Latest issue-feedback remote verification` paragraphs described older BOM-removal gates;
- keeping those older paragraphs as `Latest` markers made the first-pass route feel noisier than the actual proof chain;
- this gate keeps the historical evidence in the archive while making the README top section easier to scan.

Historical records preserved:

- `docs/review/external-review-issue-body-bom-removal-refresh.md`
- `docs/review/external-feedback-current-state-issue-body-bom-removal-issue-verification.md`
- `docs/review/external-feedback-current-state-issue-body-bom-removal-issue-verification-remote-verification.md`
- `docs/review/external-review-issue-body-readability-refresh.md`
- `docs/review/external-feedback-current-state-issue-body-readability-verification.md`

Boundaries:

- this is README first-pass copy hygiene only;
- this is not a new live issue edit;
- this is not external reviewer feedback;
- this is not hosted deployment evidence;
- this is not customer validation;
- this is not semantic retrieval quality evidence;
- this is not Evidence Ledger quality evidence;
- this is not product-complete.

Verification:

```text
tests/test_docs.py::test_readme_fast_path_issue_screen_baseline_cleanup_removes_stale_latest_issue_markers
```

Next gate:

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from the current repository state.
