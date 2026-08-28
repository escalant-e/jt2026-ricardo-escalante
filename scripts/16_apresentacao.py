from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

NAVY = RGBColor(0x0E, 0x1B, 0x33)
AZUL = RGBColor(0x00, 0x55, 0xFF)
CORAL = RGBColor(0xFC, 0x60, 0x58)
CINZA = RGBColor(0x4A, 0x5A, 0x78)
CLARO = RGBColor(0xF4, 0xF7, 0xFC)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def _rect(slide, x, y, w, h, fill, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
    shp.shadow.inherit = False
    return shp


def _text(slide, x, y, w, h, runs, size=20, color=NAVY, bold=False, align=PP_ALIGN.LEFT,
          font="Calibri", anchor=MSO_ANCHOR.TOP, space=1.0):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    first = True
    for item in runs:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.space_after = Pt(6 * space)
        if isinstance(item, str):
            item = (item, {})
        txt, opts = item
        r = p.add_run()
        r.text = txt
        r.font.size = Pt(opts.get("size", size))
        r.font.bold = opts.get("bold", bold)
        r.font.color.rgb = opts.get("color", color)
        r.font.name = opts.get("font", font)
    return tb


def header(slide, kicker, title):
    _rect(slide, 0, 0, prs.slide_width, Inches(1.25), NAVY)
    _rect(slide, Inches(0.45), Inches(0.33), Inches(0.09), Inches(0.6), CORAL)
    _text(slide, Inches(0.75), Inches(0.22), Inches(11), Inches(0.4),
          [(kicker, dict(size=13, color=RGBColor(0xA9,0xBC,0xDD), bold=True))])
    _text(slide, Inches(0.75), Inches(0.55), Inches(11.5), Inches(0.7),
          [(title, dict(size=30, color=BRANCO, bold=True))])


def footer(slide, n):
    _text(slide, Inches(0.45), Inches(7.05), Inches(5), Inches(0.35),
          [("Seazone · Hackathon Jovens Talentos AI Builder 2026", dict(size=10, color=CINZA))])
    _text(slide, Inches(12.3), Inches(7.05), Inches(0.7), Inches(0.35),
          [(str(n), dict(size=12, color=CINZA))], align=PP_ALIGN.RIGHT)


def bullets(slide, x, y, w, h, items, size=18, gap=10):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    for it in items:
        if isinstance(it, tuple):
            head, body = it
        else:
            head, body = None, it
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(gap)
        p.level = 0
        if head:
            r = p.add_run()
            r.text = "• " + head + " "
            r.font.size = Pt(size)
            r.font.bold = True
            r.font.color.rgb = NAVY
        if body:
            r = p.add_run()
            r.text = body
            r.font.size = Pt(size)
            r.font.color.rgb = CINZA


def tabela(slide, x, y, w, h, colunas, linhas, header_fill=NAVY, col_widths=None, fs=15):
    rows, cols = len(linhas) + 1, len(colunas)
    gt = slide.shapes.add_table(rows, cols, x, y, w, h).table
    if col_widths:
        total = sum(col_widths)
        for i, cw in enumerate(col_widths):
            gt.columns[i].width = Emu(int(w * cw / total))
    for j, cname in enumerate(colunas):
        cell = gt.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = header_fill
        cell.text = cname
        for p in cell.text_frame.paragraphs:
            p.alignment = PP_ALIGN.CENTER
            for r in p.runs:
                r.font.size = Pt(14)
                r.font.bold = True
                r.font.color.rgb = BRANCO
    for i, linha in enumerate(linhas, start=1):
        for j, val in enumerate(linha):
            cell = gt.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CLARO if i % 2 else BRANCO
            cell.text = str(val)
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.CENTER
                for r in p.runs:
                    r.font.size = Pt(fs)
                    r.font.color.rgb = NAVY
    return gt


def build():
    # ===== 1. Capa — recomendação sintética =====
    s = prs.slides.add_slide(BLANK)
    _rect(s, 0, 0, prs.slide_width, prs.slide_height, NAVY)
    _rect(s, 0, Inches(6.05), prs.slide_width, Inches(1.45), AZUL)
    _text(s, Inches(0.9), Inches(1.0), Inches(11.5), Inches(0.5),
          [("HACKATHON · JOVENS TALENTOS AI BUILDER 2026 · SE AZONE", dict(size=13, color=RGBColor(0xA9,0xBC,0xDD), bold=True))])
    _text(s, Inches(0.9), Inches(1.55), Inches(11.5), Inches(1.6),
          [("Recomendação: apartamentos 2Q", dict(size=38, color=BRANCO, bold=True)),
           ("começando por Morretes.", dict(size=38, color=CORAL, bold=True))])
    _text(s, Inches(0.9), Inches(3.4), Inches(11.5), Inches(1.4),
          [("Retorno líquido de encargos de 10,8% a.a. (ocupação 55%) · ticket acessível · alta confiabilidade",
            dict(size=18, color=RGBColor(0xD6,0xDF,0xF0))),
           ("Itapema (SC) · Airbnb + VivaReal · decisão apoiada por IA",
            dict(size=15, color=RGBColor(0xA9,0xBC,0xDD)))])
    _text(s, Inches(0.9), Inches(6.4), Inches(11.5), Inches(0.8),
          [("Análise completa: relatorio.md  ·  Processo com IA: ai-log/  ·  github.com/escalant-e/jt2026-ricardo-escalante",
            dict(size=13, color=BRANCO))])

    # ===== 2. Raciocínio 1 — perfil em 3 óticas =====
    s = prs.slides.add_slide(BLANK)
    header(s, "RACIOCÍNIO 1 DE 2", "Qual perfil? Três óticas, uma decisão")
    tabela(s, Inches(0.75), Inches(1.75), Inches(9.0), Inches(3.6),
           ["Tipologia", "Receita bruta (55%)", "R$/m²", "Retorno s/ capital"],
           [["4Q+", "R$ 210,8 mil", "R$ 1.114", "5,7%"],
            ["3Q", "R$ 130,5 mil", "R$ 1.183", "9,0%"],
            ["2Q", "R$ 90,3 mil", "R$ 1.202", "10,3%"],
            ["1Q", "R$ 77,3 mil", "R$ 1.807", "9,6%"]],
           col_widths=[1, 1.3, 1, 1.2], fs=15)
    _rect(s, Inches(10.05), Inches(1.75), Inches(2.55), Inches(1.5), CORAL)
    _text(s, Inches(10.25), Inches(1.95), Inches(2.15), Inches(1.2),
          [("3Q/4Q+ vencem", dict(size=15, color=BRANCO, bold=True)),
           ("faturamento bruto", dict(size=13, color=BRANCO))])
    _rect(s, Inches(10.05), Inches(3.4), Inches(2.55), Inches(1.5), AZUL)
    _text(s, Inches(10.25), Inches(3.6), Inches(2.15), Inches(1.2),
          [("1Q " , dict(size=15, color=BRANCO, bold=True)),
           ("maximiza R$/m² (1.807)", dict(size=13, color=BRANCO))])
    _rect(s, Inches(10.05), Inches(5.05), Inches(2.55), Inches(1.5), NAVY)
    _text(s, Inches(10.25), Inches(5.25), Inches(2.15), Inches(1.2),
          [("2Q melhor", dict(size=15, color=BRANCO, bold=True)),
           ("retorno (10,3%)", dict(size=13, color=BRANCO))])
    _text(s, Inches(0.75), Inches(5.7), Inches(9.0), Inches(1.1),
          [("Decisão: ", dict(size=20, color=NAVY, bold=True)),
           ("apartamento 2Q — equilíbrio entre liquidez, ticket e reprodutibilidade estatística.", dict(size=20, color=CINZA))])
    footer(s, 2)

    # ===== 3. Raciocínio 2 — localização + driver + tese =====
    s = prs.slides.add_slide(BLANK)
    header(s, "RACIOCÍNIO 2 DE 2", "Onde? O que explica receita?")
    tabela(s, Inches(0.75), Inches(1.6), Inches(6.4), Inches(3.2),
           ["Bairro", "n", "Receita anual (55%)"],
           [["MEIA PRAIA", "630", "R$ 118,4 mil"],
            ["CENTRO", "205", "R$ 102,2 mil"],
            ["MORRETES", "82", "R$ 94,5 mil"]],
           col_widths=[1.2, 0.5, 1.1], fs=15)
    bullets(s, Inches(0.75), Inches(5.0), Inches(6.4), Inches(1.8), [
        ("Localização:", "Meia Praia lidera receita; Centro é alternativa de volume."),
    ], size=16, gap=8)
    _rect(s, Inches(7.5), Inches(1.6), Inches(5.1), Inches(5.2), NAVY)
    _text(s, Inches(7.8), Inches(1.85), Inches(4.5), Inches(0.5),
          [("DRIVERS DE RECEITA (Q3)", dict(size=13, color=RGBColor(0xA9,0xBC,0xDD), bold=True))])
    drivers = [("Tamanho/capacidade", "quartos, banheiros, hóspedes — R²=0,45"),
               ("Ratings", "pouco relevantes"),
               ("Tese 'compactos 1Q no Centro'", "parcialmente validada e reposicionada: ótimo é 2Q, melhor retorno em Morretes")]
    tb = s.shapes.add_textbox(Inches(7.8), Inches(2.45), Inches(4.5), Inches(4.0))
    tf = tb.text_frame; tf.word_wrap = True
    for i, (a, b) in enumerate(drivers):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(16)
        r = p.add_run(); r.text = a + "\n"
        r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = BRANCO
        r2 = p.add_run(); r2.text = b
        r2.font.size = Pt(15); r2.font.color.rgb = RGBColor(0xD6,0xDF,0xF0)
    footer(s, 3)

    # ===== 4. A recomendação =====
    s = prs.slides.add_slide(BLANK)
    header(s, "A RECOMENDAÇÃO", "O que comprar hoje — e por quê")
    tabela(s, Inches(0.75), Inches(1.7), Inches(7.6), Inches(2.9),
           ["Ativo", "Retorno Bruto 55%", "Ret. Liq. Encargos 55%", "Preço mediano"],
           [["MORRETES · 2Q", "11,3%", "10,8%", "R$ 790 mil"],
            ["CENTRO · 2Q", "9,8%", "9,2%", "R$ 1,145M"],
            ["MEIA PRAIA · 2Q", "8,5%", "7,9%", "R$ 1,065M"]],
           col_widths=[1.3, 1, 1.1, 1], fs=15)
    bullets(s, Inches(0.75), Inches(4.9), Inches(7.6), Inches(2.0), [
        ("Racional:", "Morretes 2Q combina melhor retorno (10,8% líquido) com preço acessível (R$ 790 mil)."),
        ("Confiança:", "volumes grandes (59 listings / 1.043 anúncios) = ALTA confiabilidade."),
        ("Equilíbrio:", "liquidez, menor barreira de entrada e reprodutibilidade estatística > taxa nominal máxima."),
    ], size=15, gap=7)
    _rect(s, Inches(8.7), Inches(1.7), Inches(3.9), Inches(4.9), CLARO)
    _text(s, Inches(8.95), Inches(1.95), Inches(3.4), Inches(0.4),
          [("COMO CALCULAMOS", dict(size=13, color=AZUL, bold=True))])
    _text(s, Inches(8.95), Inches(2.4), Inches(3.4), Inches(4.0),
          [("Receita = diária mediana × 365 × ocupação.", dict(size=15, color=NAVY, bold=True)),
           ("Cenários de ocupação: 40% / 55% / 70%.", dict(size=14, color=CINZA)),
           ("Retorno líquido = receita − condomínio×12 − IPTU.", dict(size=14, color=CINZA)),
           ("Não inclui opex (limpeza, energia, taxa da plataforma).", dict(size=12, color=CINZA))])
    footer(s, 4)

    # ===== 5. Como a IA foi usada =====
    s = prs.slides.add_slide(BLANK)
    header(s, "PROCESSO", "Como a IA foi usada")
    bullets(s, Inches(0.75), Inches(1.7), Inches(11.8), Inches(4.8), [
        ("Ferramenta colaborativa, decisão humana:", "a IA testou hipóteses; o analista decidiu cada critério."),
        ("Ponto de virada (Price_AV):", "diagnóstico mostrou que o dado é disponibilidade, não ocupação → modelamos por cenários."),
        ("Qualidade:", "detectou inconsistências (owner duplicado, n pequeno, colinearidade) e auditou o relatório como revisor sênior."),
        ("Rastreabilidade:", "conversa completa em ai-log/ e scripts 01–16."),
    ], size=19, gap=14)
    footer(s, 5)

    # ===== 6. Com mais uma semana =====
    s = prs.slides.add_slide(BLANK)
    header(s, "PRÓXIMOS PASSOS", "O que faria com mais uma semana")
    bullets(s, Inches(0.75), Inches(1.7), Inches(11.8), Inches(4.8), [
        ("Ano completo:", "calibrar sazonalidade real e ocupação de inverno — elimina a principal limitação."),
        ("Custos operacionais:", "transformar 'líquido de encargos' em NOI/cap rate completo."),
        ("Modelo mais robusto + validação externa:", "sensibilidade do limiar de confiança e teste da tese de Morretes com dados censitários."),
        ("Benchmark Seazone:", "comparar com padrões de operação da empresa."),
    ], size=19, gap=14)
    footer(s, 6)

    # ===== 7. Conclusão =====
    s = prs.slides.add_slide(BLANK)
    _rect(s, 0, 0, prs.slide_width, prs.slide_height, NAVY)
    _rect(s, 0, Inches(6.2), prs.slide_width, Inches(1.3), AZUL)
    _text(s, Inches(0.9), Inches(0.9), Inches(11.5), Inches(0.5),
          [("CONCLUSÃO", dict(size=14, color=RGBColor(0xA9,0xBC,0xDD), bold=True))])
    _text(s, Inches(0.9), Inches(1.4), Inches(11.5), Inches(2.2),
          [("Investir em apartamentos 2Q,", dict(size=40, color=BRANCO, bold=True)),
           ("começando por Morretes.", dict(size=40, color=CORAL, bold=True))])
    _text(s, Inches(0.9), Inches(3.6), Inches(11.5), Inches(2.2),
          [("10,8% a.a. líquido de encargos (55% de ocupação), com ticket acessível e alta confiabilidade.",
            dict(size=20, color=RGBColor(0xD6,0xDF,0xF0))),
           ("Tese dos compactos: validada na intuição (eficiência), ajustada na execução (2Q, Morretes).",
            dict(size=17, color=RGBColor(0xA9,0xBC,0xDD)))])
    _text(s, Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.8),
          [("Obrigado!  ", dict(size=22, color=BRANCO, bold=True)),
           ("Relatório: relatorio.md · Código: scripts/ · Processo: ai-log/", dict(size=14, color=BRANCO))])
    footer(s, 7)

    out = os.path.join(os.path.dirname(__file__), "..", "output", "apresentacao_seazone_itapema.pptx")
    prs.save(out)
    print("Salvo:", out, "(", len(prs.slides._sldIdLst), "slides )")


import os
if __name__ == "__main__":
    build()