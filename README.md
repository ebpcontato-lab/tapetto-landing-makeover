# Tapetto Landing Makeover

Monte uma landing page PERSONALIZANDO o template HTML que está no arquivo .zip anexo. O template já é uma página profissional pronta — design, animações e um componente interativo central — criada para o nicho "Marcenaria Autoral sob Medida". Seu trabalho é adaptá-la para o negócio abaixo, não redesenhá-la.

## Regras inegociáveis
1. O HTML do zip é a base única. Preserve a estrutura das seções, as fontes, as animações, o componente interativo e o CSS.
2. Troque somente: textos, imagens, cores (se indicado abaixo), links e as integrações listadas.
3. O resultado continua sendo HTML/CSS/JS puro, sem framework, publicável como arquivo estático (Cloudflare, Vercel, GitHub Pages).
4. Remova as tags <meta name="robots"> e <meta name="googlebot"> com noindex: a página final DEVE poder ser indexada.
5. Mantenha o botão flutuante de WhatsApp, o suporte a prefers-reduced-motion e o loading="lazy" com alt descritivo nas imagens.
6. Zero lorem ipsum e zero copy do nicho antigo sobrando. Página inteira em português do Brasil.

## O negócio
- Nome: Tapetto
- O que vende: Tapetes e Capachos Personalizados, Gramas Sintéticas
- Onde atua: Rio de Janeiro
- Público: Homens e mulheres acima de 30 anos
- Diferenciais reais:
  · Seu Tapete e Capacho produzido na maior indústria da América Latina, são mais de 48 anos atuando no mercado nacional.
- Oferta principal: AS MELHORES SOLUÇÕES EM TAPETES E CAPACHOS PERSONALIZADOS E PROTEÇÃO PARA PISOS
- Números e provas reais:
  · Seu tapete e capacho produzido na maior fábrica da América Latina!
  · Há mais de 48 anos atuando no mercado nacional.
  · Distribuidor com dezenas de clientes satisfeitos.
- Tom de voz: Próximo e acolhedor
- Objetivo da página: Formulário preenchido (contato ou orçamento). Todo CTA principal da página aponta para esse objetivo — mesmo rótulo, mesma ação, do topo ao rodapé.

## Copy
Reescreva toda a copy para este negócio mantendo o papel e o tamanho aproximado de cada bloco: headline continua sendo promessa forte de benefício, prova continua prova, FAQ responde objeções reais deste nicho. Não invente números que não estão neste briefing — onde faltar dado real, escreva sem número.

## Prova social
- Perfil no Google Meu Negócio: https://maps.app.goo.gl/jkLHsukCuMakfaU7A — abra o perfil e puxe de lá a nota média, o total de avaliações e 3 a 5 avaliações reais (primeiro nome + texto). Ponha a nota e o total perto dos depoimentos e nos selos de confiança. Se você não tiver acesso à web, use os números informados em provas e me avise que as avaliações ficaram pendentes.

## Identidade visual
- Cores: troque a cor de destaque do template pela da marca, SEM mudar layout, tipografia, espaçamentos ou animações. Cor principal: #0f766e.
  Regra de recoloração: troque o MATIZ, não a hierarquia. Cada elemento tem que manter a mesma força visual que tinha no template original — se um texto era colorido porém suave (opacidade baixa, tom dessaturado ou claro), ele continua suave na cor nova; só o que era vívido (botão principal, destaque de headline, selo) fica vívido. Na prática: leia a cor original de cada elemento, calcule a diferença de luminosidade e saturação dela para a cor de destaque original, e reproduza essa mesma diferença a partir da cor nova. Nunca pinte corpo de texto, legenda, borda ou fundo sutil com a cor cheia — é o erro mais comum e deixa a página gritada. Fundos, textos neutros (preto, branco, cinza) e a escala de cinzas do template permanecem como estão: a cor da marca entra onde já havia cor, e não em tudo.
- Logotipo: não há arquivo — escreva "Tapetto" em texto no nav, na mesma tipografia do template.
- Fotos: mantenha as do template, trocando apenas as que destoarem do novo nicho por outras coerentes de banco de imagem.

## Integrações
- WhatsApp: troque TODAS as ocorrências de 5511999999999 por 5521998146495 — links wa.me, botão flutuante e formulário.
- Formulário: o envio deve chegar no e-mail ebpcontato@gmail.com (use o backend da plataforma). Sem backend disponível, mantenha o comportamento do template: o submit abre o WhatsApp com a mensagem montada.

Depois de entregar, diga em uma linha quais variáveis de cor e quais blocos de texto eu edito para ajustar tom e copy sem quebrar o layout — cor e copy são as coisas que mais mudam depois.

## Entrega
Um único index.html funcional (com a pasta assets do zip), pronto para publicar. Antes de terminar, confira: todos os links de WhatsApp com o número novo, nenhum texto do nicho antigo, todas as imagens anexadas usadas, títulos sem quebra estranha no celular e o componente interativo funcionando.

This project was built with [Lovable](https://lovable.dev).

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/1e6323a4-925d-4f48-82e0-7addf415fbe8).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
