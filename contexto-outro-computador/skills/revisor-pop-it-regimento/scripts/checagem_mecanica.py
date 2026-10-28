# -*- coding: utf-8 -*-
"""
Checagem mecânica de POPs / ITs / Regimentos do Grupo Gadens.

Faz APENAS as conferências que não exigem julgamento — as que um programa acerta
sempre e a leitura à mão erra de vez em quando. NÃO substitui a revisão: não sabe
dizer se a ordem dos passos faz sentido, se falta um desvio, ou se uma definição
combina com o termo. Isso continua sendo trabalho de leitura.

Só LÊ os arquivos. Nunca altera nada.

Uso:
    python3 checagem_mecanica.py "caminho\\PO.GG.SUP.009 - ....docx" [outro.docx ...]
    python3 checagem_mecanica.py --pasta "C:\\...\\Aprovação"

O que confere:
  TEXTO (vale para qualquer .docx)
    - pontuação final dos passos inconsistente (uns com ";", outros com ".")
    - vírgula indevida depois de "contendo", "após", "bem como", "sendo"
    - formas verbais misturadas no mesmo passo ("Localizar ... e realiza")
    - voz passiva no meio de passos no infinitivo ("O material é entregue")
    - parêntese aberto e não fechado
    - espaço duplo e espaço antes de pontuação
    - sobras do modelo ("Não especificado no texto de origem", etc.)

  ESTRUTURA (POP / IT / Regimento do Grupo Gadens)
    - capa x cabeçalho x rodapé (Tipo de documento, código, revisão, data)
    - matriz de papéis: onde cada papel aparece e onde falta
    - variações de grafia do mesmo papel
    - desvio circular (o responsável é o mesmo nome citado dentro da ação)
    - coluna de tabela com o mesmo valor em todas as linhas (não discrimina)
    - contradição na seção de Indicadores
    - definições quase idênticas entre si (papéis duplicados)
"""

import argparse
import difflib
import glob
import io
import os
import re
import sys
import unicodedata
import zipfile

try:
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
except ImportError:
    sys.exit("Falta a biblioteca python-docx. Instale com: pip install python-docx")

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# --------------------------------------------------------------------------
# Listas de apoio
# --------------------------------------------------------------------------

# Textos de fábrica extraídos dos modelos reais em 2026-08-26 (ver references/templates.md).
# Se algum deles sobreviveu no documento preenchido, a seção ficou sem preencher.
SOBRAS_MODELO = [
    # marca do nosso processo de elaboração — não pode circular
    "Não especificado no texto de origem",
    # PO.GG.QLD.001 / RE.GG.PRO.001 / IT.GG.PRO.001 — comuns
    "Definir o objetivo e o escopo do documento",
    "Descrever a Empresa aplicável e os setores envolvidos no processo",
    "Relacionar as normas técnicas, legislações, procedimentos, especificações",
    "Identificar e descrever os termos técnicos",
    "Identificar os entregáveis do processo",
    "Entregáveis do processo, ou seja",
    "diretrizes estratégicas de prospecção",
    # capa
    "Padrão de formatação para documentos",
    "TÍTULO DE PROCEDIMENTO OPERACIONAL PADRÃO",
    "TÍTULO DE REGIMENTO",
    "TÍTULO DA INSTRUÇÃO DE TRABALHO",
    "Escolher um item",
    # IT
    "Inserir texto explicativo da tarefa realizada",
    "Inserir imagem referente ao procedimento descrito",
    "Para cada passo realizado no procedimento, incluir o texto explicativo",
    # Regimento
    "Mencionar quais áreas estão envolvidas na reunião",
    "Informar de quem é a responsabilidade de convocar",
    "Informar recorrência, dia da semana, horário e exceções",
    "Informar se a reunião ocorrerá presencial ou online",
    "Detalhar a pauta a ser tratada em cada reunião",
    "Informar o registro/evidência/alinhamento fruto do encontro",
    "Nome da Área",
    "Informar as responsabilidades da área dentro da reunião",
    "Input necessário para reun",
    "Output necessário para reun",
    "Descrever características do input",
    "Descrever características do output",
    "Setor responsável por entregar o input",
    "Setor responsável por entregar o output",
    # controle de emissão
    "DD/MM/AAAA",
    "00/00/0000",
    "XXXX",
]

# 3ª pessoa do singular, presente — formas vistas nos documentos reais.
# Lista fechada de propósito: evita falso positivo que uma regra genérica geraria.
VERBOS_3A_PESSOA = {
    "realiza", "avalia", "verifica", "analisa", "faz", "insere", "confirma",
    "registra", "disponibiliza", "separa", "entrega", "valida", "identifica",
    "cadastra", "corrige", "atualiza", "envia", "preenche", "inspeciona",
    "acondiciona", "assina", "coleta", "organiza", "arquiva", "comunica",
    "informa", "solicita", "emite", "conduz", "controla", "garante", "autoriza",
    "recebe", "conclui", "aprova", "reprova", "encaminha", "libera", "consulta",
}

CONECTORES_SEM_VIRGULA = ["contendo", "após", "bem como", "sendo", "mediante", "durante"]

# Verbos transitivos comuns nestes documentos. Vírgula logo depois deles separa o
# verbo do objeto direto, que é erro ("a fim de garantir, ausência de duplicidade").
# Entrou em 2026-08-26: a lista de conectores acima não pegava esse caso.
VERBOS_ANTES_DO_OBJETO = [
    "garantir", "assegurar", "conter", "incluir", "informar", "verificar",
    "conferir", "registrar", "analisar", "descrever", "apresentar", "contendo",
]

