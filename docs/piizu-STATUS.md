# pii-zü — registro único das conversas (Fotos × Landing page)

Toda conversa que mexer no site ou nas fotos da pii-zü segue estas regras:

1. **Antes de começar:** `git pull` no `main` e ler este arquivo.
2. **Depois de cada mudança:** commit + push na hora (nada fica parado só na máquina).
3. **Registrar aqui** o que foi feito e o que ficou pendente, com data.
4. Fotos: a conversa **Fotos** trata e organiza; a conversa **Landing page** decide onde cada foto entra. Nenhuma das duas troca foto do site sem registrar aqui.
5. Pacote estático (ZIP): sempre gerado a partir do `main` atualizado, com o próximo número (c6, c7…).

## Situação em 10/11/2026

### Conversa Fotos
- Pasta do Drive "FOTOS SITE PII-ZU": 103 repetidas foram para a lixeira (98 que já estavam no site/biblioteca + 5 repetidas entre si). Ficaram 285.
- 267 fotos da landing page tratadas (luz, contraste, cor, nitidez), mesmos nomes e tamanhos — commit `f5aa142`.
- 49 fotos novas tratadas, formato 4:5 (1080×1350, WebP): `public/piizu/assets/biblioteca/tratadas/piizu-T01…T49.webp`.
- **10/11:** as 49 entraram na Galeria (depois das 12 que já estavam), como `assets/img/galeria/tratada-T01…T49.webp` (864×1080), com números nº 230 a nº 278.
  - Página de escolha (antes/depois): https://claude.ai/artifact/9NDPcrHCCU88h9ed9sz3fR
