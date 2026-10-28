# -*- coding: utf-8 -*-
"""
Aplica correções mecânicas em POPs / ITs / Regimentos do Grupo Gadens.

Só faz o que NÃO depende de resposta de ninguém: erro de digitação, vírgula,
concordância, voz passiva, grafia de papel, sobra de texto do modelo, campo da
capa. Nunca inventa conteúdo, nunca preenche seção vazia, nunca mexe em
"Não especificado no texto de origem" (o texto que entra ali depende da área).

Segurança:
  - trabalha numa cópia em pasta temporária, nunca no original;
  - valida o XML antes de substituir;
  - se qualquer coisa falhar, o original fica intacto;
  - `--simular` mostra o que faria sem gravar nada.

Uso:
    python3 aplicar_correcoes.py --simular
    python3 aplicar_correcoes.py --aplicar
    python3 aplicar_correcoes.py --aplicar --so "SUP.009"
"""

import argparse
import copy
import io
import os
import re
import shutil
import sys
import tempfile
import zipfile

PASTA = r"C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki\Aprovação"
MODELO_POP = (r"C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki"
              r"\1. Padrões\1. Padrões\PO.GG.QLD.001 - MODELO PADRÃO DE POP -  Grupo Gadens.docx")

# --------------------------------------------------------------------------
# Tabela de correções, por documento.
#   trocas   : (texto_velho, texto_novo) — aplicado no corpo e nas tabelas
#   apagar   : parágrafos a remover por inteiro (sobra de texto do modelo)
# --------------------------------------------------------------------------

INSTRUCAO_DEFINICOES = ("Identificar e descrever os termos técnicos, siglas, abreviaturas e "
                        "acrônimos utilizados neste documento, assegurando a padronização da "
                        "linguagem e a correta compreensão dos requisitos estabelecidos.")
INSTRUCAO_REGISTRO = "Identificar os entregáveis do processo, ou seja, o produto do processo."
INSTRUCAO_REGISTRO_2 = "Entregáveis do processo, ou seja, o produto do processo."
IND_ABRE = ("Os seguintes indicadores são utilizados para monitorar a efetividade das "
            "diretrizes deste POP:")
IND_FECHA = "Os indicadores devem ser acompanhados mensalmente nos fóruns de governança."

