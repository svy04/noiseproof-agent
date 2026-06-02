# Semantic Retrieval Persistence Application Refresh

Phase marker: semantic retrieval persistence application refresh v0.

Status: documentation-only application surface refresh.

## Purpose

Surface the local runtime proof for caller-provided-vector semantic retrieval persistence in the reviewer-facing application docs.

This refresh exists because the repo now has local Docker DB plus live FastAPI HTTP evidence for persisted semantic retrieval runs, but still has no embedding generation, vector search quality evidence, hosted deployment evidence, or Evidence Ledger generation from semantic retrieval.

## Updated Surfaces

```text
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
docs/review/external-reader-proof-path.md
```

Primary proof artifact:

```text
docs/review/semantic-retrieval-persistence-runtime-smoke.md
```

## Runtime Proof Surfaced

```text
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /retrieval-runs -> 200
retrieval_run_count_after = retrieval_run_count_before + 1
dimension mismatch -> 400
evidence_ledger_count_unchanged -> true
metadata_json.retrieval_mode = semantic_persisted
```

The surfaced runtime proof is local Docker DB plus live FastAPI HTTP evidence only. It shows caller-provided-vector semantic retrieval persistence into `retrieval_runs`.

## Claim Update

Allowed claim:

```text
NoiseProof has local runtime evidence for caller-provided-vector semantic retrieval persistence.
```

Forbidden claim:

```text
NoiseProof does not generate embeddings, does not prove vector search quality, and does not generate Evidence Ledger rows from semantic retrieval.
```

## Boundary

This is not embedding generation.

This is not vector search quality evidence.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
next product gate: semantic retrieval quality review v0
```
