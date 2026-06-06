# External-reader Proof Path Report Markdown Local Inspection Route Refresh

Status: implemented.

Phase marker: external-reader proof path report markdown local inspection route refresh v0.

## Purpose

Align `docs/review/external-reader-proof-path.md` and the README External Reviewer Fast Path with the latest report markdown local inspection proof chain.

This route gives a cold reviewer the shortest path from a persisted report markdown export to the local inspection paths, upstream stage ids, source retrieval provenance, runtime smoke, and remote workflow acceptance.

## Updated Proof Path

```text
Current Proof Route -> report markdown local inspection paths proof chain
Predecessor source-provenance proof -> retrieval-run-linked Gate/Report semantic source provenance proof chain
Predecessor handoff proof -> retrieval-run-linked Evidence Ledger semantic source provenance proof chain
Persisted Report markdown export proof -> preserved without Latest label
Historical Table-candidate Downstream Proof Routing -> preserved without Latest label
```

## What Changed

- `docs/review/external-reader-proof-path.md` now starts its Current Proof Route with the report markdown local inspection paths proof, runtime smoke, and remote verification.
- The retrieval-run-linked Gate/Report semantic source provenance proof remains visible as predecessor source-provenance proof.
- The README External Reviewer Fast Path now points first-pass readers to the report markdown local inspection paths chain and its remote verification.

## Boundary

This is external-reader route alignment only.

It is not new runtime evidence.

It is not a live issue body edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not final truth adjudication.

It is not product-complete.

## Next Gate

```text
remote verification for this reader-route refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