SECOES_POP = [
    "OBJETIVO", "APLICAÇÃO", "REFERÊNCIAS", "DEFINIÇÕES", "RECURSOS NECESSÁRIOS",
    "PRINCIPAIS PASSOS DO PROCESSO", "PAPÉIS, RESPONSABILIDADES E AUTONOMIA",
    "INDICADORES", "PONTOS CRÍTICOS DO PROCESSO", "DESVIOS / AÇÕES NECESSÁRIAS",
    "REGISTRO DO PROCESSO", "CONTROLE DE EMISSÃO",
]
SECOES_IT = [
    "OBJETIVO", "APLICAÇÃO", "REFERÊNCIAS", "DEFINIÇÕES",
    "ETAPAS DA INSTRUÇÃO DE TRABALHO", "CONTROLE DE EMISSÃO",
]
# Nomes exatos do RE.GG.PRO.001. "RESPONSÁBILIDADES" (com acento) é erro do próprio
# modelo — fica nas duas grafias para a seção ser reconhecida de qualquer jeito.
SECOES_RE = [
    "OBJETIVO", "APLICAÇÃO", "ÁREAS ENVOLVIDAS", "GOVERNANÇA E OPERACIONALIZAÇÃO",
    "PAPÉIS E RESPONSABILIDADES", "PAPÉIS E RESPONSÁBILIDADES",
    "ENTRADAS DO PROCESSO (INPUTS)", "SAÍDAS DO PROCESSO (OUTPUTS)",
    "REFERÊNCIAS", "CONTROLE DE EMISSÃO",
]

SECAO_PASSOS = {
    "PO": "PRINCIPAIS PASSOS DO PROCESSO",
    "IT": "ETAPAS DA INSTRUÇÃO DE TRABALHO",
    "RE": "GOVERNANÇA",
}


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def normaliza(s):
    """Para comparar nomes de papel: minúsculo, sem acento, sem espaço extra."""
    s = sem_acento(s.lower()).strip()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def paragrafos_do_xml(xml_bytes):
    """Junta os pedaços de texto de cada parágrafo. O Word quebra uma frase em
    vários pedaços; sem juntar, campos preenchidos parecem vazios."""
    txt = xml_bytes.decode("utf-8", errors="replace")
    saida = []
    for bloco in re.findall(r"<w:p[ >].*?</w:p>", txt, re.S):
        pedacos = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", bloco)
        junto = "".join(pedacos).strip()
        if junto:
            saida.append(junto)
    return saida


def tipo_do_documento(nome_arquivo, codigo):
    for origem in (codigo or "", os.path.basename(nome_arquivo)):
        m = re.match(r"\s*(PO|IT|RE|FL|MQ|IM|FI|FP)\.", origem)
        if m:
            return m.group(1)
    return None


# --------------------------------------------------------------------------
# Leitura do arquivo
# --------------------------------------------------------------------------

def ler_documento(caminho):
    d = docx.Document(caminho)
    dados = {"caminho": caminho, "nome": os.path.basename(caminho)}

    # Corpo: parágrafos e tabelas, na ordem em que aparecem
    corpo = []
    for filho in d.element.body.iterchildren():
        tag = filho.tag.split("}")[-1]
        if tag == "p":
            par = Paragraph(filho, d)
            texto = par.text.strip()
            if texto:
                estilo = par.style.name if par.style is not None else ""
                corpo.append(("p", texto, estilo))
        elif tag == "tbl":
            t = Table(filho, d)
            linhas = [[c.text.strip() for c in row.cells] for row in t.rows]
            corpo.append(("tbl", linhas, ""))
    dados["corpo"] = corpo
    dados["tabelas"] = [x[1] for x in corpo if x[0] == "tbl"]

    # Capa, cabeçalho e rodapé vêm do XML cru: a capa fica dentro de uma caixa
    # de texto, que o python-docx não enxerga.
    with zipfile.ZipFile(caminho) as z:
        doc_xml = z.read("word/document.xml").decode("utf-8", errors="replace")
        cab, rod = [], []
        for nome in z.namelist():
            if re.match(r"word/header\d*\.xml$", nome):
                cab += paragrafos_do_xml(z.read(nome))
            elif re.match(r"word/footer\d*\.xml$", nome):
                rod += paragrafos_do_xml(z.read(nome))
    dados["cabecalho"] = " | ".join(cab)
    dados["rodape"] = " | ".join(rod)

    corte = doc_xml.find(">OBJETIVO<")
    capa_xml = doc_xml[:corte] if corte > 0 else doc_xml
    capa_txt = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", capa_xml))
    capa_txt = re.sub(r"\s+", " ", capa_txt)
    dados["capa_texto"] = capa_txt

    def campo(rotulo, texto, ate=r"(?:Código|Data|Revisão|Status|Elaborador|Aprovador|Empresas|Tipo|$)"):
        m = re.search(rotulo + r"\s*:?\s*(.*?)\s*" + ate, texto)
        return m.group(1).strip(" :") if m else ""

    dados["capa"] = {
        "tipo": campo("Tipo de documento", capa_txt),
        "codigo": re.sub(r"\s+", "", campo("Código do documento", capa_txt)),
        "data": campo("Data", capa_txt),
        "revisao": campo("Revisão", capa_txt),
        "status": campo("Status", capa_txt),
        "elaborador": campo("Elaborador", capa_txt),
        "aprovador": campo("Aprovador", capa_txt),
    }
    dados["tipo"] = tipo_do_documento(caminho, dados["capa"]["codigo"])

    # Seções do corpo
    lista_secoes = {"PO": SECOES_POP, "IT": SECOES_IT, "RE": SECOES_RE}.get(dados["tipo"], SECOES_POP)
    secoes, atual = {}, None
    for kind, item, estilo in corpo:
        if kind == "p":
            achou = None
            alvo = normaliza(item)
            for s in lista_secoes:
                if alvo == normaliza(s) or alvo.startswith(normaliza(s)[:18]):
                    achou = s
                    break
            if achou and len(item) < 70:
                atual = achou
                secoes.setdefault(atual, {"paragrafos": [], "tabelas": [], "estilos": []})
                continue
        if atual:
            if kind == "p":
                secoes[atual]["paragrafos"].append(item)
                secoes[atual]["estilos"].append(estilo)
            else:
                secoes[atual]["tabelas"].append(item)
    dados["secoes"] = secoes
    return dados


