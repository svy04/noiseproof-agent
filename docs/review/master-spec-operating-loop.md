# Master Spec Operating Loop

Status: implemented.

Phase marker: `master_spec_operating_loop_v0`.

## Purpose

Add a stable operating loop for future NoiseProof work:

```text
read master spec
  -> inspect GOAL and current repo truth
  -> absorb primary sources and proven patterns
  -> write a short-term spec
  -> implement only that gate
  -> verify
  -> update proof surfaces
```

This keeps implementation from drifting into impressive but uninspectable work.

## Artifacts

```text
docs/MASTER-SPEC.md
docs/specs/README.md
docs/specs/2026-06-30-master-spec-operating-loop.md
apps/api/tests/test_master_spec_operating_loop.py
```

Updated surfaces:

```text
README.md
docs/GOAL.md
docs/runbook.md
```

## Source-first Reference Spine

The master spec records a source-first reference spine including:

- W3C PROV-DM
- SLSA Provenance
- OpenTelemetry
- RAGAS
- ALCE
- BEIR and trec_eval
- Model Cards
- Datasheets for Datasets
- Docling and Unstructured
- PyMuPDF/OCR tooling direction through the existing repo context
- patent scan examples for provenance/RAG transparency patterns

## Boundary

This is an operating-loop documentation gate only.

It is not new runtime behavior.

It is not retrieval, embeddings, Evidence Ledger behavior, Critic / Noise Gate
behavior, final report generation, dashboard work, hosted deployment evidence,
external reviewer feedback, customer validation, Braincrew acceptance, or
product-complete.

It is not product-complete.

It does not prove robust PDF extraction or production semantic retrieval
quality.

## Next Gate

Return to `docs/GOAL.md` and choose the next highest-value implementation or
evidence gate after the operating loop is accepted.
