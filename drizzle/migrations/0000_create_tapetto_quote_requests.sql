CREATE TABLE public.quote_requests (
  id uuid PRIMARY KEY,
  created_at timestamptz NOT NULL DEFAULT now(),
  name text NOT NULL CHECK (char_length(name) BETWEEN 2 AND 100),
  phone text NOT NULL CHECK (char_length(phone) BETWEEN 10 AND 25),
  city text NOT NULL CHECK (char_length(city) BETWEEN 2 AND 120),
  place text NOT NULL CHECK (place IN ('Minha casa ou apartamento', 'Empresa ou comércio', 'Condomínio', 'Creche ou escola')),
  timeframe text NOT NULL CHECK (timeframe IN ('O quanto antes', 'Nas próximas semanas', 'Daqui a alguns meses', 'Sem data definida')),
  details text NOT NULL DEFAULT '' CHECK (char_length(details) <= 2000),
  solution text NOT NULL CHECK (solution IN ('emp', 'esc', 'cas')),
  material text NOT NULL CHECK (material IN ('per', 'cap', 'inf'))
);
GRANT INSERT ON public.quote_requests TO anon;
GRANT ALL ON public.quote_requests TO service_role;
ALTER TABLE public.quote_requests ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Visitors can submit quote requests only" ON public.quote_requests FOR INSERT TO anon WITH CHECK (true);
COMMENT ON TABLE public.quote_requests IS 'Personalized rug quote requests. Visitors can submit but cannot read, update or delete any requests.';