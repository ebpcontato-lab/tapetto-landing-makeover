import { Body, Container, Head, Heading, Html, Preview, Section, Text } from '@react-email/components';
import type { TemplateEntry } from './registry';
import { QUOTE_RECIPIENT } from '@/lib/quote-schema';

interface Props {
  id?: string;
  name?: string;
  phone?: string;
  city?: string;
  place?: string;
  timeframe?: string;
  details?: string;
  solution?: string;
  material?: string;
}

function QuoteNotification(data: Props) {
  const fields = [
    ['Nome', data.name], ['WhatsApp', data.phone], ['Bairro/cidade', data.city],
    ['Destino do tapete', data.place], ['Prazo desejado', data.timeframe],
    ['Solução', data.solution], ['Material de interesse', data.material],
    ['Detalhes', data.details || 'Ainda estou definindo'], ['Pedido', data.id],
  ];
  return (
    <Html lang="pt-BR" dir="ltr">
      <Head />
      <Preview>Novo pedido de orçamento de tapete personalizado para a Tapetto.</Preview>
      <Body style={styles.body}>
        <Container style={styles.container}>
          <Text style={styles.brand}>Tapetto</Text>
          <Heading style={styles.heading}>Novo pedido de orçamento</Heading>
          <Text>Um visitante solicitou um orçamento de tapete personalizado.</Text>
          {fields.map(([label, value]) => (
            <Section key={label} style={styles.field}>
              <Text style={styles.label}>{label}</Text>
              <Text style={styles.value}>{value || 'Não informado'}</Text>
            </Section>
          ))}
        </Container>
      </Body>
    </Html>
  );
}

export const template = {
  component: QuoteNotification,
  subject: 'Tapetto — Novo pedido de orçamento de tapete personalizado',
  displayName: 'Pedido de orçamento',
  to: QUOTE_RECIPIENT,
  previewData: {
    id: 'exemplo', name: 'Cliente de exemplo', phone: '(21) 90000-0000', city: 'Rio de Janeiro',
    place: 'Empresa ou comércio', timeframe: 'Nas próximas semanas',
    solution: 'Empresa e comércio', material: 'Personalizado', details: 'Tapete com logotipo na entrada.',
  },
} satisfies TemplateEntry;

const styles = {
  body: { backgroundColor: '#ffffff', fontFamily: 'Arial, sans-serif', color: '#1F1813' },
  container: { maxWidth: '600px', padding: '32px 24px' },
  brand: { fontSize: '24px', color: '#8A2A10', fontWeight: 'bold' },
  heading: { fontSize: '24px', lineHeight: '32px' },
  field: { borderBottom: '1px solid #DED6C9', padding: '10px 0' },
  label: { color: '#6B5F52', margin: '0 0 4px', fontSize: '13px' },
  value: { margin: '0', fontSize: '16px', whiteSpace: 'pre-wrap' as const },
};