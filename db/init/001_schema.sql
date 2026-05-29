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
  workflow_version TEXT NOT NULL DEFAULT 'phase21-dashboard-provenance-links',
  status TEXT NOT NULL DEFAULT 'created',
  error_message TEXT,
  token_cost NUMERIC,
  latency_ms INTEGER,
  trace_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS retrieval_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question TEXT NOT NULL,
  strategy TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'completed',
  latency_ms INTEGER,
  result_count INTEGER NOT NULL DEFAULT 0,
  hit_rate NUMERIC NOT NULL DEFAULT 0,
  citation_coverage NUMERIC NOT NULL DEFAULT 0,
  missing_evidence_count INTEGER NOT NULL DEFAULT 0,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS evidence_ledger_entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
  agent_run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
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
  failure_type TEXT NOT NULL,
  description TEXT NOT NULL,
  root_cause TEXT,
  fix_status TEXT NOT NULL DEFAULT 'open',
  next_action TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
