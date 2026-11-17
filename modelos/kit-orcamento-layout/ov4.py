from PIL import Image, ImageDraw, ImageFont
from padrao import mockup_real, layout_pdf, GF
s = 24
CLI = 'Condomínio Residencial Ouro Verde - Verônica'; DATA = '17/11/2026'
def mascara(wcm, hcm, k):
    iw, ih = wcm*s, hcm*s
    a = Image.new('L', (iw, ih), 255); d = ImageDraw.Draw(a)
    m = 3*s; d.rectangle([m, m, iw-m-1, ih-m-1], fill=0)
    fw, fh = iw - 2*m, ih - 2*m
    for fs in range(int(fh*0.45), 10, -2):          # maior fonte que cabe: 86% da largura útil
        f = ImageFont.truetype(GF + 'Poppins-Bold.ttf', fs); tr = fs*0.08
        wid = max(sum(d.textlength(c, font=f) for c in t) + tr*(len(t)-1) for t in ('RESIDENCIAL', 'OURO VERDE'))
        if wid <= fw*0.86 and fs*2.3 <= fh*0.9: break
    def tl(t, cy):
        ws = [d.textlength(c, font=f) for c in t]; x = iw/2 - (sum(ws)+tr*(len(t)-1))/2
        for c, w in zip(t, ws): d.text((x, cy), c, font=f, fill=255, anchor='lm'); x += w + tr
    tl('RESIDENCIAL', ih/2 - fs*0.62); tl('OURO VERDE', ih/2 + fs*0.62); return a
for W, H, k in [(120, 60, 1.55), (60, 40, 0.92)]:
    for reb in (True, False):
        nome = f'{W}x{H} - ' + ('BORDA REBAIXADA' if reb else 'BORDA PINTADA')
        tit = f'OURO VERDE {W}×{H} - MODELO ' + ('A (BORDA REBAIXADA + BORDA PINTADA)' if reb else 'B (SOMENTE BORDA PINTADA)')
        brd = ('Borda rebaixada com 3 cm de largura no contorno externo, na cor do tapete (sem tinta) + borda pintada com 3 cm de largura na área interna, na mesma cor do logo (Verde Floresta)'
               if reb else 'Somente borda pintada com 3 cm de largura em todo o contorno, na mesma cor do logo (Verde Floresta), sem rebaixo')
        spec = [('Produto', 'Tapete de vinil personalizado'), ('Matéria-prima', 'Vinil Gold (médio tráfego)'),
                ('Cor do tapete', 'Ouro'), ('Cor da tinta (logo e borda)', 'Verde Floresta'),
                ('Medida', f'{W} × {H} cm ({W} de largura × {H} de profundidade)'), ('Borda', brd), ('Quantidade', '28 unidades'),
                ('Arte', '"RESIDENCIAL OURO VERDE" centralizado'), ('Garantia', '12 meses contra defeitos de fabricação'),
                ('Prazo', 'Até 15 dias úteis para produção e entrega')]
        mk = mascara(W-6, H-6, k) if reb else mascara(W, H, k)
        mockup_real(mk, 'Ouro', 'Verde Floresta', W, H, f'm_{nome}.png', bcm=3 if reb else 0)
        layout_pdf(f'm_{nome}.png', tit, CLI, DATA, spec, f'LAYOUT OURO VERDE {nome}.pdf', f'LAYOUT OURO VERDE {nome}.jpg')
print('ok')
