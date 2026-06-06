# Retrieval-run-linked Gate/Report Semantic Source Provenance

Status: implemented.

Purpose: preserve source retrieval provenance from retrieval-run-linked Evidence Ledger rows through the downstream Noise Gate and Report handoffs.

Marker:

```text
retrieval-run-linked Gate/Report semantic source provenance v0
```

Implemented behavior:

```text
POST /retrieval-runs/{retrieval_run_id}/noise-gate
POST /retrieval-runs/{retrieval_run_id}/report

source_retrieval_mode -> semantic_persisted
source_query_vector_source -> caller_provided_vector
source_is_semantic_retrieval_run -> true
source_retrieval_persistence_boundary -> semantic_retrieval_run_only_no_evidence_ledger
handoff_performs_semantic_retrieval -> false
```

What changed:

- `retrieval_run_noise_gate.py` now reads source retrieval provenance from linked Evidence Ledger row metadata.
- `retrieval_run_report.py` now reads the same provenance from linked Evidence Ledger row metadata.
- Noise Gate and Report warnings surface the source retrieval mode and query vector source.
- Noise Gate and Report `stage_input_manifest` records preserve the provenance fields.
- Noise Gate and Report agent-run traces preserve the provenance fields.

Verification:

```text
tests/test_routes.py::test_semantic_retrieval_run_noise_gate_and_report_preserve_source_retrieval_provenance
tests/test_docs.py::test_retrieval_run_linked_gate_report_semantic_source_provenance_is_recorded
```

Boundary:

- this is deterministic route-level provenance preservation only;
- this does not perform semantic retrieval during the Noise Gate or Report handoff;
- this is not semantic retrieval quality evidence;
- this is not embedding generation;
- this is not live OpenAI provider evidence;
- this is not Evidence Ledger quality evidence;
- this is not Noise Gate quality evidence;
- this is not report quality evidence;
- this is not final truth adjudication;
- this is not hosted deployment evidence;
- this is not external reviewer feedback;
- this is not product-complete.

Next gate:

Local Docker/FastAPI runtime smoke for retrieval-run-linked Gate/Report semantic source provenance if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from the current repository state.
