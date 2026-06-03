# Uploaded Raw File ClamAV Runtime Verification Review

Status: review-only.

Phase marker: uploaded raw file ClamAV runtime verification review v0.

## Purpose

This gate selects the next source-first scanner runtime proof after the raw upload scan execution endpoint smoke.

The endpoint currently proves local HTTP wiring and metadata persistence with the default `scanner-unavailable` adapter. It still does not prove a real ClamAV binary, signature database, or test-file detection path.

This review selects a bounded Dockerized ClamAV runtime smoke before changing the API or scanner adapter behavior.

## Source-first Anchors

- ClamAV Docker documentation: https://docs.clamav.net/manual/Installing/Docker.html
- ClamAV Scanning documentation: https://docs.clamav.net/manual/Usage/Scanning.html
- ClamAV Signature Management documentation: https://docs.clamav.net/manual/Usage/SignatureManagement.html
- EICAR Anti-Malware Testfile: https://www.eicar.org/download-anti-malware-testfile/

Interpretation used for this review:

```text
ClamAV official Docker images can run clamscan against a bind-mounted scan directory.
Signature database presence matters and must be recorded, not assumed.
EICAR is a standard anti-malware test file that is not real malware.
EICAR detection can prove scanner test-path behavior, but it does not prove production malware scanning quality.
```

## Selected Next Gate

```text
dockerized ClamAV EICAR runtime smoke v0
```

The selected smoke should:

```text
create a temporary host scan directory
write the EICAR test file into that temp directory
run a Dockerized ClamAV clamscan command against the bind-mounted temp directory
record Docker image tag and resolved image id or digest if available
record clamscan return code
record stdout/stderr summary without committing the EICAR file
record whether EICAR was detected
delete the temporary scan directory after the smoke
```

## Non-selected Paths

Do not install ClamAV on the host in this gate.

Do not switch the API endpoint default from `scanner-unavailable`.

Do not add a Docker-backed scanner adapter yet.

Do not expose daemon TCP sockets.

Do not add a download endpoint.

Do not scan user-uploaded samples with a real scanner before the EICAR smoke exists.

Do not commit the EICAR test file into the repository.

## Required Evidence Fields For The Next Gate

The next gate must report:

```text
docker_available
clamav_image
clamav_image_id_or_digest
signature_database_observed
test_file_type = eicar
test_file_committed_to_repo = false
clamscan_return_code
eicar_detected
temporary_scan_dir_deleted
real_clamav_runtime_verified
malware_scanning_evidence
api_endpoint_verified_with_real_clamav
```

Expected boundary values:

```text
test_file_type = eicar
test_file_committed_to_repo = false
malware_scanning_evidence = false
api_endpoint_verified_with_real_clamav = false
```

`real_clamav_runtime_verified` may become true only if the Dockerized ClamAV process actually runs and detects or evaluates the EICAR file with a visible signature database state.

## Boundary

This is review-only.

This is not runtime evidence.

This is not endpoint code.

This is not Dockerized ClamAV execution.

This is not real ClamAV verification yet.

This is not malware scanning evidence.

This is not API endpoint verification with real ClamAV.

This is not hosted deployment evidence.

This is not external reviewer feedback.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next Product Gate

```text
dockerized ClamAV EICAR runtime smoke v0
```
