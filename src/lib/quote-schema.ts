import { z } from 'zod';

export const QUOTE_RECIPIENT = 'comercial.piizu@gmail.com';

// Product lines offered on the landing page. To add a niche, add its ids here and in
// the NICHOS list of public/piizu/index.html (a test checks both lists match).
export const PRODUCTS = {
  'tapete': 'Tapete ou Capacho personalizado',
  'grama-12': 'Grama Decorativa 12 mm',
  'grama-20': 'Grama Decorativa 20 mm',
  'grama-30': 'Grama Recreativa 30 mm',
  'grama-50': 'Grama Esportiva 50 mm',
  'piso-piscina': 'Piso W-Kap para piscina, sauna e áreas molhadas ou úmidas',
  'piso-quadra': 'Piso modular Playkap para quadras poliesportivas, playground e áreas kids',
  'piso-rubberkap': 'Piso emborrachado Rubberkap para quadras, playground e áreas kids',
  'piso-laminado': 'Piso laminado emborrachado Kapazi',
  'piso-vinilico-regua-colada': 'Piso vinílico em régua colada',
  'piso-vinilico-placa-colada': 'Piso vinílico em placa colada 1 m × 1 m',
  'piso-vinilico-clicado': 'Piso vinílico em régua clicada',
  'fita-antiderrapante': 'Fita antiderrapante',
  'fita-demarcacao': 'Fita de demarcação',
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

// Every answer is accepted: free-text fields only need something filled in somewhere
// (a fully empty form is the only refusal), and unexpected choice values fall back to
// a default instead of blocking the request. toStoredQuote() then fits the values to
// the database limits, keeping anything adjusted in the details so nothing is lost.
const text = (max: number) => z.string().trim().max(max).catch((ctx) => String(ctx.input ?? '').trim().slice(0, max)).default('');

export const quoteSchema = z.object({
  id: z.string().uuid(),
  name: text(500),
  phone: text(200),
  city: text(500),
  place: z.enum(['Minha casa ou apartamento', 'Empresa ou comércio', 'Condomínio', 'Creche ou escola']).catch('Empresa ou comércio'),
  timeframe: z.enum(['O quanto antes', 'Nas próximas semanas', 'Daqui a alguns meses', 'Sem data definida']).catch('Sem data definida'),
  details: text(4000),
  solution: z.enum(solutionIds).catch('come'),
  material: z.enum(['per', 'cap', 'inf']).catch('per'),
  // Older static exports do not send a product; they only offered rugs.
  product: z.enum(productIds).catch('tapete').default('tapete'),
}).strict().refine((q) => [q.name, q.phone, q.city, q.details].some((v) => v.length > 0));

export type QuoteInput = z.infer<typeof quoteSchema>;

// Database limits (migration 0000): name 2–100, phone 10–25, city 2–120, details ≤ 2000.
export function toStoredQuote(q: QuoteInput) {
  const notes: string[] = [];
  const fit = (value: string, label: string, min: number, max: number) => {
    if (value.length === 0) return 'Não informado';
    if (value.length > max) { notes.push(`[${label} completo: ${value}]`); return value.slice(0, max); }
    if (value.length < min) return value.padEnd(min, '.');
    return value;
  };
  let phone = q.phone;
  if (phone.length === 0) phone = 'Não informado';
  else if (phone.length > 25) { notes.push(`[WhatsApp completo: ${phone}]`); phone = phone.slice(0, 25); }
  else if (phone.length < 10) phone = `${phone} (incompleto)`;
  return {
    row: { ...q, name: fit(q.name, 'Nome', 2, 100), phone, city: fit(q.city, 'Bairro/cidade', 2, 120), details: '' },
    notes,
  };
}
