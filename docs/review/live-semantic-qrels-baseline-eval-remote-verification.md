# Live semantic qrels baseline eval remote verification v0

Phase 863 records remote workflow verification for the Phase 862 live semantic
qrels baseline eval after it was pushed to `main`.

## Verified Head

```text
head_sha -> ed73aef0b13261ac74ee14c7402d839dc5532797
branch -> main
commit -> feat: add live semantic qrels baseline eval
```

## GitHub Actions

CI:

```text
run_id -> 27490045473
job_name -> api-smoke
job_id -> 81253278484
conclusion -> success
completed_at -> 2026-06-14T05:58:14Z
```

CI step evidence included:

```text
Compile API and local packages -> success
Check semantic retrieval quality report staleness -> success
Check qrels-backed semantic quality report staleness -> success
Check live lexical qrels baseline report staleness -> success
Check live semantic qrels baseline report staleness -> success
Check PDF extraction quality report staleness -> success
Run API smoke tests -> success
1193 passed
```

External Feedback Screen:

```text
run_id -> 27490045474
job_name -> screen
job_id -> 81253278486
conclusion -> success
completed_at -> 2026-06-14T05:57:34Z
```

## Interpretation

The Phase 862 code and documentation passed the remote CI path, including the
new live semantic qrels baseline report staleness check and the full API smoke
test suite.

The External Feedback Screen workflow also succeeded, but that is workflow
screening only. It is not external reviewer feedback.

## Boundary

This is remote workflow verification only.

It is not semantic retrieval quality evidence, not live embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.
