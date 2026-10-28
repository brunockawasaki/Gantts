# Leitura do processo como fluxo — POP, IT e Regimento

As checagens de completude (`pop-checklist.md` etc.) leem a seção de passos como **lista**:
numeração pula? papel citado está definido? Isso pega lacunas de estrutura, mas deixa passar o
defeito mais caro de um documento de processo — **um fluxo que não fecha**.

Este arquivo cobre a leitura dos passos como **cadeia causal**. Nasceu de uma comparação com uma
revisão paralela do mesmo documento (SUP.008, 2026-08-25) que encontrou 6 defeitos deste tipo que
esta skill não tinha como ver. **Rodar sempre**, junto com `coerencia-interna.md`.

Aplicar a POP (seção "Principais Passos") e IT (seção "Etapas da Instrução de Trabalho"). Em
Regimento, aplicar ao fluxo de convocação → reunião → deliberação → ata.

## 1. A ordem dos passos faz sentido?

Ler os passos na sequência em que estão numerados e perguntar se essa ordem é executável na vida
real. **[C]** quando a ordem inverte uma dependência.

Exemplo real (SUP.008): o passo 4 é "Confirmação de Agendamento" (confirmar data e horário com o
fornecedor) e o passo 5 é "Análise de disponibilidade" (analisar espaço físico e conflito com
outras entregas). Ou seja, o documento manda confirmar a data com o fornecedor **antes** de
verificar se há espaço para receber. É [C] — pergunta se a ordem é essa mesmo — e não [E], porque
pode existir uma razão operacional que a skill não conhece.

Teste: para cada passo, o que ele consome já foi produzido por um passo anterior?

## 2. Todo ramo do fluxo chega a algum lugar?