def extrair_passos(dados):
    """Passos no formato 'Título (Executor): ação'."""
    nome_secao = SECAO_PASSOS.get(dados["tipo"], "PRINCIPAIS PASSOS DO PROCESSO")
    sec = dados["secoes"].get(nome_secao)
    if not sec:
        return []
    passos = []
    for p in sec["paragrafos"]:
        # forma preferida: o executor vem entre parênteses
        m = re.match(r"^(.{3,80}?)\s*\(([^)]{2,60})\)\s*:\s*(.+)$", p)
        if m:
            passos.append({"titulo": m.group(1).strip(),
                           "executor": m.group(2).strip(),
                           "acao": m.group(3).strip(),
                           "texto": p})
            continue
        # forma sem executor declarado: "Título: ação". Também é um passo — o que
        # falta ali é o responsável, e isso vira um achado próprio
        # (conf_passos_sem_executor), não o sumiço do passo inteiro.
        # Só vale para item de LISTA: num POP que descreve fases, parágrafos
        # soltos como "Objetivo: ..." e "Resultado: ..." não são passos, e sem
        # esse filtro entravam como se fossem.
        if not estilo_de_lista(sec, p):
            continue
        m = re.match(r"^([^:]{3,80}):\s*(.+)$", p)
        if m:
            passos.append({"titulo": m.group(1).strip(),
                           "executor": "",
                           "acao": m.group(2).strip(),
                           "texto": p})
    return passos


def estilo_de_lista(sec, paragrafo):
    """O parágrafo veio como item de lista? Usa os estilos guardados junto."""
    estilos = sec.get("estilos") or []
    try:
        i = sec["paragrafos"].index(paragrafo)
    except ValueError:
        return False
    return i < len(estilos) and "list" in (estilos[i] or "").lower()


def conf_passos_sem_executor(dados, achados):
    """Passo que não diz quem executa. Um achado só para o documento inteiro —
    listar passo a passo vira ruído."""
    passos = extrair_passos(dados)
    if not passos:
        return
    sem = [p["titulo"] for p in passos if not p["executor"]]
    if len(sem) == len(passos):
        achados.append(
            "PASSOS  Nenhum dos {} passos declara quem executa — todos estão no formato "
            "\"Título: ação\", sem o responsável. A Tabela de Responsabilidades diz quem faz "
            "o quê, mas o fluxo não amarra cada passo a um papel".format(len(passos)))
    elif sem:
        achados.append(
            "PASSOS  {} de {} passos não declaram quem executa: {}".format(
                len(sem), len(passos), ", ".join(f'"{t}"' for t in sem[:4])))


# --------------------------------------------------------------------------
# Conferências de texto
# --------------------------------------------------------------------------

def conf_pontuacao_passos(dados, achados):
    passos = extrair_passos(dados)
    if len(passos) < 2:
        return
    fins = [p["texto"].rstrip()[-1:] for p in passos]

    # Padrão correto: ";" em todos, "." só no último. Não é regra do QLD.002 (ele
    # não trata de listas), é a convenção do Bruno — e é o que a correção aplica.
    # Sem esta exceção, o verificador acusaria como erro justamente o estado certo.
    correto = all(f == ";" for f in fins[:-1]) and fins[-1] == "."
    if correto:
        return
    # Todos iguais também passa: é coerente, ainda que não siga a convenção.
    if len(set(fins)) == 1:
        return

    ponto_virgula = [i for i, f in enumerate(fins, 1) if f == ";"]
    ponto = [i for i, f in enumerate(fins, 1) if f == "."]
    if ponto_virgula and ponto:
        achados.append(
            "TEXTO  Pontuação final dos passos misturada: "
            "passo(s) {} terminam com \";\" e passo(s) {} terminam com \".\" "
            "(esperado: \";\" em todos e \".\" só no último)".format(
                ", ".join(map(str, ponto_virgula)), ", ".join(map(str, ponto))))


def conf_celulas_sem_ponto(dados, achados):
    """Nas tabelas cujas células são frases inteiras: Responsabilidades e Definições.
    Fica de fora Desvios e Controle de Emissão, onde as células são rótulos curtos e
    cobrar ponto final seria só ruído.

    Definições entrou em 2026-08-26: a versão anterior olhava só Responsabilidades e
    por isso deixou passar as três definições sem ponto do PO.GG.SUP.010."""
    alvos = [
        ("Tabela de Responsabilidades", 1,
         ("PAPÉIS, RESPONSABILIDADES E AUTONOMIA", "PAPÉIS E RESPONSABILIDADES")),
        ("Tabela de Definições", 1, ("DEFINIÇÕES",)),
    ]
    for rotulo, col, secoes in alvos:
        for nome_sec in secoes:
            for tabela in dados["secoes"].get(nome_sec, {}).get("tabelas", []):
                if len(tabela) < 2:
                    continue
                faltando = []
                for n_lin, linha in enumerate(tabela[1:], 2):
                    if len(linha) <= col:
                        continue
                    t = linha[col].strip()
                    if len(t) > 25 and not t.endswith((".", ";")):
                        faltando.append("linha {}".format(n_lin))
                if faltando:
                    achados.append("TEXTO  {}: célula sem ponto final na(s) {}".format(
                        rotulo, ", ".join(faltando)))


