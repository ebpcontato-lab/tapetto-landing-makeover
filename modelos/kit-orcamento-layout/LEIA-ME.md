# Kit de orçamento e layout – pii-zü Pisos (EBP Potrique)

Padrão aprovado pelo Seu Zecones em 17/11/2026.

- `padrao.py`: layout de tapete de vinil (mockup com textura e furinhos, borda rebaixada 3 cm na cor do tapete, borda pintada por dentro, cotas, especificações, aviso em cobre). Use `mockup_real(mascara, cor_tapete, cor_tinta, larg, alt, saida, bcm=3|0)` + `layout_pdf(...)`.
  - Cor do tapete: amostra real da matéria-prima (`public/piizu/assets/img/cores/vinil-*.webp`).
  - Cor da tinta: `paleta_vinil.png` (29 cores).
- `orc.py dados.json saida.pdf`: orçamento de 1 proposta (A4) + manual de limpeza + 3 fotos.
- `orc2.py dados.json saida.pdf`: 2 orçamentos separados na mesma página (à vista em destaque, a prazo embaixo).
- `ov4.py`: exemplo completo de layouts (Ouro Verde).
- `fichas/`: fichas técnicas Gold e A/T já com logos pii-zü (esq.) e Kapazi Cooperkap-RJ (dir.). Juntar ao orçamento com pypdf = "orçamento completo".
- `exemplos/`: JSON dos orçamentos Viagem da Paz e Ouro Verde.

Os scripts usam caminhos /home/claude/orc e /home/claude/repo: copie esta pasta para /home/claude/orc e clone o repositório em /home/claude/repo.
