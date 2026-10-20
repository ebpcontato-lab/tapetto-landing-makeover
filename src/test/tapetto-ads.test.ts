import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

const html = readFileSync('public/tapetto/index.html', 'utf8');

describe('Tapetto Google Ads tag (AW-17662893947)', () => {
  it('loads the Google tag for the configured account exactly once', () => {
    expect((html.match(/googletagmanager\.com\/gtag\/js\?id=AW-17662893947/g) || []).length).toBe(1);
    expect((html.match(/gtag\('config','AW-17662893947'\)/g) || []).length).toBe(1);
  });

  it('denies ad consent by default in regions that require consent', () => {
    expect(html).toContain("gtag('consent','default'");
    expect(html).toContain("region:['EEA','UK','CH']");
    expect(html).toContain("ad_storage:'denied'");
  });

  it('fires a conversion on form submission and WhatsApp clicks', () => {
    expect((html.match(/tapettoAds\(window\.__TAPETTO_ADS\.form\);/g) || []).length).toBe(2);
    expect(html).toContain('tapettoAds(window.__TAPETTO_ADS.whatsapp)');
    expect(html).toContain('a[href*="wa.me"]');
  });

  it('shows a regional cookie banner with a privacy policy and reopen link', () => {
    expect(html).toContain('id="cookieBanner"');
    expect(html).toContain('href="privacidade.html"');
    expect(html).toContain('id="ckPrefs"');
    expect(html).toContain('tapetto-cookie-consent-v1');
  });

  it('links a privacy policy page naming the data and recipients', () => {
    const policy = readFileSync('public/tapetto/privacidade.html', 'utf8');
    expect(policy).toContain('Google Ads');
    expect(policy).toContain('tapetto.cooperkap@gmail.com');
    expect(policy).toContain('Preferências de cookies');
  });
});
