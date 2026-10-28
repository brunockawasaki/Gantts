---
name: regimento-template-workflow
description: "Bruno's standing workflow for turning raw unformatted text into Regimentos (RE) using the Grupo Gadens Word template"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6b831697-41c0-4ca9-bef9-9676cf65e9c3
  modified: 2026-07-31T19:20:04.273Z
---

Bruno sends raw/unformatted text describing a committee/meeting governance routine; the file "RE.GG.PRO.001 - MODELO PADRÃO DE REGIMENTO -  Grupo Gadens.docx" (path: `C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki\1. Padrões\1. POP\RE.GG.PRO.001 - MODELO PADRÃO DE REGIMENTO -  Grupo Gadens.docx`) must always be used as the base/template for the output document — never build a fresh docx from scratch. Same standing rule family as [[pop_it_template_workflow]] (ITs) but this is the **Regimento** (RE) document type — different template file and different section structure, do not confuse the two.

**Why:** Official Grupo Gadens standard format for Regimentos, referenced against PBQP-H 2021 / ABNT NBR ISO 9001:2015 – 7.5. Consistency matters for the company's quality system.

**How to apply:**
- Always start from a copy of the template docx (unzip → merge_runs.py → edit document.xml → rezip). Never regenerate structure with docx-js.
- Template structure (2+ pages): Page 1 = cover (title block: Tipo de documento, Código do documento, Data, Revisão, Status, Elaborador, Aprovador, Empresas abrangidas) + logo + "TÍTULO DE REGIMENTO" placeholder (replace with the actual committee/meeting name). Page 2+ = header table (Documento/Rev/Data, Referência PBQP-H/ISO) + numbered sections:
  1. OBJETIVO (texto corrido)
  2. APLICAÇÃO (texto corrido — empresa/setores aplicáveis)
  3. ÁREAS ENVOLVIDAS (texto corrido)
  4. GOVERNANÇA E OPERACIONALIZAÇÃO (tabela Item/Definição — linhas fixas: Convocação/Agendamento, Periodicidade, Formato, Pauta/Material de Apoio, Registro/Ata)
  5. PAPÉIS E RESPONSABILIDADES (tabela Área/Responsabilidades — linhas variáveis por área envolvida)
  6. ENTRADAS DO PROCESSO / INPUTS (tabela Input/Descrição/Responsável — linhas variáveis)
  7. SAÍDAS DO PROCESSO / OUTPUTS (tabela Output/Descrição/Responsável — linhas variáveis)
  8. REFERÊNCIAS (texto corrido)
  9. CONTROLE DE EMISSÃO (Tabela 1 - Controle de emissão: Revisão/Etapa/Itens Revisados/Data)
  Footer table repeats Tipo de documento/Revisão/Data.
- When Bruno pastes raw text, map it into these sections, correct Portuguese grammar/spelling, may suggest improvements, but must preserve exact template formatting (fonts, sizes, alignment, table caption style "Tabela N-Nome"). Never invent specifics not present in his text — see [[feedback_no_fabricated_content]].
- Section heading paragraphs use pStyle "PargrafodaLista" + numPr numId=1, rFonts Arial, bold, sz/szCs=20 (10pt).
- Body paragraphs: rFonts Arial (eastAsia Calibri in this template, unlike the IT template's Times New Roman — do not cross-apply), sz/szCs=20, spacing after=0/line=360 auto, ind firstLine=851, jc=both.
- Table cells in the shipped template itself sometimes omit explicit sz on rPr — do NOT copy that omission. Per [[feedback_font_arial10_registro]], always write explicit sz=20/szCs=20 on every rPr you author in table cells, since the doc default is 11pt not 10pt.
- Related: [[levantamento-processo-pop skill]] can be used upstream to collect the raw info before this formatting step.
