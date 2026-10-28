# Checagens de coerência interna — aplicam-se a POP, IT e Regimento

Estas checagens são **adicionais** ao checklist de completude por tipo (`pop-checklist.md` /
`it-checklist.md` / `regimento-checklist.md`) e à checagem formal do QLD.002
(`qld-002-<tipo>.md`). Nasceram de uma comparação entre duas revisões independentes do mesmo lote
de documentos (9 POPs de Suprimentos, 2026-08-25): a checklist original cobria estrutura e
formato, mas deixava passar problemas de coerência interna do texto que uma segunda revisão
pegou. **Sempre rodar as 5 checagens abaixo em toda revisão**, além do checklist do tipo — não são
opcionais nem "se sobrar tempo".

## 1. Texto de instrução residual do template (resíduo de preenchimento)

Frases genéricas que descrevem o que uma seção *deveria* conter, em vez de conter o conteúdo em
si, às vezes sobrevivem à transposição do texto-fonte para o template. Exemplos reais já vistos:

- Definições: "Identificar e descrever os termos técnicos, siglas, abreviaturas e acrônimos
  utilizados neste documento, assegurando a padronização da linguagem e a correta compreensão dos
  requisitos estabelecidos."
- Registro do Processo: "Identificar os entregáveis do processo, ou seja, o produto do processo."

