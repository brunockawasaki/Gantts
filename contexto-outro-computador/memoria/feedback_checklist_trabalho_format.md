---
name: feedback-checklist-trabalho-format
description: "Bruno's preferred Word format for turning a list of findings/action items into a fillable checklist — trigger phrase \"checklist de trabalho\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a472d24e-e52e-49e1-a2a2-249ab3afa8e2
  modified: 2026-08-12T21:01:26.546Z
---

When Bruno asks for a **"checklist de trabalho"** (or "monte um checklist para eu preencher"/"faça uma lista como essa"), build a Word (.docx) document — not a chat list — using this exact format, reconfirmed by Bruno on 2026-08-12 as the standard (this supersedes an earlier, more elaborate draft of this memory from the same date — the format below is the one he actually approved and asked to be reused every time):

- Document title (centered, bold, large) + a short italic gray subtitle describing the batch of files/topic covered.
- One heading per source file/topic: bold, colored (navy), with a thin bottom border rule under it — the heading text is literally the filename (or topic name), e.g. "RE.IG.PJC.001 — Regimento dos Comitês de Due Diligence".
- Under each heading, one checklist item per point: a checkbox glyph "☐" + two spaces + the plain-text point (no bold numbering, no em-dash formatting needed — just state the correction/decision needed, in the same wording used when the list was first given in chat).
- Immediately below each item: one blank paragraph with a thin bottom border (light gray, thinner than the heading's), giving Bruno a physical line to write his answer/decision directly in Word. One line is enough — not two.
- No intro paragraph and no closing "Como usar" section needed — the format is self-explanatory (checkbox + blank line).
- Body font Arial 10pt throughout (project standard, see [[feedback_font_arial10_registro]]).

**Why:** This is the format from the "Checklist de Correções" doc Bruno confirmed liking on 2026-08-12, built directly from a per-file corrections list already worked out in chat (see e.g. the RE.IG.PJC review). It's for action items Bruno needs to personally resolve/decide — distinct from a findings/verdict report (see the "Revisão dos Apontamentos" doc from the same session, which uses inline [MEU]/[NÃO MEU]-style verdicts instead of checkboxes).

**How to apply:**
- The trigger is the phrase "checklist de trabalho" itself, OR a follow-up like "faça uma lista como essa" right after Claude has just produced this kind of Word doc — both mean: reuse this exact structure.
- Build with python-docx (Node.js/docx-js and Word COM are both unavailable in this environment) — see the `gen_checklist_ig.py`-style script pattern: fresh `docx.Document()`, Arial 10pt Normal style, `w:pBdr/w:bottom` border trick for both heading underline and blank answer-lines (must insert the `w:pBdr` element before `w:spacing`/`w:ind` in the paragraph's `pPr` per CT_PPr schema order, or Word validation fails).
- This is a fresh/blank document, NOT a transposition into the POP/IT/Regimento template — do not confuse with [[pop_it_template_workflow]] or [[regimento_template_workflow]].
- Content for the checklist itself comes from whatever list of points was just discussed/organized in the conversation (e.g. corrections needed per file) — group items exactly the way they were grouped in chat (usually by filename).
