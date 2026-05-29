CREATE TABLE IF NOT EXISTS report_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
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
