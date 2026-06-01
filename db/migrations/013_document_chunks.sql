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
