---
name: reference-po-gg-qld-002
description: "Official Grupo Gadens rulebook (PO.GG.QLD.002) for document naming, coding, approval flow and formatting — the authoritative source, overrides prior assumptions"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0b51ec10-09dd-45f3-99ef-321f9e69ee3a
  modified: 2026-10-21T20:58:44.967Z
---

The file `PO.GG.QLD.002 - Regras de elaboração de documento Grupo Gadens` (both `.pdf` and `.docx` exist; folder: `...\1. Bruno Kawasaki\1. Padrões\1. POP\`) is the official Grupo Gadens Procedimento Operacional Padrão defining how ALL internal documents (Manual da Qualidade, POP, Regimento, IT, Fluxograma, Política de Departamento) must be coded, approved, and formatted. Read/cite it before making naming or formatting decisions for any Grupo Gadens document — it is the ground truth, above any pattern inferred from example files.

**Current version as of 2026-08-14: Revisão 03, Status "Em aprovação"** (not yet formally approved — still subject to change; re-check before treating any single rule as final if a long time has passed). **Re-verified 2026-08-26 against the .docx: still Revisão 03, dated 14/08/2026. Everything this memory says about the Matriz de Aprovação was confirmed correct.** **Re-verified 2026-10-21: current .docx is at `...\1. Bruno Kawasaki\1. Padrões\1. Padrões\` (file dated 02/09), header says Rev. 03 (26/08/2026), last row of the revision table still has approval "A definir". Folder also holds the IT/POP/RE templates and ATA.docx. Project Next process files live in `...\OneDrive - Grupo Gadens\Processos - Documentos\Processos Grupo Gadens\1. Projetos\1. Projeto Next\2. Processos` (0. Macro Grupo Gadens has FL.GG.PRO.01 .bpm/.png and "Projeto Next - Linha Axial - Fase 2.xlsx").**

⚠️ **ALWAYS read the `.docx`, never the `.pdf`.** Both files sit in the same folder and **the PDF is stale**: it is Revisão 02 (29/06/2026) and is missing the entire MATRIZ DE APROVAÇÃO section — which is precisely what Revisão 03 added ("Inserção de matriz de aprovação e reorganização de títulos"). On 2026-08-26 I read the PDF because Bruno's message linked to it, concluded from its absence that the approval matrix "was never in QLD.002 and had been invented", and rewrote the review skill's reference file around that false conclusion — then had to undo it. The lesson generalizes beyond this file: **when a source contradicts an existing note, check whether I'm looking at an older export before concluding the note was wrong.** Absence of a section in one export is not evidence the section never existed.

Also confirmed 2026-08-26: Tabela 5 (Padrões de formatação) has exactly **eight** items and **none of them mentions bullets/markers** — so a hyphen or "•" prefix in a list is a [D] padronização call (Bruno's stated preference), never an [E] "violates QLD.002". And the rulebook has a defect of its own: header/footer say Revisão 03 but Tabela 7 has no row 3 — the last two rows are both numbered "2", the final one still with approval "A definir".

**Why:** Bruno shared this alongside a hand-refined IT so future documents follow the real rule instead of patterns I guessed from individual examples. Re-read in full on 2026-08-14 to refresh this memory and to build a `qld-002.md` reference for a colleague's review skill — this revision fixed some gaps in the prior summary (Matriz de Aprovação, Execução e Responsabilidade, PRO sector code, full Tabela 6/7 control examples).

## Document code structure
`[Tipo].[Sigla Empresa].[Sigla Setor].[Sequência Numérica] – [Título do documento]`
Example: `PO.GG.QLD.001 – Manual da Qualidade`, `IT.CM.EXB.001 - Fundações`.

**Tipo (Tabela 2):** MQ=Manual da Qualidade, PO=Procedimento Operacional, IT=Instrução de Trabalho, IM=Instrução de Material, FI=Ficha de Inspeção, FP=Formulário Padrão, FL=Fluxogramas, RE=Regimento.

**Sigla Empresa (Tabela 3):** GG=Grupo Gadens, IG=Incorporadora Gadens, CM=Construtora Make It, AS=Auto Shopping Linha Verde, TB=Triunfo do Brasil, SC=Shopping Cidade, UL=ULTJ.

**Sigla Setor (Tabela 4):** NNG=Novos Negócios, INC=Incorporação, COM=Comercial, PJC=Projetos Complementares, ORC=Orçamento, PLA=Planejamento, SUP=Suprimentos, EXB=Execução da Obra, CTT=Contratos, RCH=Recursos Humanos, POB=Pós Obra, JUR=Jurídico, FIN=Financeiro, CON=Contabilidade, TI=Tecnologia da Informação, QLD=Qualidade, SST=Segurança do Trabalho, CTE=Controle Engenharia, GMO=Gestão de Mão de Obra, AST=Assistência Técnica, CIM=Crédito Imobiliário, ARQ=Arquitetura, ADM=Administrativo, CNT=Controladoria, GPI=Gestão de Projetos de Incorporação, LEG=Legalização, **PRO=Processos** (missing from an earlier version of this memory — used e.g. in IT.GG.PRO.001, the IT master template itself).

Note: FIS (Fiscal) and ORC used in this session's PO.GG.FIS.001/ORC.001-003 are NOT in the official Tabela 4 list above — they were inferred/agreed with Bruno ad hoc when the table didn't have an obvious fit. ORC does appear officially; FIS does not (closest official candidates would be CON=Contabilidade or a request to add FIS formally) — flag this to Bruno if it comes up again.

The Setor code reflects the process/subject the document belongs to (e.g. a construction-site execution IT like "Fundações" → EXB), not necessarily the department currently drafting/reviewing it — **except** when Bruno explicitly overrides this: for "IT.CM.QLD - Fundações" he kept QLD (Qualidade) on purpose, because Alessandro Braz owns both Qualidade and Segurança do Trabalho (SST) and some activities tie directly to his role rather than to Execução da Obra (EXB). So: propose the Tabela-4-correct sector code by default, but if Bruno says to keep a different one, treat it as a deliberate per-document call tied to who owns/approves that specific content — not a signal to change the general rule.

## Matriz de Aprovação (Tabela — quem aprova cada tipo)
- **Manual da Qualidade**: Aprovação = Gestor do setor de Qualidade; Validação = Setor de Processos. Toda revisão.
- **POP / Regimento / IT**: Aprovação = Gestor da área elaboradora; Validação = Setor de Processos; Setor de Qualidade aponta oportunidades de melhoria quando identificado. Toda revisão.
- **Fluxograma**: Aprovação = Gestor da área elaboradora + Diretoria (só na elaboração inicial e quando solicitado); Validação = Setor de Processos.
- **Política de Departamento**: segue regra própria do setor de Compliance (fora do escopo deste POP).

## Execução e Responsabilidade (papéis do processo de documentação em si)
- **Gestor do Processo**: elabora, mantém atualizado, identifica melhorias, aprova/reprova conforme matriz.
- **Setor de Qualidade**: verifica pontos de qualidade, sugere melhorias.
- **Setor de Processos**: verifica pontos de processo, identifica melhorias, valida conforme as regras deste POP para aprovação final do Gestor do Processo.
- **Diretoria** (área elaboradora): aprova/reprova conforme matriz (só entra formalmente para Fluxogramas, ver acima).

## Document type → application/purpose (Tabela 1)
- Manual da Qualidade — Geral — metodologia/critérios do SGQ.
- Procedimento Operacional Padrão — Geral — etapas de um processo.
- Regimento — Geral — etapas de reunião deliberativa (envolvidos, entradas, saídas).
- Instrução de Trabalho — Obra — etapas e recursos para atividades controladas em canteiro de obra.
- Fluxograma — Geral — fluxo processual contínuo entre áreas.
- Política de Departamento — Geral — padronizar processos/mitigar riscos do departamento.
"Aplicação" (§2 in IT/POP) = a Empresa do Grupo a que o documento se aplica (Geral, Make It, Gadens, Triunfo, ULTJ etc.), não uma descrição de escopo genérica.

## Formatting rules (Tabela 5) — supersedes prior inferred defaults
- Fonte: Arial 10 (Manual da Qualidade pode usar Arial 11 ou Calibri — exceção).
- Cor da letra: Preto, texto 1.
- Parágrafo: maiúscula no início, recuo de 1,5 cm (≈851 twips firstLine — matches what's already used, confirmed correct).
- Espaçamento texto: entre linhas 1,5 (line=360 auto), 12pt antes/depois dos títulos (spacing before/after=240 twips — matches what's already used).
- Espaçamento tabela: simples entre linhas, 12pt antes/depois do parágrafo.
- Margens: 1,5 cm superior/inferior, 2,5 cm esquerda, 1,5 cm direita. **NOTE: this is asymmetric and does NOT match the current IT.GG.PRO.001 template file, which uses 1440 twips (2,54 cm) on all four sides — flag this mismatch to Bruno rather than silently changing the shared template.**
- Títulos: numerados, CAIXA ALTA, negrito. Primeiro nível "0.0.", segundo nível "0.0.0." (hierarchical numbering with the dotted sub-level, not just a bold sub-heading without a number).
- Tabelas: título da tabela "TABELA XX"; itens/legendas da tabela em minúsculo e negrito; informações em minúsculo (sem negrito); legenda da tabela (caption) em Arial tam. 9, preto, centralizado. Cor: cabeçalho da tabela = preto sobre preenchimento cinza (1º tom), células de informação = sem cor de fundo, borda preta, Arial 10.
- **(Corrigido em 2026-10-07: na IT final do Bruno as listas são listas reais do Word com marcador — só não levam "✓"/"•" digitados; ver pop_it_template_workflow.)** Body/checklist item lists: sem símbolo ✓/• digitado no texto. Bruno removed all "✓ " prefixes I had added when refining the Fundações IT; the official rule never mentions a bullet glyph, only the numbered-heading and paragraph rules above. Treat unmarked plain paragraphs (each item its own paragraph, semicolon at the end except the last item which ends in a period) as the correct list style going forward.

## Revision control (§5.3–5.4, §6)
- Revisão 00 = elaboração do documento (not 01 — a discrepancy I introduced once in the Fundações IT and need to correct: number the very first issue as "00").
- Revisão 01 = primeira alteração; segue em ordem crescente (01, 02, 03…) a partir daí.
- "Controle de Emissão" table (Tabela 6/7 pattern): columns Revisão | Etapa | Itens Revisados | Data. The "Etapa" cell holds role + person per line ("Elaboração: Nome" / "Aprovação: Nome"), not a separate "Responsável" column — matches the approach already used for the Fundações IT control table.

## Publishing workflow (§5.2)
Esteira de controle: (A) elaboração entre área responsável e Setor de Processos → (B) validação/aprovação conforme matriz de aprovação → (C) publicação no diretório do Grupo Gadens. Relevant context when Bruno is iterating on drafts before final approval.

Related: [[pop_it_template_workflow]], [[regimento_template_workflow]], [[feedback_transposicao_estrita_template]].
