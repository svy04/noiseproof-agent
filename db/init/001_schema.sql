CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_type TEXT NOT NULL,
  source_uri TEXT,
  filename TEXT,
  title TEXT,
  source_date DATE,
  profile_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  extraction_quality TEXT NOT NULL DEFAULT 'unknown',
  status TEXT NOT NULL DEFAULT 'registered',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS agent_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_question TEXT NOT NULL,
  workflow_version TEXT NOT NULL DEFAULT 'phase40-lineage-warning-code-dashboard',
  status TEXT NOT NULL DEFAULT 'created',
  error_message TEXT,
  token_cost NUMERIC,
  latency_ms INTEGER,
  trace_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS workflow_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question TEXT NOT NULL,
  workflow_version TEXT NOT NULL DEFAULT 'phase40-lineage-warning-code-dashboard',
  status TEXT NOT NULL DEFAULT 'created' CHECK (
    status IN (
      'created',
      'running',
      'completed',
      'failed',
      'blocked',
      'needs_revision'
    )
  ),
  trace_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  started_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ,
  latency_ms INTEGER,
  error_message TEXT
);

CREATE TABLE IF NOT EXISTS retrieval_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question TEXT NOT NULL,
  strategy TEXT NOT NULL,
  workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL,
  status TEXT NOT NULL DEFAULT 'completed',
  latency_ms INTEGER,
  result_count INTEGER NOT NULL DEFAULT 0,
  hit_rate NUMERIC NOT NULL DEFAULT 0,
  citation_coverage NUMERIC NOT NULL DEFAULT 0,
  missing_evidence_count INTEGER NOT NULL DEFAULT 0,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS uploaded_file_intake_manifests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_sha256 TEXT NOT NULL,
  filename TEXT,
  source_type TEXT NOT NULL,
  content_type TEXT,
  size_bytes INTEGER NOT NULL DEFAULT 0 CHECK (size_bytes >= 0),
  parser TEXT,
  profile_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  storage_decision TEXT NOT NULL DEFAULT 'do_not_persist_raw_upload_yet',
  replayable BOOLEAN NOT NULL DEFAULT false,
  persistence_boundary TEXT NOT NULL DEFAULT 'manifest_only_no_raw_file_storage',
  warnings_json JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_uploaded_file_intake_manifests_content_sha256
  ON uploaded_file_intake_manifests(content_sha256);

