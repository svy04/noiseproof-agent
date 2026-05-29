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
  workflow_version TEXT NOT NULL DEFAULT 'phase6-evidence-ledger-preview',
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
