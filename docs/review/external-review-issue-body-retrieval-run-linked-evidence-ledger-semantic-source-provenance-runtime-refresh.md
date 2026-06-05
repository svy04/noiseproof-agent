# External Review Issue Body Retrieval-run-linked Evidence Ledger Semantic Source Provenance Runtime Refresh

Status: implemented.

Phase marker: external review issue body retrieval-run-linked Evidence Ledger semantic source provenance runtime refresh v0.

## Purpose

Record the owner-authored issue #1 body refresh that routes external reviewers to the latest retrieval-run-linked Evidence Ledger semantic source provenance proof chain.

This keeps the public review request current after Phase 624 through Phase 626.

## Live Issue

Issue: https://github.com/svy04/noiseproof-agent/issues/1

Observed after edit:

```text
updatedAt: 2026-06-05T23:41:58Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
has_semantic_source_provenance_proof: true
has_semantic_source_provenance_runtime_smoke: true
has_semantic_source_provenance_remote_verification: true
has_issue_body_refresh_record: true
has_handoff_semantic_retrieval_false_marker: true
has_quality_boundary: true
```

## Latest Proof Links Added

```text
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-refresh.md
```

## Markers Routed To Reviewers

```text
POST /documents/{document_id}/semantic-retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id} -> 200
GET /agent-runs -> 200
source_retrieval_mode -> semantic_persisted
source_query_vector_source -> caller_provided_vector
source_is_semantic_retrieval_run -> true
source_retrieval_persistence_boundary -> semantic_retrieval_run_only_no_evidence_ledger
persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
handoff_performs_semantic_retrieval -> false
no_embeddings -> true
no_llm -> true
```

## Boundary

This is owner-authored issue body routing only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not a new retrieval algorithm.

This is not embedding generation.

This is not live OpenAI provider evidence.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger quality evidence.

This is not final truth adjudication.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

```text
external feedback current-state retrieval-run-linked Evidence Ledger semantic source provenance issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
