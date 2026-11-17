import json, sys, datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader, simpleSplit

F = '/usr/share/fonts/truetype/google-fonts/'
pdfmetrics.registerFont(TTFont('R', F + 'Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('M', F + 'Poppins-Medium.ttf'))
pdfmetrics.registerFont(TTFont('B', F + 'Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('I', F + 'Poppins-Italic.ttf'))

NAVY = colors.HexColor('#1B2A4A'); GREY = colors.HexColor('#F1F2F4'); INK = colors.HexColor('#222222'); MUT = colors.HexColor('#666666')
L = '/home/claude/repo/public/piizu/assets/'
LOGO_P = L + 'biblioteca/logos/piizu-pisos-horizontal.png'
LOGO_K = L + 'img/marca/kapazi-cooperkap-rj-grafite.png'

UN = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
DZ = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
CT = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
def ate999(n):
    if n == 0: return ''
    if n == 100: return 'cem'
    c, r = divmod(n, 100); p = []
    if c: p.append(CT[c])
    if r:
        if r < 20: p.append(UN[r])
        else:
            d, u = divmod(r, 10); p.append(DZ[d] + (' e ' + UN[u] if u else ''))
    return ' e '.join(p)
def extenso(v):
    reais = int(v); cent = int(round((v - reais) * 100))
    mil, r = divmod(reais, 1000); partes = []
    if mil: partes.append(('mil' if mil == 1 else ate999(mil) + ' mil'))
    if r: partes.append(ate999(r))
    s = (' e ' if (mil and r and (r < 100 or r % 100 == 0)) else ' ').join(partes) if partes else 'zero'
    s += ' real' if reais == 1 else ' reais'
    if cent: s += ' e ' + ate999(cent) + (' centavo' if cent == 1 else ' centavos')
    return s
def brl(v): return 'R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

d = json.load(open(sys.argv[1]))
out = sys.argv[2]
W, H = A4; M = 40
c = canvas.Canvas(out, pagesize=A4)
c.setTitle(d['titulo'])
# logos
lp = ImageReader(LOGO_P); w, h = lp.getSize(); lh = 46; c.drawImage(lp, M, H - 40 - lh, lh * w / h, lh, mask='auto')
lk = ImageReader(LOGO_K); w, h = lk.getSize(); kh = 46; kw = kh * w / h; c.drawImage(lk, W - M - kw, H - 40 - kh, kw, kh, mask='auto')
y = H - 110
c.setFillColor(INK); c.setFont('B', 12); c.drawCentredString(W / 2, y, 'EBP POTRIQUE LTDA')
c.setFont('R', 8.5); c.setFillColor(MUT)
for t in ['CNPJ 50.639.581/0001-84  |  I.E. 12.857.454  |  Distribuidor Ind. Kapazi - RJ',
          'Rua Tirol, 1146 - Jacarepaguá - Freguesia, Rio de Janeiro - RJ, CEP 22.750-002',
          'Vendedor: Ezequiel Potrique  |  Tel. WhatsApp: (21) 99814-6495']:
    y -= 12; c.drawCentredString(W / 2, y, t)
y -= 12; c.setStrokeColor(NAVY); c.setLineWidth(2); c.line(M, y, W - M, y)
total = sum(i['qtd'] * i['unit'] for i in d['itens'])
y -= 26; c.setFillColor(NAVY); c.setFont('B', 15); c.drawString(M, y, d['titulo'])
c.setFont('B', 13); c.drawRightString(W - M, y, brl(total))
c.setFont('R', 8.5); c.setFillColor(MUT); c.drawRightString(W - M, y - 13, 'Data: ' + d['data'])
# cliente
y -= 30; bh = 16 + 13 * len(d['cliente'])
c.setFillColor(GREY); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=0, fill=1)
c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M + 10, y - 13, 'CLIENTE')
yy = y - 13
for k, v in d['cliente']:
    yy -= 13; c.setFillColor(INK); c.setFont('M', 8.5); c.drawString(M + 10, yy, k + ':'); c.setFont('R', 8.5); c.drawString(M + 95, yy, v)
y -= bh + 20
c.setFillColor(INK); c.setFont('R', 9.5)
frase = f"Conforme solicitado, apresentamos nossa proposta no valor total de {brl(total)} ({extenso(total)})."
for ln in simpleSplit(frase, 'R', 9.5, W - 2 * M): c.drawString(M, y, ln); y -= 13
# tabela
y -= 8; cols = [M, M + 50, W - M - 170, W - M - 85, W - M]
c.setFillColor(NAVY); c.rect(M, y - 20, W - 2 * M, 20, stroke=0, fill=1)
c.setFillColor(colors.white); c.setFont('B', 8.5)
c.drawCentredString((cols[0] + cols[1]) / 2, y - 13, 'QTD.'); c.drawString(cols[1] + 8, y - 13, 'DESCRIÇÃO')
c.drawRightString(cols[3] - 8, y - 13, 'VALOR UNIT.'); c.drawRightString(cols[4] - 8, y - 13, 'TOTAL')
y -= 20
for it in d['itens']:
    img = it.get('img'); rh = 70 if img else 40
    c.setStrokeColor(colors.HexColor('#DDDDDD')); c.setLineWidth(0.6); c.line(M, y - rh, W - M, y - rh)
    c.setFillColor(INK); c.setFont('M', 9.5); c.drawCentredString((cols[0] + cols[1]) / 2, y - rh / 2 - 3, str(it['qtd']))
    tx = cols[1] + 8
    if img:
        ir = ImageReader(img); iw, ih = ir.getSize(); ph = rh - 12; pw = min(ph * iw / ih, 120); ph = pw * ih / iw
        c.drawImage(ir, tx, y - rh / 2 - ph / 2, pw, ph, mask='auto'); tx += pw + 10
    tw = cols[3] - 80 - tx
    l1 = simpleSplit(it['desc'], 'B', 9, tw); l2 = simpleSplit(it['dim'], 'R', 8, tw)
    yy = y - rh / 2 + (len(l1) * 11 + len(l2) * 10) / 2 - 8
    c.setFont('B', 9)
    for ln in l1: c.drawString(tx, yy, ln); yy -= 11
    c.setFont('R', 8); c.setFillColor(MUT)
    for ln in l2: c.drawString(tx, yy, ln); yy -= 10
    c.setFillColor(INK); c.setFont('R', 9.5); c.drawRightString(cols[3] - 8, y - rh / 2 - 3, brl(it['unit']))
    c.setFont('M', 9.5); c.drawRightString(cols[4] - 8, y - rh / 2 - 3, brl(it['qtd'] * it['unit']))
    y -= rh
y -= 22; c.setFillColor(NAVY); c.setFont('B', 12); c.drawRightString(W - M, y, 'VALOR TOTAL: ' + brl(total))
if d.get('nota_produto'):
    y -= 16; ls = []
    for p in d['nota_produto']: ls += simpleSplit(p, 'R', 8.5, W - 2 * M - 24)
    bh = 18 + 11.5 * len(ls)
    c.setFillColor(colors.HexColor('#FFF4EC')); c.setStrokeColor(colors.HexColor('#BF561C')); c.setLineWidth(1)
    c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=1, fill=1)
    c.setFillColor(colors.HexColor('#BF561C')); c.setFont('B', 9); c.drawString(M + 12, y - 13, 'PRODUTO DESTE ORÇAMENTO')
    yy = y - 26; c.setFillColor(INK); c.setFont('R', 8.5)
    for ln in ls: c.drawString(M + 12, yy, ln); yy -= 11.5
    y -= bh
y -= 26; c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M, y, 'CONDIÇÕES DE PAGAMENTO'); y -= 13
c.setFillColor(INK); c.setFont('R', 8.5)
for p in d['condicoes']:
    for ln in simpleSplit(p, 'R', 8.5, W - 2 * M): c.drawString(M, y, ln); y -= 11.5
    y -= 3
