# -*- coding: utf-8 -*-
"""Gantt do fluxo de lançamentos (Comercial), a partir de
'resumo fluxo Gadens Next lançamentos.xlsx'. Escala em dias corridos, dia 0 = entrada PL.
A 3ª linha da planilha de origem (IMAGENS mais curta) foi ignorada a pedido do Bruno."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SAIDA = (r"C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki"
         r"\Projeto teste\Gantt - Fluxo de Lançamentos (Comercial).xlsx")

DIA_MAX, PASSO = 190, 5
COL0 = 6                       # primeira coluna da régua (F)
N_COLS = DIA_MAX // PASSO + 1  # 48

# Ordem e cores seguem a planilha de origem de 02/10 (versão 2). As cores são os
# slots 1 a 5 da paleta de referência do dataviz, atribuídos na ordem das faixas —
# validados para daltonismo nos dois modos. A paleta anterior (tons dessaturados)
# estava reprovada: verde e azul acinzentados ficavam a dE 8,4, abaixo do piso de 15.
FRENTES = [
    ("DOCUMENTAÇÃO", "2A78D6", [("entrada PL", 0), ("retorno 1º PL", 30), ("retorno 2º PL", 70),
                                ("retorno 3º PL", 110), ("alvará", 140), ("RI", 180)]),
    ("IMAGENS",      "EB6834", [("1º tiro", 45), ("2º tiro", 125), ("3º tiro", 140), ("HR", 150)]),
    ("ORÇAMENTO",    "1BAF7A", [("início orçamento", 80), ("1ª revisão orçamentária", 120),
                                ("orçamento final", 140)]),
    ("MAQUETE",      "EDA100", [("início maquete", 125), ("maquete final", 185)]),
    ("TAKES",        "E87BA4", [("início takes", 150), ("takes HR", 190)]),
]
FASE_INICIAL = "Anteprojeto"   # marcação do dia 0 na planilha de origem

CINZA_T, CINZA_C = "3F3F3F", "F2F2F2"
fina = Side(style="thin", color="D9D9D9")
BORDA = Border(left=fina, right=fina, top=fina, bottom=fina)


def col_do_dia(dia):
    return COL0 + dia // PASSO


def clarear(hex_cor, fator=0.72):
    r, g, b = (int(hex_cor[i:i+2], 16) for i in (0, 2, 4))
    return "".join(f"{int(c + (255 - c) * fator):02X}" for c in (r, g, b))


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Gantt"

    # ---------- título ----------
    ws["A1"] = "Fluxo de Lançamentos — Comercial"
    ws["A1"].font = Font(name="Arial", size=14, bold=True, color=CINZA_T)
    ws["A2"] = ("Escala em dias corridos a partir da entrada do PL (dia 0).  "
                "Origem: resumo fluxo Gadens Next lançamentos.xlsx, versão 2, de 02/10.")
    ws["A2"].font = Font(name="Arial", size=9, italic=True, color="7F7F7F")

    # ---------- etiqueta da fase, acima da régua ----------
    # Estava só na página; a planilha ficou sem. Vem da célula do dia 0 da origem.
    c = ws.cell(3, COL0, FASE_INICIAL)
    c.font = Font(name="Arial", size=8, bold=True, italic=True, color="7F7F7F")
    c.alignment = Alignment(horizontal="left", vertical="bottom")
    ws.row_dimensions[3].height = 13

    # ---------- cabeçalho ----------
    LIN_CAB = 4
    for col, texto, larg in ((1, "Frente", 17), (2, "Início (dia)", 10),
                             (3, "Fim (dia)", 9), (4, "Duração", 9), (5, "Marcos", 8)):
        c = ws.cell(LIN_CAB, col, texto)
        c.font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=CINZA_T)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDA
        ws.column_dimensions[get_column_letter(col)].width = larg

    for i in range(N_COLS):
        dia = i * PASSO
        col = COL0 + i
        c = ws.cell(LIN_CAB, col, dia)
        c.font = Font(name="Arial", size=7, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=CINZA_T if dia % 25 == 0 else "7F7F7F")
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = BORDA
        ws.column_dimensions[get_column_letter(col)].width = 3.1
    ws.row_dimensions[LIN_CAB].height = 20

    # ---------- uma frente = linha de rótulos + linha de barra ----------
    linha = LIN_CAB + 1
    for nome, cor, marcos in FRENTES:
        dias = [d for _, d in marcos]
        ini, fim = min(dias), max(dias)

        lin_rot, lin_bar = linha, linha + 1
        ws.row_dimensions[lin_rot].height = 11
        ws.row_dimensions[lin_bar].height = 17

        # rótulos dos marcos, começando na coluna do próprio marco
        for rotulo, dia in marcos:
            c = ws.cell(lin_rot, col_do_dia(dia), rotulo)
            c.font = Font(name="Arial", size=7, color=cor, bold=True)
            c.alignment = Alignment(horizontal="left", vertical="bottom")

        # coluna de identificação
        cel = ws.cell(lin_bar, 1, nome)
        cel.font = Font(name="Arial", size=9, bold=True, color=CINZA_T)
        cel.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        # a cor identifica pela barra lateral; texto branco sobre amarelo não tem contraste
        cel.border = Border(left=Side(style="thick", color=cor), top=fina,
                            right=fina, bottom=fina)
        for col, valor in ((2, ini), (3, fim), (4, fim - ini), (5, len(marcos))):
            c = ws.cell(lin_bar, col, valor)
            c.font = Font(name="Arial", size=9, color=CINZA_T)
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.border = BORDA

        claro = clarear(cor)
        dias_marco = set(dias)
        for i in range(N_COLS):
            dia = i * PASSO
            c = ws.cell(lin_bar, COL0 + i)
            c.border = BORDA
            if dia in dias_marco:
                c.value = "◆"
                c.fill = PatternFill("solid", fgColor=cor)
                c.font = Font(name="Arial", size=8, bold=True, color="FFFFFF")
                c.alignment = Alignment(horizontal="center", vertical="center")
            elif ini < dia < fim:
                c.fill = PatternFill("solid", fgColor=claro)
            elif dia % 25 == 0:
                c.fill = PatternFill("solid", fgColor=CINZA_C)
        linha += 2

    # ---------- tabela de marcos ----------
    lin = linha + 1
    ws.cell(lin, 1, "MARCOS, EM ORDEM").font = Font(name="Arial", size=11, bold=True, color=CINZA_T)
    lin += 1
    for col, texto in ((1, "Frente"), (2, "Marco"), (3, "Dia"), (4, "Dias desde o anterior")):
        c = ws.cell(lin, col, texto)
        c.font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=CINZA_T)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDA
    ws.column_dimensions["B"].width = 22

    todos = sorted(((d, n, c, m) for n, c, ms in FRENTES for m, d in ms), key=lambda x: (x[0], x[1]))
    anterior = None
    for i, (dia, frente, cor, marco) in enumerate(todos):
        r = lin + 1 + i
        vals = [frente, marco, dia, "" if anterior is None else dia - anterior]
        for col, v in enumerate(vals, start=1):
            c = ws.cell(r, col, v)
            c.font = Font(name="Arial", size=9,
                          color="FFFFFF" if col == 1 else CINZA_T,
                          bold=(col == 1))
            if col == 1:
                c.fill = PatternFill("solid", fgColor=cor)
                c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
            else:
                c.alignment = Alignment(horizontal="center" if col > 2 else "left",
                                        vertical="center", indent=0 if col > 2 else 1)
            c.border = BORDA
        anterior = dia

    # ---------- impressão ----------
    ws.freeze_panes = ws.cell(LIN_CAB + 1, COL0)
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = f"{LIN_CAB}:{LIN_CAB}"
    ws.sheet_view.showGridLines = False

    wb.save(SAIDA)
    print(f"gerado: {SAIDA}")
    print(f"  {len(FRENTES)} frentes, {len(todos)} marcos, régua de 0 a {DIA_MAX} dias")


if __name__ == "__main__":
    main()
