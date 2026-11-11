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

### Pendências
- [ ] Seu Zecones enviar a lista de fotos do acervo para excluir (lixeira do Drive).
- [ ] Desligar os números nas fotos (`FOTO_NUM=false`) quando terminar a escolha.
- [ ] Pergunta frequente sobre bordas, quando chegar o arquivo de bordas.