y -= 6; c.setFont('B', 8.5); c.drawString(M, y, 'Prazo de produção e entrega: até 15 dias úteis.'); y -= 12
c.drawString(M, y, 'Validade da proposta: 15 dias.')
y -= 40; c.setFont('R', 9); c.drawString(M, y, 'Rio de Janeiro, ' + d['data_extenso'] + '.')
y -= 50; c.setLineWidth(0.8); c.setStrokeColor(INK); c.line(W / 2 - 110, y, W / 2 + 110, y)
c.setFont('B', 9); c.drawCentredString(W / 2, y - 12, 'EBP POTRIQUE LTDA'); c.setFont('R', 8.5); c.drawCentredString(W / 2, y - 24, 'Ezequiel Potrique - Vendedor')
c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, 42, W - M, 42)
c.setFont('R', 8); c.setFillColor(MUT); c.drawCentredString(W / 2, 30, 'Vendedor: Ezequiel Potrique  |  Tel. WhatsApp: (21) 99814-6495')
if d.get('manutencao'):
    c.showPage()
    lp = ImageReader(LOGO_P); w, h = lp.getSize(); c.drawImage(lp, M, H - 40 - 46, 46 * w / h, 46, mask='auto')
    lk = ImageReader(LOGO_K); w, h = lk.getSize(); c.drawImage(lk, W - M - 46 * w / h, H - 40 - 46, 46 * w / h, 46, mask='auto')
    y = H - 115; c.setStrokeColor(NAVY); c.setLineWidth(2); c.line(M, y, W - M, y)
    y -= 26; c.setFillColor(NAVY); c.setFont('B', 15); c.drawString(M, y, d['manutencao']['titulo'])
    y -= 14; c.setFont('R', 8.5); c.setFillColor(MUT); c.drawString(M, y, 'Conforme a ficha técnica da Indústria Kapazi (enviada junto com este orçamento).')
    y -= 22
    for i, t in enumerate(d['manutencao']['itens'], 1):
        ls = simpleSplit(t, 'R', 9.5, W - 2 * M - 30)
        c.setFillColor(NAVY); c.circle(M + 9, y + 3, 8, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont('B', 8); c.drawCentredString(M + 9, y, str(i))
        c.setFillColor(INK); c.setFont('R', 9.5)
        for ln in ls: c.drawString(M + 26, y, ln); y -= 13
        y -= 7
    for tit, txt in d['manutencao'].get('blocos', []):
        y -= 6; ls = simpleSplit(txt, 'R', 9, W - 2 * M - 24); bh = 22 + 12 * len(ls)
        c.setFillColor(GREY); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=0, fill=1)
        c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M + 12, y - 14, tit)
        yy = y - 28; c.setFillColor(INK); c.setFont('R', 9)
        for ln in ls: c.drawString(M + 12, yy, ln); yy -= 12
        y -= bh + 8
    if d.get('fotos'):
        y -= 10; c.setFillColor(NAVY); c.setFont('B', 11); c.drawString(M, y, 'ALGUNS DOS NOSSOS TRABALHOS'); y -= 10
        gap = 12; fw = (W - 2 * M - gap) / 2; fh = min((y - 60 - 2 * 16 - gap) / 2, fw * 0.75)
        pos = [(M, y), (M + fw + gap, y), (M + (fw + gap) / 2, y - fh - 16 - gap)]
        for i, (fp, leg) in enumerate(d['fotos']):
            x, y = pos[i]
            from PIL import Image as PI
            im = PI.open(fp).convert('RGB'); r = fw / fh; iw, ih = im.size
            if iw / ih > r: nw = int(ih * r); im = im.crop(((iw - nw) // 2, 0, (iw - nw) // 2 + nw, ih))
            else: nh = int(iw / r); im = im.crop((0, (ih - nh) // 2, iw, (ih - nh) // 2 + nh))
            c.drawImage(ImageReader(im), x, y - fh, fw, fh)
            c.setFillColor(MUT); c.setFont('R', 7.5); c.drawCentredString(x + fw / 2, y - fh - 10, leg)
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, 42, W - M, 42)
    c.setFont('R', 8); c.setFillColor(MUT); c.drawCentredString(W / 2, 30, 'Vendedor: Ezequiel Potrique  |  Tel. WhatsApp: (21) 99814-6495')
c.save()
print('ok', brl(total), extenso(total))