def conf_virgula_conector(dados, achados):
    for kind, item, _estilo in dados["corpo"]:
        if kind != "p":
            continue
        for con in CONECTORES_SEM_VIRGULA:
            if re.search(r"\b" + con + r"\s*,", item, re.I):
                achados.append("TEXTO  Vírgula indevida depois de \"{}\": ...{}...".format(
                    con, trecho(item, con)))
        for v in VERBOS_ANTES_DO_OBJETO:
            # vírgula entre o verbo e o objeto: "garantir, ausência de duplicidade"
            if re.search(r"\b" + v + r"\s*,\s+[a-zà-ú]", item, re.I):
                achados.append(
                    "TEXTO  Vírgula separando o verbo do objeto em \"{}\": ...{}...".format(
                        v, trecho(item, v)))


def conf_verbo_misturado(dados, achados):
    for p in extrair_passos(dados):
        acao = p["acao"]
        primeira = re.match(r"\s*(\w+)", acao)
        if not primeira:
            continue
        pal = primeira.group(1).lower()
        comeca_infinitivo = len(pal) > 4 and pal.endswith(("ar", "er", "ir"))
        if not comeca_infinitivo:
            continue
        # Tira trechos entre aspas: nomes de tela/campo viram falso positivo
        # (ex.: tela "consulta de estoque" — "consulta" ali é substantivo).
        limpo = re.sub(r"[\"“”'«»][^\"“”'«»]{0,60}[\"“”'«»]", " ", acao).lower()
        for m in re.finditer(r"\b(\w+)\b", limpo):
            palavra = m.group(1)
            if palavra not in VERBOS_3A_PESSOA:
                continue
            # "consulta de estoque": uso como substantivo, pelo que vem depois
            if re.match(r"\s+(de|do|da|dos|das)\b", limpo[m.end():]):
                continue
            # "agendamento de entrega", "local da Entrega": uso como substantivo,
            # pelo que vem antes. Preposição ou artigo na frente indica substantivo;
            # "e" fica de fora de propósito, porque "e realiza" é erro de verdade.
            antes = limpo[:m.start()].rstrip()
            if re.search(r"\b(de|do|da|dos|das|em|na|no|nas|nos|com|por|para|ao|aos|à|às|a|o)$",
                         antes):
                continue
            achados.append(
                "TEXTO  Passo \"{}\": formas verbais misturadas — começa no infinitivo "
                "(\"{}\") e usa \"{}\" (3ª pessoa)".format(p["titulo"], pal, palavra))
            break


def conf_voz_passiva(dados, achados):
    for p in extrair_passos(dados):
        # Cobre a passiva simples ("é entregue") e a perifrástica com auxiliar
        # ("deverá ser cadastrado", "deve ser validado") — esta última passava
        # batido até 2026-08-26 e é a forma mais comum nestes documentos.
        PART = (r"(?:\w+(?:ado|ada|ados|adas|ido|ida|idos|idas)"
                r"|entregues?|feitas?|feitos?|feito|dita|dito|ditas|ditos"
                r"|vista|visto|vistas|vistos|posta|posto|postas|postos"
                r"|aberta|aberto|abertas|abertos|escrita|escrito|paga|pago)")
        m = (re.search(r"\b(é|são|foi|foram|será|serão)\s+" + PART + r"\b", p["acao"], re.I)
             or re.search(r"\b(deve|devem|deverá|deverão|pode|podem|poderá|poderão)"
                          r"\s+ser\s+" + PART + r"\b", p["acao"], re.I))
        if m:
            achados.append("TEXTO  Passo \"{}\": voz passiva (\"{}\") — os demais passos usam infinitivo".format(
                p["titulo"], m.group(0)))


def conf_parenteses(dados, achados):
    for kind, item, _estilo in dados["corpo"]:
        if kind == "p" and item.count("(") != item.count(")"):
            achados.append("TEXTO  Parêntese aberto e não fechado: ...{}...".format(item[:90]))
        elif kind == "tbl":
            for linha in item:
                for cel in linha:
                    if cel.count("(") != cel.count(")"):
                        achados.append("TEXTO  Parêntese aberto e não fechado (tabela): ...{}...".format(cel[:90]))


def conf_espacos(dados, achados):
    for kind, item, _estilo in dados["corpo"]:
        if kind != "p":
            continue
        if "  " in item:
            achados.append("TEXTO  Espaço duplo: ...{}...".format(item[:90]))
        if re.search(r"\s+[,;.]", item):
            achados.append("TEXTO  Espaço antes de pontuação: ...{}...".format(item[:90]))


def conf_sobras_modelo(dados, achados):
    def varre(texto, onde):
        for sobra in SOBRAS_MODELO:
            if sobra.lower() in texto.lower():
                achados.append("MODELO  Sobra do modelo em {}: \"{}\"".format(onde, sobra))
    for nome, sec in dados["secoes"].items():
        for p in sec["paragrafos"]:
            varre(p, nome)
        for tab in sec["tabelas"]:
            for linha in tab:
                for cel in linha:
                    varre(cel, nome + " (tabela)")


