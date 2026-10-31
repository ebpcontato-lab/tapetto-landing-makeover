-- Solutions became six segments (condomínios, escolas, salas comerciais, comércios,
-- indústrias, residências). Valid ids live in src/lib/quote-schema.ts.
ALTER TABLE public.quote_requests DROP CONSTRAINT IF EXISTS quote_requests_solution_check;
ALTER TABLE public.quote_requests ADD CONSTRAINT quote_requests_solution_check
  CHECK (char_length(solution) BETWEEN 2 AND 20 AND solution ~ '^[a-z0-9-]+$');
