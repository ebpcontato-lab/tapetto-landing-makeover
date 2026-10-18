import { beforeEach, describe, expect, it, vi } from 'vitest';
import { template } from '@/lib/email-templates/quote-notification';
import { notifyQuote } from '@/lib/quote-notification.server';
import { sendTemplateEmail } from '@/lib/email-templates/send-email';

vi.mock('@/lib/email-templates/send-email', () => ({ sendTemplateEmail: vi.fn() }));
const quote = {
  id: '268f6bb7-fbf7-41ed-a25f-41cb230857b0', name: 'Cliente Teste', phone: '(21) 90000-0000',
  city: 'Rio de Janeiro', place: 'Condomínio' as const, timeframe: 'Nas próximas semanas' as const,
  details: 'Tapete com logotipo', solution: 'cas' as const, material: 'per' as const,
};

describe('Quote email notification', () => {
  beforeEach(() => vi.clearAllMocks());
  it('sends all quote details only to the corrected business recipient', async () => {
    vi.mocked(sendTemplateEmail).mockResolvedValue({ sent: true });
    expect(template.to).toBe('tapetto.cooperkap@gmail.com');
    expect(await notifyQuote(quote)).toEqual({ emailSent: true });
    expect(sendTemplateEmail).toHaveBeenCalledWith('quote-notification', 'tapetto.cooperkap@gmail.com', {
      templateData: { ...quote, solution: 'Casa e condomínio', material: 'Personalizado' },
      idempotencyKey: `quote-notification-${quote.id}`, replyTo: 'tapetto.cooperkap@gmail.com',
    });
  });
  it('does not retry a suppressed recipient', async () => {
    vi.mocked(sendTemplateEmail).mockResolvedValue({ sent: false, reason: 'recipient_suppressed' });
    expect(await notifyQuote(quote)).toEqual({ emailSent: false });
    expect(sendTemplateEmail).toHaveBeenCalledTimes(1);
  });
  it('does not fail a saved request when email sending is unavailable', async () => {
    vi.mocked(sendTemplateEmail).mockRejectedValue(new Error('Unavailable'));
    expect(await notifyQuote(quote)).toEqual({ emailSent: false });
    expect(sendTemplateEmail).toHaveBeenCalledTimes(1);
  });
});