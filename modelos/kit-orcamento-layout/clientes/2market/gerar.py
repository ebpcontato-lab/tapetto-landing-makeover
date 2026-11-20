import sys, math, subprocess
sys.path.insert(0, '/home/claude/orc')
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import padrao as P
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader, simpleSplit

CORES = '/home/claude/repo/public/piizu/assets/img/cores/'
CLI = '2MARKET - Seu mercadinho 24h (Pilares - RJ)'; DATA = '20/11/2026'
W, H, PX = 100, 60, 20

# ---- logo: separa amarelo e laranja ----
lg = np.asarray(Image.open('/mnt/user-data/uploads/fce6d28b-image.jpg').convert('RGB')).astype(float)
mx = lg.max(2); ys, xs = np.where(mx > 70)
y0, y1, x0, x1 = ys.min() - 4, ys.max() + 5, xs.min() - 4, xs.max() + 5
lg = lg[y0:y1, x0:x1]; mx = lg.max(2)
alpha = np.clip((mx - 40) / 160, 0, 1)
ratio = lg[..., 1] / np.maximum(lg[..., 0], 1)
amarelo = alpha * (ratio > 0.62); laranja = alpha * (ratio <= 0.62)
LOGO = [Image.fromarray((amarelo * 255).astype(np.uint8)), Image.fromarray((laranja * 255).astype(np.uint8))]
LR = lg.shape[1] / lg.shape[0]

def mascaras(iw, ih, faixa_px, respiro=0.84):
    """retorna máscaras (amarelo, laranja) da área interna; faixa_px = borda pintada/vulcanizada em laranja"""
    my = Image.new('L', (iw, ih), 0); mo = Image.new('L', (iw, ih), 0)
    if faixa_px:
        d = ImageDraw.Draw(mo); d.rectangle([0, 0, iw - 1, ih - 1], fill=255)
        d.rectangle([faixa_px, faixa_px, iw - faixa_px - 1, ih - faixa_px - 1], fill=0)
    fw, fh = iw - 2 * faixa_px, ih - 2 * faixa_px
    lw = fw * respiro; lh = lw / LR
    if lh > fh * 0.80: lh = fh * 0.80; lw = lh * LR
    lw, lh = int(lw), int(lh); ox, oy = (iw - lw) // 2, (ih - lh) // 2
    for src, dst in zip(LOGO, (my, mo)):
        r = src.resize((lw, lh), Image.LANCZOS); cur = dst.crop((ox, oy, ox + lw, oy + lh))
        dst.paste(Image.fromarray(np.maximum(np.asarray(cur), np.asarray(r))), (ox, oy))
    return [np.asarray(m).astype(float)[..., None] / 255 for m in (my, mo)]

def amostra(nome):
    a = np.asarray(Image.open(CORES + nome + '.webp').convert('RGB')).reshape(-1, 3).astype(float)
    l = a.sum(1); return a[l > np.percentile(l, 50)].mean(0)