CORRECOES = {
    "PO.GG.QLD.004": {
        # mesma contradição do CM.QLD.001: as duas frases de fábrica pressupõem
        # indicadores, e o conteúdo diz que não existem
        "apagar": [IND_ABRE, IND_FECHA],
        "trocas": [
            # título da capa estava sem o "TA"
            ("TRATIVA COM BASE EM AVALIAÇÃO", "TRATATIVA COM BASE EM AVALIAÇÃO"),
            # cabeçalho e rodapé traziam 26/08; capa e Controle de Emissão dizem 29/09
            ("00 (26/08/2026)", "00 (29/09/2026)"),
            ("Data: 26/08/2026", "Data: 29/09/2026"),
        ],
    },
    "PO.CM.QLD.001": {
        # A seção INDICADORES dizia "Este POP não possui indicadores próprios" entre as
        # duas frases de fábrica, que pressupõem que existem indicadores monitorados.
        # Mesma correção já feita no SUP.006 e no SUP.008.
        "apagar": [IND_ABRE, IND_FECHA],
        "trocas": [
            # cabeçalho e rodapé traziam 26/08; a capa e o Controle de Emissão dizem 29/09
            # "Rev." e a data ficam em CÉLULAS diferentes do cabeçalho, então o
            # padrão tem que caber dentro de um parágrafo só
            ("00 (26/08/2026)", "00 (29/09/2026)"),
            ("Data: 26/08/2026", "Data: 29/09/2026"),
            # nome da empresa na ordem usada nos demais documentos da Make It
            ("Make It Construtora", "Construtora Make It"),
            # substantivo comum com maiúscula
            ("Todo Indicador no Setor", "Todo indicador no Setor"),
            # regência: as outras duas ocorrências no mesmo passo já usam "chegar a/à"
            ("chegar na causa raiz", "chegar à causa raiz"),
        ],
    },
    "PO.GG.CIM.001": {
        "apagar": [INSTRUCAO_REGISTRO],
        "trocas": [
            # cabeçalho e rodapé traziam o código e a revisão do MODELO, não deste
            # documento. A capa é a fonte correta: PO.GG.CIM.001, Rev. 00, 27/08/2026.
            ("PO.GG.QLD.001", "PO.GG.CIM.001"),
            ("01 (30/06/2026)", "00 (27/08/2026)"),
            ("Revisão:02", "Revisão:00"),
            ("Data: 30/06/2026", "Data: 27/08/2026"),
            # escrita
            ("Sitema da CEF", "Sistema da CEF"),
            ("Share Point", "SharePoint"),
            ("Click Up", "ClickUp"),
            ("Infra estrutura", "Infraestrutura"),
            ("Coordenador de suprimentos", "Coordenador de Suprimentos"),
            ("Coordenador de Assistência técnica", "Coordenador de Assistência Técnica"),
            ("com isso ao podem surgir", "com isso podem surgir"),
        ],
    },
    "PO.GG.SUP.006": {
        "apagar": [INSTRUCAO_DEFINICOES, INSTRUCAO_REGISTRO, IND_ABRE, IND_FECHA],
        "trocas": [
            ('Validar com o solicitante e caso necessário, escalonar',
             'Validar com o solicitante e, caso necessário, escalonar'),
            ("e avalia impacto na obra", "e avaliar impacto na obra"),
            ("bem como, separar a quantidade", "bem como separar a quantidade"),
            ("Conferir documento de transferência: (código do material, descrição, quantidade, "
             "condição física do material e registrar divergências se houver;",
             "Conferir o documento de transferência (código do material, descrição, quantidade "
             "e condição física do material) e registrar divergências, se houver;"),
            ("Engenheiro de Obra", "Engenheiro da Obra"),
        ],
    },
    "PO.GG.SUP.007": {
        "apagar": [],
        "trocas": [
            ('verificar Integridade do material',
             'verificar a integridade do material'),
            ("materiais da curva A., realizar", "materiais da curva A, realizar"),
            ("Inventario de Estoque", "Inventário de Estoque"),
            ("realizar inventarios", "realizar inventários"),
            ("fazer o inventario", "fazer o inventário"),
        ],
    },
    "PO.GG.SUP.008": {
        "apagar": [INSTRUCAO_REGISTRO_2, IND_ABRE, IND_FECHA],
        "trocas": [
            ('Verifica Necessidade da Obra',
             'Verifica a necessidade da obra'),
            ('Analisa os pedidos Aprovados',
             'Analisa os pedidos aprovados'),
            ('Faz Agendamento de Entrega de Material',
             'Faz o agendamento de entrega de material'),
            ('Analisa Espaço Físico Disponível',
             'Analisa o espaço físico disponível'),
            ('atendam a necessidade da Obra',
             'atendam a necessidade da obra'),
            ('para atender a demanda da Obra',
             'para atender a demanda da obra'),
            ("supervisor de Almoxarifado", "Supervisor de Almoxarifado"),
            ("Supervisor de Almoxarife", "Supervisor de Almoxarifado"),
        ],
    },
    "PO.GG.SUP.009": {
        "apagar": [INSTRUCAO_DEFINICOES, INSTRUCAO_REGISTRO],
        "trocas": [
            ('Registro da Movimentação errada',
             'Registro da movimentação errada'),
            ("Supervisor Almoxarifado", "Supervisor de Almoxarifado"),
            ("Supervisor de Almoxarife", "Supervisor de Almoxarifado"),
            ("Localizar o material no estoque e realiza a separação",
             "Localizar o material no estoque e realizar a separação"),
            ("preenchida da forma correta, contendo, data",
             "preenchida da forma correta, contendo data"),
            ("O material é entregue ao solicitante.",
             "Entregar o material ao solicitante."),
            ("no sistema, após, manter o arquivo", "no sistema e, em seguida, manter o arquivo"),
        ],
    },
    "PO.GG.SUP.010": {
        "apagar": [INSTRUCAO_REGISTRO],
        "trocas": [
            ('Validação dos Tributos e Impostos do Item',
             'Validação dos tributos e impostos do item'),
            ("Supervisor do Almoxarifado", "Supervisor de Almoxarifado"),
            ("autorizado por sua gerência solicitar", "autorizado por sua gerência para solicitar"),
            ("a fim de garantir, ausência de duplicidade",
             "a fim de garantir ausência de duplicidade"),
            ("deve-se parametrizar os impostos", "devem-se parametrizar os impostos"),
            ("evitar erros de Divergência que dificultam",
             "evitar divergências que dificultam"),
            # voz passiva -> infinitivo, para ficar igual aos demais passos
            ("Solicitação para cadastro de item, deve ser recebida apenas pelo e-mail",
             "Receber a solicitação de cadastro de item apenas pelo e-mail"),
            ("O item deverá ser cadastrado no sistema contendo: descrição padronizada, "
             "unidade de medida, observações técnicas",
             "Cadastrar o item no sistema com descrição padronizada, unidade de medida e "
             "observações técnicas"),
            ("Após o cadastro deverá ser realizada uma conferência, a fim de garantir "
             "ausência de duplicidade, descrição correta, unidade de medida adequada",
             "Após o cadastro, realizar uma conferência para garantir ausência de "
             "duplicidade, descrição correta e unidade de medida adequada"),
        ],
    },
    "PO.GG.SUP.011": {
        "apagar": [INSTRUCAO_DEFINICOES, INSTRUCAO_REGISTRO],
        "trocas": [
            ('vai até o Almoxarifado e informa',
             'vai até o almoxarifado e informa'),
            ('devolvida com Avaria',
             'devolvida com avaria'),
            ('Verificação da Disponibilidade da Ferramenta',
             'Verificação da disponibilidade da ferramenta'),
            ('registro de Saída e entrada da Ferramenta',
             'registro de saída e entrada da ferramenta'),
            ("o solicitante verifica a fermenta", "o solicitante verifica a ferramenta"),
            ("Supervisor do Almoxarifado", "Supervisor de Almoxarifado"),
            ("dados do requisitante quantidade do item",
             "dados do requisitante, quantidade do item"),
            # Bruno tirou a "política interna" dos outros 8 por não haver política
            # aprovada e divulgada; este ficou para trás.
            ("Arquivo-morto. Proteção: Acesso restrito. Retenção: Conforme política interna",
             "Arquivo-morto"),
        ],
    },
    "PO.GG.SUP.012": {
        "apagar": [],
        "trocas": [
            ('Armazena os materiais por categoria e preserva a integridade física',
             'Armazenar os materiais por categoria e preservar a integridade física'),
            ('Armazena as notas fiscais digitalizadas',
             'Armazenar as notas fiscais digitalizadas'),
            ('(Quantidade Recebida, Material, Integridade da Embalagem, Condições do Material)',
             '(quantidade recebida, material, integridade da embalagem e condições do material)'),
            ('encontradas na Conferência:',
             'encontradas na conferência:'),
            ('sendo que, caso haja divergência comunicar o supervisor',
             'sendo que, caso haja divergência, comunicar o supervisor'),
            ('Informar o comprador responsável, sobre a necessidade do material na obra e caso necessário, recusar',
             'Informar o comprador responsável sobre a necessidade do material na obra e, caso necessário, recusar'),
            ('no local da Entrega',
             'no local da entrega'),
            ('Conferência Documental',
             'Conferência documental'),
            ('Conferência Física',
             'Conferência física'),
            ('Registro de Divergência',
             'Registro de divergência'),
            ('Aceite do Material',
             'Aceite do material'),
            ("Supervisor de Almoxarife", "Supervisor de Almoxarifado"),
            ("Supervisor do Almoxarifado", "Supervisor de Almoxarifado"),
            ("unidade de medida.", "unidade de medida)."),
            ("destinada ao Almoxarifado Correto Receber o Fornecedor",
             "destinada ao almoxarifado correto. Receber o fornecedor"),
            ("Carimbar a assinar a nota fiscal", "Carimbar e assinar a nota fiscal"),
            ("Armazenagem do material (almoxarife)", "Armazenagem do Material (Almoxarife)"),
            ("Registro do Nota Fiscal", "Registro da Nota Fiscal"),
        ],
    },
    "PO.GG.SUP.013": {
        "apagar": [],
        "trocas": [
            ('Gerir do Almoxarifado',
             'Gerir o Almoxarifado'),
            ('erros Contábeis',
             'erros contábeis'),
            ('Mega e Sharepoint',
             'Mega e SharePoint'),
            ('Almoxarife (responsável pelo AR);',
             'Almoxarife (responsável pelo AR).'),
            ('rastreio do Usuário',
             'rastreio do usuário'),
            ('CNPJ do Fornecedor',
             'CNPJ do fornecedor'),
            ('itens disponíveis para Recebimento',
             'itens disponíveis para recebimento'),
            ('Registrar no Corpo da Nota Fiscal o Número da AR',
             'Registrar no corpo da Nota Fiscal o número da AR'),
            ('pasta do Sharepoint',
             'pasta do SharePoint'),
            ('(Salvamento de notas em geral)',
             '(salvamento de notas em geral)'),
            ('Limitada a gestão dos recebimentos AR',
             'Limitada à gestão dos recebimentos de AR'),
            ('Insere os Dados no Sistema',
             'Insere os dados no sistema'),
            ('Analisa os Dados Inseridos',
             'Analisa os dados inseridos'),
            ('Confirma os Dados',
             'Confirma os dados'),
            ('Registra o Lançamento',
             'Registra o lançamento'),
            ('Disponibiliza o Documento',
             'Disponibiliza o documento'),
            ("9001:20/15", "9001:2015"),
            ("Supervisor do Almoxarifado", "Supervisor de Almoxarifado"),
            ("Disponibilizar o documento (almoxarife)",
             "Disponibilizar o Documento (Almoxarife)"),
        ],
    },
    "PO.GG.SUP.014": {
        "apagar": [],
        "trocas": [
            ('Almoxarifiado',
             'Almoxarifado'),
            ('garantindo organização, controle, rastreabilidade evitando duplicidade',
             'garantindo organização, controle e rastreabilidade, evitando duplicidade'),
            ('procedimentos para Manutenção do cadastro',
             'procedimentos para manutenção do cadastro'),
            ("Supervisor de Almoxarife", "Supervisor de Almoxarifado"),
            ("cadastro.Materiais@grupogadens.com.br", "cadastro.materiais@grupogadens.com.br"),
        ],
    },
    "PO.IG.INC.001": {
        "apagar": [],
        "trocas": [
            ("Projetos Complementares Gadens", "Projetos Complementares"),
        ],
    },
    "PO.CM.PJC.001": {
        "apagar": [],
        "trocas": [
            ('Congelamento pós-fase de EP',
             'Congelamento pós-fase de PE'),
            (', acústica',
             ', Acústica'),
            ('Tempo entre 20 e 29',
             'tempo entre 20 e 29'),
            ('; Diagramas unifilares',
             '; diagramas unifilares'),
            ('Alvenaria estrutural',
             'Alvenaria Estrutural'),
            ('; Reemissão de PE',
             '; reemissão de PE'),
            ('Revisador', 'Revisor'),
            ('Comite Extraordinario de Revisao',
             'Comitê Extraordinário de Revisão'),
            ('no caso a alteração obter tempo entre 20 e 29',
             'caso a alteração obtenha tempo entre 20 e 29'),
            ('que fazer com que os projetos tenham',
             'que fazem com que os projetos tenham'),
            ('aditivos de obras referente a alterações',
             'aditivos de obras referentes a alterações'),
            ('pois trata-se de desvios',
             'pois se trata de desvios'),
            ('compatibilizadas; quantitativos final',
             'compatibilizadas; quantitativo final'),
            ('de rede de gás, Quantitativo final',
             'de rede de gás; quantitativo final'),
            ('como de Alto Impacto o processo',
             'como de Alto Impacto, o processo'),
            ('como Médio Impacto o processo',
             'como Médio Impacto, o processo'),
            ('como Baixo Impacto o processo',
             'como Baixo Impacto, o processo'),
            ('como Médio/Alto Impacto o processo',
             'como Médio/Alto Impacto, o processo'),
            ('como Médio/alto Impacto o processo',
             'como Médio/Alto Impacto, o processo'),
            ('alterações Médio/Alto Impacto',
             'Alterações de Médio/Alto Impacto'),
            ('alterações Médio Impacto',
             'Alterações de Médio Impacto'),
            ('alterações Baixo Impacto',
             'Alterações de Baixo Impacto'),
            ('Aplica-se a Construtora Make It',
             'Aplica-se à Construtora Make It'),
            ('com quantitativos finalizados para lançamento do empreendimento',
             'com quantitativos definitivos para lançamento do empreendimento.'),
            ("papéis, responsábilidades e autonomia", "papéis, responsabilidades e autonomia"),
        ],
    },
    "PO.IG.PJC.001": {
        "apagar": [],
        "trocas": [
            ('Congelamento pós-fase de EP',
             'Congelamento pós-fase de PE'),
            (', acústica',
             ', Acústica'),
            ('Tempo entre 20 e 29',
             'tempo entre 20 e 29'),
            ('; Diagramas unifilares',
             '; diagramas unifilares'),
            ('Revisador', 'Revisor'),
            ('Comite Extraordinario de Revisao',
             'Comitê Extraordinário de Revisão'),
            ('no caso a alteração obter tempo entre 20 e 29',
             'caso a alteração obtenha tempo entre 20 e 29'),
            ('que fazer com que os projetos tenham',
             'que fazem com que os projetos tenham'),
            ('aditivos de obras referente a alterações',
             'aditivos de obras referentes a alterações'),
            ('pois trata-se de desvios',
             'pois se trata de desvios'),
            ('compatibilizadas; quantitativos final',
             'compatibilizadas; quantitativo final'),
            ('de rede de gás, Quantitativo final',
             'de rede de gás; quantitativo final'),
            ('como de Alto Impacto o processo',
             'como de Alto Impacto, o processo'),
            ('como Médio Impacto o processo',
             'como Médio Impacto, o processo'),
            ('como Baixo Impacto o processo',
             'como Baixo Impacto, o processo'),
            ('como Médio/Alto Impacto o processo',
             'como Médio/Alto Impacto, o processo'),
            ('como Médio/alto Impacto o processo',
             'como Médio/Alto Impacto, o processo'),
            ('alterações Médio/Alto Impacto',
             'Alterações de Médio/Alto Impacto'),
            ('alterações Médio Impacto',
             'Alterações de Médio Impacto'),
            ('alterações Baixo Impacto',
             'Alterações de Baixo Impacto'),
            ('Aplica-se a Incorporadora Gadens',
             'Aplica-se à Incorporadora Gadens'),
            ('O objetivo é compatibilizar final entre disciplinas, absorção de interferências do AP, solicitações de furações, consolidação de IFCs e quantitativos.',
             'O objetivo é a compatibilização final entre disciplinas, a absorção de interferências do AP, as solicitações de furações e a consolidação de IFCs e quantitativos.'),
            ('O objetivo é detalhar completamente para a execução em obra.',
             'O objetivo é o detalhamento completo para execução em obra.'),
            ('é permitida somente correções',
             'é permitida — somente correções'),
            ('plantas finalizadas com quantitativos finalizados',
             'plantas finalizadas com quantitativos definitivos'),
            ('O resultado é plantas', 'O resultado são as plantas'),
            ('detalhado; Alto Impacto em prazo e custo',
             'detalhado; alto impacto em prazo e custo'),
            ('Revisador: Bruno Kawasaki Validador:',
             'Revisador: Bruno Kawasaki / Validador:'),
            ("papéis, responsábilidades e autonomia", "papéis, responsabilidades e autonomia"),
            ("Alterações De Alto Impacto", "Alterações de Alto Impacto"),
            ("alterações De Alto Impacto", "alterações de Alto Impacto"),
        ],
    },
}


