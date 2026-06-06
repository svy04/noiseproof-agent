# External-reader Proof Path Semantic Source Provenance Route Refresh

Status: implemented.

Purpose: align `docs/review/external-reader-proof-path.md` with the current retrieval-run-linked Evidence Ledger semantic source provenance proof chain.

Marker:

```text
external-reader proof path semantic source provenance route refresh v0
```

Updated route:

```text
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-refresh.md
docs/review/external-feedback-current-state-retrieval-run-linked-evidence-ledger-semantic-source-provenance-issue-verification-remote-verification.md
```

What changed:

- added `## Current Proof Route`;
- made retrieval-run-linked Evidence Ledger semantic source provenance the first proof route;
- changed `Latest persisted Report markdown export proof` to `Persisted Report markdown export proof`;
- changed `## Latest Table-candidate Downstream Proof Routing` to `## Historical Table-candidate Downstream Proof Routing`;
- preserved older report and table-candidate proof artifacts as historical or specialized proof paths.

Boundaries:

- this is external-reader route alignment only;
- this is not new runtime evidence;
- this is not a live issue body edit;
- this is not external reviewer feedback;
- this is not hosted deployment evidence;
- this is not semantic retrieval quality evidence;
- this is not embedding generation;
- this is not Evidence Ledger quality evidence;
- this is not final truth adjudication;
- this is not product-complete.

Verification:

```text
tests/test_docs.py::test_external_reader_proof_path_semantic_source_provenance_route_refresh_is_recorded
```

Next gate:

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from the current repository state.
