# External-reader Proof Path Encrypted PDF Handoff Ops Route Refresh

Status: implemented.

Phase marker: external-reader proof path encrypted PDF handoff ops route refresh v0.

## Purpose

Surface the uploaded PDF encrypted failure-mode proof chain in the repository-native reviewer path without replacing the current workflow proof bundle markdown route.

This is a focused intake proof route. It helps an external reviewer inspect whether password-protected PDFs are treated as explicit failure candidates and whether the explicit chunk handoff path keeps that failure metadata visible in operations views.

## Routed Proof Artifacts

```text
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md
```

## Route Markers

```text
POST /documents/upload-chunks
pdf_encrypted_requires_password
pdf_encrypted_failure_candidate_count
PDF Encrypted Failure Candidates
```

## Surfaces Refreshed

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
apps/api/tests/test_docs.py
```

## Boundary

This is reader-route alignment only.

It is not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not decryption, not password bypass, not customer validation, not Braincrew acceptance, and not product-complete.

The route points to metadata-derived operations visibility: `pdf_encrypted_failure_candidate_count` and `PDF Encrypted Failure Candidates`. It does not prove that encrypted PDFs can be decrypted, parsed, chunked, or used for trustworthy downstream retrieval.

## Next Gate

Remote verification for this route refresh after push, issue-body refresh if the public feedback issue should also route reviewers to this focused proof, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