# Nomes próprios que podem aparecer com maiúscula no meio da frase sem ser erro.
# Os nomes de papel NÃO ficam aqui: são colhidos do próprio documento, porque
# variam de POP para POP.
PROPRIOS = {
    "mega", "erp", "sharepoint", "bizagi", "word", "excel", "outlook", "teams",
    "gadens", "make", "it", "grupo", "triunfo", "ultj", "incorporadora",
    "ar", "ncm", "cnpj", "cnae", "nf", "pbqp", "abnt", "iso", "cno", "cib",
    "art", "rrt", "sgq", "pop", "obs", "curva",
    "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
    "agosto", "setembro", "outubro", "novembro", "dezembro",
}


def conf_capitalizacao(dados, achados):
    """Substantivo comum com maiúscula no meio da frase ("devolvida com Avaria",
    "Integridade da Embalagem"). Os nomes de papel do próprio documento e a lista
    de nomes próprios acima ficam de fora, senão vira ruído.

    Entrou em 2026-08-26: eu tinha decidido não fazer esta checagem por medo de
    falso positivo, e uma revisão paralela achou o defeito em 4 dos 9 documentos."""
    def raiz(p):
        p = normaliza(p)
        return p[:-1] if p.endswith("s") and len(p) > 4 else p

    permitidos = set(raiz(x) for x in PROPRIOS)

    # Papéis do próprio documento
    for reg in coletar_papeis(dados).values():
        for g in reg["grafias"]:
            permitidos.update(raiz(w) for w in normaliza(g).split())

    # Nomes de documento e sistema declarados pelo próprio POP: os termos da
    # tabela de Definições e os itens de Recursos Necessários. É onde "Ficha de
    # Retirada de Ferramentas", "Nota Fiscal" e "ERP Mega" são apresentados.
    declarados = []
    for tab in dados["secoes"].get("DEFINIÇÕES", {}).get("tabelas", []):
        declarados += [lin[0] for lin in tab[1:] if lin]
    declarados += dados["secoes"].get("RECURSOS NECESSÁRIOS", {}).get("paragrafos", [])
    for d in declarados:
        permitidos.update(raiz(w) for w in normaliza(d).split())

    # Varre os passos E as tabelas de Responsabilidades e Desvios — a versão
    # anterior só olhava os passos, e por isso não via "devolvida com Avaria".
    trechos = [(p["acao"], f"passo \"{p['titulo']}\"") for p in extrair_passos(dados)]
    for nome_sec, rotulo in (("PAPÉIS, RESPONSABILIDADES E AUTONOMIA", "Tabela de Responsabilidades"),
                             ("DESVIOS / AÇÕES NECESSÁRIAS", "Tabela de Desvios")):
        for tab in dados["secoes"].get(nome_sec, {}).get("tabelas", []):
            for lin in tab[1:]:
                for cel in lin:
                    if cel.strip():
                        trechos.append((cel, rotulo))

    achou = {}
    for texto, onde in trechos:
        for frase in re.split(r"(?<=[.;:])\s+|\n", texto):
            palavras = re.findall(r"\b[\wÀ-ÿ]+\b", frase)
            for i, pal in enumerate(palavras):
                if i == 0 or not pal[:1].isupper() or pal.isupper() or len(pal) < 4:
                    continue
                if raiz(pal) in permitidos:
                    continue
                achou.setdefault(pal, onde)
    for pal, onde in sorted(achou.items()):
        achados.append(
            "TEXTO  Maiúscula no meio da frase: \"{}\" ({}) — se não for nome próprio, "
            "nome de documento nem papel, deve ficar em minúscula".format(pal, onde))


def conf_executor_duplo(dados, achados):
    """Passo atribuído a dois papéis de uma vez, com as ações misturadas na mesma
    frase. Não dá para saber quem faz o quê."""
    for p in extrair_passos(dados):
        if re.search(r"\s[-/]\s|\se\s", p["executor"]):
            achados.append(
                "PASSOS  Passo \"{}\" está atribuído a mais de um papel ao mesmo tempo "
                "(\"{}\") e as ações vêm juntas na mesma frase — separar quem faz o quê".format(
                    p["titulo"], p["executor"]))


def conf_recurso_nao_usado(dados, achados):
    """Sistema listado em Recursos Necessários e que não aparece em nenhum passo.
    O checklist já cobria o contrário (sistema citado no corpo e ausente de
    Recursos); faltava esta direção."""
    sec = dados["secoes"].get("RECURSOS NECESSÁRIOS", {})
    sistemas, coletando = [], False
    for p in sec.get("paragrafos", []):
        alvo = normaliza(p)
        if alvo.startswith("sistemas"):
            coletando = True
            continue
        if alvo.startswith(("documentos", "papeis")):
            coletando = False
            continue
        if coletando:
            nome = p.strip(" .;:")
            if 2 < len(nome) < 50 and "nao especificado" not in normaliza(nome):
                sistemas.append(nome)

    corpo_passos = " ".join(p["texto"] for p in extrair_passos(dados))
    if not corpo_passos:
        return
    for s in sistemas:
        # compara pelo nome mais distintivo ("ERP Mega" -> "mega")
        chave = [w for w in normaliza(s).split() if w not in ("erp", "sistema", "de", "do", "da")]
        if not chave:
            continue
        if not any(w in normaliza(corpo_passos) for w in chave):
            achados.append(
                "RECURSOS  \"{}\" está listado em Recursos Necessários (5.1) mas não é usado "
                "em nenhum passo do processo".format(s))


