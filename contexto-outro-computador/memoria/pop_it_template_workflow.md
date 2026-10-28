---
name: pop-it-template-workflow
description: "Bruno's standing workflow for turning raw unformatted text into Instruções de Trabalho (IT) using the Grupo Gadens Word template"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0b51ec10-09dd-45f3-99ef-321f9e69ee3a
  modified: 2026-08-17T20:44:00.055Z
---

Note: Bruno corrected an earlier framing of this document as a "POP" — the correct name is **Instrução de Trabalho (IT)**, not POP. Always call it IT.

Bruno sends raw/unformatted text describing a work procedure; the file "IT.GG.PRO.001 - MODELO PADRÃO DE INSTRUÇÃO DE TRABALHO - Grupo Gadens.docx" (path: `C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\1. Bruno Kawasaki\1. Padrões\2. IT\IT.GG.PRO.001 - MODELO PADRÃO DE INSTRUÇÃO DE TRABALHO -  Grupo Gadens.docx`) must always be used as the base/template for the output document — never build a fresh docx from scratch.

**Why:** This is the official Grupo Gadens standard document format for Instruções de Trabalho (IT), referenced against PBQP-H 2021 / ABNT NBR ISO 9001:2015 – 7.5. Consistency across all ITs matters for the company's quality system.

**How to apply:**
- Always start from a copy of the template docx (unzip → edit document.xml → rezip), never regenerate the doc structure with docx-js from scratch, to preserve exact fonts, sizes, alignment, legends/captions, header/footer tables.
- Template structure (2 pages): Page 1 = cover (title block table: Tipo de documento, Código do documento, Data, Revisão, Status, Elaborador, Aprovador, Empresas abrangidas). Page 2 = header table (Documento/Rev/Data, Referência PBQP-H/ISO) + numbered sections: 1. OBJETIVO, 2. APLICAÇÃO, 3. REFERÊNCIAS, 4. DEFINIÇÕES (Tabela 1 - Siglas e definições), 5. ETAPAS DA INSTRUÇÃO DE TRABALHO (texto explicativo + imagem por passo), 6. CONTROLE DE EMISSÃO (Tabela 2, Revisão/Etapa/Itens Revisados/Data); footer table repeats Tipo de documento/Revisão/Data.
- When Bruno pastes raw text, map it into these sections, correct Portuguese grammar/spelling, may suggest improvements, but must preserve exact template formatting (fonts, sizes, alignment, caption style "Tabela N-Nome").
- Related: [[levantamento-processo-pop skill]] can be used upstream to collect the raw process info before this formatting step.

**Update (2026-08-06):** Bruno hand-edited the "IT.08.003/IT.CM - Fundações" IT and removed every "✓ " / "• " bullet-symbol prefix I had added to checklist-style items — the official rulebook [[reference-po-gg-qld-002]] never specifies a bullet glyph for lists, only numbered CAIXA ALTA/negrito headings and plain-paragraph body text. **Going forward: list/checklist items are plain paragraphs (one item per paragraph, same indent/spacing as body text), never prefixed with ✓ or •.** Punctuation: each item ends in a semicolon except the last item in the group, which ends in a period. See [[reference-po-gg-qld-002]] for the full official formatting/coding rulebook, which supersedes ad hoc formatting choices made before it was shared.

**Exact formatting standard confirmed by Bruno (2026-07-20), verified against his hand-edited copy of a generated IT — apply these XML patterns for every future IT generated from this template (bullet-symbol part now superseded, see update above):**
- Body text font throughout: Arial, `w:eastAsia="Times New Roman"`, `sz`/`szCs` = 20 (10pt), `lang eastAsia="pt-BR"`. Step/paragraph text uses `<w:spacing w:after="0" w:line="360" w:lineRule="auto"/><w:ind w:firstLine="851"/>` (no `jc` — left/justify per style).
- Step images: each in their own paragraph, `<w:spacing w:before="240" w:after="0" w:line="360" w:lineRule="auto"/><w:jc w:val="center"/>` and **no `w:ind`** (do not carry over the firstLine indent from a cloned text paragraph — center the image with no first-line indent). Image width fixed at 13cm (`Cm(13)`, i.e. `cx="4680000"` EMU), height auto by aspect ratio (`noChangeAspect="1"`).
- Table rows added programmatically (e.g. via python-docx `table.add_row()`) do NOT inherit the original rows' `pPr`/`rFonts` — this silently drops back to the default Word font (not Arial 10 bold) and was the "título 4 font changed" bug Bruno flagged. Always explicitly deep-copy the `pPr` (with its `rFonts`, `b`, `color`, `jc`) from an existing correctly-formatted row's cell paragraph into every new row's cells — never rely on `add_row()` alone for formatting.
- **Why:** Bruno corrected the font on section 4 (Definições table) and the image spacing/indentation/centering by hand and asked that this be adopted as the permanent standard, not re-derived each time.
- **How to apply:** When building new ITs from the template, reuse these exact pPr/rPr snippets for text paragraphs, image paragraphs, and any dynamically-added table rows, rather than accepting python-docx's default inherited formatting.

**Update (2026-08-17):** Whenever explaining apontamentos, sugestões, ou pontos técnicos sobre o conteúdo de uma IT (não só a estrutura do documento) — inclusive quando o processo é de engenharia/obra — usar linguagem prática e didática, sem assumir formação técnica: ver [[feedback_explicacao_didatica_leigo]].

**Update (2026-10-07) — padrão final que o Bruno aplicou na IT.CM.QLD.001 (Fundações) e novo local do template (isto CORRIGE o "Update 2026-08-06" acima):**
- O template oficial de IT mudou de lugar (a pasta "1. Padrões/2. IT" não existe mais). Versão mais nova (02/09/2026): OneDrive/1. Bruno Kawasaki/1. Padrões/1. Padrões/IT.GG.PRO.001 - MODELO PADRÃO...docx. Cópias oficiais também em OneDrive/Central de Documentos_ - POLÍTICAS E GOVERNANÇA/Instruções de Trabalho (ITs)/0. Template/ e OneDrive/Processos - Documentos/Processos Grupo Gadens/3. Templates/2. IT/ (podem estar mais antigas — conferir a data). ITs publicadas ficam em OneDrive/Processos - Documentos/Processos Grupo Gadens/1. Projetos/1. Projeto Next/2. Processos/8. Incorporação e Engenharia - EP até Finalização de Obra/5. ITs/1. Qualidade/. O template novo traz Controle de Emissão com Elaboração/Revisor/Validador/Aprovação.
- Listas NÃO são parágrafos simples: Bruno usa listas reais do Word com marcador (estilo PargrafodaLista, numPr ilvl=0, bullet Symbol; no template o numId=2 é bullet) — apenas SEM os caracteres "✓"/"•" digitados à mão. Cada item termina em ";" e o último em "."; spacing after=0 line=360, jc=both.
- Subtítulos da seção 5 são numerados automaticamente pela lista multinível do título (numId=1): ilvl=1 vira "5.1.", ilvl=2 vira "5.1.1."; negrito e CAIXA ALTA (w:caps) conforme o QLD.002. O texto é digitado em caixa normal.
- Passos: "Passo N:" em negrito + texto (aprovado na IT.07.001); imagens centralizadas, before=240, 13 cm de largura.
- O formulário que gera essa estrutura sozinho está descrito em [[project_formulario_it]].
