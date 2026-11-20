import sys, io
sys.path.insert(0, '/home/claude/orc')
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader, simpleSplit
from pypdf import PdfReader, PdfWriter
from PIL import Image as PI

F = '/usr/share/fonts/truetype/google-fonts/'
for n, f in [('R', 'Poppins-Regular'), ('M', 'Poppins-Medium'), ('B', 'Poppins-Bold')]:
    pdfmetrics.registerFont(TTFont(n, F + f + '.ttf'))
NAVY = colors.HexColor('#1B2A4A'); GREY = colors.HexColor('#F1F2F4'); INK = colors.HexColor('#222222'); MUT = colors.HexColor('#666666')
COBRE = colors.HexColor('#BF561C'); VERDE = colors.HexColor('#1E7B4A'); VERM = colors.HexColor('#C62828')
L = '/home/claude/repo/public/piizu/assets/'
LOGO_P = L + 'biblioteca/logos/piizu-pisos-horizontal.png'; LOGO_K = L + 'img/marca/kapazi-cooperkap-rj-grafite.png'
from orc2_ext import extenso, brl

DATA = '20/11/2026'; DATA_EXT = '20 de novembro de 2026'
CLIENTE = [('Razão social', '2MARKET - Seu mercadinho 24h'), ('CNPJ', ''), ('Contato', ''),
           ('Endereço', ''), ('Bairro / Cidade', 'Pilares - Rio de Janeiro - RJ')]
AREA = 1.00 * 0.60   # 100 x 60: o lado de 60 cm já está no fator de corte
def preco(custo_m2, mk): return round(AREA * custo_m2 * mk, 2)
DIM = '100 × 60 cm | Tapete Preto, logo em Amarelo e Laranja'
OPC = [
 ('ORÇAMENTO 1 - VINIL GOLD COM LOGO PINTADO', 'Somente borda pintada "sem acréscimo"', 'Tapete e capacho de Vinil Gold (médio tráfego) com logo pintado',
  DIM + ' | Somente borda pintada com 3 cm de largura, em Laranja (não leva borda rebaixada nem borda flex). Sem acréscimo', preco(246, 1.6), 'm1.png'),
 ('ORÇAMENTO 2 - VINIL GOLD COM LOGO PINTADO', 'Borda rebaixada + pintada "com acréscimo"', 'Tapete e capacho de Vinil Gold (médio tráfego) com logo pintado',
  DIM + ' | Borda rebaixada com 3 cm de largura, na cor do tapete (com acréscimo de investimento mais em conta) + borda pintada com 3 cm de largura, em Laranja (sem acréscimo)', preco(246 + 12, 1.6), 'm2.png'),
 ('ORÇAMENTO 3 - VINIL GOLD COM LOGO VULCANIZADO', 'Borda vulcanizada "com acréscimo"', 'Tapete e capacho de Vinil Gold (médio tráfego) com logo vulcanizado',
  '100 × 60 cm | Tapete Preto, logo em vinil Amarelo e Laranja | Borda vulcanizada em vinil Laranja (não leva borda rebaixada, pintada nem flex). Acabamento premium (com acréscimo)', preco(503 + 23, 1.6), 'm3.png'),
 ('ORÇAMENTO 4 - CLEANKAP COM LOGO PINTADO', 'Somente borda pintada "sem acréscimo"', 'Tapete e capacho Cleankap - linha Premium Dupla Função (alto tráfego)',
  DIM + ' | Somente borda pintada com 3 cm de largura, em Laranja (não leva borda flex). Sem acréscimo', preco(382, 1.8), 'm4.png'),
 ('ORÇAMENTO 5 - CLEANKAP COM LOGO PINTADO', 'Borda flex antitropeço "com acréscimo"', 'Tapete e capacho Cleankap - linha Premium Dupla Função (alto tráfego)',
  DIM + ' | Somente borda flex antitropeço com 3 cm de largura, na cor Ouro (não leva borda pintada). Acabamento premium (com acréscimo). Não temos borda flex na cor Laranja; será utilizada a cor Ouro, a mais próxima do logo', preco(436, 1.8), 'm5.png'),
]
W, H = A4; M = 40