Quando um passo abre uma condicional ("caso o pedido não esteja aprovado...", "se houver
divergência..."), seguir esse ramo até o fim. **[C]** quando o ramo morre sem desfecho.

Exemplo real (SUP.008): o passo 2 diz que, se o pedido não estiver aprovado, o Almoxarife aciona
o comprador e informa o responsável da obra — e para aí. Não diz se o agendamento fica suspenso,
se há prazo de retorno, nem quem retoma o processo depois.

**Um ramo só está fechado se responder três coisas: QUEM faz, POR QUAL canal, e o que acontece
com o processo depois.** Ter uma frase de desfecho não basta.

Exemplo real de leitura frouxa (SUP.010, 2026-08-25): o passo 2 diz que, se o item já existir,
"o solicitante será orientado a utilizar o cadastro existente". Na revisão eu li isso, julguei
que o ramo tinha desfecho e segui. Não tinha: não diz **quem** orienta, **por qual canal**, nem
que o processo **se encerra ali** — e é a única bifurcação do fluxo inteiro. Uma revisão paralela
pegou; a minha não. Aplicar o teste dos três itens, não a impressão de que "tem uma frase ali".

## 3. O fluxo tem saída?

O último passo precisa entregar alguma coisa a alguém, encerrar formalmente, ou passar o bastão
para outro processo nomeado. **[C]** quando o processo simplesmente para.

Exemplo real (SUP.008): o último passo é "Recebimento no dia Agendado — verificar se o horário
está de acordo com o agendamento", e acaba. Não diz o que acontece na sequência nem conecta com
o registro de entrada, que é objeto do PO.GG.SUP.007.

Teste: depois do último passo, o que acontece? Se a resposta está em outro documento, esse
documento está citado em Referências?

## 4. O executor nomeado em cada passo é quem realmente faz aquilo?

Cada passo traz um responsável entre parênteses. Verificar se esse papel tem de fato o poder/a
posição de executar aquela ação, à luz do que as outras seções do documento dizem. **[C]** quando
o passo atribui a alguém uma ação que o próprio documento diz ser de outro (ou de um terceiro
externo).

Exemplo real (SUP.008): os 6 passos estão todos atribuídos ao "Almoxarife", incluindo etapas que
dependem de terceiros — a aprovação do pedido é do Supervisor (o próprio passo 2 diz isso), a
entrega é do fornecedor, e a necessidade de material vem do responsável da obra.

Teste: o papel entre parênteses executa, ou apenas participa/aguarda? Um papel que só recebe o
resultado não é o executor do passo.

## 5. Desvios derivados dos passos — não só os declarados

O checklist de completude já cobre "desvio mencionado no texto e ausente da tabela de Desvios".
Isto aqui é o passo seguinte, e é o que produz achado de verdade: **percorrer cada passo
perguntando o que pode dar errado ali, e conferir se a tabela de Desvios cobre**.

Não apontar como [E] a ausência de cada desvio possível (a área é quem sabe o que é relevante) —
o formato certo é **um [C] que já traz a lista concreta do que não está coberto**, para a área
responder de uma vez.

Exemplo real (SUP.008): a tabela tem uma única situação, "Informações não validadas", que é vaga
e não corresponde a nenhum ponto identificável do fluxo. Ficam sem tratamento desvios prováveis e
diretamente deriváveis dos passos: fornecedor que não confirma o agendamento (passo 3), entrega
que chega fora do horário agendado (passo 6), entrega sem agendamento prévio (passo 6), e
ausência de espaço físico na data pretendida (passo 5).

Comparar com o achado fraco que a versão anterior desta skill produzia para o mesmo documento —
"o desvio é genérico e a ação não diz o que fazer se não validar" — que aponta o sintoma sem
entregar nada acionável. **Sempre produzir a lista.**

## 6. O documento entrega o que o próprio Objetivo promete?

**Esta é a checagem de maior valor do arquivo — e a mais fácil de esquecer**, porque exige olhar o
documento inteiro de uma vez em vez de seção por seção.

Ler o Objetivo (seção 1), extrair o que ele promete entregar, e conferir se os passos entregam
aquilo — ou se justamente a parte central fica delegada a algo que o documento nunca define.
**[C]** quando o núcleo do que o POP existe para padronizar não está padronizado dentro dele.

Exemplo real (SUP.010): o Objetivo é "estabelecer critérios e procedimentos para criação,
alteração, **padronização** e controle do cadastro de itens". O passo 3 manda "padronizar
descrição uniforme, **seguindo modelo lógico e estruturado**" — e o modelo nunca é apresentado,
nem citado em Referências. Ou seja, o POP existe para padronizar descrição de item e a regra de
padronização é a única coisa que fica de fora. Não apareceu em nenhuma checagem por seção, porque
cada seção isolada parecia completa.

Teste: para cada substantivo-chave do Objetivo ("padronização", "rastreabilidade", "controle"),
existe passo, tabela ou referência que diga **como** aquilo é feito? Se a resposta for "o
documento manda fazer, mas não diz como", é [C].

## 7. O desvio previsto é detectável pelo fluxo descrito?

Para cada linha da tabela de Desvios, procurar o passo que faria aquele desvio aparecer. **[C]**
quando o documento prevê um problema que o próprio processo não tem como enxergar.

Exemplo real (SUP.013): o ponto crítico e o único desvio são "divergência entre pedido de compra e
nota fiscal". Mas nenhum passo compara a nota com o pedido — o passo 3 confronta os dados
lançados no sistema com a nota fiscal, e só. O documento monitora um problema que ninguém, seguindo
o POP, conseguiria detectar.

Teste: se eu executasse só os passos escritos, em que momento eu tropeçaria neste desvio? Se não
houver momento, ou falta um passo de conferência, ou o desvio pertence a outro processo.

O contrário também vale e já está na seção 5: desvio provável que sai dos passos e não está na
tabela.

## 8. Dois passos fazendo a mesma coisa

Ler os títulos e as ações em sequência e verificar se dois passos consecutivos não são a mesma
atividade com nomes diferentes. **[C]** pedindo para unificar ou diferenciar.

Exemplos reais: SUP.014, passo 3 "Análise da Solicitação" e passo 4 "Conferência das informações
do Item" — ambos são o Supervisor analisando o mesmo item. SUP.012, passos 4, 5 e 6 (registro de
divergência, recusa, aceite) em que o aceite vem depois da recusa sem condição de entrada, então
não se sabe se ele vale quando não há divergência, quando a divergência é aceita, ou nos dois.

## 9. O processo tem prazo em algum lugar?

Percorrer o documento inteiro procurando qualquer prazo: de execução, de resposta, de retenção, de
devolução. **[C]** quando não há nenhum — e o apontamento fica mais forte quando o próprio Objetivo
promete algo que depende de prazo.

Exemplos reais: SUP.011 promete "redução de extravios" e não define prazo de devolução, então o
desvio "Extravio da Ferramenta" fica sem gatilho. SUP.012 não tem prazo para a conferência após a
chegada nem para o retorno do comprador sobre a recusa — que é justamente onde o material fica
parado. SUP.014 não tem prazo para a análise nem para a devolutiva ao solicitante.

Não inventar o prazo: perguntar qual é, apontando onde a falta dói mais.

## 10. O Registro do Processo bate com o que os passos produzem?

O checklist de completude compara o Registro contra os **sistemas** de Recursos Necessários. Falta
a comparação mais importante: contra as **saídas que os próprios passos descrevem**. **[C]** quando
o registro listado não é o que o processo gera.

Exemplo real (SUP.008): o Registro do Processo lista "Registro de Movimentações / Mega", que é o
entregável do POP de estoque (SUP.007). Este processo, pelos seus próprios passos, gera
confirmação de agendamento por e-mail e registro em planilha ou sistema de controle (ambos
citados no passo 4) — e nenhum dos dois está na tabela de Registro.

Teste: listar o que cada passo produz (documento, e-mail, lançamento, assinatura) e conferir
contra a tabela de Registro, nas duas direções.
