"""Padrão pii-zü: mockup de tapete de vinil + layout em PDF/JPG com logos e especificações."""
import numpy as np, math, random, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader, simpleSplit
GF = '/usr/share/fonts/truetype/google-fonts/'
for n, f in [('R', 'Poppins-Regular'), ('M', 'Poppins-Medium'), ('B', 'Poppins-Bold')]:
    pdfmetrics.registerFont(TTFont(n, GF + f + '.ttf'))
L = '/home/claude/repo/public/piizu/assets/'

def coil(w, h, seed=7):
    random.seed(seed)
    t = Image.new('L', (w, h), 120); d = ImageDraw.Draw(t)
    for _ in range(int(w * h / 22)):
        x, y = random.uniform(-10, w + 10), random.uniform(-10, h + 10); rr = random.uniform(2.5, 5.5); a0 = random.uniform(0, 6.28)
        d.line([(x + math.cos(a0 + k * .45) * rr + k * .5, y + math.sin(a0 + k * .45) * rr) for k in range(14)], fill=random.randint(150, 255), width=random.choice([1, 2, 2]))
    return np.asarray(t.filter(ImageFilter.GaussianBlur(.6))).astype(float) / 255

def mockup(inner_art, wcm, hcm, border_rgb, out_png, px=12, bcm=3):
    W, H, BP = wcm * px, hcm * px, bcm * px
    inner = inner_art.convert('RGB').resize((W - 2 * BP, H - 2 * BP), Image.LANCZOS)
    tex = coil(W, H); mat = np.zeros((H, W, 3))
    t = tex[BP:H - BP, BP:W - BP, None]
    mat[BP:H - BP, BP:W - BP] = np.asarray(inner).astype(float) * (.55 + .6 * t) + 18 * t
    fine = np.asarray(Image.effect_noise((W, H), 8).convert('L')).astype(float) / 255
    bord = np.array(border_rgb, float)[None, None, :] * (.92 + .16 * fine[..., None])
    m = np.ones((H, W), bool); m[BP:H - BP, BP:W - BP] = False; mat[m] = bord[m]
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rectangle([BP, BP, W - BP, H - BP], outline=255, width=4)
    mat *= (1 - .5 * np.asarray(sh.filter(ImageFilter.GaussianBlur(3))).astype(float)[..., None] / 255)
    hl = Image.new('L', (W, H), 0); ImageDraw.Draw(hl).rectangle([BP - 3, BP - 3, W - BP + 3, H - BP + 3], outline=255, width=1)
    mat += 30 * (np.asarray(hl.filter(ImageFilter.GaussianBlur(1))).astype(float) / 255)[..., None]
    mat = Image.fromarray(np.clip(mat, 0, 255).astype(np.uint8))
    mk = Image.new('L', (W, H), 0); ImageDraw.Draw(mk).rounded_rectangle([0, 0, W - 1, H - 1], radius=10, fill=255)
    sc = max(1.0, W / 1800); CW, CH = int(W + 360 * sc), int(H + 330 * sc); ox, oy = int(230 * sc), int(90 * sc)
    C = Image.new('RGB', (CW, CH), 'white')
    s = Image.new('L', (CW, CH), 0); ImageDraw.Draw(s).rounded_rectangle([ox + 8, oy + 14, ox + W + 8, oy + H + 14], radius=12, fill=110)
    C = Image.composite(Image.new('RGB', (CW, CH), (150, 150, 150)), C, s.filter(ImageFilter.GaussianBlur(14)))
    C.paste(mat, (ox, oy), mk)
    d = ImageDraw.Draw(C); col = (40, 40, 40); f = ImageFont.truetype(GF + 'Poppins-Medium.ttf', int(46 * sc))
    def arrow(x1, y1, x2, y2):
        d.line([(x1, y1), (x2, y2)], fill=col, width=int(4 * sc))
        for ax, ay, bx, by in [(x1, y1, x2, y2), (x2, y2, x1, y1)]:
            a = math.atan2(by - ay, bx - ax)
            d.polygon([(ax, ay), (ax + 26 * sc * math.cos(a + .4), ay + 26 * sc * math.sin(a + .4)), (ax + 26 * sc * math.cos(a - .4), ay + 26 * sc * math.sin(a - .4))], fill=col)
    xl = ox - int(80 * sc); arrow(xl, oy, xl, oy + H)
    for yy in (oy, oy + H): d.line([(xl - 20, yy), (ox - 15, yy)], fill=col, width=2)
    lb = Image.new('RGBA', (int(300 * sc), int(80 * sc)), (255, 255, 255, 0)); ImageDraw.Draw(lb).text((int(150 * sc), int(40 * sc)), f'{hcm} cm', font=f, fill=col, anchor='mm')
    lb = lb.rotate(90, expand=True); C.paste(lb, (xl - int(95 * sc), oy + H // 2 - int(150 * sc)), lb)
    yb = oy + H + int(85 * sc); arrow(ox, yb, ox + W, yb)
    for xx in (ox, ox + W): d.line([(xx, oy + H + 20), (xx, yb + 20)], fill=col, width=2)
    d.rectangle([ox + W // 2 - int(110 * sc), yb - int(30 * sc), ox + W // 2 + int(110 * sc), yb + int(30 * sc)], fill='white'); d.text((ox + W // 2, yb), f'{wcm} cm', font=f, fill=col, anchor='mm')
    C.save(out_png); return mat

def layout_pdf(mock_png, titulo, cliente, data, spec, out_pdf, out_jpg):
    PW, PH = landscape(A4); M = 32; navy = HexColor('#1B2A4A'); g = HexColor('#444444'); cobre = HexColor('#BF561C')
    c = canvas.Canvas(out_pdf, pagesize=landscape(A4)); c.setTitle(titulo)
    for path, right in [(L + 'biblioteca/logos/piizu-pisos-horizontal.png', False), (L + 'img/marca/kapazi-cooperkap-rj-grafite.png', True)]:
        im = ImageReader(path); w, h = im.getSize(); lh = 46; lw = lh * w / h
        c.drawImage(im, PW - M - lw if right else M, PH - 14 - lh, lw, lh, mask='auto')
    c.setFillColor(navy); c.setFont('B', 12); c.drawCentredString(PW / 2, PH - 26, 'EBP POTRIQUE LTDA')
    c.setFont('R', 7.8); c.setFillColor(g)
    for i, t in enumerate(['CNPJ 50.639.581/0001-84 | I.E. 12.857.454 | Distribuidor Ind. Kapazi - RJ',
                           'Rua Tirol, 1146 - Jacarepaguá - Freguesia, Rio de Janeiro - RJ - CEP 22.750-002',
                           'Vendedor: Ezequiel Potrique | Tel. WhatsApp: (21) 99814-6495']):
        c.drawCentredString(PW / 2, PH - 37 - 10 * i, t)
    c.setStrokeColor(navy); c.setLineWidth(1.5); c.line(M, PH - 66, PW - M, PH - 66)
    c.setFont('B', 11); c.setFillColor(navy); c.drawString(M, PH - 82, titulo)
    c.setFont('R', 8.5); c.setFillColor(g); c.drawRightString(PW - M, PH - 82, f'Cliente: {cliente}  |  Data: {data}')
    im = ImageReader(mock_png); w, h = im.getSize(); iw = PW - 2 * M - 230; ih = iw * h / w
    mid = (PH - 96 + 60) / 2; c.drawImage(im, M, mid - ih / 2, iw, ih)
    x = PW - M - 215; y = mid + 150
    c.setFillColor(navy); c.roundRect(x, y - 22, 215, 22, 3, stroke=0, fill=1)
    c.setFillColor(white); c.setFont('B', 9.5); c.drawString(x + 10, y - 15, 'ESPECIFICAÇÕES'); y -= 30
    for k, v in spec:
        c.setFillColor(navy); c.setFont('B', 8); c.drawString(x + 4, y, k.upper()); c.setFillColor(g); c.setFont('R', 8.5)
        for ln in simpleSplit(v, 'R', 8.5, 205): y -= 11; c.drawString(x + 4, y, ln)
        y -= 6; c.setStrokeColor(HexColor('#DDDDDD')); c.setLineWidth(.5); c.line(x, y, x + 215, y); y -= 11
    c.setFillColor(cobre); c.setFont('M', 7.8)
    c.drawString(M, 54, 'Imagem ilustrativa: as cores do layout são uma simulação digital e podem não representar fielmente a cor real da matéria-prima e da tinta, que também')
    c.drawString(M, 44, 'variam conforme a tela de cada aparelho. A produção começa após a aprovação deste layout.')
    c.setStrokeColor(navy); c.setLineWidth(1); c.line(M, 36, PW - M, 36)
    c.setFillColor(cobre); c.setFont('B', 8); c.drawCentredString(PW / 2, 22, 'pii-zü Pisos  |  Distribuidor Autorizado Indústria Kapazi - RJ  |  WhatsApp (21) 99814-6495')
    c.save()
    subprocess.run(['pdftoppm', '-r', '200', '-jpeg', '-jpegopt', 'quality=93', '-singlefile', out_pdf, out_jpg[:-4]], check=True)

def coil2(w, h, seed=11):
    """Textura de vinil enrolado: laços finos com furinhos minúsculos entre eles."""
    rnd = random.Random(seed)
    t = Image.new('L', (w, h), 60); d = ImageDraw.Draw(t)
    for _ in range(int(w * h / 11)):
        x, y = rnd.uniform(-8, w + 8), rnd.uniform(-8, h + 8); rx = rnd.uniform(3.5, 6.5); ry = rx * rnd.uniform(.6, 1.0)
        a0 = rnd.uniform(0, 360); span = rnd.uniform(200, 340)
        d.arc([x - rx, y - ry, x + rx, y + ry], a0, a0 + span, fill=rnd.randint(150, 235), width=2)
    return np.asarray(t.filter(ImageFilter.GaussianBlur(.55))).astype(float) / 200

def mockup2(inner_art, wcm, hcm, border_rgb, out_png, px=20, bcm=3):
    """Mesmo padrão do mockup, com textura realista da matéria-prima (furinhos)."""
    import types
    W, H, BP = wcm * px, hcm * px, bcm * px
    inner = np.asarray(inner_art.convert('RGB').resize((W - 2 * BP, H - 2 * BP), Image.LANCZOS)).astype(float)
    lum = coil2(W, H)[BP:H - BP, BP:W - BP, None]
    art = Image.fromarray(np.clip(inner * lum, 0, 255).astype(np.uint8))
    g = globals(); old = g['coil']
    g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.375)   # neutraliza textura antiga: .55+.6*.375 = .775
    try:
        arr = np.asarray(art).astype(float) / 0.775 - 18 * 0.375 / 0.775
        return mockup(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), wcm, hcm, border_rgb, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

CORES = '/home/claude/repo/public/piizu/assets/img/cores/'
SLUG = {'Ouro': 'ouro', 'Verde Floresta': 'floresta', 'Bege': 'bege', 'Creme': 'creme', 'Preto': 'preto', 'Grafite': 'grafite',
        'Cinza': 'cinza', 'Prata': 'prata', 'Branco': 'branco', 'Verde Limão': 'limao', 'Verde Água': 'agua', 'Verde Piscina': 'piscina',
        'Verde Bandeira': 'bandeira', 'Verde Musgo': 'musgo', 'Azul Bebê': 'azul-bebe', 'Azul Marítimo': 'maritimo', 'Azul Royal': 'royal',
        'Azul Marinho': 'marinho', 'Roxo': 'roxo', 'Rosa Bebê': 'rosa-bebe', 'Pink': 'pink', 'Bordô': 'bordo', 'Vermelho': 'vermelho',
        'Vermelho Ferrari': 'ferrari', 'Laranja': 'laranja', 'Amarelo': 'amarelo', 'Marrom': 'marrom'}

def tex_real(cor, w, h, tile=70, seed=3):
    """Textura com a amostra REAL do vinil (paleta Gold do site), em mosaico espelhado."""
    sw = Image.open(CORES + f'vinil-{SLUG[cor]}.webp').convert('RGB').resize((tile, tile), Image.LANCZOS)
    rnd = random.Random(seed); out = Image.new('RGB', (w, h))
    variants = [sw, sw.transpose(Image.FLIP_LEFT_RIGHT), sw.transpose(Image.FLIP_TOP_BOTTOM), sw.transpose(Image.ROTATE_180)]
    for y in range(0, h, tile):
        for x in range(0, w, tile):
            out.paste(variants[((x // tile) % 2) + 2 * ((y // tile) % 2)], (x, y))
    return np.asarray(out).astype(float)

def cor_media(cor):
    a = np.asarray(Image.open(CORES + f'vinil-{SLUG[cor]}.webp').convert('RGB')).reshape(-1, 3).astype(float)
    return tuple(int(v) for v in a.mean(0))

def mockup_real(mask, cor_tapete, cor_tinta, wcm, hcm, out_png, px=20, bcm=3):
    """mask: imagem L do tamanho da área interna (0 = tapete, 255 = tinta)."""
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    inner = tex_real(cor_tapete, iw, ih) * (1 - a) + tex_real(cor_tinta, iw, ih, seed=5) * a
    arr = inner / 0.775 - 18 * 0.375 / 0.775
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.375)
    try:
        return mockup(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), wcm, hcm, cor_media(cor_tapete), out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

def cor_real(cor):
    a = np.asarray(Image.open(CORES + f'vinil-{SLUG[cor]}.webp').convert('RGB')).reshape(-1, 3).astype(float)
    l = a.sum(1); return a[l > np.percentile(l, 60)].mean(0)

def mockup_real(mask, cor_tapete, cor_tinta, wcm, hcm, out_png, px=20, bcm=3):
    """Cor tirada da amostra REAL do vinil (paleta Gold) + textura de laços com furinhos."""
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    lum = coil2(W, H)[BP:H - BP, BP:W - BP, None] / 0.95
    col = cor_real(cor_tapete)[None, None, :] * (1 - a) + cor_real(cor_tinta)[None, None, :] * a
    arr = (col * lum) / 0.775 - 18 * 0.375 / 0.775
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.375)
    try:
        bord = tuple(int(v * 0.92) for v in cor_real(cor_tapete))
        return mockup(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)), wcm, hcm, bord, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

# Paleta oficial do vinil (imagem enviada pelo Seu Zecones): cor exata de cada quadrado
PALETA_POS = {'Branco': None, 'Prata': (465, 140), 'Cinza': (620, 140), 'Grafite': (775, 140),
    'Preto': (155, 290), 'Verde Limão': (310, 290), 'Verde Água': (465, 290), 'Verde Piscina': (620, 290), 'Verde Bandeira': (775, 290),
    'Verde Musgo': (155, 440), 'Verde Floresta': (310, 440), 'Azul Bebê': (465, 440), 'Azul Marítimo': (620, 440), 'Azul Royal': (775, 440),
    'Azul Marinho': (155, 590), 'Roxo': (310, 590), 'Rosa Bebê': (465, 590), 'Pink': (620, 590), 'Bordô': (775, 590),
    'Vermelho': (155, 740), 'Vermelho Ferrari': (310, 740), 'Laranja': (465, 740), 'Amarelo': (620, 740), 'Marrom': (775, 740),
    'Cerâmica': (155, 890), 'Ouro': (310, 890), 'Bege': (465, 890), 'Creme': (620, 890)}
def cor_real(cor):
    if cor == 'Branco': return np.array([245., 245., 245.])
    im = Image.open('/home/claude/orc/paleta_vinil.png').convert('RGB'); x, y = PALETA_POS[cor]
    return np.asarray(im.crop((x - 8, y - 4, x + 8, y + 4))).reshape(-1, 3).astype(float).mean(0)

def mockup_real(mask, cor_tapete, cor_tinta, wcm, hcm, out_png, px=20, bcm=3):
    """Cor exata da paleta oficial do vinil + textura com furinhos, sem distorcer o tom."""
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    lum = coil2(W, H)[BP:H - BP, BP:W - BP, None]; lum = lum / lum.mean()
    col = cor_real(cor_tapete)[None, None, :] * (1 - a) + cor_real(cor_tinta)[None, None, :] * a
    fin = col * lum
    m = fin.max(2, keepdims=True); fin = np.where(m > 255, fin * 255 / np.maximum(m, 1), fin)   # preserva o tom
    pre = np.clip(fin - 13.5, 0, 255)          # mockup aplica x*1.0 + 13.5 com coil = .75
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.75)
    try:
        bord = tuple(int(v * 0.94) for v in cor_real(cor_tapete))
        return mockup(Image.fromarray(pre.astype(np.uint8)), wcm, hcm, bord, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

def cor_tinta(cor):            # paleta de PINTURA (imagem de 29 quadrados)
    if cor == 'Branco': return np.array([245., 245., 245.])
    im = Image.open('/home/claude/orc/paleta_vinil.png').convert('RGB'); x, y = PALETA_POS[cor]
    return np.asarray(im.crop((x - 8, y - 4, x + 8, y + 4))).reshape(-1, 3).astype(float).mean(0)

def cor_materia(cor):          # amostra REAL da matéria-prima Vinil Gold
    a = np.asarray(Image.open(CORES + f'vinil-{SLUG[cor]}.webp').convert('RGB')).reshape(-1, 3).astype(float)
    l = a.sum(1); return a[l > np.percentile(l, 50)].mean(0)

def mockup_real(mask, cor_tapete, cor_tin, wcm, hcm, out_png, px=20, bcm=3):
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    lum = coil2(W, H)[BP:H - BP, BP:W - BP, None]; lum = lum / lum.mean()
    col = cor_materia(cor_tapete)[None, None, :] * (1 - a) + cor_tinta(cor_tin)[None, None, :] * a
    fin = col * lum; m = fin.max(2, keepdims=True); fin = np.where(m > 255, fin * 255 / np.maximum(m, 1), fin)
    pre = np.clip(fin - 13.5, 0, 255)
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.75)
    try:
        bord = tuple(int(v * 0.94) for v in cor_materia(cor_tapete))
        return mockup(Image.fromarray(pre.astype(np.uint8)), wcm, hcm, bord, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

MATERIA = '/home/claude/orc/materia/'   # texturas oficiais da matéria-prima (app da Indústria Kapazi)
def tex_kapazi(nome, w, h):
    t = np.asarray(Image.open(MATERIA + nome).convert('RGB')).astype(float)
    reps = (h // t.shape[0] + 1, w // t.shape[1] + 1, 1)
    return np.tile(t, reps)[:h, :w]

def mockup_real(mask, cor_tapete, cor_tin, wcm, hcm, out_png, px=20, bcm=3, textura='vinil-gold-ouro.png'):
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    base = tex_kapazi(textura, iw, ih)
    lum = base.mean(2, keepdims=True); lum = lum / lum.mean()
    tinta = cor_tinta(cor_tin)[None, None, :] * lum
    fin = base * (1 - a) + tinta * a
    m = fin.max(2, keepdims=True); fin = np.where(m > 255, fin * 255 / np.maximum(m, 1), fin)
    pre = np.clip(fin - 13.5, 0, 255)
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.75)
    try:
        bord = tuple(int(v * 0.94) for v in base.reshape(-1, 3).mean(0))
        return mockup(Image.fromarray(pre.astype(np.uint8)), wcm, hcm, bord, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old

# DECISÃO FINAL (17/11): cor do tapete = amostra REAL da matéria-prima (cor_materia); tinta = paleta (cor_tinta)
def mockup_real(mask, cor_tapete, cor_tin, wcm, hcm, out_png, px=20, bcm=3):
    W, H, BP = wcm * px, hcm * px, bcm * px
    iw, ih = W - 2 * BP, H - 2 * BP
    a = np.asarray(mask.convert('L').resize((iw, ih), Image.LANCZOS)).astype(float)[..., None] / 255
    lum = coil2(W, H)[BP:H - BP, BP:W - BP, None]; lum = lum / lum.mean()
    col = cor_materia(cor_tapete)[None, None, :] * (1 - a) + cor_tinta(cor_tin)[None, None, :] * a
    fin = col * lum; m = fin.max(2, keepdims=True); fin = np.where(m > 255, fin * 255 / np.maximum(m, 1), fin)
    pre = np.clip(fin - 13.5, 0, 255)
    g = globals(); old = g['coil']; g['coil'] = lambda w, h, seed=7: np.full((h, w), 0.75)
    try:
        bord = tuple(int(v * 0.94) for v in cor_materia(cor_tapete))
        return mockup(Image.fromarray(pre.astype(np.uint8)), wcm, hcm, bord, out_png, px=px, bcm=bcm)
    finally:
        g['coil'] = old
