CREATE TABLE IF NOT EXISTS evidence_ledger_entries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id UUID REFERENCES agent_runs(id) ON DELETE SET NULL,
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
