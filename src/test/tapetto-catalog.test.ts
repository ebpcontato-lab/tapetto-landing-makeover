import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

const html = readFileSync('public/tapetto/index.html', 'utf8');

function catalog(name: string): Array<{ id: string; pz?: string; sp?: string[][] }> {
  const literal = html.match(new RegExp(`var ${name} = (\\[[\\s\\S]*?\\n\\]);`))?.[1];
  if (!literal) throw new Error(`Missing catalog: ${name}`);
  return Function(`"use strict"; return (${literal});`)();
}

describe('Tapetto personalized-only catalog', () => {
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
});