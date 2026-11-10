import { describe, expect, it } from 'vitest';
import { PRODUCTS, QUOTE_RECIPIENT, quoteSchema, toStoredQuote } from '@/lib/quote-schema';

const quote = { id: '268f6bb7-fbf7-41ed-a25f-41cb230857b0', name: 'Cliente Teste', phone: '(21) 90000-0000', city: 'Rio de Janeiro', place: 'Condomínio', timeframe: 'Nas próximas semanas', details: 'Tapete com logotipo', solution: 'cas', material: 'per' };

describe('pii-zu quote requests', () => {
  it('uses the corrected business email', () => { expect(QUOTE_RECIPIENT).toBe('comercial.piizu@gmail.com'); });
  it('accepts a complete personalized rug quote', () => { expect(quoteSchema.safeParse(quote).success).toBe(true); });
  it('accepts every product line offered on the page', () => {
    for (const product of Object.keys(PRODUCTS)) expect(quoteSchema.safeParse({ ...quote, product }).success).toBe(true);
  });
  it('accepts the six solution segments and the earlier ones', () => {
    for (const solution of ['cond', 'esco', 'sala', 'come', 'indu', 'resi', 'quad', 'emp', 'esc', 'cas']) {
      expect(quoteSchema.safeParse({ ...quote, solution }).success).toBe(true);
    }
  });
  it('treats requests without a product as rug requests', () => {
    expect(quoteSchema.parse(quote).product).toBe('tapete');
  });
  it('keeps the request when a choice value is unknown, falling back to defaults', () => {
    expect(quoteSchema.parse({ ...quote, product: 'carro' }).product).toBe('tapete');
    expect(quoteSchema.parse({ ...quote, solution: 'gra' }).solution).toBe('come');
    expect(quoteSchema.parse({ ...quote, material: 'gra' }).material).toBe('per');
  });
  it('rejects an arbitrary email recipient from visitors', () => { expect(quoteSchema.safeParse({ ...quote, recipient: 'other@example.com' }).success).toBe(false); });
  it('accepts every answer, refusing only a fully empty form', () => {
    expect(quoteSchema.safeParse({ ...quote, phone: '123' }).success).toBe(true);
    expect(quoteSchema.safeParse({ ...quote, name: 'A', city: '', phone: 'zap da loja' }).success).toBe(true);
    expect(quoteSchema.safeParse({ ...quote, name: '', phone: '', city: '', details: '' }).success).toBe(false);
  });
  it('fits stored values to the database limits without losing what was typed', () => {
    const short = toStoredQuote(quoteSchema.parse({ ...quote, name: 'A', phone: '99998888', city: '' }));
    expect(short.row.name).toBe('A.');
    expect(short.row.phone).toBe('99998888 (incompleto)');
    expect(short.row.city).toBe('Não informado');
    const long = toStoredQuote(quoteSchema.parse({ ...quote, name: 'N'.repeat(150), phone: '1'.repeat(30) }));
    expect(long.row.name).toHaveLength(100);
    expect(long.row.phone).toHaveLength(25);
    expect(long.notes.join(' ')).toContain('N'.repeat(150));
    expect(long.notes.join(' ')).toContain('1'.repeat(30));
    for (const r of [short.row, long.row]) {
      expect(r.name.length).toBeGreaterThanOrEqual(2); expect(r.name.length).toBeLessThanOrEqual(100);
      expect(r.phone.length).toBeGreaterThanOrEqual(10); expect(r.phone.length).toBeLessThanOrEqual(25);
      expect(r.city.length).toBeGreaterThanOrEqual(2); expect(r.city.length).toBeLessThanOrEqual(120);
    }
  });
});