def cabecalho(c, completo):
    lp = ImageReader(LOGO_P); w, h = lp.getSize(); c.drawImage(lp, M, H - 40 - 46, 46 * w / h, 46, mask='auto')
    lk = ImageReader(LOGO_K); w, h = lk.getSize(); c.drawImage(lk, W - M - 46 * w / h, H - 40 - 46, 46 * w / h, 46, mask='auto')
    if not completo:
        y = H - 105; c.setStrokeColor(NAVY); c.setLineWidth(2); c.line(M, y, W - M, y); return y
    y = H - 110
    c.setFillColor(INK); c.setFont('B', 12); c.drawCentredString(W / 2, y, 'EBP POTRIQUE LTDA')
    c.setFont('R', 8.5); c.setFillColor(MUT)
    for t in ['CNPJ 50.639.581/0001-84  |  I.E. 12.857.454  |  Distribuidor Ind. Kapazi - RJ',
              'Rua Tirol, 1146 - Jacarepaguá - Freguesia, Rio de Janeiro - RJ, CEP 22.750-002',
              'Vendedor: Ezequiel Potrique  |  Tel. WhatsApp: (21) 99814-6495']:
        y -= 12; c.drawCentredString(W / 2, y, t)
    y -= 12; c.setStrokeColor(NAVY); c.setLineWidth(2); c.line(M, y, W - M, y); return y

def rodape(c):
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.line(M, 42, W - M, 42)
    c.setFont('R', 8); c.setFillColor(MUT); c.drawCentredString(W / 2, 30, 'pii-zü Pisos  |  Vendedor: Ezequiel Potrique  |  Tel. WhatsApp: (21) 99814-6495')

buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=A4); c.setTitle('Orçamento 2MARKET - pii-zü Pisos')
y = cabecalho(c, True)
y -= 26; c.setFillColor(NAVY); c.setFont('B', 14); c.drawString(M, y, 'ORÇAMENTO 2MARKET - TAPETE E CAPACHO PERSONALIZADO')
c.setFont('R', 8.5); c.setFillColor(MUT); c.drawRightString(W - M, y, 'Data: ' + DATA)
c.setFont('B', 9.5); c.setFillColor(COBRE); c.drawString(M, y - 15, f'{len(OPC)} ORÇAMENTOS SEPARADOS - ESCOLHA UM'); y -= 10
y -= 24; bh = 16 + 13 * len(CLIENTE)
c.setFillColor(GREY); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=0, fill=1)
c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M + 10, y - 13, 'CLIENTE'); yy = y - 13
for k, v in CLIENTE:
    yy -= 13; c.setFillColor(INK); c.setFont('M', 8.5); c.drawString(M + 10, yy, k + ':'); c.setFont('R', 8.5); c.drawString(M + 110, yy, v)
y -= bh + 16
frase = (f'Conforme solicitado, apresentamos abaixo {len(OPC)} orçamentos independentes para 1 (um) tapete e capacho de 100 × 60 cm. '
         'A diferença entre eles é a matéria-prima, o tipo de logo e o acabamento da borda. Escolha um deles: os valores não se somam.')