- Acervo completo numerado A001–A268 (todas tratadas) para o Seu Zecones marcar o que sai: https://claude.ai/artifact/49uVgjAkrPh82AAV8ZK9NK
- **10/11:** foto nº 145 (Birutt@o, `portfolio-124.webp`) retirada do site — tinha a marca de outra empresa ("Alovisi Tapetes") no tapete.
- Pacote estático mais recente: `piizu-site-2026-11-10-c8.zip`.
- **10/11 (noite):** as fotos da pasta "FOTOS SITE PII-ZU" entraram no site. Folha numerada da pasta (nº 1–285): https://claude.ai/artifact/5J2HCTQfv6Nj9Rr6JdmdqT
  - 69 já estavam no site (iguais ou a mesma foto em outro ângulo) e ficaram de fora. Em 2 delas a foto da pasta era mais nítida e substituiu a do site: `tratada-T23.webp` (AMZ Tropical) e `tratada-T29.webp` (Maxi Farma).
  - 194 novas, tratadas no mesmo padrão (4:5, 864×1080, foto inteira com fundo desfocado), em `assets/img/galeria/tratada-F###.webp` (### = número da folha). Números no site: nº 279 a nº 472.
  - 160 Tapetes/Capachos foram para a Galeria e para "Compare os modelos", cada uma no seu material: Vinil Gold 52, Vinil A/T 4, Cleankap 85, Waterkap 7, Duo 6. 6 Capachos com aparência de fibra de coco (folha nº 5, 90, 117, 118, 119, 268) entraram só na Galeria, sem modelo.
  - 34 de outros produtos ficaram guardadas no `<template id="todasFotos">` com o setor certo (piso-piscina 28, capa-elevador 4, piso-rubberkap 2). Não aparecem na página porque hoje ela não tem seção desses produtos.
  - **10/11 (23h):** novo grupo em "Compare os modelos" (mesma dobra): **Áreas Molhadas ou Úmidas — Pisos vazados**, com W-Kap (10 fotos), Acquakap (4), S-Kap (8) e H-Kap (6), item novo na lista de linhas e 4 opções novas no formulário. Espaços da seção apertados no computador para caber na dobra (1536×864 e maiores).
  - Não entraram: 4 fotos HDR de 6–7 MB (folha nº 213–216), grandes demais para o conector do Drive, e 18 fotos com menos de 65 KB (resolução baixa).

## Situação em 11/11/2026

### Conversa Landing page
- **Espaço Cleankap ("Compare os modelos") completado com as fotos da pasta "FOTOS SITE PII-ZU":** as 69 fotos da pasta que já estavam no site (repetidas, ficaram de fora em 10/11) só apareciam na Galeria e nas Soluções, em nenhum modelo. Conferidas uma a uma: **33 são Cleankap** e entraram no Cleankap (de 87 para 120 fotos), sem arquivo novo, usando as fotos que já estavam no site:
  - folha nº 21, 25, 27/121, 31, 38, 43, 46, 47, 60/184, 63, 70, 73, 75, 76, 78, 82, 95, 96, 127, 132, 137, 139, 142, 158, 159, 160, 177, 181, 187, 209, 212, 219, 220 → `tratada-T04, T05, T08, T09, T12, T13, T14, T17, T21, T22, T24, T25, T26, T28, T30, T31, T34, T35, T37, T38, T39, T42, T43, T48, T49` e `portfolio-002, 007, 010, 025, 070, 113, 120, 161`.
  - Ficaram fora do Cleankap as repetidas de vinil (nº 6, 18, 26, 40, 41, 52, 57, 64, 66, 67, 74, 88, 110, 134, 135, 145, 164, 173, 196, 197, 199, 200, 207), fibra de coco (257, 261), capa de elevador (192, 193, 203, 205), piso laminado (2) e 4 com textura duvidosa (9 Share, 143 Garden Center, 172 t:me, 186 CCAA).
- As 22 fotos da pasta sem miniatura (4 HDR de 6–7 MB e 18 com menos de 65 KB) continuam fora do site; não deu para conferir se alguma é Cleankap.

### Conversa Fotos (11/11)
- Fotos **nº 2** (Super Essências, `tapete-super-essencias.webp`) e **nº 3** (Hipermais Bem-Vindo, `tapete-hipermais-bem-vindo.webp`) retiradas do site, de todos os lugares (Galeria, quadro do topo, Soluções e Cleankap), a pedido do Seu Zecones. Arquivos mantidos no repositório.
- **Logo novo "pii-zü PISOS"** (balão laranja + palavra pii-zü PISOS) aplicado no site: topo, rodapé, ícone da aba (favicon), ícone do celular e imagem de compartilhamento (WhatsApp/Facebook). Arquivos em `assets/img/marca/piizu-pisos-*.svg` e `piizu-balao-laranja.svg`; cópias em PNG em `assets/biblioteca/logos/`. Os logos antigos (`piizu-grafite-prata-cobre.svg`, `piizu-horizontal-*`) não são mais usados na página. **Daqui pra frente, usar só o logo novo.**
- **Topo (11/11):** texto "Nosso grande diferencial Além de ser KAPAZI? … Distribuidor Autorizado Ind. Kapazi RJ." foi para **baixo da foto** do topo; o botão "Quero uma solução assim!" ficou logo abaixo de "Seu Personalizado produzido nas linhas Superiores…". Foto do topo um pouco menor no computador para tudo caber na primeira tela.
- **Topo reorganizado (11/11, padrão landing page):** título → "Nosso diferencial: direto da Indústria Kapazi, você recebe exatamente o que comprou." + 2 itens (✔ só linhas superiores Gold e A/T; ✖ não usamos Vinil Silver: custa menos, mas dura bem menos) → botão "Quero uma solução assim!" → estrelas Kapazi + "Pode confiar: aqui é pii-zü Pisos, Distribuidor Autorizado Ind. Kapazi RJ." O texto que estava embaixo da foto saiu (foi resumido nesses itens); foto do topo voltou ao tamanho normal. Aviso de cookies menor no celular.

- **Exclusão do acervo (11/11, noite):** Seu Zecones marcou na página do acervo A001–A268 as fotos 6, 23, 24, 28, 31, 35, 38, 40, 65, 128, 151, 167, 170, 171. Foram para a lixeira do Drive e saíram do site (Galeria, Compare, quadro do topo). Correspondência: A006=folha 6 (T01), A023=folha 27 (T07), A024=folha 28 (F028), A028=folha 32 (F032), A031=folha 35 (F035), A035=folha 39 (F039), A038=folha 42 (F042), A040=folha 44 (F044), A065=folha 70 (T21), A128=folha 135 (T33), A151=folha 159 (T38), A167=folha 176 (F176), A170=folha 180 (F180), A171=folha 181 (T42). **Atenção:** a página do acervo (A001–A268, https://claude.ai/artifact/49uVgjAkrPh82AAV8ZK9NK) e a folha numerada (1–285, https://claude.ai/artifact/5J2HCTQfv6Nj9Rr6JdmdqT) têm numerações diferentes — A-número ≠ número da folha ≠ nº no site.

- **12/11:** "a mais bem aprovada" → "a mais bem **avaliada** no ReclameAqui e no Google". Quadro de fotos do topo no maior tamanho possível: setas agora ficam **por cima da foto**; no computador a coluna da foto ficou mais larga e a foto ocupa a altura da primeira tela (1366×768: 437→649 px de altura); no celular a foto ocupa a largura toda (342×428 em 390 px).

- **12/11 — LANDING ENXUTA PARA TRÁFEGO PAGO** (pedido do Seu Zecones). Antes, a versão completa e todo o conteúdo foram guardados como **"projeto site pii-zü"**: `modelos/projeto-site-piizu/` (index.html + CONTEUDO.md com todos os textos e lista de fotos) e branch `projeto-site-piizu`. O que mudou na página:
  - menu do topo escondido (só logo, Kapazi, selo e botão Orçamento);
  - faixa de autoridade virou 3 números curtos (48+ anos · Nº 1 da América Latina · Com a sua marca);
  - "Nossas Soluções" virou "Escolha pelo tipo de entrada" com 2 opções + "Na dúvida? A gente indica"; **Áreas Molhadas saiu** de Compare os modelos (fica para página própria);
  - seção "Soluções orientadas e guiadas" escondida (`#projetos hidden`, o HTML ficou para o script);
  - Galeria com as **20** melhores fotos (antes 199); números das fotos **desligados** (`FOTO_NUM=false`);
  - Dúvidas: 5 curtas (logo, escorrega, limpeza, prazo, preço);
  - Orçamento: "Como funciona" em 3 passos; formulário com Nome, WhatsApp, Para onde é e Mensagem (opcional). Linha, Bairro e Quando precisa continuam no HTML, escondidos, para não quebrar o envio; a mensagem do WhatsApp agora leva "Para onde é" e não leva mais a "Solução" da seção escondida;
  - sem numeração "01 / 02 /…"; título e descrição do Google/WhatsApp agora falam de **Tapetes e Capachos** (sem grama/piscina). Regra: manter sempre **"Tapete e Capacho"** nos textos (Capacho é muito buscado).
  - Página: ~1.200 → ~470 palavras.

- **12/11 (noite):** diferencial do topo reescrito: "Nosso diferencial: linhas Alto Padrão e Premium, direto da Indústria Kapazi. Aqui seu Tapete ou Capacho dura muito mais." ✔ Produzimos só em Vinil Gold (médio tráfego) e Vinil A/T (alto tráfego). ✖ Muitos fornecedores usam o Vinil Silver: custa menos, mas dura bem menos.

- **13/11 — fotos reduzidas (conversa Landing page):** completada a redução da landing enxuta.
  - Quadro do topo: de 165 para as **mesmas 20 fotos da Galeria** (lê `#galTr`, não mais o `<template>`).
  - "Ver fotos" de Compare os modelos, conferido foto a foto pelo material: **Vinil Gold 12** (de 47), **Vinil A/T 6**, **Cleankap 12** (de 110), **Waterkap 3** (de 7), **Duo 6** (de 8).
  - Correções de material: F130 (Cleankap) saiu do Waterkap; F178 (quadriculado = Waterkap) saiu do Duo e foi para o Waterkap; F037 (listrado), F053 (placa de borracha) e F163 (trançado marrom) saíram do Waterkap por não serem claramente Waterkap; F217 (arte de catálogo com texto) saiu do Cleankap; F228 (estampado liso) e F222 (imagem de computador) fora do Vinil Gold.
  - Os arquivos e o `<template id="todasFotos">` continuam no projeto.

- **13/11 (tarde) — conversa Landing page, a pedido do Seu Zecones:**
  - Bordas: Flex = "Todos os modelos, exceto fibra de coco", com novo texto (supermercados, farmácias, idosos, carrinhos, alto tráfego); Rebaixada = "borda de 3 cm… Médio e Alto tráfego"; Unik = "Para varandas e entradas" (sem sacadas; Cleankap não tem mais Unik); nota: todos os Tapetes e Capachos têm costado antiderrapante. Fotos das bordas com **lupa** (abrem ampliadas).
  - **Pendente:** fotos do **catálogo** Kapazi de cada borda ao lado da foto real — os PDFs de bordas não estão no repositório.
  - Dúvida nova 07 "Quais tipos de borda?" (Quanto custa passou a 08).
  - "Dupla Função" no estilo do "Linha Vinil" + frase: Dupla Função (Cleankap, Waterkap, Duo) tem vida útil muito maior que o vinil.
  - Topo: "… (alto tráfego). Tapetes produzidos com matéria-prima virgem."
  - Como funciona, passo 3: "Todo processo de produção é feito na Indústria Kapazi e entregamos pronto para uso."
  - **Selo sempre com o texto "Distribuidor autorizado Indústria Kapazi"** (topo, rodapé e orçamento); no celular o selo + texto fica numa faixa abaixo dos logos no topo. Faixa com os 3 logos (pii-zü cobre, Kapazi Cooperkap, selo) também na seção de orçamento.

- **13/11 (noite) — tag do Google Ads em todas as páginas:** /site, /site/areas-molhadas, /condominios, /grama-sintetica e /piizu/privacidade.html estavam sem a tag do Google (AW-17662893947) e sem o Pixel da Meta — o Google Ads acusou "site sem tag". Agora todas têm o mesmo bloco do /piizu; nas que têm WhatsApp/formulário, a conversão Contato e o Lead disparam no clique do WhatsApp e no botão do formulário. **Regra: toda página nova leva esse bloco** (ver AGENTS.md).

- **13/11 (noite) — Google (busca):** criado `public/sitemap.xml` (landing /piizu/index.html e privacidade) e `Sitemap:` no robots.txt; redirecionamento de piizu.com.br/ para a landing passou a ser **301 (permanente)**. As prévias (/site, /condominios, /grama-sintetica, /site/areas-molhadas) seguem com noindex — ao publicar de verdade, tirar o noindex e incluir no sitemap. Pendente com o Seu Zecones: verificar o domínio no Google Search Console e enviar o sitemap.

### Pendências
- [ ] Seu Zecones enviar a lista de fotos do acervo para excluir (lixeira do Drive).
- [ ] Desligar os números nas fotos (`FOTO_NUM=false`) quando terminar a escolha.
- [ ] Pergunta frequente sobre bordas, quando chegar o arquivo de bordas.

## Projeto site completo pii-zü (iniciado 12/11/2026)
- Modelo no canvas Design: https://claude.ai/artifact/DiFCmM9AwmEGNU53XqBoeY ("projeto site pii-zü — modelo")
- 3 telas: Home (6 categorias: Tapetes e Capachos, Grama Sintética, Carpetes, Piso Vinílico, Áreas Molhadas, Quadras Poliesportivas), Landing Grama Sintética (tráfego pago, sem menu) e modelo de página de categoria (Áreas Molhadas).
- Visual: mesmo da landing (grafite #202328, cobre, laranja #BF561C, Fraunces + Inter, logo "pii-zü PISOS").
- Faltando: fotos de carpete, mais fotos reais de grama e piso vinílico; textos S-Kap/H-Kap (fichas técnicas); grama 20 mm x 30 mm (uso indicado); se a pii-zü instala a grama.
- 12/11: incluída a Capa de Elevador Liftkap (7ª categoria) e a seção "Para condomínios residenciais" na Home — condomínios residenciais são público foco do site.
- 13/11: criada a Landing Condomínios (síndicos e administradoras, tráfego pago, sem menu): kit completo por área, destaque Liftkap, por que a pii-zü, como funciona, dúvidas e formulário com checklist de itens. Home linka para ela.
- 13/11 — regras comerciais confirmadas pelo Seu Zecones (usar em todo o site):
  - Visita técnica com especialista, sem custo.
  - Emitimos nota fiscal.
  - Pagamento à vista com desconto de 5% a 7%.
  - Prazo: itens personalizados (medidas + logotipo) até 15 dias úteis; demais (grama, pisos para área molhada/úmida, laminados Bus/Liso/Moeda/Colmeia, fitas antiderrapantes e de demarcação etc.) até 5 dias úteis.
  - Grama Sintética: a pii-zü faz a instalação. Alturas: 12 mm decorativa; 20 e 30 mm recreativa (jardim, quintal, entorno de piscina); 50 mm campo de futebol profissional e esportes.
  - Áreas molhadas (W-Kap, Acquakap, S-Kap, H-Kap): entorno de piscinas, saunas, vestiários de academias e clubes, banheiros infantis de escolas e creches, indústrias. Textos S-Kap/H-Kap tirados das fichas técnicas.
  - Próximo: Seu Zecones vai montar um NOVO ACERVO com as melhores fotos (inclusive carpete) e pedir para atualizar todos os projetos com ele. Hoje não há nenhuma foto de carpete no repo nem no Drive.
- A landing de Tapetes e Capachos atual segue como está; o site novo não mexe nela.

- 13/11 — Fichas técnicas Kapazi lidas (pastas do Drive enviadas pelo Seu Zecones) e resumidas em `modelos/projeto-site-piizu/FICHAS-TECNICAS.md`. Usar esse arquivo como fonte dos textos técnicos de todos os projetos. Já aplicado no modelo do site (Áreas Molhadas, Grama, Home, Condomínios). Atenção: W-Kap é rolo de 1,20 x 10 m (4 mm) e Acquakap é o modular 30 x 30 cm. Ficha do Laminado Colmeia não veio.
- 13/11 — Regra do Seu Zecones: no site, só o essencial de cada ficha (o que é + onde usar, 1 linha). Nada de medidas, cores, rolos ou garantia nos cards. O FICHAS-TECNICAS.md fica como consulta interna.
- 13/11 — Correções do Seu Zecones: W-Kap é só em placas modulares (todas as cores), não rolo. Laminado Colmeia: sem ficha, mesma composição, rolo nas mesmas dimensões. Vinil Silver/Light/Pintado/Vulcanizado: fora dos personalizados, mas citar no site como venda por rolo. Wind Banner saiu de linha.
- 13/11 (conversa Landing) — Landing: novas dúvidas 04 "Tem garantia?" (até 12 meses; Gold em tráfego médio, A/T em alto tráfego) e 05 "Serve para piscina e área molhada?" (piscinas, saunas, vestiários, banheiros, lavanderias — W-Kap e S-Kap); Cleankap ganhou "fica rente ao chão e não enrosca na porta". Dúvidas agora são 7. ZIP c17.
- 13/11 — Páginas novas no ar como PRÉVIA (noindex, sem tags de anúncio, formulário abre o WhatsApp): piizu.com.br/site/ (Home), /site/areas-molhadas/, /grama-sintetica/ e /condominios/. Arquivos em public/site, public/grama-sintetica, public/condominios; imagens em public/novas/img. A raiz piizu.com.br continua na landing de Tapetes e Capachos (anúncios). Canvas de design segue como referência.
- 13/11 — REGRA do Seu Zecones para o NOVO ACERVO de fotos (Drive): usar SÓ no site e nas landings novas (Grama, Condomínios, Áreas Molhadas etc.), escolhendo as de melhor qualidade. NÃO colocar na landing de Tapetes e Capachos (/piizu): para ela, ele vai escolher as fotos uma a uma.
- 13/11 — "Matéria-prima virgem" adicionado (Vinil Gold e A/T): landing /piizu (hero, mesma linha, dobra conferida), /site e /condominios, e canvas. Fonte da Kapazi pendente (Seu Zecones vai pedir). Tapete Urban retirado do portfólio. ZIP c18.

## 13/11/2026 — Landing Tapetes e Capachos enriquecida (c19)
- Novo bloco aberto "Escolha a borda" (#bordas) em #materiais: Flex (Vinil Gold, Vinil A/T obrigatória, Cleankap, Duo), Rebaixada (Vinil Gold), Unik (Cleankap, Duo), Sem borda (Vinil Gold, Cleankap, Duo). Vulcanizada fora (Vinil Vulcanizado não é usado em personalizados).
- Foto aérea da fábrica Kapazi (assets/img/fabrica-kapazi.webp) na faixa #autoridade; também no site (/site e /condominios, /novas/img/fabrica-kapazi.webp).
- Novas fotos no "Compare os modelos": Vinil Gold (Unique Residence, redondo), Cleankap (Upper, Royal, Prospère, Pesca&Cia, Bom Tom), Duo (entrada). 4 delas também na galeria.
- Dobra conferida (desktop e celular), sem erro de JS. ZIP piizu-site-2026-11-13-c19.zip.
- Correção do Seu Zecones (13/11): Borda Unik somente no Tapete Duo (foto trocada para o Duo). Borda Vulcanizada entra para Vinil Gold e Vinil A/T (foto: vinil açougue supermercado). Flex sem a nota "obrigatória". Grade de bordas agora com 5 cards (3+2 no computador, 2 por linha no celular). ZIP c20.
- Correção 2 (13/11, 12h24): Rebaixada e Vulcanizada = todos os Vinil, exceto Silver. Flex = Vinil, Cleankap, Duo e Waterkap Elite. Nova borda Pintada = Vinil e Cleankap. Nota: no Vinil e no Cleankap dá para combinar duas bordas no mesmo Tapete ou Capacho. Waterkap no Compare ganhou "Nova linha Waterkap Elite, mais encorpada, com borda Flex". 6 cards (3x2). ZIP c21.
- Correção 3 (13/11, 12h29): Sem borda disponível em todos os modelos (não é o indicado, fica a critério do cliente). ZIP c22.

## 13/11/2026 13h20 — c24
- Waterkap, Waterkap Elite e Duo em negrito cobre (igual Vinil e Cleankap) na linha "Retém a sujeira e a água".
- Novo quadro "Waterkap Elite" (tag Novo) no Compare, com 4 fotos (Drive WATERKAP, arquivos 190284/288/291/293-1600-auto: preto, grafite, marrom, hall). Dupla Função agora "4 opções".
- Fotos com ênfase na borda Flex (Drive "Cleankap com borda flex"): CDL Paverama (azul), SIR, D'Rosi, A4 Promaq, Catedral — no Cleankap do Compare e na galeria; card Flex do catálogo de bordas com a borda azul da CDL.
- Vulcanizada com o texto do PDF "Bordas - Vinil" (vinil recortado e preenchido com outra cor, como quebra-cabeça).
- Quadros de fotos (Ver fotos e galeria) mostram a pontinha da próxima foto também no computador.
- PDFs "Bordas - Vinil/Cleankap/Duo" (12 MB) não baixam pelo conector (limite 10 MB): fotos de Rebaixada/Vulcanizada/Pintada pendentes.

## 13/11/2026 13h40 — c25
- Fotos ruins de borda Flex (CDL, SIR, D'Rosi, A4, Catedral) retiradas. Cards de borda agora com Tapete inteiro: Flex = Ralpha Posto (vinil, flex cinza), Rebaixada = Almeida (vinil azul), Pintada = Influ Church (borda dourada), Unik = Duo cinza no piso. Fontes: Drive pasta Vinil (16c5s…) e Duo (1d8pS…).
- Compare: Vinil Gold + Automar e Cléo Modas; Cleankap + Satélite (flex), Morana, Rio da Vida; Duo + ambientado, provador, elevador. Tudo com Tapete inteiro, sem corte.
- Waterkap Elite: texto pela Tabela 08/10 (o mais robusto da linha; mais denso, pesado e resistente; preto, grafite e marrom; borda Flex). Fotos do Elite ainda a confirmar (vieram da pasta WATERKAP, 190xxx-1600-auto).
- Computador: sem pontinha da próxima foto, setas menores (30px). Celular: primeiro quadro (topo) agora mostra a pontinha da próxima foto e passa com toque nela.
- 13h49: Borda do açougue = Rebaixada (card Rebaixada usa a foto do açougue). Vulcanizada sem foto até receber prints dos PDFs Bordas (12 MB, conector limita 10 MB; navegador do app não pôde ser ligado nesta conversa). ZIP c26.

## 13/11/2026 — Galeria: +98 fotos fortes da pasta "FOTOS SITE PII-ZU"
- Adicionadas 98 fotos tratada-F (tapetes cheios, coloridos, com logo/fachada) ao #galTr, depois das 27 fotos de destaque. Galeria/quadro do topo agora com 141 fotos.
- Ficaram de fora só closes de textura, amostras, capachos de catálogo genéricos e fotos fracas.
- 13/11 (2): removidas de todo o site (galeria + abas de materiais) as 12 fotos que o cliente mandou excluir (2,3,7,8,9,11,13,17,19,25,26,27 da folha de 28) e a cópia F233 do Home Sweet Home. Frase "Nossos Tapetes e Capachos personalizados no Rio de Janeiro e por todo Brasil" subiu para baixo do quadro do topo; seção #galeria escondida (fica só no DOM como fonte do quadro); link do menu aponta para #fotos.
- 13/11 (3): Compare os modelos ganhou "Capachos de Fibra de Coco" (6 fotos) e "Outras soluções" (Capa Liftkap 7 fotos; Pisos para Playground e Áreas Kids 12 fotos), com opções no formulário. Números nas fotos LIGADOS de novo (FOTO_NUM=true) até o cliente definir as fotos; fotos sem número receberam nº 473–504. Foto 10 excluída (confirmado). Foto 170 (portfolio-158) não aparece no site hoje. Pendente: as 4 fotos pesadas da pasta (nº 213–216) — cliente vai mandar depois.
- 13/11 (4): DECISÃO DO CLIENTE — a landing piizu.com.br fica só para Tapetes e Capachos (Vinil Gold, Vinil A/T, Cleankap, Duo, Waterkap clássico, Waterkap Elite e Fibra de Coco). Saíram "Outras soluções" (Liftkap e playground) e as opções de áreas molhadas, Liftkap e playground do formulário; entrou a opção Waterkap Elite no formulário. Pisos para áreas molhadas, Playkap, Liftkap e gramas vão para as próximas páginas.
- 13/11 (5): dúvida 05 trocada — sai "piscina e área molhada" (W-Kap/S-Kap); entra "E em dia de chuva, com o piso molhado?" destacando os Dupla Função (Cleankap, Waterkap, Waterkap Elite, Duo).
