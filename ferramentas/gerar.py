#!/usr/bin/env python3
"""Gera os cronogramas (HTML) e os menus a partir de dados/*.json.

Uso (na raiz do repositório):
    python ferramentas/gerar.py

Só usa a biblioteca padrão do Python. Não precisa instalar nada.

O que ele faz:
  1. lê cada arquivo de dados/*.json (um por projeto);
  2. escreve cronogramas/<projeto>.html usando ferramentas/modelo_gantt.html;
  3. escreve o menu de cada empresa (<empresa>/index.html);
  4. escreve o menu principal (index.html).

Os números dos menus (término previsto, atraso sobre o ideal, tarefas concluídas)
são calculados aqui com a mesma regra do cronograma, então menu e Gantt não divergem.
"""
import copy
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(RAIZ, "dados")
FERR = os.path.join(RAIZ, "ferramentas")
ORDEM_EMPRESAS = ["Gadens", "Make It"]   # ordem dos caminhos no menu principal


def slug(texto):
    s = texto.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def ler(caminho):
    with open(caminho, encoding="utf-8") as f:
        return f.read()


def gravar(caminho, texto):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def br(d):
    return d.strftime("%d/%m/%Y")


# --------------------------------------------------------------------------
# Cálculo do cronograma (mesma regra do JavaScript do modelo_gantt.html)
# --------------------------------------------------------------------------
def calcular(D):
    uteis = D.get("diasUteis") is not False
    feriados = set(D.get("feriados", []))
    d = dt.date.fromisoformat(D["inicio"])
    cal = []
    while len(cal) < 4000:
        if not uteis or (d.weekday() < 5 and d.isoformat() not in feriados):
            cal.append(d)
        d += dt.timedelta(days=1)

    def idx(texto):
        alvo = dt.date.fromisoformat(texto)
        for i, x in enumerate(cal):
            if x >= alvo:
                return i
        return len(cal) - 1

    T = {}
    for t in D["tarefas"]:
        t["_id"] = str(t["id"])
        T[t["_id"]] = t
    ordem, visto = [], set()

    def visita(t):
        if t["_id"] in visto:
            return
        visto.add(t["_id"])
        for dep in t.get("depende", []):
            visita(T[str(dep)])
        ordem.append(t)

    for t in D["tarefas"]:
        visita(t)

    for t in ordem:
        t["_dur"] = 0 if t.get("marco") else max(1, round(t.get("duracao") or 1))
        dep = max([T[str(x)]["_ef"] for x in t.get("depende", [])], default=0)
        fixo = idx(t["inicio"]) if t.get("inicio") else None
        iniciada = (t.get("progresso") or 0) > 0
        if fixo is not None and iniciada:
            es = fixo        # tarefa iniciada: vale a data informada
        else:
            es = max(fixo or 0, dep)   # a iniciar: dependência pode empurrar
        t["_es"], t["_ef"] = es, es + t["_dur"]
        if t["_dur"]:
            t["_ini"], t["_fim"] = cal[es], cal[es + t["_dur"] - 1]
        else:
            usa_anterior = es > 0 and t.get("depende") and not t.get("inicio")
            t["_ini"] = t["_fim"] = cal[es - 1] if usa_anterior else cal[es]

    previsto = [t for t in D["tarefas"] if not t.get("referencia")]
    ideal = [t for t in D["tarefas"] if t.get("referencia")]
    reais = [t for t in previsto if not t.get("marco")]
    res = {
        "termino": max(t["_fim"] for t in previsto),
        "concluidas": sum(1 for t in reais if (t.get("progresso") or 0) >= 100),
        "total": len(reais),
        "uteis": uteis,
        "ideal": None,
        "dif": None,
    }
    if ideal:
        res["ideal"] = max(t["_fim"] for t in ideal)
        res["dif"] = max(t["_ef"] for t in previsto) - max(t["_ef"] for t in ideal)
    return res


# --------------------------------------------------------------------------
# Páginas
# --------------------------------------------------------------------------
def carregar_projetos():
    projetos = []
    for caminho in sorted(glob.glob(os.path.join(DADOS, "*.json"))):
        bruto = json.loads(ler(caminho))
        meta = bruto.pop("_meta", {})
        D = bruto
        projetos.append({"arquivo": os.path.basename(caminho), "meta": meta, "D": D})
    return projetos


def pagina_gantt(modelo, p):
    D, meta = p["D"], p["meta"]
    empresa = meta.get("empresa", "Make It")
    dados = json.dumps(D, ensure_ascii=False, indent=1)
    return (modelo.replace("__TITULO__", D["projeto"])
                  .replace("__EMPRESA__", empresa)
                  .replace("__EMPRESA_SLUG__", slug(empresa))
                  .replace("__DADOS__", dados))


