import { EmailAPIError } from '@lovable.dev/email-js';
import { QUOTE_RECIPIENT, quoteSchema } from './quote-schema';
import { sendTemplateEmail } from './email-templates/send-email';
import type { z } from 'zod';

const solutions = { emp: 'Empresa e comércio', esc: 'Creche e escola', cas: 'Casa e condomínio' };
const materials = { per: 'Personalizado', cap: 'Capacho personalizado', inf: 'Tapete infantil' };

// Notification failures must never undo a successfully saved customer request.
export async function notifyQuote(quote: z.infer<typeof quoteSchema>) {
  try {
    const result = await sendTemplateEmail('quote-notification', QUOTE_RECIPIENT, {
      templateData: { ...quote, solution: solutions[quote.solution], material: materials[quote.material] },
      idempotencyKey: `quote-notification-${quote.id}`,
      replyTo: QUOTE_RECIPIENT,
    });
    return { emailSent: result.sent };
  } catch (error) {
    // Log only the delivery state, not customer information or credentials.
    console.warn('Quote notification not sent:', error instanceof EmailAPIError ? error.code : 'send_failed');
    return { emailSent: false };
  }
}