# --------------------------------------------------------------------------

def lista_do_modelo(caminho_modelo):
    """Pega do modelo atual o bloco <w:dropDownList> do campo 'Tipo de documento'."""
    x = zipfile.ZipFile(caminho_modelo).read("word/document.xml").decode("utf-8")
    m = re.search(r'<w:alias w:val="Tipo de documento"/>.*?(<w:dropDownList>.*?</w:dropDownList>)',
                  x, re.S)
    if not m:
        raise RuntimeError("nao achei a lista suspensa no modelo")
    return m.group(1)


def corrige_capa(xml, lista_nova, log):
    """A capa dos documentos antigos traz uma lista suspensa desatualizada, sem a
    opção 'Procedimento Operacional Padrão'. Troca a lista e o valor escolhido."""
    antes = xml
    # 1. troca as opções da lista suspensa
    def troca_lista(m):
        return m.group(0).replace(m.group(1), lista_nova)
    xml = re.sub(r'(?s)(?<=<w:alias w:val="Tipo de documento"/>)(.*?)(<w:dropDownList>.*?</w:dropDownList>)',
                 lambda m: m.group(1) + lista_nova, xml)
    if xml != antes:
        log.append('capa: lista suspensa "Tipo de documento" atualizada para a do modelo atual')

    # 2. troca o valor selecionado
    antes2 = xml
    xml = re.sub(r'(<w:alias w:val="Tipo de documento"/>.*?<w:sdtContent>.*?<w:t[^>]*>)'
                 r'Procedimento Operacional\s*(</w:t>)',
                 r'\1Procedimento Operacional Padrão\2', xml, flags=re.S)
    if xml != antes2:
        log.append('capa: "Procedimento Operacional" -> "Procedimento Operacional Padrão"')
    return xml


