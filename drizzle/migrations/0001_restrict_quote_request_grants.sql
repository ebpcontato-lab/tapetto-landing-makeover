REVOKE ALL ON public.quote_requests FROM anon, authenticated;
GRANT INSERT ON public.quote_requests TO anon;
GRANT ALL ON public.quote_requests TO service_role;