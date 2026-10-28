---
name: pop-template-workflow
description: "Bruno's standing workflow for turning raw unformatted text into POPs (Procedimento Operacional Padrão) using the Grupo Gadens Word template"
metadata: 
  node_type: memory
  type: project
  originSessionId: a472d24e-e52e-49e1-a2a2-249ab3afa8e2
  modified: 2026-08-17T20:43:51.030Z
---

Bruno sends raw/unformatted text (or a messy source .docx) describing a work process; the file `PO.GG.QLD.001 - MODELO PADRÃO DE POP -  Grupo Gadens.docx` (path: `C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki\1. Padrões\1. POP\`) must always be used as the base/template for the output document — never build a fresh docx from scratch. Same standing rule family as [[pop_it_template_workflow]] (ITs, despite that memory's filename) and [[regimento_template_workflow]] (Regimentos), but this is the **POP** document type specifically — different section structure from both, do not confuse.

**Why:** This memory didn't exist before 2026-08-14 despite POP being the document type built most often this session (~30 documents: PLA, GMO, ORC, FIS...) — the pipeline only lived in scratch scripts and was never persisted. Written while designing a more robust review workflow (see [[revisao_pop_it_regimento_workflow]]) so the creation side is equally durable.

**Template section structure (12 sections):**
1. OBJETIVO (texto corrido)
2. APLICAÇÃO (texto corrido — "Empresa: X. Setores envolvidos: Y.")
3. REFERÊNCIAS (texto corrido, itens separados por "; ")
4. DEFINIÇÕES (Tabela 1 - Siglas e definições: Termo/Sigla | Definição)
5. RECURSOS NECESSÁRIOS (3 listas com marcadores: Sistemas / Documentos-Entradas / Papéis-chave)
6. PRINCIPAIS PASSOS DO PROCESSO (lista numerada)
7. PAPÉIS, RESPONSABILIDADES E AUTONOMIA (Tabela 2: Papel Funcional | Responsabilidades | Limites de Autonomia)
8. INDICADORES (texto corrido + lista com marcadores; intro padrão "Os seguintes indicadores são utilizados para monitorar a efetividade das diretrizes deste POP:" — **o padrão de fábrica do template traz "...diretrizes estratégicas de prospecção definidas neste POP:", que é um resíduo errado a substituir sempre**, mesmo quando o POP não é de prospecção)
9. PONTOS CRÍTICOS DO PROCESSO (lista com marcadores)
10. DESVIOS / AÇÕES NECESSÁRIAS (Tabela 3: Situação de Desvio | Ação Necessária | Responsável)
11. REGISTRO DO PROCESSO (texto corrido + Tabela 4: Identificação | Armazenamento)
12. CONTROLE DE EMISSÃO (Tabela 5: Revisão | Etapa | Itens Revisados | Data — célula "Etapa" contém "Elaboração: Nome" + quebra de linha + "Aprovação: Nome", não uma coluna "Responsável" separada)

**How to apply:**
- Always start from a fresh unzip of the template docx (never reuse a copy from a prior task in the same session — re-verify it's clean: `grep -c "TÍTULO"` on `word/document.xml` must be 2, with no leftover filled names, before every batch).
- Environment has no Node.js/docx-js and Word COM is unreliable (frequent `TYPE_E_CANTLOADLIBRARY` errors) — use the Perl+PowerShell OOXML pipeline documented in [[reference_ooxml_toolkit]], not python-docx, for template-based fills (python-docx is fine for *fresh* documents like the checklist, see [[feedback_checklist_trabalho_format]]).
- Cover fields to always replace: Título, Código, Data (both ISO `w:val` and `DD/MM/AAAA` display), Revisão (template default is "02" → new docs are "00"), Elaborador (template default "Bruno Kawasaki"), Aprovador (template default "Alessandro Braz, Carlos Vargas"). **Never touch** "Empresas abrangidas" — see [[feedback_grupo_gadens_naming]]. Status field default is "Aprovado" — only override if the source explicitly states a different status (see the GMO.001 "Em aprovação" case).
- **If the document code, elaborador, or aprovador aren't clearly given in the source (or match the template's own placeholder defaults suspiciously exactly), ask Bruno rather than guessing** — confirmed pattern from ORC.001 (code) and PO.GG.FIS.001 (elaborador/aprovador turned out to be unedited template defaults).
- When a required section has no content in the source (common when the source was actually an IT or otherwise structurally thinner than a POP — see the FIS.001 case), write "Não especificado no texto de origem." rather than inventing anything — never leave a section silently empty either.
- Font: Arial 10pt (`sz`/`szCs`=20) explicit on every authored `rPr`, no exceptions — see [[feedback_font_arial10_registro]].
- Never invent structure, titles, or content beyond what the source says — see [[feedback_no_fabricated_content]] and [[feedback_transposicao_estrita_template]].
- Validate the packed .docx via well-formed-XML check (PowerShell `[xml]$x = $xmlText`) + structural sanity (`<w:tbl>`/`<w:tr>` counts matching expected row counts) whenever Word COM is unavailable for a real open-test; say so explicitly when delivering, and recommend Bruno open the file once before circulating it.
- Related: [[levantamento-processo-pop skill]] can be used upstream to collect raw process info before this formatting step.
- Whenever explaining apontamentos, sugestões, ou pontos técnicos sobre o conteúdo de um POP (não só a estrutura do documento) — inclusive quando o processo é de engenharia/obra — usar linguagem prática e didática, sem assumir formação técnica: ver [[feedback_explicacao_didatica_leigo]].