def troca_no_xml(xml, velho, novo):
    """Troca texto em cabeçalho/rodapé mesmo quando o Word quebrou a frase em
    vários pedaços. Sem isso, "9001:20/15" (que no XML está como "9001:20" + "/"
    + "15") passava batido — foi o que aconteceu na primeira rodada."""
    saida, pos = [], 0
    for bloco in re.finditer(r"<w:p[ >].*?</w:p>", xml, re.S):
        trecho_p = bloco.group(0)
        pedacos = list(re.finditer(r"(<w:t[^>]*>)([^<]*)(</w:t>)", trecho_p))
        junto = "".join(m.group(2) for m in pedacos)
        if velho not in junto:
            continue
        novo_junto = junto.replace(velho, novo)
        # devolve tudo no primeiro pedaço e esvazia os demais
        partes, ja = [], 0
        for i, m in enumerate(pedacos):
            partes.append(trecho_p[ja:m.start()])
            abre = m.group(1)
            if 'xml:space' not in abre:
                abre = abre[:-1] + ' xml:space="preserve">'
            partes.append(abre + (novo_junto if i == 0 else "") + m.group(3))
            ja = m.end()
        partes.append(trecho_p[ja:])
        novo_p = "".join(partes)
        saida.append(xml[pos:bloco.start()] + novo_p)
        pos = bloco.end()
    return "".join(saida) + xml[pos:] if saida else xml


