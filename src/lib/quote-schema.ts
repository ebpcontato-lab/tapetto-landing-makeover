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
  'piso-piscina': 'Piso W-Kap para piscina, sauna e áreas molhadas ou úmidas',
  'piso-quadra': 'Piso modular para quadra poliesportiva',
  'piso-laminado': 'Piso laminado Kapazi',
  'piso-vinilico-regua-colada': 'Piso vinílico em régua colada',
  'piso-vinilico-placa-colada': 'Piso vinílico em placa colada 1 m × 1 m',
  'piso-vinilico-clicado': 'Piso vinílico em régua clicada',
  'fita-antiderrapante': 'Fita antiderrapante',
  'capa-elevador': 'Capa de proteção para elevador de serviço',
} as const;
export type ProductId = keyof typeof PRODUCTS;
const productIds = Object.keys(PRODUCTS) as [ProductId, ...ProductId[]];

// Segments of the "Soluções" section (AMB list in public/piizu/index.html).
export const SOLUTIONS = {
  cond: 'Condomínios', esco: 'Escolas', come: 'Comércio e varejo',
  sala: 'Salas e conjuntos comerciais', indu: 'Indústrias', resi: 'Residências', quad: 'Quadras e áreas play e kids',
  // Earlier segments, still accepted from older static exports.
  emp: 'Empresa e comércio', esc: 'Creche e escola', cas: 'Casa e condomínio',
} as const;
export type SolutionId = keyof typeof SOLUTIONS;
const solutionIds = Object.keys(SOLUTIONS) as [SolutionId, ...SolutionId[]];
// Closest earlier segment, used to save while the database still has the old check.
export const LEGACY_SOLUTION: Partial<Record<SolutionId, 'emp' | 'esc' | 'cas'>> = {
  cond: 'cas', resi: 'cas', esco: 'esc', sala: 'emp', come: 'emp', indu: 'emp', quad: 'cas',
};

export const quoteSchema = z.object({
  id: z.string().uuid(),
  name: z.string().trim().min(2).max(100),
  phone: z.string().trim().min(10).max(25).regex(/^[+\d\s().-]+$/).refine((value) => value.replace(/\D/g, '').length >= 10),
  city: z.string().trim().min(2).max(120),
  place: z.enum(['Minha casa ou apartamento', 'Empresa ou comércio', 'Condomínio', 'Creche ou escola']),
  timeframe: z.enum(['O quanto antes', 'Nas próximas semanas', 'Daqui a alguns meses', 'Sem data definida']),
  details: z.string().trim().max(2000),
  solution: z.enum(solutionIds),
  material: z.enum(['per', 'cap', 'inf']),
  // Older static exports do not send a product; they only offered rugs.
  product: z.enum(productIds).default('tapete'),
}).strict();