def conf_registro_nao_produzido(dados, achados):
    """Entregável na tabela de Registro que nenhum passo produz. É a direção que
    faltava da checagem de Registro x saídas dos passos."""
    tabs = dados["secoes"].get("REGISTRO DO PROCESSO", {}).get("tabelas", [])
    corpo = normaliza(" ".join(p["texto"] for p in extrair_passos(dados)))
    if not corpo:
        return
    for tab in tabs:
        for linha in tab[1:]:
            if not linha:
                continue
            item = linha[0].strip(" .;:")
            if len(item) < 5:
                continue
            palavras = [w for w in normaliza(item).split()
                        if len(w) > 3 and w not in ("registro", "registros", "processo")]
            if palavras and not any(w in corpo for w in palavras):
                achados.append(
                    "REGISTRO  \"{}\" está na tabela de Registro do Processo, mas nenhum passo "
                    "descreve a produção desse entregável".format(item))


def conf_estilo_lista(dados, achados):
    """Seções que são listas (Referências, Pontos Críticos, Recursos) devem usar
    o mesmo estilo de parágrafo. Quando uma delas vira parágrafo comum, o item
    perde o recuo e fica diferente do resto do documento."""
    secoes_lista = ("REFERÊNCIAS", "PONTOS CRÍTICOS DO PROCESSO", "RECURSOS NECESSÁRIOS",
                    "INDICADORES", "ÁREAS ENVOLVIDAS")
    contagem = {}
    for nome in secoes_lista:
        for e in dados["secoes"].get(nome, {}).get("estilos", []):
            contagem[e] = contagem.get(e, 0) + 1
    if not contagem:
        return
    dominante = max(contagem, key=contagem.get)
    if contagem[dominante] < 3:
        return
    for nome in secoes_lista:
        estilos = dados["secoes"].get(nome, {}).get("estilos", [])
        fora = {e for e in estilos if e != dominante}
        if estilos and fora and all(e != dominante for e in estilos):
            achados.append(
                "FORMATO  Seção {}: os itens usam o estilo \"{}\", enquanto as demais "
                "seções de lista do documento usam \"{}\" — o item fica sem o mesmo "
                "recuo/marcador do resto".format(nome, ", ".join(sorted(fora)), dominante))


def trecho(texto, termo):
    i = texto.lower().find(termo.lower())
    return texto[max(0, i - 15):i + len(termo) + 25]


# --------------------------------------------------------------------------
# Conferências de estrutura
# --------------------------------------------------------------------------

def conf_capa_cabecalho_rodape(dados, achados):
    capa, cab, rod = dados["capa"], dados["cabecalho"], dados["rodape"]

    tipo_capa = capa["tipo"]
    m = re.search(r"Tipo de documento\s*:?\s*(.+?)\s*(?:\||Revisão|$)", rod)
    tipo_rod = m.group(1).strip() if m else ""
    if tipo_capa and tipo_rod and normaliza(tipo_capa) != normaliza(tipo_rod):
        achados.append("CAPA  \"Tipo de documento\" diverge: capa diz \"{}\", rodapé diz \"{}\"".format(
            tipo_capa, tipo_rod))

    cod = capa["codigo"]
    modelos = {"PO.GG.QLD.001", "IT.GG.PRO.001", "RE.GG.PRO.001"}
    nome_arq = os.path.basename(dados["caminho"])
    if cod in modelos and not nome_arq.startswith(cod):
        achados.append(
            "CAPA  O código da capa é \"{}\", que é o código do MODELO em branco — "
            "ficou sem preencher com o código real deste documento".format(cod))
    elif cod and cod not in re.sub(r"\s+", "", cab):
        achados.append("CAPA  Código da capa (\"{}\") não confere com o cabeçalho".format(cod))

    if re.search(r"X{3,}|\bxxx\b", nome_arq, re.I):
        achados.append(
            "CAPA  O nome do arquivo ainda tem \"XXX.xxx\" no lugar do setor e do número: \"{}\"".format(
                nome_arq))

    rev = re.sub(r"\D", "", capa["revisao"] or "")
    rev_rod = re.search(r"Revisão\s*:?\s*(\d+)", rod)
    if rev and rev_rod and rev.lstrip("0") != rev_rod.group(1).lstrip("0"):
        achados.append("CAPA  Revisão diverge: capa \"{}\", rodapé \"{}\"".format(rev, rev_rod.group(1)))

    if capa["status"] and normaliza(capa["status"]) == normaliza("Aprovado"):
        emissao = dados["secoes"].get("CONTROLE DE EMISSÃO", {}).get("tabelas", [])
        tem_data = any(re.search(r"\d{2}/\d{2}/\d{4}", c)
                       for tab in emissao for lin in tab for c in lin)
        if not tem_data:
            achados.append("CAPA  Status \"Aprovado\" sem data de aprovação no Controle de Emissão")