def troca_no_paragrafo(par, velho, novo):
    """Substitui texto que pode estar quebrado em vários pedaços (runs), mantendo
    a formatação do primeiro pedaço."""
    runs = par.runs
    inteiro = "".join(r.text for r in runs)
    if velho not in inteiro:
        return 0
    n = 0
    while velho in inteiro:
        ini = inteiro.index(velho)
        fim = ini + len(velho)
        pos, primeiro = 0, None
        for r in runs:
            ini_r, fim_r = pos, pos + len(r.text)
            if fim_r > ini and ini_r < fim:          # run tocado pela substituição
                corte_i = max(ini, ini_r) - ini_r
                corte_f = min(fim, fim_r) - ini_r
                if primeiro is None:
                    primeiro = r
                    r.text = r.text[:corte_i] + novo + r.text[corte_f:]
                else:
                    r.text = r.text[:corte_i] + r.text[corte_f:]
            pos = fim_r
        n += 1
        inteiro = "".join(r.text for r in runs)
    return n


SECOES_LISTA = ("REFERÊNCIAS", "PONTOS CRÍTICOS DO PROCESSO", "RECURSOS NECESSÁRIOS",
                "INDICADORES", "ÁREAS ENVOLVIDAS")


def _secoes(d):
    """Mapa seção -> lista de parágrafos, para as correções que dependem de onde
    o parágrafo está (pontuação de passo, estilo de lista)."""
    import re as _re
    titulos = ["OBJETIVO", "APLICAÇÃO", "REFERÊNCIAS", "DEFINIÇÕES", "RECURSOS NECESSÁRIOS",
               "PRINCIPAIS PASSOS DO PROCESSO", "PAPÉIS, RESPONSABILIDADES E AUTONOMIA",
               "INDICADORES", "PONTOS CRÍTICOS DO PROCESSO", "DESVIOS / AÇÕES NECESSÁRIAS",
               "REGISTRO DO PROCESSO", "CONTROLE DE EMISSÃO"]
    mapa, atual = {}, None
    for p in d.paragraphs:
        t = p.text.strip()
        if not t:
            continue
        achou = next((x for x in titulos if t.upper() == x or t.upper().startswith(x[:18])), None)
        if achou and len(t) < 70:
            atual = achou
            mapa.setdefault(atual, [])
            continue
        if atual:
            mapa[atual].append(p)
    return mapa


