import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { LEGACY_SOLUTION, PRODUCTS, SOLUTIONS } from '@/lib/quote-schema';

const html = readFileSync('public/piizu/index.html', 'utf8');

function catalog(name: string): Array<{ id: string; pz?: string; sp?: string[][] }> {
  const literal = html.match(new RegExp(`var ${name} = (\\[[\\s\\S]*?\\n\\]);`))?.[1];
  if (!literal) throw new Error(`Missing catalog: ${name}`);
  return Function(`"use strict"; return (${literal});`)();
}

describe('piizu personalized-only catalog', () => {
  it('does not offer synthetic grass as a solution or material', () => {
    for (const name of ['AMB', 'MATS']) {
      const products = catalog(name);
      expect(products.length).toBeGreaterThan(0);
      expect(products.some((product) => product.id === 'gra')).toBe(false);
    }
  });

  it('offers personalization for every remaining solution and material', () => {
    for (const product of catalog('AMB')) {
      expect(product.sp?.some(([key, value]) => key === 'Personalização' && (value?.length ?? 0) > 0)).toBe(true);
    }
    for (const product of catalog('MATS')) {
      expect(product.pz?.length).toBeGreaterThan(0);
    }
  });

  it('offers in the page exactly the products the quote form accepts, with the same names', () => {
    const nichos = catalog('NICHOS') as unknown as Array<{ id: string; itens: Array<{ id: string; rotulo: string }> }>;
    const itens = nichos.flatMap((nicho) => nicho.itens);
    expect(itens.map((item) => item.id).sort()).toEqual(Object.keys(PRODUCTS).sort());
    for (const item of itens) expect(item.rotulo).toBe(PRODUCTS[item.id as keyof typeof PRODUCTS]);
  });

  it('has gallery photos for every product niche', () => {
    for (const nicho of catalog('NICHOS')) expect(html).toContain(`data-setor="${nicho.id}"`);
  });

  it('offers only solution segments the quote form accepts, each with a fallback for the old database check', () => {
    for (const segment of catalog('AMB')) {
      expect(Object.keys(SOLUTIONS)).toContain(segment.id);
      expect(LEGACY_SOLUTION[segment.id as keyof typeof SOLUTIONS]).toBeDefined();
    }
  });
});
