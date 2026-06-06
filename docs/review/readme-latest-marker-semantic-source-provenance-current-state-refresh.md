# README Latest-marker Semantic Source Provenance Current-state Refresh

Status: implemented.

Purpose: align the README External Reviewer Fast Path with the current retrieval-run-linked Evidence Ledger semantic source provenance proof chain.

Marker:

```text
readme latest-marker semantic source provenance current-state refresh v0
```

Updated first-pass README routing:

```text
Latest proof routing:
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-refresh.md

Latest external-feedback state:
pending after retrieval-run-linked Evidence Ledger semantic source provenance issue verification
candidate_count=0
draft_count=0
self-authored issue comment only

Latest recorded remote verification state:
docs/review/external-feedback-current-state-retrieval-run-linked-evidence-ledger-semantic-source-provenance-issue-verification-remote-verification.md
CI run 27046055674
External Feedback Screen run 27046055690
```

Why this gate exists:

- the detailed proof archive already contained the retrieval-run-linked Evidence Ledger semantic source provenance proof chain;
- the live issue body already routed reviewers to that proof chain;
- the README top fast path still pointed to older retrieval run semantic provenance and PDF table-candidate feedback markers;
- this refresh keeps the public first-pass route aligned with the current proof chain without claiming new runtime capability.

Evidence source:

- `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md`
- `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md`
- `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md`
- `docs/review/external-review-issue-body-retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-refresh.md`
- `docs/review/external-feedback-current-state-retrieval-run-linked-evidence-ledger-semantic-source-provenance-issue-verification.md`
- `docs/review/external-feedback-current-state-retrieval-run-linked-evidence-ledger-semantic-source-provenance-issue-verification-remote-verification.md`

Boundaries:

- this is README current-state alignment only;
- this is not external reviewer feedback;
- this is not hosted deployment evidence;
- this is not semantic retrieval quality evidence;
- this is not embedding generation;
- this is not live OpenAI provider evidence;
- this is not Evidence Ledger quality evidence;
- this is not final truth adjudication;
- this is not Noise Gate behavior;
- this is not report generation;
- this is not product-complete.

Verification:

```text
tests/test_docs.py::test_readme_latest_marker_semantic_source_provenance_current_state_refresh_updates_first_pass_markers
```

Next gate:

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from the current repository state.