def _fim_do_paragrafo(par, novo_fim):
    """Troca a pontuação final do parágrafo, mexendo só no último pedaço com texto."""
    for r in reversed(par.runs):
        if r.text.strip():
            r.text = r.text.rstrip().rstrip(".;,") + novo_fim
            return True
    return False


def corrige_pontuacao_passos(d, log):
    """Deixa a pontuação dos passos coerente: ';' em todos menos o último, que
    leva '.'. O QLD.002 não define isso, mas misturar dentro do mesmo documento é
    incoerência interna — e a convenção do Bruno é ';' exceto no último."""
    passos = [p for p in _secoes(d).get("PRINCIPAIS PASSOS DO PROCESSO", [])
              if re.match(r"^.{3,80}?\s*\([^)]{2,60}\)\s*:", p.text.strip())]
    if len(passos) < 2:
        return
    fins = {p.text.strip()[-1] for p in passos}
    if not (";" in fins and "." in fins):
        return                                  # já está coerente, não mexe
    for i, p in enumerate(passos):
        _fim_do_paragrafo(p, "." if i == len(passos) - 1 else ";")
    log.append(f"pontuação dos {len(passos)} passos padronizada (';' e '.' no último)")


def corrige_celulas_sem_ponto(d, log):
    """Fecha com ponto as células que são frases inteiras, nas tabelas de
    Responsabilidades e de Definições."""
    n = 0
    for t in d.tables:
        if not t.rows:
            continue
        cab = " ".join(c.text.strip().lower() for c in t.rows[0].cells)
        if not ("responsabilidades" in cab or "definição" in cab):
            continue
        for linha in t.rows[1:]:
            if len(linha.cells) < 2:
                continue
            cel = linha.cells[1]
            txt = cel.text.strip()
            if len(txt) > 25 and not txt.endswith((".", ";")):
                if cel.paragraphs and _fim_do_paragrafo(cel.paragraphs[-1], "."):
                    n += 1
    if n:
        log.append(f"ponto final acrescentado em {n} célula(s) de tabela")


def _fluxos_das_referencias(d):
    """Códigos FL.* citados na seção REFERÊNCIAS, na ordem em que aparecem."""
    dentro, refs = False, []
    for p in d.paragraphs:
        t = p.text.strip()
        if t.upper().startswith("REFER"):
            dentro = True
            continue
        if dentro:
            if t.upper().startswith("DEFINI"):
                break
            if re.match(r"FL\.[A-Z]{2}\.[A-Z]{3}\.\d{3}", t):
                refs.append(t.rstrip(" .;"))
    return refs


def _frases_do_fluxo(refs):
    """Monta as duas frases no padrão que o Bruno adotou à mão (SUP.006 a 014)."""
    if not refs:
        return None, None
    if len(refs) == 1:
        abre = f"O processo é executado conforme fluxo, {refs[0]}, contemplando as seguintes etapas macro:"
        fecha = f"Os detalhamentos operacionais encontram-se descritos no fluxo, {refs[0]}."
    else:
        lista = ", ".join(refs[:-1]) + " e " + refs[-1]
        abre = f"O processo é executado conforme os fluxos, {lista}, contemplando as seguintes etapas macro:"
        fecha = f"Os detalhamentos operacionais encontram-se descritos nos fluxos, {lista}."
    return abre, fecha


