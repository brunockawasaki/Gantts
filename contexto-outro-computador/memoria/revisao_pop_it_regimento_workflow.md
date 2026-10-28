---
name: revisao-pop-it-regimento-workflow
description: "Bruno's standing workflow for auditing/reviewing an already-elaborated POP, IT, or Regimento against PO.GG.QLD.002 and per-type structural completeness — adapted from a colleague's (Fabrício's) Claude skill, generalized for our creation+review method"
metadata: 
  node_type: memory
  type: project
  originSessionId: a472d24e-e52e-49e1-a2a2-249ab3afa8e2
  modified: 2026-08-26T12:33:44.634Z
---

Trigger: whenever Bruno asks to revisar, auditar, conferir, or apontar erros/pendências in an already-elaborated POP/IT/Regimento — even without those exact words ("dá uma olhada nesse documento", "tá certo isso?", "compara com o QLD.002"). Not for generating a new document from raw text (that's [[pop_template_workflow]] / [[pop_it_template_workflow]] / [[regimento_template_workflow]]) and not for reviewing the templates/QLD.002 themselves.

**As of 2026-08-25, this workflow is implemented as a single unified installed Claude Code skill**: `revisor-pop-it-regimento` (`~/.claude/skills/revisor-pop-it-regimento/`), covering POP, IT, and Regimento in one skill — invoke via the Skill tool, don't hand-roll the workflow when the file type matches. It has `SKILL.md`, three per-type adapted copies of the QLD.002 rules (`references/qld-002-pop.md`, `qld-002-it.md`, `qld-002-regimento.md`), three per-type structural completeness checklists (`pop-checklist.md`, `it-checklist.md`, `regimento-checklist.md`), and `scripts/gen_checklist.py` (shared script). This replaced two earlier separate skills (`revisor-pop-gadens`, `revisor-regimento-gadens`, both still present on disk but superseded — not yet deleted, pending Bruno's validation of the unified one) and adds the IT coverage (6-section checklist) that neither of those had. The unified skill mirrors, but is not identical to, Fabrício's original single generic skill (`revisor-pop-it-regimento`, sent 2026-08-21, re-shared 2026-08-25 as a `.md` file for Bruno to incorporate): ours always generates the Word checklist (not optional), splits the shared `qld-002.md` into three type-adapted copies instead of one generic file, adds guardrails his didn't have (blank-template-vs-real-revision; column-fusion-vs-content-loss from source transposition; not treating IT's leaner 6-section structure as a completeness gap vs POP's 12), and doesn't assume the Claude.ai web upload path convention (`/mnt/user-data/uploads`) since this environment uses local Windows paths.

