# Live embedding-backed domain qrels owner-runtime eval packet v0

Phase marker: live embedding-backed domain qrels owner-runtime eval packet v0.

This packet prepares the next semantic retrieval quality gate without making a
provider call in CI or committing secrets.

## What Changed

NoiseProof now has a CI-safe harness:

```text
app.services.live_embedding_domain_qrels_harness
```

The harness exposes:

```text
--print-owner-runtime-eval-packet
--discover-owner-runtime-input
--print-owner-runtime-eval-report-contract
--validate-owner-runtime-eval-report <runtime-report-path-outside-repo>
```

## Owner-runtime Packet

The packet points to the representative domain qrels fixture:

```text
fixture_root -> examples/representative-semantic-retrieval-quality
query_count -> 6
chunk_count -> 12
qrel_count -> 24
provider_call_count -> 18
required_source_types -> csv, html, markdown, memo, pdf
run_source -> owner_runtime_openai_embedding_domain_qrels
query_embedding_source -> owner_runtime_provider_generated
chunk_embedding_source -> owner_runtime_provider_generated
```

The success criteria require:

```text
coverage_status -> passed
provider_response_dimension_check -> passed
usage_metadata_present -> true
qrels_evaluated -> true
unjudged_retrieved_count_at_k -> 0
can_claim_production_semantic_quality -> false
openai_api_key_printed -> false
secret_logged -> false
secret_committed_to_repo -> false
```

## Current Local Discovery

The current local discovery result is:

```text
phase_marker -> live embedding-backed domain qrels owner-runtime input discovery v0
owner_runtime_input_status -> missing_openai_api_key
openai_api_key_present -> false
openai_api_key_printed -> false
opt_in_enabled -> false
api_calls_attempted -> false
```

This means the actual owner-runtime qrels eval remains pending until the owner
configures `OPENAI_API_KEY` outside the repository and explicitly enables
`NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`.

## Validator Boundary

The validator accepts only metadata-only reports outside the repository. It
rejects reports with secret-bearing fields such as `openai_api_key`,
`authorization`, `token`, or `provider_raw_response`.

Validator phase marker:

```text
live embedding-backed domain qrels owner-runtime eval validator v0
```

## Next Gate

```text
owner_runtime_live_embedding_domain_qrels_eval_v0
```

## Boundary

This is an owner-runtime packet, discovery, and validator gate.

It is not live embedding generation proof.

It is not production semantic retrieval quality evidence.

It is not a public benchmark result.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.
