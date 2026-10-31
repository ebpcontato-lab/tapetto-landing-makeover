-- Product line chosen by the visitor (rugs, synthetic grass, floors, future niches).
-- Valid ids live in src/lib/quote-schema.ts, so new niches need no further migration.
ALTER TABLE public.quote_requests
  ADD COLUMN product text NOT NULL DEFAULT 'tapete'
  CHECK (char_length(product) BETWEEN 2 AND 40 AND product ~ '^[a-z0-9-]+$');
