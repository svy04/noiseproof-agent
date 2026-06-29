# Source Assimilation Registry

Status: implemented.

Phase marker: `source_assimilation_registry_v0`.

## Purpose

Create a single registry where future NoiseProof gates record the primary
sources, papers, standards, maintained projects, and patents they borrow from.

The registry prevents source-first work from becoming name-dropping. Each card
must say what pattern is borrowed, how it maps locally, where the boundary is,
when to reject the pattern, and what rights/license caution applies.

## Artifacts

```text
docs/research/source-assimilation-registry.md
docs/specs/2026-06-30-source-assimilation-registry.md
apps/api/tests/test_source_assimilation_registry.py
```

Updated surfaces:

```text
docs/MASTER-SPEC.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
```

## Registry Coverage

The initial registry includes source cards for:

- W3C PROV-DM
- SLSA Provenance
- OpenTelemetry
- RAGAS
- ALCE
- BEIR and trec_eval
- Model Cards
- Datasheets for Datasets
- Diataxis
- Docling and Unstructured
- US20260105079A1
- US10628389B2

## Boundary

This is a documentation and research-operating gate only.

It is not new runtime behavior.

It is not API behavior.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not robust PDF extraction evidence.

It is not production semantic retrieval quality evidence.

It is not benchmark evidence.

It is not patent implementation permission.

It is not product-complete.

## Next Gate

Use the registry while selecting the next evidence gate. Current repeated proof
gaps still include external reviewer feedback, robust PDF extraction evidence,
production semantic retrieval quality, hosted deployment, and hosted
observability.
