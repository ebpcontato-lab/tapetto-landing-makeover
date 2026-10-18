import { z } from 'zod';

export const QUOTE_RECIPIENT = 'tapetto.cooperkap@gmail.com';

export const quoteSchema = z.object({
  id: z.string().uuid(),
  name: z.string().trim().min(2).max(100),
  phone: z.string().trim().min(10).max(25).regex(/^[+\d\s().-]+$/).refine((value) => value.replace(/\D/g, '').length >= 10),
  city: z.string().trim().min(2).max(120),
  place: z.enum(['Minha casa ou apartamento', 'Empresa ou comércio', 'Condomínio', 'Creche ou escola']),
  timeframe: z.enum(['O quanto antes', 'Nas próximas semanas', 'Daqui a alguns meses', 'Sem data definida']),
  details: z.string().trim().max(2000),
  solution: z.enum(['emp', 'esc', 'cas']),
  material: z.enum(['per', 'cap', 'inf']),
}).strict();