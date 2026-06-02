# External Review Guide

This repository is currently asking for bounded external review of the NoiseProof Agent portfolio proof path.

The next evidence gate is:

```text
external reviewer feedback v0
```

## Fast Path

Please start here:

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/review/external-reviewer-link-map.md`
4. `docs/application/portfolio-index.md`
5. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
   - uploaded-file intake manifest proof; not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
6. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
   - uploaded-file intake manifest persistence proof; not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
7. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
   - uploaded-file parsed document persistence proof; not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.
8. `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
   - uploaded-file chunk persistence proof; not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
9. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
   - uploaded-file chunk handoff proof via `POST /documents/upload-chunks`; not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.
10. `docs/review/external-feedback-intake-criteria.md`

Public feedback issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Useful Review Questions

Please leave one evidence-referenced comment that names what you inspected.

Useful critique can answer one of these:

```text
Which claim feels over-stated?
Which artifact is easiest to inspect?
Which artifact is too self-authored or too weak?
What missing evidence would most improve trust?
Does this signal Forward Deployed Engineer work?
What does it not yet prove for Product Engineer?
What should be cut, compressed, or made more direct?
```

## Preferred Comment Shape

```text
Reviewer role:
Evidence inspected:
Feedback:
Claim boundary:
Missing evidence:
Hiring signal:
Optional next action:
```

## Boundary

This guide is not external reviewer feedback.

This guide is not customer validation.

This guide is not Braincrew acceptance.

This guide is not hosted deployment evidence.

Self-authored comments, generic praise, issue status updates, bot summaries, and CI checks do not close the `external reviewer feedback v0` gate.

The gate advances only when an outside reviewer leaves substantive, evidence-referenced feedback that satisfies:

```text
docs/review/external-feedback-intake-criteria.md
```
