---
name: feedback-reconferir-versao-atual
description: "Never repeat an earlier finding without re-reading the current file; when several copies of a document exist (Downloads / Projeto teste / Aprovação), identify which is current BEFORE asserting anything about it"
metadata:
  type: feedback
---

Antes de repetir qualquer apontamento feito numa rodada anterior, **reler o arquivo atual**. E quando o mesmo documento existir em mais de uma pasta (Downloads, Projeto teste, Aprovação), **descobrir qual é a versão corrente antes de afirmar qualquer coisa** — comparar conteúdo (presença de trechos que só a versão nova tem) e tamanho, não só a data de alteração, que o OneDrive e as minhas próprias edições mexem.

**Why:** Em 2026-09-02 revisei o PO.GG.SUP.012 na cópia da Downloads, onde a capa dizia Revisão 01 e o cabeçalho/rodapé diziam 00. Reportei a divergência, coloquei no checklist como "precisa de decisão", e repeti isso em duas respostas seguintes. A cópia da Aprovação — a que o Bruno realmente usa — sempre esteve coerente em 00 (19/06/2026) nos três lugares. Ele mandou um print da capa e perguntou "Como, se eu estou vendo que está correto?". Estava certo: o apontamento nunca valeu para o arquivo dele.

Pior: eu tinha o sinal na mão. Ao comparar as pastas vi que a versão da Aprovação era maior e continha o conteúdo novo — prova de que era a atual — e mesmo assim afirmei que ela estava desatualizada, e propus substituir a versão certa pela errada. O Bruno autorizou com base nessa informação errada minha; só não deu prejuízo porque conferi antes de copiar e inverti o sentido a tempo.

**How to apply:**
- Nunca reafirmar um achado de rodada anterior sem reabrir o arquivo. Achado é sobre um arquivo específico, não sobre "o documento".
- Havendo cópias em várias pastas, listar todas e identificar a corrente por conteúdo antes de revisar ou de propor mover/substituir.
- Quando uma comparação contradisser o que eu disse antes, tratar a comparação como a verdade e corrigir de imediato — não seguir repetindo a versão antiga da história.
- Apontamento que morreu (arquivo substituído, item já resolvido) sai do checklist; não deixar o Bruno gastar tempo com item morto.

Related: [[revisao_pop_it_regimento_workflow]], [[feedback_confirmacao_nao_e_autorizacao]]
