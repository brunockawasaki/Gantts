---
name: feedback-entender-antes-de-conferir
description: "Bruno pediu (2026-08-26) que eu analise e entenda o texto do processo, não só confira requisitos contra checklist — vale para revisão de POP/IT/Regimento e para qualquer análise de documento"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87663fe1-caf6-4526-9fb6-4e324de2cd03
  modified: 2026-08-28T18:38:27.016Z
---

Ao revisar qualquer documento de processo, **entender o texto vem antes de conferir requisito**. Checklist é rede de segurança, não é o trabalho. Palavras dele: *"quero que além de checagem de requisitos, você realmente analise o texto e entenda"*.

**Why:** Em 2026-08-26, na devolutiva do checklist dos 9 POPs de Suprimentos, sete apontamentos meus foram vetados por ele — todos do mesmo tipo: eu tratava o documento como formulário a preencher, não como processo a entender. Exemplos: apontei que a definição de Almoxarife falava em "estoque" num POP de ferramentas (ele: *"As ferramentas estão localizadas no almoxarifado, refine mais seu raciocínio"*); apontei que o e-mail não podia ser sistema e entrada ao mesmo tempo (ele: *"pode ser tanto a ferramenta, quanto o produto da ferramenta"*); apontei falta de sequência explícita entre passos (ele: *"não é necessário deixar o texto redundante... utilizar o 'raciocínio lógico'"*). Nenhum desses seria escrito se eu tivesse lido o processo como processo.

O outro lado é que os melhores achados da sessão vieram de entendimento, não de checklist: o POP que existe para padronizar descrição de item e nunca define o padrão; o POP que prevê um desvio que o próprio fluxo não consegue detectar; o POP que promete reduzir extravio e não define prazo de devolução; o POP que manda confirmar data com o fornecedor antes de verificar se há espaço.

**How to apply:**
- Antes de escrever qualquer apontamento, responder para mim mesmo: o que este processo entrega e para quem; quem faz o quê e em que ordem; o que daria errado se alguém seguisse o documento ao pé da letra; onde isso quebra na vida real.
- Teste de cada apontamento: **se eu mostrar isso a quem executa o processo, ele reconhece como problema?** Se for só "não bate com o checklist", apagar.
- Está implementado como passo 2 obrigatório do fluxo da skill `revisor-pop-it-regimento`, e as sete regras vetadas estão em `references/nao-apontar.md` daquela skill.
- Vale além da revisão de documento: quando ele pedir análise de qualquer coisa, ler para entender o sentido, não para conferir contra uma lista.
- Relacionado: [[revisao_pop_it_regimento_workflow]], [[feedback_linguagem_simples_direta]], [[feedback_explicacao_didatica_leigo]].
