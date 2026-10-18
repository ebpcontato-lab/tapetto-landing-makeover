import { createFileRoute } from '@tanstack/react-router';
import { createClient } from '@supabase/supabase-js';
import type { Database } from '@/integrations/supabase/types';
import { quoteSchema } from '@/lib/quote-schema';

export const Route = createFileRoute('/api/public/quotes')({
  server: {
    handlers: {
      POST: async ({ request }) => {
        const headers = { 'Cache-Control': 'no-store' };
        const origin = request.headers.get('origin');
        if (!origin || origin !== new URL(request.url).origin) {
          return Response.json({ error: 'Solicitação não autorizada.' }, { status: 403, headers });
        }
        if (!request.headers.get('content-type')?.startsWith('application/json')) {
          return Response.json({ error: 'Formato inválido.' }, { status: 415, headers });
        }
        const body = await request.text();
        if (body.length > 12000) return Response.json({ error: 'Pedido muito longo.' }, { status: 413, headers });
        let input: unknown;
        try { input = JSON.parse(body); }
        catch { return Response.json({ error: 'Pedido inválido.' }, { status: 400, headers }); }
        const parsed = quoteSchema.safeParse(input);
        if (!parsed.success) return Response.json({ error: 'Confira nome, WhatsApp, cidade e os detalhes do pedido.' }, { status: 400, headers });

        const url = process.env['SUPABASE_URL'];
        const key = process.env['SUPABASE_PUBLISHABLE_KEY'];
        if (!url || !key) return Response.json({ error: 'Não foi possível registrar seu pedido. Tente novamente.' }, { status: 503, headers });
        // Use INSERT-only visitor permissions, never privileged credentials.
        const client = createClient<Database>(url, key, {
          auth: { persistSession: false, autoRefreshToken: false },
          global: {
            fetch: (input, init) => {
              const requestHeaders = new Headers(init?.headers);
              if (key.startsWith('sb_') && requestHeaders.get('Authorization') === `Bearer ${key}`) requestHeaders.delete('Authorization');
              requestHeaders.set('apikey', key);
              return fetch(input, { ...init, headers: requestHeaders });
            },
          },
        });
        const { error } = await client.from('quote_requests').insert(parsed.data);
        if (error && error.code !== '23505') {
          console.error('Quote request insert failed:', error.code);
          return Response.json({ error: 'Não foi possível registrar seu pedido. Tente novamente.' }, { status: 503, headers });
        }
        // Email delivery is not claimed until the owner configures a sender domain.
        return Response.json({ saved: true, emailSent: false }, { status: 201, headers });
      },
    },
  },
});