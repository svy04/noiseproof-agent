# External Review Issue Body Report Markdown Local Inspection Route Refresh

Status: owner-authored issue body edit.

Phase marker: external review issue body report markdown local inspection route refresh v0.

## Purpose

Record the owner-authored issue #1 body refresh that routes external reviewers to the current report markdown local inspection paths proof chain.

This keeps the public review request current after Phase 650 and Phase 651.

## Live Issue

Issue: https://github.com/svy04/noiseproof-agent/issues/1

Observed after edit:

```text
updatedAt: 2026-06-06T04:31:28Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
body_length: 8231
has_report_markdown_local_inspection_paths_proof: true
has_report_markdown_local_inspection_runtime_smoke: true
has_report_markdown_local_inspection_remote_verification: true
has_report_markdown_local_inspection_route_refresh_record: true
has_current_report_markdown_path_marker: true
has_workflow_trace_path_marker: true
has_retrieval_run_list_path_marker: true
has_evidence_ledger_list_path_marker: true
has_noise_gate_list_path_marker: true
old_gate_report_latest_label_present: false
```

## Latest Proof Links Added

```text
docs/review/report-markdown-local-inspection-paths.md
docs/review/report-markdown-local-inspection-paths-runtime-smoke.md
docs/review/report-markdown-local-inspection-paths-runtime-smoke-remote-verification.md
docs/review/external-reader-proof-path-report-markdown-local-inspection-route-refresh.md
```

## Markers Routed To Reviewers

```text
GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK
text/markdown; charset=utf-8
## Local Inspection Paths
current report markdown path
current report workflow-trace filter
current workflow trace path
retrieval-run list path
Evidence Ledger list path
Noise Gate list path
Stage Input Links remain visible
Source Retrieval Provenance remains visible
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

This is not Noise Gate quality evidence.

This is not report quality evidence.

This is not final truth adjudication.

This is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

```text
external feedback current-state report markdown local inspection issue verification v0, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```