def corrige_frases_do_fluxo(d, log):
    """Garante a frase de abertura e a de fechamento da seção de passos, as duas
    citando o código do fluxo. Padrão definido pelo Bruno editando à mão; aqui só
    é replicado nos documentos que ficaram sem."""
    refs = _fluxos_das_referencias(d)
    abre, fecha = _frases_do_fluxo(refs)
    if not abre:
        log.append("fluxo: nenhum FL.* em Referências — frases do fluxo não foram mexidas")
        return

    mapa = _secoes(d)
    passos = mapa.get("PRINCIPAIS PASSOS DO PROCESSO", [])
    if not passos:
        return

    e_passo = lambda p: bool(re.match(r"^.{3,80}?\s*\([^)]{2,60}\)\s*:", p.text.strip()))

    # --- abertura ---
    atual = next((p for p in passos if "conforme fluxo" in p.text or "conforme os fluxos" in p.text), None)
    if atual is None:
        primeiro = next((p for p in passos if e_passo(p)), None)
        if primeiro is not None:
            novo = primeiro.insert_paragraph_before(abre)
            novo.style = primeiro.style
            log.append("fluxo: frase de abertura da seção 6 inserida, com o código do fluxo")
    elif atual.text.strip() != abre:
        _troca_texto_inteiro(atual, abre)
        log.append("fluxo: frase de abertura ajustada para citar o código")

    # --- fechamento ---
    atual = next((p for p in passos if "detalhamentos operacionais" in p.text), None)
    if atual is None:
        ultimo = [p for p in passos if e_passo(p)]
        if ultimo:
            # insere depois do último passo
            novo_el = copy.deepcopy(ultimo[-1]._element)
            ultimo[-1]._element.addnext(novo_el)
            from docx.text.paragraph import Paragraph as _P
            _troca_texto_inteiro(_P(novo_el, ultimo[-1]._parent), fecha)
            log.append("fluxo: frase de fechamento da seção 6 inserida, com o código do fluxo")
    elif atual.text.strip() != fecha:
        _troca_texto_inteiro(atual, fecha)
        log.append("fluxo: frase de fechamento ajustada para citar o código")


def _troca_texto_inteiro(par, texto):
    """Troca todo o texto do parágrafo, mantendo a formatação do primeiro pedaço."""
    if not par.runs:
        par.add_run(texto)
        return
    par.runs[0].text = texto
    for r in par.runs[1:]:
        r.text = ""


def corrige_estilo_lista(d, log):
    """Seções de lista devem usar o mesmo estilo de parágrafo. Quando uma delas
    ficou como parágrafo comum, o item perde o recuo do resto do documento."""
    mapa = _secoes(d)
    contagem = {}
    for nome in SECOES_LISTA:
        for p in mapa.get(nome, []):
            e = p.style.name if p.style is not None else ""
            contagem[e] = contagem.get(e, 0) + 1
    if not contagem:
        return
    dominante = max(contagem, key=contagem.get)
    if contagem[dominante] < 3:
        return
    for nome in mapa:
        if nome not in SECOES_LISTA:
            continue
        ps = mapa[nome]
        if ps and all((p.style.name if p.style is not None else "") != dominante for p in ps):
            for p in ps:
                p.style = d.styles[dominante]
            log.append(f"seção {nome}: estilo dos itens alinhado para \"{dominante}\"")


def aplica(caminho, cfg, lista_nova, simular):
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    log = []
    tmp = tempfile.mkdtemp()
    trabalho = os.path.join(tmp, "doc.docx")
    shutil.copy2(caminho, trabalho)

    d = docx.Document(trabalho)

    # --- apagar parágrafos que são sobra de texto do modelo ---
    for alvo in cfg.get("apagar", []):
        for p in list(d.paragraphs):
            if p.text.strip() == alvo.strip():
                p._element.getparent().remove(p._element)
                log.append(f"apagado: \"{alvo[:60]}...\"")

    # --- trocas de texto no corpo e nas tabelas ---
    def todos_paragrafos():
        for p in d.paragraphs:
            yield p
        for t in d.tables:
            for row in t.rows:
                for c in row.cells:
                    for p in c.paragraphs:
                        yield p

    for velho, novo in cfg.get("trocas", []):
        total = sum(troca_no_paragrafo(p, velho, novo) for p in todos_paragrafos())
        if total:
            log.append(f"trocado ({total}x): \"{velho[:55]}\" -> \"{novo[:55]}\"")

    # --- correções automáticas, iguais para todos os documentos ---
    corrige_frases_do_fluxo(d, log)
    corrige_pontuacao_passos(d, log)