**Why:** Built 2026-08-14 after analyzing a skill file Fabrício (a colleague on Projeto Next) built for the same purpose (`revisor-pop-it-regimento`). Its core discipline — classify findings, never assert technical merit as wrong, check structural completeness systematically — is genuinely good and was independently reconstructed by hand during the ORC/GMO apontamentos review earlier this session. This memory formalizes it as our standing method, adds guardrails specific to our situation (we create documents too, Fabrício's skill only reviews), and always closes the loop into the already-approved [[feedback_checklist_trabalho_format]] Word deliverable.

## Review flow

1. Read the document in full (extract via the [[reference_ooxml_toolkit]] Perl pipeline, or `Read` for non-docx). For .docx, extract cabeçalho/rodapé too — they carry código/revisão/data that can diverge from the cover or body.
2. Identify the type from the código prefix (PO/IT/RE) and load the matching completeness checklist below.
3. Run the QLD.002 formal checks: código estrutura (`[Tipo].[Sigla Empresa].[Sigla Setor].[Sequência] – [Título]`, see [[reference_po_gg_qld_002]]), esteira/matriz de aprovação coherence, capa × cabeçalho × rodapé consistency, unfilled placeholders, título/tabela formatting per Tabela 5.
4. Run the per-type structural completeness checklist (below).
5. Classify every finding:
   - **[E]** erro objetivo — corrige direto, não depende de decisão de ninguém.
   - **[C]** conteúdo — precisa de confirmação da área responsável pelo processo.
   - **[D]** decisão — escopo/padrão do projeto; cabe a Bruno ou à governança do Next.
   - **[C/D]** quando genuinamente não dá pra saber — uma frase curta explicando a hesitação. Não travar a revisão por causa disso.
6. Write findings grouped by document, chat text format below (Fabrício's block format, kept as-is — it's clean and Bruno already reads it fine).
7. **Always also build the "checklist de trabalho" Word doc** (see [[feedback_checklist_trabalho_format]]) covering every [C]/[D]/[C/D] item — confirmed standing preference 2026-08-14, do this automatically without being asked again each time.

## The rule that separates apontamento from opinião técnica (the most important rule — do not loosen)

- **Sempre aponte**: ausência de estrutura esperada — falta de limiar/critério onde deveria haver um, indicador que não mede o desvio que o próprio documento declara, ação de desvio que não corrige nada, papel citado no texto e ausente da tabela de responsabilidades, contradição interna, referência citada e não listada, placeholder não preenchido, capa desatualizada (**mas ver guarda-corpo abaixo antes de afirmar isso**), numeração de seção incoerente com o escopo.
- **Nunca afirme como erro** que um valor técnico existente está errado no mérito (tolerância de engenharia, prazo de negócio, regra de precificação). Bruno e eu somos de processos, não especialistas na área fim. Se um valor existe mas parece questionável, vira pergunta [C] para a área confirmar — nunca afirmação de erro.
- Teste rápido antes de escrever um apontamento: "isso é ausência de estrutura (aponto) ou é o conteúdo técnico de uma estrutura que já existe (pergunto, não afirmo)?"

## Guarda-corpo específico nosso (Fabrício não precisa dele — ele nunca cria documentos com Claude, nós criamos)

**Nunca comparar a capa/cabeçalho/rodapé de um documento preenchido contra os valores-padrão de fábrica do template em branco como se fossem uma revisão anterior real.** Antes de apontar "capa desatualizada" ou "revisão anterior diverge", confirmar se os valores "diferentes" não são simplesmente o placeholder do template (`Bruno Kawasaki` / `Alessandro Braz, Carlos Vargas` / Revisão `02` / Status `Aprovado` são os defaults conhecidos de fábrica — ver [[reference_ooxml_toolkit]]). Isso já gerou um apontamento incorreto real (ORC.002/ORC.003, "capa desatualizada... rev. vigente é 01 por Bruno / Carlos Vargas" — não existia essa revisão, era o template em branco sendo confundido com histórico real).

## Guarda-corpos de escopo herdados da skill do Fabrício

- Não compara documentos "irmãos" entre si por padrão (ex.: os 5 Regimentos de comitê de fase, os 3 POPs de Orçamento) — só se Bruno pedir explicitamente e fornecer os documentos juntos na mesma tarefa.
- Não revisa os templates/modelos padrão em si (PO.GG.QLD.001, IT.GG.PRO.001, RE.GG.PRO.001, QLD.002) — isso é conversa separada com Bruno/governança do Next.
- Não decide se um POP/Regimento espelhado entre Gadens e Make It é duplicidade — ações e documentos espelhados entre as duas empresas são intencionais por padrão; nunca sinalizar como redundância sem confirmar antes.

## Checklist de completude estrutural por tipo

**POP** (12 seções, ver [[pop_template_workflow]]): Objetivo, Aplicação, Referências, Definições, Recursos Necessários (Sistemas/Documentos/Papéis-chave), Principais Passos, Papéis-Responsabilidades-Autonomia, Indicadores, Pontos Críticos, Desvios/Ações, Registro do Processo, Controle de Emissão.

**IT** (6 seções, ver [[pop_it_template_workflow]] — note the filename says "pop_it" but the content is about IT specifically): Objetivo, Aplicação, Referências, Definições, Etapas da Instrução de Trabalho (texto explicativo + imagem por passo), Controle de Emissão. IT não tem Recursos/Responsabilidades/Indicadores/Pontos Críticos/Desvios/Registro como seções próprias — não apontar a ausência delas como erro, é a estrutura correta do tipo.

**Regimento** (9 seções, ver [[regimento_template_workflow]]): Objetivo, Aplicação, Áreas Envolvidas, Governança e Operacionalização (Convocação/Periodicidade/Formato/Pauta/Registro), Papéis e Responsabilidades, Entradas/Inputs, Saídas/Outputs, Referências, Controle de Emissão.

Ao revisar um documento gerado por nós mesmos (não só auditando um documento de terceiros), diferenciar explicitamente: lacuna que já existia na fonte original (não é erro de transposição, é do processo/área) vs. lacuna que eu introduzi ao transpor. A primeira categoria é a maioria dos achados [C]/[D] que já vimos.

## Formato de saída (chat)

```
### [Código do documento] - [Título curto]

1. [E] Descrição objetiva do erro e onde está. Ação: o que corrigir.
2. [C] Descrição do que precisa confirmação. Pergunta específica para a área.
3. [D] Descrição da lacuna de escopo/decisão. Quem decide.
```

Fechar com uma linha de resumo quando houver muitos documentos: quantos [E], [C], [D], e sugestão de sequência de ataque. Texto corrido, sem tabela nem artifact no chat (a estrutura acionável vai para o Word checklist, não para o chat).

**Update (2026-08-25):** a colleague of Bruno's ran a parallel/independent review pass over the same batch of 9 Suprimentos POPs and found far more findings than this skill did. Comparing point-by-point surfaced 5 categories of defect the checklist genuinely didn't cover: residual template fill-in instructions left in the body (e.g. "Identificar e descrever os termos técnicos..." in Definições), internal contradiction within an opening+content+closing section (e.g. Indicadores opening/closing text presupposing indicators exist while the body says "este POP não possui indicadores próprios"), term/role consistency checked only in one direction (added: a defined term never used in the body, e.g. "Aprovador" defined but body uses "Engenheiro da Obra"/"Engenheiro de Obra"; a role with its own responsibility row that never executes any process step; two spellings of the same role within one document), a table column filled with the same non-discriminating value for every row (e.g. "Limites de Autonomia" = "Plena" for all 4 roles), and basic redação/grammar breaks (mixed verb mood, unclosed parenthesis, misplaced comma). These 5 categories are now formalized as `references/coerencia-interna.md` in the skill and made a **mandatory** step in the review flow (not optional) — see the skill's SKILL.md. One of the colleague's findings (claiming code "FL" isn't in QLD.002's document-type table) looked wrong against this skill's own captured copy of QLD.002 (which does list "FL | Fluxogramas") — flagged back to Bruno as something to double-check rather than accepted at face value, since instinct should be to verify surprising claims against the actual reference before absorbing them.

**Update 2 (2026-08-25, same day):** a third parallel review — this one of a single document in depth (SUP.008) — exposed 5 more failure causes, two of them self-inflicted by this skill's own guardrails being applied beyond their scope: (1) the "blank template vs real revision" guardrail was downgrading internal capa × rodapé divergence from [E] to a [D] batch note ("the value came from the template") — it only ever applied to comparisons against a supposed *prior revision*, never to internal inconsistency within one file; (2) the "column fusion" guardrail was being read as permission not to *read* the fused text at all, losing content gaps inside it (e.g. "Retenção: Conforme política interna" — which policy?) — it protects the form, not the content. Both now have explicit "Limite de escopo" subsections in SKILL.md. The other three: (3) an entirely missing category — reading the steps as a **causal chain** rather than a list (step order that inverts a dependency, conditional branches that dead-end, a flow with no exit/handoff, the named executor vs who actually performs the step, deriving probable desvios from each step, Registro vs what the steps actually produce) → new `references/fluxo-e-desvios.md`; (4) two missing cross-checks (capa × rodapé field-by-field including "Tipo de documento"; the cover's Aprovador must be the last *dated* event in Controle de Emissão) → section 6 of `coerencia-interna.md`; (5) findings written aggregated instead of split per concrete gap — aggregating hides findings (one "Papéis-chave lists 4, Tabela 2 has 1" hid that Comprador was also missing from Definições and that Supervisor had a third spelling) → "Granularidade" section in SKILL.md.

