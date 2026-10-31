import { z } from 'zod';

export const QUOTE_RECIPIENT = 'comercial.piizu@gmail.com';

// Product lines offered on the landing page. To add a niche, add its ids here and in
// the NICHOS list of public/piizu/index.html (a test checks both lists match).
export const PRODUCTS = {
  'tapete': 'Tapete ou capacho personalizado',
  'grama-12': 'Grama Decorativa 12 mm',
  'grama-20': 'Grama Decorativa 20 mm',
  'grama-30': 'Grama Recreativa 30 mm',
  'grama-50': 'Grama Esportiva 50 mm',
  'piso-piscina': 'Piso W-Kap para piscina e áreas molhadas',
  'piso-quadra': 'Piso modular para quadra poliesportiva',
} as const;
export type ProductId = keyof typeof PRODUCTS;
const productIds = Object.keys(PRODUCTS) as [ProductId, ...ProductId[]];

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
  // Older static exports do not send a product; they only offered rugs.
  product: z.enum(productIds).default('tapete'),
}).strict();