# DESATIVADO em 2026-09-02. O Bruno retirou os pontos finais que eu tinha
# acrescentado e escreveu no checklist: "Ponto final retirado, Claude não se
# atentou ao template". Conferi: o QLD.002 não diz nada sobre pontuação em
# célula, e a Tabela 1 do modelo vem com as células vazias — não existe a
# regra que eu estava aplicando. Era invenção minha, automatizada.
    # corrige_celulas_sem_ponto(d, log)
    corrige_estilo_lista(d, log)

    d.save(trabalho)

    # --- capa e cabeçalho: mexem no XML cru ---
    desmontado = os.path.join(tmp, "z")
    with zipfile.ZipFile(trabalho) as z:
        z.extractall(desmontado)

    alvo_xml = os.path.join(desmontado, "word", "document.xml")
    with open(alvo_xml, encoding="utf-8") as f:
        xml = f.read()
    xml = corrige_capa(xml, lista_nova, log)
    # A capa fica dentro de uma caixa de texto (<w:txbxContent>), que o python-docx
    # não enxerga — por isso as trocas do corpo não chegam nela. Aplicamos aqui,
    # só dentro das caixas de texto, para não mexer duas vezes no corpo.
    def _trocas_na_capa(m):
        bloco = m.group(0)
        for velho, novo in cfg.get("trocas", []):
            bloco = troca_no_xml(bloco, velho, novo)
        return bloco

    antes = xml
    xml = re.sub(r"<w:txbxContent>.*?</w:txbxContent>", _trocas_na_capa, xml, flags=re.S)
    if xml != antes:
        log.append("capa: texto da caixa de texto corrigido")
    with open(alvo_xml, "w", encoding="utf-8") as f:
        f.write(xml)

    # cabeçalho e rodapé (o erro "9001:20/15" do SUP.013 mora no cabeçalho)
    for nome in os.listdir(os.path.join(desmontado, "word")):
        if not re.match(r"(header|footer)\d*\.xml$", nome):
            continue
        cam = os.path.join(desmontado, "word", nome)
        with open(cam, encoding="utf-8") as f:
            h = f.read()
        original = h
        for velho, novo in cfg.get("trocas", []):
            h = troca_no_xml(h, velho, novo)
        if h != original:
            with open(cam, "w", encoding="utf-8") as f:
                f.write(h)
            log.append(f"{nome}: texto do cabeçalho/rodapé corrigido")

    # --- remonta ---
    saida = os.path.join(tmp, "final.docx")
    with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, _, arqs in os.walk(desmontado):
            for a in arqs:
                cheio = os.path.join(raiz, a)
                z.write(cheio, os.path.relpath(cheio, desmontado).replace("\\", "/"))

    # --- valida antes de encostar no original ---
    import xml.dom.minidom as minidom
    with zipfile.ZipFile(saida) as z:
        for nome in z.namelist():
            if nome.endswith(".xml") or nome.endswith(".rels"):
                minidom.parseString(z.read(nome))
        if "word/document.xml" not in z.namelist():
            raise RuntimeError("pacote sem word/document.xml")
    import docx as _d
    _d.Document(saida)   # abre de novo: se estiver quebrado, estoura aqui

    if log and not simular:
        shutil.copy2(saida, caminho)
    shutil.rmtree(tmp, ignore_errors=True)
    return log


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true", help="mostra sem gravar")
    g.add_argument("--aplicar", action="store_true", help="grava nos arquivos")
    ap.add_argument("--so", help="filtra por parte do nome, ex.: SUP.009")
    ap.add_argument("--pasta", default=PASTA, help="pasta com os documentos")
    ap.add_argument("--modelo", default=MODELO_POP, help="caminho do PO.GG.QLD.001")
    args = ap.parse_args()

    lista_nova = lista_do_modelo(args.modelo)
    total = 0
    for prefixo, cfg in sorted(CORRECOES.items()):
        if args.so and args.so not in prefixo:
            continue
        achados = [f for f in os.listdir(args.pasta) if f.startswith(prefixo) and f.endswith(".docx")]
        if not achados:
            print(f"{prefixo}: ARQUIVO NAO ENCONTRADO"); continue
        caminho = os.path.join(args.pasta, achados[0])
        print("=" * 78)
        print(achados[0])
        try:
            log = aplica(caminho, cfg, lista_nova, args.simular)
        except Exception as e:
            print(f"  FALHOU (original intacto): {e}")
            continue
        if not log:
            print("  nada a corrigir")
        for l in log:
            print("  - " + l)
        total += len(log)
    print("=" * 78)
    modo = "SIMULACAO — nada foi gravado" if args.simular else "APLICADO"
    print(f"{total} correcao(oes). {modo}.")


if __name__ == "__main__":
    main()