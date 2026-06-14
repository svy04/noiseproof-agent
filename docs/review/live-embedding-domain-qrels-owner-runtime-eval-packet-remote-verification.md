# Live embedding-backed domain qrels owner-runtime eval packet remote verification v0

Phase 867 records remote workflow verification for the Phase 866 live
embedding-backed domain qrels owner-runtime eval packet after it was pushed to
`main`.

## Verified Head

```text
head_sha -> 4bda105f31698521302341ed69e30addae9190b0
branch -> main
commit -> feat: add live embedding domain qrels owner-runtime packet
```

## GitHub Actions

CI:

```text
run_id -> 27491187230
job_name -> api-smoke
job_id -> 81256509435
conclusion -> success
completed_at -> 2026-06-14T06:54:16Z
```

CI step evidence included:

```text
Compile API and local packages -> success
Check semantic retrieval quality report staleness -> success
Check qrels-backed semantic quality report staleness -> success
Check live lexical qrels baseline report staleness -> success
Check live semantic qrels baseline report staleness -> success
Check representative live semantic quality report staleness -> success
Check PDF extraction quality report staleness -> success
Check embedding provider owner runtime input discovery missing state -> success
Check live embedding domain qrels owner-runtime input discovery -> success
Run API smoke tests -> success
```

External Feedback Screen:

```text
run_id -> 27491187229
job_name -> screen
job_id -> 81256509371
conclusion -> success
completed_at -> 2026-06-14T06:53:42Z
```

## Interpretation

The Phase 866 code and documentation passed the remote CI path, including the
new live embedding domain qrels owner-runtime input discovery check and the API
smoke test suite.

The External Feedback Screen workflow also succeeded, but that is workflow
screening only. It is not external reviewer feedback.

## Boundary

This is remote workflow verification only.

It is not live embedding generation proof, not production semantic retrieval quality evidence,
not a public benchmark result, not hosted deployment evidence,
not external reviewer feedback, not customer validation, not Braincrew
acceptance, and not product-complete.
