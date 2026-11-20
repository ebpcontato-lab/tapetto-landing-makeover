UN = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
def brl(v): return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
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
