# Live lexical qrels baseline eval remote verification v0

Phase 861 records remote workflow verification for the Phase 860 live lexical
qrels baseline eval after it was pushed to `main`.

## Verified Head

```text
head_sha -> 8a7cc07aac8c4d7c218424a0ecf50381cfea0d3c
branch -> main
commit -> feat: add live lexical qrels baseline eval
```

## GitHub Actions

CI:

```text
run_id -> 27489607815
job_name -> api-smoke
job_id -> 81252099416
conclusion -> success
completed_at -> 2026-06-14T05:36:33Z
```

CI step evidence included:

```text
Compile API and local packages -> success
Check semantic retrieval quality report staleness -> success
Check qrels-backed semantic quality report staleness -> success
Check live lexical qrels baseline report staleness -> success
Check PDF extraction quality report staleness -> success
Run API smoke tests -> success
1187 passed
```

External Feedback Screen:

```text
run_id -> 27489607811
job_name -> screen
job_id -> 81252099394
conclusion -> success
completed_at -> 2026-06-14T05:35:45Z
```

## Interpretation

The Phase 860 code and documentation passed the remote CI path, including the
new live lexical qrels baseline report staleness check and the full API smoke
test suite.

The External Feedback Screen workflow also succeeded, but that is workflow
screening only. It is not external reviewer feedback.

## Boundary

This is remote workflow verification only.

It is not semantic retrieval quality evidence, not embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.