def partes_nome(projeto):
    if " · " in projeto:
        nome, resto = projeto.split(" · ", 1)
        return nome, resto
    return projeto, ""


def cartao_projeto(p, r):
    nome, resto = partes_nome(p["D"]["projeto"])
    arquivo = urllib.parse.quote(p["D"]["projeto"] + ".html")
    un = "dias úteis" if r["uteis"] else "dias"
    sobre = f"+{r['dif']} {un}" if r["dif"] is not None else "—"
    ideal = br(r["ideal"]) if r["ideal"] else "—"
    return (
        f'    <a class="card" href="../cronogramas/{arquivo}">\n'
        f'      <span class="tag">{resto}</span>\n'
        f'      <h2>{nome}</h2>\n'
        f'      <dl class="dados">\n'
        f'        <div><dt>Término previsto</dt><dd>{br(r["termino"])}</dd></div>\n'
        f'        <div><dt>Sobre o ideal</dt><dd class="alerta">{sobre}</dd></div>\n'
        f'        <div><dt>Tarefas concluídas</dt><dd>{r["concluidas"]} de {r["total"]}</dd></div>\n'
        f'        <div><dt>Término ideal</dt><dd>{ideal}</dd></div>\n'
        f'      </dl>\n'
        f'      <div class="go">Abrir cronograma &rarr;</div>\n'
        f'    </a>'
    )


def frase_empresa(lista):
    nomes = [partes_nome(p["D"]["projeto"])[0] for p in lista]
    sufixos = {partes_nome(p["D"]["projeto"])[1] for p in lista}
    n = len(lista)
    plural = "cronograma" if n == 1 else "cronogramas"
    if len(nomes) > 1:
        lista_nomes = ", ".join(nomes[:-1]) + " e " + nomes[-1]
    else:
        lista_nomes = nomes[0]
    texto = f"{n} {plural}: {lista_nomes}"
    if len(sufixos) == 1 and next(iter(sufixos)):
        s = next(iter(sufixos))
        texto += ", " + s[0].lower() + s[1:]
    return texto + "."


def main():
    modelo_gantt = ler(os.path.join(FERR, "modelo_gantt.html"))
    modelo_menu = ler(os.path.join(FERR, "modelo_menu.html"))
    modelo_empresa = ler(os.path.join(FERR, "modelo_empresa.html"))

    projetos = carregar_projetos()
    if not projetos:
        sys.exit("Nenhum arquivo em dados/*.json")

    por_empresa = {}
    posicoes = []
    for p in projetos:
        r = calcular(copy.deepcopy(p["D"]))   # cópia: o cálculo não altera os dados
        p["r"] = r
        por_empresa.setdefault(p["meta"].get("empresa", "Make It"), []).append(p)
        if p["meta"].get("posicao"):
            posicoes.append(dt.date.fromisoformat(p["meta"]["posicao"]))
        saida = os.path.join(RAIZ, "cronogramas", p["D"]["projeto"] + ".html")
        gravar(saida, pagina_gantt(modelo_gantt, p))
        print("cronograma:", os.path.relpath(saida, RAIZ))

    posicao = br(max(posicoes)) if posicoes else ""

    # menu de cada empresa
    for empresa, lista in por_empresa.items():
        cartoes = "\n\n".join(cartao_projeto(p, p["r"]) for p in lista)
        html = (modelo_empresa.replace("__EMPRESA__", empresa)
                              .replace("__CARTOES__", cartoes)
                              .replace("__POSICAO__", posicao))
        saida = os.path.join(RAIZ, slug(empresa), "index.html")
        gravar(saida, html)
        print("menu da empresa:", os.path.relpath(saida, RAIZ))

    # menu principal
    empresas = list(ORDEM_EMPRESAS) + [e for e in por_empresa if e not in ORDEM_EMPRESAS]
    cartoes = []
    for i, empresa in enumerate(empresas, 1):
        lista = por_empresa.get(empresa)
        if lista:
            cartoes.append(
                f'    <a class="card" href="{slug(empresa)}/">\n'
                f'      <div class="num">{i}</div>\n'
                f'      <h2>{empresa}</h2>\n'
                f'      <p>{frase_empresa(lista)}</p>\n'
                f'      <div class="go">Abrir &rarr;</div>\n'
                f'    </a>')
        else:
            cartoes.append(
                f'    <div class="card off" aria-disabled="true">\n'
                f'      <div class="num">{i}</div>\n'
                f'      <h2>{empresa}</h2>\n'
                f'      <p>Nenhum cronograma publicado ainda.</p>\n'
                f'      <div class="go">Em breve</div>\n'
                f'    </div>')
    html = modelo_menu.replace("__CARTOES__", "\n\n".join(cartoes)).replace("__POSICAO__", posicao)
    gravar(os.path.join(RAIZ, "index.html"), html)
    print("menu principal: index.html")


if __name__ == "__main__":
    main()
