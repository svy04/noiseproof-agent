# ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery CI Remote Verification

Status: implemented

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci remote verification v0

## Goal

Record remote GitHub Actions evidence that the no-payload owner runtime input discovery missing-state check executed successfully.

This verifies that the CI workflow actually ran the discovery guard after it was added. It does not run the owner-provided runtime smoke.

## Remote Evidence

```text
run_id: 26927767832
job_id: 79441163152
head: 3089f02
workflow: CI
event: push
job: api-smoke
job_conclusion: success
step_number: 8
step_name: Check ClamAV owner runtime input discovery no-payload missing state
step_conclusion: success
```

The inspected run metadata shows:

```text
owner_runtime_input_missing
```

That status is the expected missing-input state for CI because owner-provided runtime-only signature input must not be stored in the repository or CI configuration.

## Command Used

```bash
gh run view 26927767832 --repo svy04/noiseproof-agent --json databaseId,headSha,conclusion,status,event,workflowName,createdAt,updatedAt,url,jobs
```

## Boundary

```text
does not include a test signature payload
does not synthesize a test signature
does not store a payload in the repository
does not put a payload in CI configuration
does not call the scan endpoint with malicious input
not endpoint malicious-detection runtime proof
not EICAR-through-API proof
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not customer validation
not Braincrew acceptance
not product-complete
```

## Verification

```bash
cd apps/api
uv run pytest tests/test_docs.py -q -k "input_discovery_ci_remote_verification"
```

## Next Gate

ClamAV API endpoint malicious-detection owner-provided runtime smoke v0.

That gate still requires owner-provided runtime-only input and a report output path outside the repository.