def coletar_papeis(dados):
    """Onde cada papel aparece. Chave = nome normalizado."""
    achados = {}

    # Nomes que são documento, não papel — apareciam na matriz por engano.
    NAO_E_PAPEL = ("solicitacao", "registro", "ficha", "aviso", "formulario",
                   "nota fiscal", "pedido", "requisicao", "relatorio", "termo")

    def add(nome, onde):
        nome = re.sub(r"\s*\(.*?\)\s*", " ", nome)
        nome = nome.split(":")[0]          # "Almoxarife: responsável pelo estoque"
        nome = nome.strip(" .;:")
        if any(normaliza(nome).startswith(x) for x in NAO_E_PAPEL):
            return
        if not nome or len(nome) < 4 or len(nome) > 55:
            return
        if re.search(r"\d", nome):
            return
        chave = normaliza(nome)
        reg = achados.setdefault(chave, {"grafias": set(), "locais": set()})
        reg["grafias"].add(nome)
        reg["locais"].add(onde)

    # A tabela de Definições NÃO entra como origem de papel: ela é de termos e
    # siglas, não de cargos (regra 1 de nao-apontar.md). Antes, "Base Consolidada"
    # e "Compatibilização" viravam papéis fantasmas na matriz.
    termos_definidos = set()
    for tab in dados["secoes"].get("DEFINIÇÕES", {}).get("tabelas", []):
        for linha in tab[1:]:
            if linha:
                termos_definidos.add(normaliza(re.sub(r"\s*\(.*?\)\s*", " ", linha[0])))

    sec_rec = dados["secoes"].get("RECURSOS NECESSÁRIOS", {})
    coletando = False
    for p in sec_rec.get("paragrafos", []):
        if normaliza(p).startswith("papeis"):
            coletando = True
            continue
        if coletando:
            if normaliza(p).startswith(("sistemas", "documentos")):
                coletando = False
                continue
            add(p, "Papéis-chave")

    for nome_sec in ("PAPÉIS, RESPONSABILIDADES E AUTONOMIA", "PAPÉIS E RESPONSABILIDADES"):
        for tab in dados["secoes"].get(nome_sec, {}).get("tabelas", []):
            for linha in tab[1:]:
                add(linha[0].replace("\n", " "), "Tabela de Responsabilidades")

    for tab in dados["secoes"].get("DESVIOS / AÇÕES NECESSÁRIAS", {}).get("tabelas", []):
        for linha in tab[1:]:
            if len(linha) >= 3:
                add(linha[-1], "Tabela de Desvios")

    for p in extrair_passos(dados):
        for parte in re.split(r"[-/]", p["executor"]):
            add(parte, "Passos do processo")

    # Papel citado DENTRO do texto da ação também participa do passo, mesmo sem
    # estar entre parênteses como executor. Ex.: SUP.012, passo 5 — "informar o
    # comprador responsável ... após o comprador autorizar". Sem isto, o Comprador
    # aparecia como "não executa nenhum passo", o que é falso.
    acoes = " ".join(p["acao"] for p in extrair_passos(dados))
    acoes_norm = normaliza(acoes)
    for chave, reg in achados.items():
        if "Passos do processo" in reg["locais"]:
            continue
        if chave and chave in acoes_norm:
            reg["locais"].add("Passos do processo")

    return achados


def agrupar_papeis(papeis):
    """Junta grafias do mesmo papel num grupo só, para não repetir o mesmo papel
    três vezes só porque está escrito de três jeitos."""
    chaves = sorted(papeis)
    grupos = []
    for chave in chaves:
        for g in grupos:
            if any(difflib.SequenceMatcher(None, chave, k).ratio() >= 0.78 for k in g):
                g.append(chave)
                break
        else:
            grupos.append([chave])

    saida = []
    for g in grupos:
        grafias, locais = set(), set()
        for k in g:
            grafias |= papeis[k]["grafias"]
            locais |= papeis[k]["locais"]
        saida.append({"grafias": grafias, "locais": locais})
    return saida


def conf_matriz_papeis(dados, achados):
    # IT não tem tabela de Papéis/Responsabilidades — é a estrutura correta do
    # tipo, e a tabela de Definições dela guarda siglas, não papéis. Cobrar
    # matriz de papéis numa IT gera só ruído.
    if dados["tipo"] == "IT":
        return
    papeis = coletar_papeis(dados)
    if not papeis:
        return

    for grupo in agrupar_papeis(papeis):
        nome = sorted(grupo["grafias"], key=len)[-1]
        locais = grupo["locais"]

        faltas = []
        if "Tabela de Responsabilidades" not in locais:
            faltas.append("não tem linha na Tabela de Responsabilidades")
        if "Passos do processo" not in locais:
            faltas.append("não executa nenhum passo")
        # "não está nas Definições" NÃO entra: a Tabela 1 é de termos e siglas,
        # e ausência de cargo ali não é erro (regra 1 de nao-apontar.md).
        if faltas:
            achados.append("PAPÉIS  \"{}\" aparece em [{}] — {}".format(
                nome, ", ".join(sorted(locais)), "; ".join(faltas)))

        # Só reporta grafia divergente se a diferença for real, e não apenas
        # espaço ou barra a mais (ex.: "Obra / Engenheiro" x "Obra/Engenheiro").
        reais = {re.sub(r"[\s/\-]+", "", g).lower() for g in grupo["grafias"]}
        if len(reais) > 1:
            achados.append("PAPÉIS  Grafias diferentes do mesmo papel: {}".format(
                " / ".join("\"{}\"".format(g) for g in sorted(grupo["grafias"]))))


def conf_desvio_circular(dados, achados):
    for tab in dados["secoes"].get("DESVIOS / AÇÕES NECESSÁRIAS", {}).get("tabelas", []):
        for n, linha in enumerate(tab[1:], 2):
            if len(linha) < 3:
                continue
            acao, responsavel = linha[1], linha[2].strip(" .")
            if responsavel and len(responsavel) > 4 and normaliza(responsavel) in normaliza(acao):
                achados.append(
                    "DESVIOS  Linha {}: ação circular — o responsável é \"{}\" e a ação manda "
                    "tratar com \"{}\"".format(n, responsavel, responsavel))


def conf_coluna_sem_variacao(dados, achados):
    for n_tab, tabela in enumerate(dados["tabelas"], 1):
        if len(tabela) < 3:
            continue
        n_col = min(len(l) for l in tabela)
        for c in range(1, n_col):
            valores = [l[c].strip() for l in tabela[1:]]
            if len(set(valores)) == 1 and valores[0] and len(valores[0]) < 60:
                achados.append(
                    "TABELAS  Tabela {}, coluna \"{}\": todas as {} linhas têm o mesmo valor "
                    "(\"{}\") — a coluna não diferencia nada".format(
                        n_tab, tabela[0][c] if c < len(tabela[0]) else c, len(valores), valores[0]))


