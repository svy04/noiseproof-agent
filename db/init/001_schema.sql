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