c.setFillColor(INK); c.setFont('R', 9.5)
for ln in simpleSplit(frase, 'R', 9.5, W - 2 * M): c.drawString(M, y, ln); y -= 13
cols = [M + 10, M + 50, W - M - 170, W - M - 90, W - M - 10]
rh = 80; boxh = 26 + 18 + rh + 50
for k, (tit, sub, desc, dim, unit, img) in enumerate(OPC):
    if y - 12 - boxh < 55:
        rodape(c); c.showPage(); y = cabecalho(c, False) - 6
    y -= 12; top = y
    c.setStrokeColor(NAVY); c.setLineWidth(1.2); c.setFillColor(colors.white); c.roundRect(M, top - boxh, W - 2 * M, boxh, 6, stroke=1, fill=1)
    c.setFillColor(COBRE); c.roundRect(M, top - 24, W - 2 * M, 24, 6, stroke=0, fill=1); c.rect(M, top - 24, W - 2 * M, 8, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont('B', 10); c.drawString(M + 12, top - 16, tit)
    c.setFont('M', 8.5); c.drawRightString(W - M - 12, top - 16, sub)
    y = top - 30
    c.setFillColor(NAVY); c.rect(cols[0], y - 18, cols[4] - cols[0], 18, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont('B', 8)
    c.drawCentredString((cols[0] + cols[1]) / 2, y - 12, 'QTD.'); c.drawString(cols[1] + 8, y - 12, 'DESCRIÇÃO')
    c.drawRightString(cols[3] - 6, y - 12, 'VALOR UNIT.'); c.drawRightString(cols[4] - 6, y - 12, 'TOTAL')
    y -= 18
    c.setFillColor(INK); c.setFont('M', 9.5); c.drawCentredString((cols[0] + cols[1]) / 2, y - rh / 2 - 3, '1')
    tx = cols[1] + 8; ir = ImageReader(img); iw, ih = ir.getSize(); pw = 80; ph = pw * ih / iw
    c.drawImage(ir, tx, y - rh / 2 - ph / 2, pw, ph); tx += 88
    tw = cols[3] - 62 - tx
    l1 = simpleSplit(desc, 'B', 8.3, tw); l2 = simpleSplit(dim, 'R', 7.2, tw)
    yy = y - rh / 2 + (len(l1) * 10 + len(l2) * 8.8) / 2 - 7
    c.setFont('B', 8.3)
    for ln in l1: c.drawString(tx, yy, ln); yy -= 10
    c.setFont('R', 7.2); c.setFillColor(MUT)
    for ln in l2: c.drawString(tx, yy, ln); yy -= 8.8
    c.setFillColor(INK); c.setFont('R', 9); c.drawRightString(cols[3] - 6, y - rh / 2 - 3, brl(unit))
    c.setFont('M', 9); c.drawRightString(cols[4] - 6, y - rh / 2 - 3, brl(unit))
    y -= rh
    av = round(unit * 0.95, 2)
    y -= 16; c.setFillColor(VERDE); c.setFont('B', 11); c.drawRightString(cols[4] - 6, y, f'ORÇAMENTO {k+1} À VISTA (5% de desconto): ' + brl(av))
    c.setFont('R', 7.5); c.setFillColor(MUT); c.drawRightString(cols[4] - 6, y - 11, '(' + extenso(av) + ')')
    c.setFillColor(NAVY); c.setFont('M', 9.5); c.drawRightString(cols[4] - 6, y - 25, f'A prazo: {brl(unit)}')
    y = top - boxh - 4
rodape(c); c.showPage()

# ---- página: produto, alerta, condições, assinatura
y = cabecalho(c, False) - 10
nota = ['Orçamentos 1, 2 e 3 - VINIL GOLD (médio tráfego): 100% PVC, 12 mm de espessura total, base antiderrapante, indicado para áreas internas ou externas com médio tráfego. Vida útil média de 2 anos, podendo prolongar com a manutenção (limpeza e retirada de sólidos).',
        'Orçamento 3 - logo vulcanizado: o desenho é recortado em vinil colorido e encaixado no próprio tapete, sem tinta. A borda vulcanizada acompanha o logo vulcanizado.',
        'Orçamentos 4 e 5 - CLEANKAP, linha Premium Dupla Função (alto tráfego): superfície em poliamida, 8 mm de espessura, base em PVC antiderrapante. Vida útil até 3x maior que a do vinil, dependendo da manutenção.',
        'Borda rebaixada (orçamento 2): acréscimo com investimento mais em conta. É feita na própria matéria-prima do tapete de vinil, sem tinta. Além de ajudar a prevenir tropeços, mantém uma melhor apresentação do tapete até o final da sua vida útil.',
        'Borda flex (orçamento 5): não temos borda flex na cor Laranja; será utilizada a cor Ouro, a mais próxima do logo.']
y -= 16; ls = []
for p in nota: ls += simpleSplit('• ' + p, 'R', 8.5, W - 2 * M - 24) + ['']
ls = ls[:-1]; bh = 18 + 11.5 * len(ls)
c.setFillColor(colors.HexColor('#FFF4EC')); c.setStrokeColor(COBRE); c.setLineWidth(1); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=1, fill=1)
c.setFillColor(COBRE); c.setFont('B', 9); c.drawString(M + 12, y - 13, 'PRODUTO DESTES ORÇAMENTOS')
yy = y - 26; c.setFillColor(INK); c.setFont('R', 8.5)
for ln in ls: c.drawString(M + 12, yy, ln); yy -= 11.5
y -= bh + 10
tj = 'ATENÇÃO: trabalhamos somente com Vinil Gold (médio tráfego) e Vinil A/T (alto tráfego). Não trabalhamos com o modelo inferior Vinil Silver: custo menor, mas tempo de vida útil também menor.'
ls = simpleSplit(tj, 'B', 8.5, W - 2 * M - 24); bh = 12 + 11.5 * len(ls)
c.setFillColor(VERM); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=0, fill=1)
yy = y - 15; c.setFillColor(colors.white); c.setFont('B', 8.5)
for ln in ls: c.drawString(M + 12, yy, ln); yy -= 11.5
y -= bh + 26
c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M, y, 'CONDIÇÕES DE PAGAMENTO (VALEM PARA TODOS OS ORÇAMENTOS)'); y -= 13
cond = ['Por se tratar de itens personalizados: 50% de sinal após a aprovação do orçamento, mais os 50% restantes em até 6 vezes iguais sem juros no cartão.',
        'Opções com desconto: 5% para pagamento de 100% do valor à vista, ou 5% sobre os 50% restantes pagos à vista no ato da entrega.',
        'Garantia de 12 meses direto da Indústria Kapazi contra defeitos de fabricação.']