**Teste**: a frase explica O QUE a seção deveria conter (instrução de preenchimento) em vez de
preencher com o conteúdo real do processo? Se sim, é **[E]** — apagar. Confirmar que não é
conteúdo real do processo antes de apagar (ex.: uma IT que genuinamente descreve "identificar e
descrever X" como um PASSO do processo não se enquadra aqui).

Pista útil (não é comparação cruzada proibida, é só um sinal dentro da mesma tarefa): se a mesma
frase aparece em alguns documentos do lote sendo revisado e não em outros, na mesma seção do mesmo
template, isso reforça que é resíduo de preenchimento inconsistente, não texto intencional. O
apontamento vale por si só em cada documento, independente desse sinal.

## 2. Contradição interna dentro de uma mesma seção

Seções com estrutura de "frase de abertura + conteúdo + frase de fechamento" (o exemplo mais comum
é INDICADORES no POP: abre com "Os seguintes indicadores são utilizados para monitorar a
efetividade..." e fecha com "Os indicadores devem ser acompanhados mensalmente...") precisam ser
lidas como um todo, não frase a frase. Se o conteúdo do meio diz "este POP não possui indicadores
próprios" mas a abertura e o fechamento pressupõem que indicadores existem e são monitorados, isso
é uma contradição interna — **[E]**. Ação: se não há indicador, a abertura/fechamento devem ser
ajustadas para não pressupor monitoramento; se há indicador, a frase "não possui" precisa sair.

Aplicar o mesmo teste a qualquer seção com esse formato abertura+conteúdo+fechamento, não só
Indicadores — é um padrão de defeito, não uma regra exclusiva de uma seção.

## 3. Consistência de termos e papéis — nas duas direções

O checklist de completude de cada tipo já cobre "termo usado no corpo e nunca definido" (uma
direção). **Sempre cobrir também a direção inversa e os casos de grafia/identidade**:

- Termo definido na tabela de Definições mas nunca usado no corpo do documento (ex.: "Aprovador"
  definido, mas o corpo usa "Engenheiro da Obra" / "Engenheiro de Obra" — variantes que nem batem
  entre si).
- Papel com responsabilidade própria na tabela de Papéis/Responsabilidades mas que nunca aparece
  como executor de nenhum passo do processo (ex.: "Solicitante" responsável por "Emitir a
  Solicitação", mas nenhum passo tem "(Solicitante)" como executor).
- Duas ou mais grafias do mesmo papel dentro do **mesmo documento** (ex.: "Supervisor de
  Almoxarife" numa tabela e "Supervisor de Almoxarifado" em outra, no mesmo arquivo) — sempre
  **[E]**, mesmo que o papel já tenha sido apontado por outro motivo (ex.: ausência em uma tabela);
  grafia inconsistente e completude são defeitos distintos e cada um merece seu próprio item.
- Dois papéis que parecem descrever a mesma pessoa/função com nomes diferentes (ex.: "Solicitante"
  definido como sinônimo de um "Almoxarife" específico em Definições, mas tratado como papel
  distinto em outra tabela) — **[E]** pedindo esclarecimento sobre se são o mesmo papel.
- **O mesmo papel com responsabilidade diferente em dois lugares do documento.** Comparar o que a
  tabela de Definições diz que o papel faz contra o que "Papéis-chave" e a tabela de
  Responsabilidades dizem. **[E]** quando divergem.

  Exemplo real (SUP.010): a Tabela 1 define o Supervisor de Almoxarifado como "responsável pelo
  **cadastro** do material ou serviço"; a seção 5.3 o descreve como "responsável pela
  **validação** de itens". Cadastrar e validar são atividades diferentes, e o documento atribui
  as duas ao mesmo papel em lugares distintos sem dizer que faz as duas. Esta checagem faltava
  até 2026-08-26 — a regra existente só olhava se o termo estava definido, não se as descrições
  batiam entre si.

## 4. Coluna que não discrimina nada

Quando uma coluna existe para diferenciar itens (ex.: "Limites de Autonomia" por papel) mas todas
as linhas têm exatamente o mesmo valor genérico (ex.: todas "Plena"), isso **não** é o mesmo caso
que "Não especificado" (já coberto no checklist de completude) — está preenchido, mas não carrega
informação real. Apontar como **[C]**: perguntar à área se cada papel realmente tem autonomia
plena e idêntica, ou se a coluna deveria discriminar por papel (ex.: quem aprova/reprova vs quem
só executa vs quem escalona).

## 5. Redação e gramática básica

Revisar a redação de cada passo/frase do corpo, não só a estrutura. Sempre **[E]** quando
objetivamente quebrado — isso não é opinião de estilo, é defeito de escrita que atrapalharia a
leitura por um executor real do processo:

- Mistura de modo verbal na mesma frase/item de lista (ex.: infinitivo e terceira pessoa do
  singular no mesmo passo: "Realizar a verificação... e avalia impacto..." — deveria ser
  "avaliar").
- Pontuação que quebra a frase (parêntese aberto sem fechar, vírgula que separa indevidamente
  sujeito de verbo).
- Frases que misturam duas ações diferentes sem separação clara (ex.: uma lista de itens a
  conferir emendada com uma instrução de ação, tudo dentro do mesmo parêntese/frase).

## 6. ~~A definição cabe no escopo deste documento?~~ — REGRA CANCELADA

Esta seção mandava apontar quando uma definição descrevia algo além do processo em questão. **O
a governança vetou em 2026-08-26**, nos dois exemplos que eu tinha usado para escrevê-la:

- SUP.011 define Almoxarife como "responsável pelo estoque do local" num POP de ferramentas →
  *"As ferramentas estão localizadas no almoxarifado, refine mais seu raciocínio."*
- SUP.014 define o Supervisor como responsável pelo cadastro **e** pela manutenção →
  *"Não tem como falar de cadastro de itens, sem se referir à manutenção dos itens já cadastrados."*

**Não apontar escopo de definição.** Ver `nao-apontar.md`, regra 4. A checagem que continua
valendo é outra, e está na seção 3 acima: o **mesmo papel descrito com responsabilidades
diferentes em dois lugares do mesmo documento** — isso sim é contradição interna.

## 7. O mesmo documento com nomes diferentes entre seções

A checagem de grafia da seção 3 vale para papéis. Vale igual para **documentos e formulários**:
o mesmo artefato citado com nomes diferentes em seções diferentes é **[E]**.

Exemplos reais: SUP.011 chama a mesma ficha de "Ficha de Controle de Retirada de Ferramentas"
(5.1), "Ficha de Retirada de Ferramenta" (passo 3) e "ficha de retirada de ferramenta" (passos 3
e 4). SUP.014 chama o mesmo documento de "Solicitação de validação do Item" na tabela de Registro
e de "Solicitação de Análise" no passo 2.

## 8. Cruzamentos de capa, rodapé e cadeia de aprovação

Duas checagens que o checklist formal do `qld-002-<tipo>.md` não fechava sozinho:

**Capa × cabeçalho × rodapé, campo a campo.** O checklist formal manda conferir código, revisão e
data. Estender ao campo **"Tipo de documento"**, que diverge com frequência: capa trazendo
"Procedimento Operacional" e rodapé trazendo "Procedimento Operacional Padrão" é **[E]** por
documento. Ver o limite de escopo do guarda-corpo de template em branco no `SKILL.md` — valor
divergente herdado do template continua sendo [E], porque a incoerência é visível para quem lê.

**O Aprovador da capa tem que ser o último evento datado do Controle de Emissão.** Pela matriz de
aprovação do QLD.002, a aprovação final é do gestor da área e é o último evento da esteira. Então:
o nome que está como "Aprovador" na capa precisa aparecer como o último evento **com data
preenchida** na tabela de Controle de Emissão. **[E]** quando a cadeia não fecha.

Exemplo real (SUP.008): a capa registra Aprovador "Cleber Colin" com Status "Em aprovação"; a
Revisão 0 registra aprovação de Cleber Colin em 21/08/2026; e a Revisão 1 registra "Validador:
Carlos Vargas — A definir" como último evento. O último evento da esteira não é a aprovação do
gestor, e a data de aprovação da Revisão 0 coincide com a data de elaboração da Revisão 1.

Conferir sempre os três juntos, não isoladamente: (a) quem consta como Aprovador na capa, (b) qual
é o último evento datado da tabela, (c) o que o Status declara. Se os três não contarem a mesma
história, é [E] — e a pergunta sobre qual é a versão correta vira um [C] à parte.

## Nota sobre generosidade nas perguntas [C] de aprofundamento de processo

Além dessas 5 checagens, é válido — e incentivado — fazer perguntas **[C]** de aprofundamento
sobre lacunas de processo que a estrutura do documento deixa aparentes, mesmo sem uma regra
específica que as capture. Exemplos: "o passo de transporte entre obras não define responsável,
prazo, nem o que fazer se o material chegar avariado"; "os passos tratam o Almoxarife
genericamente, sem diferenciar o da obra de origem do da obra de destino". Isso **não** é afirmar
que o processo está errado no mérito (isso continua proibido pela regra principal do `SKILL.md`) —
é perguntar se uma lacuna aparente foi uma omissão de documentação ou uma escolha real do
processo. Não hesitar em fazer esse tipo de pergunta com mais frequência do que o padrão anterior.
