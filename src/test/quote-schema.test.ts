import { describe, expect, it } from 'vitest';
import { QUOTE_RECIPIENT, quoteSchema } from '@/lib/quote-schema';

const quote = { id: '268f6bb7-fbf7-41ed-a25f-41cb230857b0', name: 'Cliente Teste', phone: '(21) 90000-0000', city: 'Rio de Janeiro', place: 'Condomínio', timeframe: 'Nas próximas semanas', details: 'Tapete com logotipo', solution: 'cas', material: 'per' };

describe('Tapetto quote requests', () => {
  it('uses the requested business email', () => { expect(QUOTE_RECIPIENT).toBe('tapetto.coperkap@gmail.com'); });
  it('accepts a complete personalized rug quote', () => { expect(quoteSchema.safeParse(quote).success).toBe(true); });
  it('excludes synthetic grass requests', () => {
    expect(quoteSchema.safeParse({ ...quote, solution: 'gra' }).success).toBe(false);
    expect(quoteSchema.safeParse({ ...quote, material: 'gra' }).success).toBe(false);
  });
  it('rejects an arbitrary email recipient from visitors', () => { expect(quoteSchema.safeParse({ ...quote, recipient: 'other@example.com' }).success).toBe(false); });
  it('requires usable contact information', () => { expect(quoteSchema.safeParse({ ...quote, phone: '123' }).success).toBe(false); });
});