CREATE TABLE IF NOT EXISTS uploaded_raw_files (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_sha256 TEXT NOT NULL,
  storage_key TEXT NOT NULL UNIQUE,
  filename TEXT,
  source_type TEXT NOT NULL,
  content_type TEXT,
  size_bytes INTEGER NOT NULL DEFAULT 0 CHECK (size_bytes >= 0),
  storage_backend TEXT NOT NULL DEFAULT 'postgres_bytea',
  quarantine_status TEXT NOT NULL DEFAULT 'stored_quarantined' CHECK (
    quarantine_status IN ('stored_quarantined', 'rejected')
  ),
  persistence_boundary TEXT NOT NULL DEFAULT 'raw_upload_quarantine_db_bytea_guarded_download_endpoint',
  raw_bytes BYTEA NOT NULL,
  warnings_json JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_uploaded_raw_files_content_sha256
  ON uploaded_raw_files(content_sha256);

CREATE TABLE IF NOT EXISTS raw_file_scan_results (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE,
  scanner_name TEXT NOT NULL,
  scanner_version TEXT,
  signature_db_version TEXT,
  scan_started_at TIMESTAMPTZ,
  scan_finished_at TIMESTAMPTZ,
  scan_status TEXT NOT NULL DEFAULT 'pending' CHECK (
    scan_status IN ('pending', 'running', 'completed', 'failed', 'skipped')
  ),
  scan_verdict TEXT NOT NULL DEFAULT 'pending' CHECK (
    scan_verdict IN (
      'pending',
      'clean',
      'suspicious',
      'infected',
      'scan_error',
      'skipped'
    )
  ),
  matched_signature TEXT,
  error_message TEXT,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_raw_file_id
  ON raw_file_scan_results(raw_file_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_scan_status
  ON raw_file_scan_results(scan_status);

CREATE INDEX IF NOT EXISTS idx_raw_file_scan_results_scan_verdict
  ON raw_file_scan_results(scan_verdict);

CREATE TABLE IF NOT EXISTS raw_file_download_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_file_id UUID NOT NULL REFERENCES uploaded_raw_files(id) ON DELETE CASCADE,
  latest_scan_result_id UUID REFERENCES raw_file_scan_results(id) ON DELETE SET NULL,
  download_result TEXT NOT NULL CHECK (
    download_result IN ('allowed', 'blocked')
  ),
  blocked_reason TEXT CHECK (
    blocked_reason IS NULL OR blocked_reason IN (
      'missing_clean_scan',
      'latest_scan_not_clean',
      'quarantine_status_blocked',
      'rate_limited',
      'raw_file_missing'
    )
  ),
  http_status_code INTEGER NOT NULL CHECK (
    http_status_code >= 100 AND http_status_code <= 599
  ),
  authorization_boundary TEXT NOT NULL DEFAULT 'local_v0_no_auth_not_production',
  rate_limit_boundary TEXT NOT NULL DEFAULT 'local_v0_in_memory_fixed_window_not_production',
  filename_boundary TEXT NOT NULL DEFAULT 'local_v0_content_disposition_filename_safety_not_production',
  client_host_boundary TEXT NOT NULL DEFAULT 'local_request_client_host_not_identity',
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_raw_file_id
  ON raw_file_download_events(raw_file_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_latest_scan_result_id
  ON raw_file_download_events(latest_scan_result_id);

CREATE INDEX IF NOT EXISTS idx_raw_file_download_events_download_result
  ON raw_file_download_events(download_result);

CREATE TABLE IF NOT EXISTS document_chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
  source_type TEXT NOT NULL,
  source_uri TEXT,
  filename TEXT,
  chunk_strategy TEXT NOT NULL,
  chunk_index INTEGER NOT NULL CHECK (chunk_index >= 0),
  chunk_text TEXT NOT NULL,
  character_start INTEGER CHECK (character_start IS NULL OR character_start >= 0),
  character_end INTEGER CHECK (character_end IS NULL OR character_end >= 0),
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  persistence_boundary TEXT NOT NULL DEFAULT 'chunk_text_only_no_raw_file_storage',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (document_id, chunk_strategy, chunk_index)
);

CREATE INDEX IF NOT EXISTS idx_document_chunks_document_id
  ON document_chunks(document_id);

CREATE INDEX IF NOT EXISTS idx_document_chunks_strategy
  ON document_chunks(chunk_strategy);

CREATE TABLE IF NOT EXISTS chunk_embeddings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  chunk_id UUID NOT NULL REFERENCES document_chunks(id) ON DELETE CASCADE,
  embedding_model TEXT NOT NULL,
  embedding_dimension INTEGER NOT NULL CHECK (embedding_dimension > 0),
  embedding_text_hash TEXT NOT NULL,
  embedding_created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  distance_metric TEXT NOT NULL DEFAULT 'cosine' CHECK (
    distance_metric IN ('cosine', 'l2', 'inner_product')
  ),
  embedding_status TEXT NOT NULL DEFAULT 'planned' CHECK (
    embedding_status IN ('planned', 'created', 'stale', 'failed')
  ),
  embedding vector,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (chunk_id, embedding_model, embedding_text_hash, distance_metric)
);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_chunk_id
  ON chunk_embeddings(chunk_id);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_model
  ON chunk_embeddings(embedding_model);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_status
  ON chunk_embeddings(embedding_status);

CREATE TABLE IF NOT EXISTS evidence_ledger_entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  agent_run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL,
  retrieval_run_id UUID REFERENCES retrieval_runs(id) ON DELETE SET NULL,
  workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid(),
  question TEXT NOT NULL,
  claim TEXT NOT NULL,
  source_id TEXT,
  source_type TEXT,
  source_date TEXT,
  evidence_span TEXT NOT NULL,
  confidence TEXT NOT NULL,
  limitation TEXT NOT NULL,
  contradicting_source_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
  status TEXT NOT NULL CHECK (
    status IN (
      'supported',
      'weakly_supported',
      'contradicted',
      'unsupported',
      'blocked'
    )
  ),
  matched_terms JSONB NOT NULL DEFAULT '[]'::jsonb,
  role TEXT NOT NULL,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS noise_gate_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid(),
  agent_run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL,
  stage_input_manifest JSONB NOT NULL DEFAULT '{}'::jsonb,
  question TEXT NOT NULL,
  decision TEXT NOT NULL CHECK (
    decision IN ('pass', 'needs_revision', 'blocked')
  ),
  final_response_allowed BOOLEAN NOT NULL DEFAULT false,
  checks JSONB NOT NULL DEFAULT '[]'::jsonb,
  blocked_claims JSONB NOT NULL DEFAULT '[]'::jsonb,
  downgraded_claims JSONB NOT NULL DEFAULT '[]'::jsonb,
  allowed_claims JSONB NOT NULL DEFAULT '[]'::jsonb,
  required_revisions JSONB NOT NULL DEFAULT '[]'::jsonb,
  fallback_message TEXT,
  warnings JSONB NOT NULL DEFAULT '[]'::jsonb,
  evidence_entry_count INTEGER NOT NULL DEFAULT 0,
  draft_claim_count INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS report_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid(),
  agent_run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL,
  stage_input_manifest JSONB NOT NULL DEFAULT '{}'::jsonb,
  question TEXT NOT NULL,
  status TEXT NOT NULL CHECK (
    status IN ('generated', 'needs_revision', 'blocked')
  ),
  report JSONB,
  gate JSONB NOT NULL DEFAULT '{}'::jsonb,
  gate_decision TEXT NOT NULL CHECK (
    gate_decision IN ('pass', 'needs_revision', 'blocked')
  ),
  fallback_message TEXT,
  required_revisions JSONB NOT NULL DEFAULT '[]'::jsonb,
  warnings JSONB NOT NULL DEFAULT '[]'::jsonb,
  claim_count INTEGER NOT NULL DEFAULT 0,
  evidence_entry_count INTEGER NOT NULL DEFAULT 0,
  draft_claim_count INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS failure_cases (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL,
  failure_type TEXT NOT NULL,
  description TEXT NOT NULL,
  root_cause TEXT,
  fix_status TEXT NOT NULL DEFAULT 'open',
  next_action TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