def conf_indicadores(dados, achados):
    sec = dados["secoes"].get("INDICADORES")
    if not sec:
        return
    texto = " ".join(sec["paragrafos"]).lower()
    tem_abertura = "seguintes indicadores" in texto
    tem_fechamento = "acompanhados mensalmente" in texto
    diz_que_nao_tem = "não possui indicadores" in texto
    if diz_que_nao_tem and (tem_abertura or tem_fechamento):
        achados.append(
            "INDICADORES  Contradição: a seção diz \"não possui indicadores próprios\", "
            "mas mantém a frase de abertura e/ou de fechamento que pressupõe que existem "
            "indicadores monitorados")


def conf_definicoes_parecidas(dados, achados):
    tabs = dados["secoes"].get("DEFINIÇÕES", {}).get("tabelas", [])
    itens = [(l[0], l[1]) for tab in tabs for l in tab[1:] if len(l) >= 2]
    # Quase toda definição começa igual ("Colaborador responsável pela..."), o que
    # infla a semelhança. Tira esse começo antes de comparar, senão o programa
    # aponta pares que só compartilham a fórmula de abertura.
    def miolo(s):
        s = normaliza(s)
        for prefixo in ("colaborador devidamente autorizado por sua gerencia para",
                        "colaborador devidamente autorizado por sua gerencia",
                        "colaborador responsavel pela", "colaborador responsavel pelo",
                        "colaborador responsavel por", "colaborador responsavel",
                        "colaborador que", "colaborador"):
            if s.startswith(prefixo):
                return s[len(prefixo):].strip()
        return s

    for i, (t1, d1) in enumerate(itens):
        for t2, d2 in itens[i + 1:]:
            m1, m2 = miolo(d1), miolo(d2)
            if len(m1) < 15 or len(m2) < 15:
                continue
            r = difflib.SequenceMatcher(None, m1, m2).ratio()
            if r >= 0.68:
                achados.append(
                    "DEFINIÇÕES  \"{}\" e \"{}\" descrevem quase a mesma coisa ({:.0f}% igual, "
                    "descontada a fórmula de abertura) — conferir se não são o mesmo termo "
                    "definido duas vezes".format(t1, t2, r * 100))


# --------------------------------------------------------------------------
# Execução
# --------------------------------------------------------------------------

CHECAGENS = [
    conf_capa_cabecalho_rodape,
    conf_sobras_modelo,
    conf_matriz_papeis,
    conf_definicoes_parecidas,
    conf_desvio_circular,
    conf_coluna_sem_variacao,
    conf_indicadores,
    conf_passos_sem_executor,
    conf_pontuacao_passos,
    conf_verbo_misturado,
    conf_voz_passiva,
    conf_virgula_conector,
    conf_parenteses,
# DESATIVADO em 2026-09-02. O Bruno retirou os pontos finais que eu tinha
# acrescentado e escreveu no checklist: "Ponto final retirado, Claude não se
# atentou ao template". Conferi: o QLD.002 não diz nada sobre pontuação em
# célula, e a Tabela 1 do modelo vem com as células vazias — não existe a
# regra que eu estava aplicando. Era invenção minha, automatizada.
    # conf_celulas_sem_ponto,
    conf_capitalizacao,
    conf_executor_duplo,
    conf_recurso_nao_usado,
    conf_registro_nao_produzido,
    conf_estilo_lista,
    conf_espacos,
]


def revisar(caminho):
    dados = ler_documento(caminho)
    achados = []
    for chk in CHECAGENS:
        try:
            chk(dados, achados)
        except Exception as e:
            achados.append("(erro interno na checagem {}: {})".format(chk.__name__, e))
    vistos, unicos = set(), []
    for a in achados:
        if a not in vistos:
            vistos.add(a)
            unicos.append(a)
    return dados, unicos


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ap = argparse.ArgumentParser(description="Checagem mecânica de POP / IT / Regimento.")
    ap.add_argument("arquivos", nargs="*", help="arquivos .docx")
    ap.add_argument("--pasta", help="revisa todos os .docx da pasta")
    args = ap.parse_args()

    caminhos = list(args.arquivos)
    if args.pasta:
        caminhos += sorted(glob.glob(os.path.join(args.pasta, "*.docx")))
    caminhos = [c for c in caminhos if not os.path.basename(c).startswith("~$")]
    if not caminhos:
        ap.error("informe ao menos um arquivo .docx ou use --pasta")

    total = 0
    for caminho in caminhos:
        print("=" * 78)
        print(os.path.basename(caminho))
        print("=" * 78)
        try:
            dados, achados = revisar(caminho)
        except Exception as e:
            print("  NÃO FOI POSSÍVEL LER: {}".format(e))
            continue
        if dados["tipo"] not in ("PO", "IT", "RE"):
            print("  (fora do padrão POP/IT/Regimento — só as checagens de texto valem)")
        if not achados:
            print("  Nada encontrado pelas checagens mecânicas.")
        for a in achados:
            print("  - " + a)
        total += len(achados)
        print()

    print("=" * 78)
    print("TOTAL: {} apontamento(s) mecânico(s) em {} documento(s).".format(total, len(caminhos)))
    print("Lembrete: isto NÃO substitui a revisão. Ordem dos passos, desvios que faltam,")
    print("definição que não combina com o termo — nada disso é conferido aqui.")


if __name__ == "__main__":
    main()
