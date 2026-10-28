# Leitura analítica do fluxograma — heurísticas de gargalo/oportunidade

Fonte: material de referência trazido pelo Bruno (infográfico "Elementos do Bizagi", conta
@mapeandonapratica) sobre como interpretar cada elemento BPMN/Bizagi como sinal de possível
problema ou melhoria. Isto é a metade "analítica" desta skill — complementa (não substitui) a
checagem de notação de `references/metodologia-bpmn-gadens.md`.

## Princípio-guia — não afrouxar

> Nenhum elemento representa automaticamente um problema. Mas cada um deles deve provocar uma
> pergunta. Modelar é representar como o processo funciona. Analisar é entender por que ele
> funciona dessa maneira. Melhorar é eliminar tudo o que gera espera, desperdício, retrabalho e
> perda de informação.

Por isso todo achado desta seção é classificado **[O] Oportunidade** — nunca **[E]**. É sempre
formulado como pergunta ou hipótese a confirmar com a área, nunca como afirmação de que o
processo está errado. A pergunta "o diagrama está correto na notação?" já é coberta pelos
apontamentos [E]/[C]/[D] de notação; esta seção responde a outra pergunta: "o que esse modelo
está tentando nos mostrar?".

## Gatilhos por elemento

- **Muitas raias com o fluxo cruzando entre elas com frequência** → pode indicar excesso de
  handoffs, esperas e ruído de comunicação entre áreas. Pergunta: esses handoffs são
  necessários, ou dá para consolidar responsabilidade?
- **Muitos gateways (principalmente exclusivos em sequência)** → pode indicar decisões demais,
  critérios de aprovação pouco claros, ou alçadas redundantes. Pergunta: todo esse ponto de
  decisão existe porque o processo exige, ou porque ninguém definiu uma regra mais simples?
- **Tarefas manuais e repetitivas** (ícone de mão, ou várias "Usuário Tarefa" fazendo a mesma
  coisa em pontos diferentes) → oportunidade de padronização ou automação (RPA, Power Automate).
- **Eventos intermediários/de borda** → mostram onde ocorrem exceções, atrasos, erros,
  interrupções. Pergunta: essa exceção tem um dono e um SLA definidos, ou só existe no desenho?
- **Fluxos de mensagem** (entre pools/raias diferentes) → pontos de comunicação que podem
  precisar de responsável, canal e SLA mais claros. Pergunta: como e em quanto tempo essa
  mensagem chega ao destinatário?
- **Objetos de dados** → ajudam a achar formulário duplicado, registro manual paralelo a um
  sistema, informação que é gerada mas não chega a quem precisa dela.
- **Subprocessos** → podem revelar atividade recorrente que deveria estar padronizada e
  reutilizada em vez de redesenhada a cada fluxo novo.
- **Caminhos paralelos** (gateway paralelo) → etapas que talvez pudessem rodar simultaneamente
  para reduzir o tempo total, se hoje estão sequenciais sem necessidade real de ordem.
- **Muitas anotações** → pode indicar regra de negócio ainda não formalizada em nenhum documento
  (POP/IT/Regimento) — só existe como nota solta no fluxograma.
- **Fluxo muito longo** → excesso de etapas, movimentações, controles e atividades que não geram
  valor perceptível para quem recebe o resultado do processo.

## Como aplicar sem virar ruído

1. Não gerar um [O] para cada ocorrência isolada do elemento — só quando o padrão é notável
   (ex.: 5+ raias cruzando repetidamente, 3+ gateways exclusivos encadeados, uma tarefa manual
   que se repete em 2+ pontos do mesmo fluxo).
2. Sempre formular como pergunta específica ancorada no fluxo real (não a pergunta genérica da
   lista acima solta) — cite a raia/tarefa/gateway exato observado.
3. Se o mesmo fluxograma já é claramente um TO-BE desenhado para resolver um gargalo específico
   (ver anotações do próprio documento), não reabrir esse gargalo como [O] — ele já foi
   endereçado; checar só se a solução desenhada faz sentido.
4. [O] entra no checklist Word junto com [C]/[D], pois também depende de resposta da área — mas
   mantém a etiqueta [O] para o Bruno saber que é leitura analítica, não pendência de notação.
