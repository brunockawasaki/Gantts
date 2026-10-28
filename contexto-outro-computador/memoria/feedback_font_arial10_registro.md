---
name: feedback-font-arial10-registro
description: "Every run in every POP/IT table and bullet must explicitly carry Arial 10pt (w:sz/w:szCs val=\"20\") — never omit sz and rely on doc defaults"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a472d24e-e52e-49e1-a2a2-249ab3afa8e2
  modified: 2026-07-22T16:38:35.102Z
---

Every `<w:rPr>` used to fill content into the [[pop_it_template_workflow]] template must explicitly include `<w:sz w:val="20"/><w:szCs w:val="20"/>` (Arial, 10pt) alongside `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>`. Never reuse an rPr constant that omits `w:sz`.

**Why:** the document's `docDefaults` in `styles.xml` sets size 22 (11pt), not 20 (10pt). Any run filled with an rPr that lacks explicit `w:sz` silently renders at 11pt instead of the template's standard 10pt. This bug was caught by the user in section 11 (REGISTRO DO PROCESSO) of the PO.GG.PLA.00x batch (2026-07-22): the `$R_TBL_PLAIN` constant (`<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>` with no size) had been reused across ~25 fill scripts this session for that table, and likely produced the same defect anywhere it was used, silently, since no visual diff was checked at that granularity.

**How to apply:** before writing any new `fill_*.pl` script, audit all rPr constants (`$R_RECURSOS`, `$R_PASSOS`, `$R_PONTOS`, `$R_DEFTBL`, `$R_TBL_PLAIN`, and any new ones) to confirm every one includes `<w:sz w:val="20"/><w:szCs w:val="20"/>`. Never introduce a "plain" rPr variant that drops the size just because the fonts look the same on screen — compare against the actual XML output of a real filled paragraph in the template before assuming a shorter rPr is safe.