def textura_cleankap(w, h):
    t = np.asarray(Image.open(CORES + 'cleankap-preto.webp').convert('L')).astype(float)
    t = np.tile(t, (h // t.shape[0] + 1, w // t.shape[1] + 1))[:h, :w]
    n = np.asarray(Image.effect_noise((w, h), 30).convert('L')).astype(float)
    lum = 0.6 * t / t.mean() + 0.4 * n / n.mean()
    return np.asarray(Image.fromarray(np.clip(lum * 120, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7))).astype(float)[..., None] / 120

def render(linha, borda, out):
    """linha: gold_pintado | gold_vulc | clean ; borda: pintada | vulcanizada | flex"""
    bcm = 3 if borda in ('flex', 'rebaixada') else 0
    Wp, Hp, BP = W * PX, H * PX, bcm * PX; iw, ih = Wp - 2 * BP, Hp - 2 * BP
    faixa = 0 if borda == 'flex' else 3 * PX
    ay, ao = mascaras(iw, ih, faixa)
    if linha == 'clean':
        base = amostra('cleankap-preto'); cy, co = P.cor_tinta('Amarelo'), P.cor_tinta('Laranja')
        lum = textura_cleankap(Wp, Hp)[BP:Hp - BP, BP:Wp - BP]
    else:
        base = P.cor_materia('Preto')
        if linha == 'gold_vulc': cy, co = P.cor_materia('Amarelo'), P.cor_materia('Laranja')
        else: cy, co = P.cor_tinta('Amarelo'), P.cor_tinta('Laranja')
        lum = P.coil2(Wp, Hp)[BP:Hp - BP, BP:Wp - BP, None]
    lum = lum / lum.mean()
    col = base[None, None, :] * (1 - ay - ao).clip(0, 1) + cy[None, None, :] * ay + co[None, None, :] * ao
    fin = col * lum; m = fin.max(2, keepdims=True); fin = np.where(m > 255, fin * 255 / np.maximum(m, 1), fin)
    if linha == 'gold_vulc':   # emenda da vulcanização: contorno fino escuro entre as peças
        edge = np.asarray(Image.fromarray(((ay + ao)[..., 0] * 255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1))).astype(float)[..., None] / 255
        fin = fin * (1 - 0.35 * np.clip(edge * 3, 0, 1))
    pre = np.clip(fin - 13.5, 0, 255)
    bord = tuple(int(v) for v in P.cor_tinta('Ouro') * 0.9) if borda == 'flex' else tuple(int(v * 0.94) for v in base)
    g = vars(P); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.75)
    try: P.mockup(Image.fromarray(pre.astype(np.uint8)), W, H, bord, out, px=PX, bcm=bcm)
    finally: g['coil'] = old

def layout_pdf(mock_png, titulo, sub, spec, out_pdf, out_jpg):
    PW, PH = landscape(A4); M = 32; navy = HexColor('#1B2A4A'); gr = HexColor('#444444'); cobre = HexColor('#BF561C')
    c = canvas.Canvas(out_pdf, pagesize=landscape(A4)); c.setTitle(titulo)
    for path, right in [(P.L + 'biblioteca/logos/piizu-pisos-horizontal.png', False), (P.L + 'img/marca/kapazi-cooperkap-rj-grafite.png', True)]:
        im = ImageReader(path); w, h = im.getSize(); lh = 46; lw = lh * w / h
        c.drawImage(im, PW - M - lw if right else M, PH - 14 - lh, lw, lh, mask='auto')
    c.setFillColor(navy); c.setFont('B', 12); c.drawCentredString(PW / 2, PH - 26, 'EBP POTRIQUE LTDA')
    c.setFont('R', 7.8); c.setFillColor(gr)
    for i, t in enumerate(['CNPJ 50.639.581/0001-84 | I.E. 12.857.454 | Distribuidor Ind. Kapazi - RJ',
                           'Rua Tirol, 1146 - Jacarepaguá - Freguesia, Rio de Janeiro - RJ - CEP 22.750-002',
                           'Vendedor: Ezequiel Potrique | Tel. WhatsApp: (21) 99814-6495']):
        c.drawCentredString(PW / 2, PH - 37 - 10 * i, t)
    c.setStrokeColor(navy); c.setLineWidth(1.5); c.line(M, PH - 66, PW - M, PH - 66)
    c.setFont('B', 15); c.setFillColor(cobre); c.drawCentredString(PW / 2, PH - 88, titulo)
    c.setFont('B', 10.5); c.setFillColor(navy); c.drawCentredString(PW / 2, PH - 103, sub)
    c.setFont('R', 8.5); c.setFillColor(gr); c.drawCentredString(PW / 2, PH - 116, f'Cliente: {CLI} | Data: {DATA}')
    im = ImageReader(mock_png); w, h = im.getSize(); iw = PW - 2 * M - 235; ih = iw * h / w
    top = PH - 124; bot = 72
    if ih > top - bot: ih = top - bot; iw = ih * w / h
    mid = (top + bot) / 2; c.drawImage(im, M, mid - ih / 2, iw, ih)
    x = PW - M - 220; y = top - 2
    c.setFillColor(navy); c.roundRect(x, y - 22, 220, 22, 3, stroke=0, fill=1)
    c.setFillColor(white); c.setFont('B', 9.5); c.drawString(x + 10, y - 15, 'ESPECIFICAÇÕES'); y -= 30
    for k, v in spec:
        c.setFillColor(navy); c.setFont('B', 7.6); c.drawString(x + 4, y, k.upper()); c.setFillColor(gr); c.setFont('R', 7.9)
        for ln in simpleSplit(v, 'R', 7.9, 212): y -= 9.6; c.drawString(x + 4, y, ln)
        y -= 4; c.setStrokeColor(HexColor('#DDDDDD')); c.setLineWidth(.5); c.line(x, y, x + 220, y); y -= 9.5
    c.setFillColor(cobre); c.setFont('M', 7.8)
    av = ('Imagem ilustrativa: as cores do layout são uma simulação digital e podem não representar fielmente a cor real da matéria-prima e da tinta, '
          'que também variam conforme a tela de cada aparelho. A produção começa após a aprovação deste layout.')
    lns = simpleSplit(av, 'M', 7.8, PW - 2 * M - 240)
    for i, ln in enumerate(lns): c.drawString(M, 44 + 10 * (len(lns) - 1 - i), ln)
    c.setStrokeColor(navy); c.setLineWidth(1); c.line(M, 36, PW - M, 36)
    c.setFillColor(cobre); c.setFont('B', 8); c.drawCentredString(PW / 2, 22, 'pii-zü Pisos | Distribuidor Autorizado Indústria Kapazi Cooperkap - RJ | WhatsApp (21) 99814-6495')
    c.save()
    subprocess.run(['pdftoppm', '-r', '200', '-jpeg', '-jpegopt', 'quality=93', '-singlefile', out_pdf, out_jpg[:-4]], check=True)

VG = 'Média de 2 anos, podendo prolongar com a manutenção (limpeza e retirada de sólidos)'
VC = 'Até 3x mais que o vinil, dependendo da manutenção (limpeza e retirada de sólidos)'
COM = [('Medida', '100 × 60 cm (100 de largura × 60 de profundidade)'), ('Quantidade', '1 unidade'),
       ('Arte', 'Logo "2MARKET - Seu mercadinho 24h" centralizado')]
FIM = [('Garantia', '12 meses contra defeitos de fabricação'), ('Prazo', 'Até 15 dias úteis para produção e entrega')]
OPC = [
 ('1 - VINIL GOLD PINTADO', 'gold_pintado', 'pintada', 'LAYOUT VINIL GOLD COM SOMENTE BORDA PINTADA "SEM ACRÉSCIMO"',
  [('Produto', 'Tapete e capacho de vinil personalizado (logo pintado)'), ('Matéria-prima', 'Vinil Gold (médio tráfego)'),
   ('Cor do tapete', 'Preto'), ('Cor da tinta (logo e borda)', 'Logo em Amarelo e Laranja; borda em Laranja')] + COM +
  [('Borda', 'Somente borda pintada com 3 cm de largura, em Laranja, em todo o contorno (não leva borda rebaixada nem borda flex). Sem acréscimo'),
   ('Vida útil', VG)] + FIM),
 ('2 - VINIL GOLD BORDA REBAIXADA', 'gold_pintado', 'rebaixada', 'LAYOUT VINIL GOLD COM BORDA REBAIXADA E PINTADA "COM ACRÉSCIMO"',
  [('Produto', 'Tapete e capacho de vinil personalizado (logo pintado)'), ('Matéria-prima', 'Vinil Gold (médio tráfego)'),
   ('Cor do tapete', 'Preto'), ('Cor da tinta (logo e borda)', 'Logo em Amarelo e Laranja; borda pintada em Laranja')] + COM +
  [('Borda', 'Borda rebaixada com 3 cm de largura no contorno externo, na cor do tapete (Preto, sem tinta) + borda pintada com 3 cm de largura por dentro, em Laranja (não leva borda flex). Borda pintada sem acréscimo'),
   ('Sobre a borda rebaixada', 'Acréscimo com investimento mais em conta: feita na própria matéria-prima do tapete de vinil, sem tinta. Além de ajudar a prevenir tropeços, mantém uma melhor apresentação do tapete até o final da sua vida útil'),
   ('Vida útil', VG)] + FIM),
 ('3 - VINIL GOLD VULCANIZADO', 'gold_vulc', 'vulcanizada', 'LAYOUT VINIL GOLD VULCANIZADO COM BORDA VULCANIZADA "COM ACRÉSCIMO"',
  [('Produto', 'Tapete e capacho de vinil personalizado (logo vulcanizado: recortado em vinil colorido e unido ao tapete, sem tinta)'),
   ('Matéria-prima', 'Vinil Gold (médio tráfego)'), ('Cor do tapete', 'Preto'),
   ('Cor do vinil do logo e da borda', 'Logo em vinil Amarelo e Laranja; borda em vinil Laranja')] + COM +
  [('Borda', 'Borda vulcanizada em vinil Laranja, em todo o contorno (não leva borda rebaixada, pintada nem flex). Acabamento premium (com acréscimo)'),
   ('Vida útil', VG)] + FIM),
 ('4 - CLEANKAP BORDA PINTADA', 'clean', 'pintada', 'LAYOUT CLEANKAP COM SOMENTE BORDA PINTADA "SEM ACRÉSCIMO"',
  [('Produto', 'Tapete e capacho personalizado - linha Premium Dupla Função (alto tráfego)'), ('Matéria-prima', 'Cleankap'),
   ('Cor do tapete', 'Preto'), ('Cor da tinta (logo e borda)', 'Logo em Amarelo e Laranja; borda em Laranja')] + COM +
  [('Borda', 'Somente borda pintada com 3 cm de largura, em Laranja, em todo o contorno (não leva borda flex). Sem acréscimo'),
   ('Vida útil', VC)] + FIM),
 ('5 - CLEANKAP BORDA FLEX', 'clean', 'flex', 'LAYOUT CLEANKAP COM BORDA FLEX ANTITROPEÇO "COM ACRÉSCIMO"',
  [('Produto', 'Tapete e capacho personalizado - linha Premium Dupla Função (alto tráfego)'), ('Matéria-prima', 'Cleankap'),
   ('Cor do tapete', 'Preto'), ('Cor da tinta (logo)', 'Amarelo e Laranja')] + COM +
  [('Borda', 'Somente borda flex antitropeço com 3 cm de largura, na cor Ouro (não leva borda pintada). Acabamento premium (com acréscimo)'),
   ('Observação', 'Não temos borda flex na cor Laranja; será utilizada a cor Ouro, a mais próxima do logo'),
   ('Vida útil', VC)] + FIM),
]
from pypdf import PdfWriter
wr = PdfWriter()
for nome, linha, borda, tit, spec in OPC:
    render(linha, borda, f'm{nome[0]}.png')
    base = f'LAYOUT 2MARKET OPÇÃO {nome}'
    layout_pdf(f'm{nome[0]}.png', tit, 'LOGO: 2MARKET', spec, base + '.pdf', base + '.jpg')
    wr.append(base + '.pdf')
wr.write('LAYOUTS 2MARKET (5 opções).pdf'); print('ok')
