CREATE TABLE IF NOT EXISTS noise_gate_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
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