**Transversal lesson, worth more than the individual rules:** when a parallel review finds substantially more, the cause is almost never "looked harder" — it is a missing check category or one of our own rules applied outside its scope. Map the cause before rewriting the checklist. Also: verify surprising findings against the actual reference before absorbing them (the "FL" claim was wrong; and three findings I nearly wrote myself — empty footer Data field, lowercase section titles, both false — died on verification because the runs were split in XML and the titles carry `w:caps`).

**Update 3 (2026-08-31):** Bruno cobrou duas vezes o checklist Word que a skill manda gerar sempre — eu tinha feito a revisão, aplicado as correções e escrito o resumo no chat, e simplesmente não gerado o arquivo. A regra ("sempre gerar, não é opcional") já estava escrita como último passo do fluxo e mesmo assim foi pulada. **Conserto estrutural, não mais uma exortação: o checklist agora é o passo 10 e a resposta no chat é o 11.** Gerando o arquivo ANTES de escrever o texto, o chat vira resumo de um entregável que já existe, em vez de substituto dele. Se a revisão não produzir nenhum item [C]/[D], dizer isso explicitamente em vez de simplesmente não gerar nada. Aplicado nas duas skills (`revisor-pop-it-regimento` e a versão compartilhável `revisor-documentos-gadens`).

Related: [[reference_po_gg_qld_002]], [[feedback_checklist_trabalho_format]], [[feedback_no_fabricated_content]].
