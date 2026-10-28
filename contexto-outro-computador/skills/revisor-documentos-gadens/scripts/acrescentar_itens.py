# -*- coding: utf-8 -*-
"""
Acrescenta itens novos a um checklist Word já existente, SEM apagar o que o Bruno
já respondeu.

Regerar o checklist do zero apaga as respostas escritas nas linhas em branco.
Este script abre o arquivo que já existe, descobre quais itens ainda não estão
lá, e insere só esses no fim do bloco do documento correspondente — copiando a
formatação de um item existente, para ficar igual ao resto.

Uso:
    python3 acrescentar_itens.py --arquivo "<checklist.docx>" --novos novos.json [--simular]

novos.json: {"PO.GG.SUP.006": ["texto do item novo", ...], ...}
"""

import argparse
import copy
import io
import json
import os
import re
import shutil
import sys
import unicodedata

from docx import Document


def chave(texto):
    """Identidade do item, para saber se ele já está no arquivo. Usa o verbo
    inicial mais o começo da descrição — o suficiente para não duplicar e para
    tolerar pequenas diferenças de pontuação."""
    t = texto.lstrip("☐ ").strip()
    t = "".join(c for c in unicodedata.normalize("NFD", t.lower())
                if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:55]


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", required=True)
    ap.add_argument("--novos", required=True)
    ap.add_argument("--simular", action="store_true")
    args = ap.parse_args()

    with open(args.novos, encoding="utf-8") as f:
        novos = json.load(f)

    doc = Document(args.arquivo)
    paras = doc.paragraphs

    # Mapeia onde começa cada bloco de documento
    blocos = []
    for i, p in enumerate(paras):
        t = p.text.strip()
        if re.match(r"^(PO|IT|RE)\.[A-Z]{2}\.[A-Z]{3}\.\d{3}", t):
            blocos.append((i, t.split()[0].rstrip("—-").strip()))
    if not blocos:
        sys.exit("nao achei nenhum cabecalho de documento no arquivo")

    # Modelo de formatação: primeiro item e sua linha de resposta
    modelo_item = modelo_linha = None
    for i, p in enumerate(paras):
        if p.text.strip().startswith("☐"):
            modelo_item = p._element
            modelo_linha = paras[i + 1]._element
            break
    if modelo_item is None:
        sys.exit("nao achei nenhum item no arquivo para copiar a formatacao")

    total = 0
    for n, (ini, codigo) in enumerate(blocos):
        fim = blocos[n + 1][0] if n + 1 < len(blocos) else len(paras)
        existentes = {chave(paras[j].text) for j in range(ini, fim)
                      if paras[j].text.strip().startswith("☐")}

        faltando = [x for x in novos.get(codigo, []) if chave(x) not in existentes]
        if not faltando:
            print(f"  {codigo}: nada a acrescentar")
            continue

        # ponto de inserção: antes do próximo cabeçalho (ou no fim do documento)
        ancora = paras[fim]._element if fim < len(paras) else None
        for texto in faltando:
            novo_item = copy.deepcopy(modelo_item)
            nova_linha = copy.deepcopy(modelo_linha)
            # troca o texto, mantendo a formatação do primeiro pedaço
            ts = novo_item.findall(".//{http://schemas.openxmlformats.org/"
                                   "wordprocessingml/2006/main}t")
            if ts:
                ts[0].text = "☐  " + texto
                for extra in ts[1:]:
                    extra.text = ""
            if ancora is not None:
                ancora.addprevious(novo_item)
                ancora.addprevious(nova_linha)
            else:
                doc.element.body.append(novo_item)
                doc.element.body.append(nova_linha)
        print(f"  {codigo}: +{len(faltando)} item(ns)")
        total += len(faltando)

    if args.simular:
        print(f"\n{total} item(ns) seriam acrescentados. SIMULACAO — nada gravado.")
        return

    backup = args.arquivo.replace(".docx", " (antes da inclusao).docx")
    shutil.copy2(args.arquivo, backup)
    doc.save(args.arquivo)
    print(f"\n{total} item(ns) acrescentados.")
    print(f"Copia do arquivo anterior: {os.path.basename(backup)}")


if __name__ == "__main__":
    main()
