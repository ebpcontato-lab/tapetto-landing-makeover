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

### Pendências
- [ ] Seu Zecones enviar a lista de fotos do acervo para excluir (lixeira do Drive).
- [ ] Desligar os números nas fotos (`FOTO_NUM=false`) quando terminar a escolha.
- [ ] Pergunta frequente sobre bordas, quando chegar o arquivo de bordas.
