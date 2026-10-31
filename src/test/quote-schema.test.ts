import { describe, expect, it } from 'vitest';
import { PRODUCTS, QUOTE_RECIPIENT, quoteSchema } from '@/lib/quote-schema';

const quote = { id: '268f6bb7-fbf7-41ed-a25f-41cb230857b0', name: 'Cliente Teste', phone: '(21) 90000-0000', city: 'Rio de Janeiro', place: 'Condomínio', timeframe: 'Nas próximas semanas', details: 'Tapete com logotipo', solution: 'cas', material: 'per' };

describe('pii-zu quote requests', () => {
  it('uses the corrected business email', () => { expect(QUOTE_RECIPIENT).toBe('comercial.piizu@gmail.com'); });
  it('accepts a complete personalized rug quote', () => { expect(quoteSchema.safeParse(quote).success).toBe(true); });
  it('accepts every product line offered on the page', () => {
    for (const product of Object.keys(PRODUCTS)) expect(quoteSchema.safeParse({ ...quote, product }).success).toBe(true);
  });
  it('accepts the six solution segments and the earlier ones', () => {
    for (const solution of ['cond', 'esco', 'sala', 'come', 'indu', 'resi', 'emp', 'esc', 'cas']) {
      expect(quoteSchema.safeParse({ ...quote, solution }).success).toBe(true);
    }
  });
  it('treats requests without a product as rug requests', () => {
    expect(quoteSchema.parse(quote).product).toBe('tapete');
  });
  it('rejects unknown products and keeps rug-only solution and material lists', () => {
    expect(quoteSchema.safeParse({ ...quote, product: 'carro' }).success).toBe(false);
    expect(quoteSchema.safeParse({ ...quote, solution: 'gra' }).success).toBe(false);
    expect(quoteSchema.safeParse({ ...quote, material: 'gra' }).success).toBe(false);
  });
  it('rejects an arbitrary email recipient from visitors', () => { expect(quoteSchema.safeParse({ ...quote, recipient: 'other@example.com' }).success).toBe(false); });
  it('requires usable contact information', () => { expect(quoteSchema.safeParse({ ...quote, phone: '123' }).success).toBe(false); });
});