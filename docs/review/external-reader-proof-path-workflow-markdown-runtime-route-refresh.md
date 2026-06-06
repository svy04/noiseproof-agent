# External-reader Proof Path Workflow Markdown Runtime Route Refresh

Status: implemented.

Phase marker: external-reader proof path workflow markdown runtime route refresh v0.

## Purpose

Align `docs/review/external-reader-proof-path.md` and the README External Reviewer Fast Path with the workflow proof bundle markdown export runtime smoke.

This route gives a cold reviewer the shortest repository-native path from the operations dashboard to a markdown proof bundle that can be inspected before opening JSON.

## Updated Proof Path

```text
Current Proof Route -> workflow proof bundle markdown export runtime smoke
Predecessor workflow checklist dashboard proof -> workflow proof bundle reviewer checklist dashboard runtime smoke
Predecessor report inspection proof -> report markdown local inspection paths proof chain
Predecessor source-provenance proof -> retrieval-run-linked Gate/Report semantic source provenance proof chain
Predecessor handoff proof -> retrieval-run-linked Evidence Ledger semantic source provenance proof chain
```

Current route artifacts:

```text
docs/review/workflow-proof-bundle-markdown-export.md
docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md
```

Preserved predecessor workflow checklist artifacts:

```text
docs/review/workflow-proof-bundle-reviewer-checklist-dashboard-discovery.md
docs/review/workflow-proof-bundle-reviewer-checklist-dashboard-runtime-smoke.md
docs/review/external-reader-proof-path-workflow-checklist-dashboard-runtime-route-refresh.md
```

## What Changed

- `docs/review/external-reader-proof-path.md` now starts its Current Proof Route with `docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md`.
- The workflow proof bundle reviewer checklist dashboard runtime smoke remains visible as predecessor workflow checklist proof.
- The report markdown local inspection paths chain remains visible as predecessor report inspection proof.
- The README External Reviewer Fast Path now points first-pass readers to the workflow proof bundle markdown export runtime smoke.

## Boundary

This is external-reader route alignment only.

It is not new runtime evidence.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not hosted observability.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not product-complete.

## Next Gate

```text
remote verification for this reader-route refresh after push, issue-body refresh if the public issue should route to this proof, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