c.setFillColor(INK); c.setFont('R', 8.5)
for p in cond:
    for ln in simpleSplit(p, 'R', 8.5, W - 2 * M): c.drawString(M, y, ln); y -= 11.5
    y -= 3
y -= 6; c.setFont('B', 8.5); c.drawString(M, y, 'Prazo de produção e entrega: até 15 dias úteis após a aprovação do layout.'); y -= 12
c.drawString(M, y, 'Validade da proposta: 15 dias.')
y -= 40; c.setFont('R', 9); c.drawString(M, y, 'Rio de Janeiro, ' + DATA_EXT + '.')
y -= 50; c.setLineWidth(0.8); c.setStrokeColor(INK); c.line(W / 2 - 110, y, W / 2 + 110, y)
c.setFont('B', 9); c.drawCentredString(W / 2, y - 12, 'EBP POTRIQUE LTDA'); c.setFont('R', 8.5); c.drawCentredString(W / 2, y - 24, 'Ezequiel Potrique - Vendedor')
rodape(c); c.showPage()

# ---- manual de limpeza (Gold e Cleankap) + fotos
def manual(titulo, itens, blocos):
    y = cabecalho(c, False)
    y -= 26; c.setFillColor(NAVY); c.setFont('B', 14); c.drawString(M, y, titulo)
    y -= 14; c.setFont('R', 8.5); c.setFillColor(MUT); c.drawString(M, y, 'Conforme a ficha técnica da Indústria Kapazi (enviada junto com este orçamento).')
    y -= 22
    for i, t in enumerate(itens, 1):
        ls = simpleSplit(t, 'R', 9.5, W - 2 * M - 30)
        c.setFillColor(NAVY); c.circle(M + 9, y + 3, 8, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont('B', 8); c.drawCentredString(M + 9, y, str(i))
        c.setFillColor(INK); c.setFont('R', 9.5)
        for ln in ls: c.drawString(M + 26, y, ln); y -= 13
        y -= 6
    for tit, txt in blocos:
        y -= 4; ls = simpleSplit(txt, 'R', 9, W - 2 * M - 24); bh = 22 + 12 * len(ls)
        c.setFillColor(GREY); c.roundRect(M, y - bh, W - 2 * M, bh, 4, stroke=0, fill=1)
        c.setFillColor(NAVY); c.setFont('B', 9); c.drawString(M + 12, y - 14, tit)
        yy = y - 28; c.setFillColor(INK); c.setFont('R', 9)
        for ln in ls: c.drawString(M + 12, yy, ln); yy -= 12
        y -= bh + 8
    return y

y = manual('MANUTENÇÃO E LIMPEZA - VINIL GOLD (ORÇAMENTOS 1, 2 E 3)',
 ['Limpeza diária: sacuda o tapete ou passe o aspirador de pó para tirar a sujeira solta.', 'O costado do produto (a base) também deve ser limpo.',
  'Periodicamente, lave o tapete com água e sabão neutro.', 'Seque em superfície plana e seca, e confira se o local está limpo e seco antes de voltar a colocar o tapete no piso.',
  'Não use máquina de lavar. Se usar lavadora de alta pressão, use sempre o MODO LEVE.', 'Não armazene o tapete dobrado nem em local úmido.',
  'A frequência da limpeza depende do local onde o tapete fica: quanto maior o tráfego, mais frequente.'],
 [('PROIBIDO', 'Não use produtos químicos com solvente, como acetona, thinner, álcool, gasolina, diesel ou cloro.'),
  ('GARANTIA', '1 ano contra defeitos de fabricação (6 meses em elevadores de serviço, supermercados, postos de gasolina, aeroportos e shoppings). O desgaste natural do uso não é coberto, e a falta de conservação e limpeza implica a perda da garantia. Dimensões podem variar até 2%, conforme portaria do INMETRO.')])
rodape(c); c.showPage()
y = manual('MANUTENÇÃO E LIMPEZA - CLEANKAP (ORÇAMENTOS 4 E 5)',
 ['Limpeza diária: sacuda o tapete até retirar a sujeira solta. Não use escovas, pois podem danificar a superfície.', 'Passe o aspirador de pó.',
  'Lave somente à mão, com sabão neutro.', 'A frequência da limpeza depende do local onde o tapete fica.',
  'Seque ao ar livre, sobre superfície plana. Não use secadora nem passe ferro.', 'Não deixe o tapete exposto ao sol nem a altas temperaturas.',
  'Confira se o local está limpo e seco antes de voltar a colocar o tapete no piso.'],
 [('PROIBIDO', 'Não use nenhum tipo de solvente, thinner, álcool ou detergentes alcalinos típicos de limpeza de superfícies.'),
  ('GARANTIA', '1 ano contra defeitos de fabricação. Dimensões podem variar até 2%, conforme portaria do INMETRO.')])
fotos = [('/home/claude/orc/fotos_padrao/1-loja-gracie-barra.jpg', 'Gracie Barra'), ('/home/claude/orc/fotos_padrao/2-loja-autentica-moda.jpg', 'Autêntica Moda Feminina'),
         ('/home/claude/orc/fotos_padrao/3-loja-byd-concessionaria.jpg', 'BYD')]
y -= 10; c.setFillColor(NAVY); c.setFont('B', 11); c.drawString(M, y, 'ALGUNS DOS NOSSOS TRABALHOS'); y -= 10
gap = 12; fw = (W - 2 * M - gap) / 2; fh = min((y - 60 - 2 * 16 - gap) / 2, fw * 0.75)
pos = [(M, y), (M + fw + gap, y), (M + (fw + gap) / 2, y - fh - 16 - gap)]
for i, (fp, leg) in enumerate(fotos):
    x, yy = pos[i]; im = PI.open(fp).convert('RGB'); r = fw / fh; iw, ih = im.size
    if iw / ih > r: nw = int(ih * r); im = im.crop(((iw - nw) // 2, 0, (iw - nw) // 2 + nw, ih))
    else: nh = int(iw / r); im = im.crop((0, (ih - nh) // 2, iw, (ih - nh) // 2 + nh))
    c.drawImage(ImageReader(im), x, yy - fh, fw, fh)
    c.setFillColor(MUT); c.setFont('R', 7.5); c.drawCentredString(x + fw / 2, yy - fh - 10, leg)
rodape(c); c.save()

# ---- fichas: Gold (já com logos) + Cleankap com logos pii-zü (esq.) e Kapazi Cooperkap - RJ (dir.)
fc = PdfReader('ficha-cleankap.pdf'); pg = fc.pages[0]; pw, ph = float(pg.mediabox.width), float(pg.mediabox.height)
ob = io.BytesIO(); o = canvas.Canvas(ob, pagesize=(pw, ph))
for path, right in [(LOGO_P, False), (LOGO_K, True)]:
    im = ImageReader(path); w, h = im.getSize(); lh = 26; lw = lh * w / h; x = pw - 14 - lw if right else 14
    o.setFillColor(colors.white); o.roundRect(x - 5, ph - 8 - lh - 4, lw + 10, lh + 8, 4, stroke=0, fill=1)
    o.drawImage(im, x, ph - 8 - lh, lw, lh, mask='auto')
o.save(); pg.merge_page(PdfReader(ob).pages[0])
w = PdfWriter(); w.append(PdfReader(buf))
w.append(PdfReader('/home/claude/orc/fichas/FICHA TÉCNICA - VINIL GOLD (médio tráfego).pdf'))
w.add_page(pg)
w.write('ORÇAMENTO 2MARKET - pii-zü Pisos.pdf')
print([o[4] for o in OPC])
