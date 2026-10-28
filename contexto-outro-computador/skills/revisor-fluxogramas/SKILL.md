---
name: revisor-fluxogramas
description: >
  Revisa e audita fluxogramas/diagramas de processo (BPMN, notação Bizagi) do Grupo Gadens já
  elaborados — em imagem/print ou em Mermaid/texto — contra a metodologia BPMN oficial do Grupo
  Gadens e contra um framework de leitura analítica de gargalos/oportunidades, produzindo
  apontamentos classificados [E]/[C]/[D]/[O] e sempre um checklist Word para o Bruno preencher
  junto. Use sempre que o Bruno pedir para revisar, auditar, conferir ou "dar uma olhada" num
  fluxograma, diagrama de processo, mapeamento BPMN ou fluxo desenhado (Bizagi, Mermaid, imagem),
  mesmo sem usar essas palavras exatas — por exemplo "revisa esse fluxo", "tá certo esse
  diagrama?", "confere a notação desse BPMN", ou anexar uma imagem/arquivo de fluxograma pedindo
  para conferir. NÃO use para desenhar/mapear um processo do zero a partir de relato em texto
  (isso é `process-mapping` ou `anthropic-skills:analista-processos-bpmn-lean`), NÃO use para
  revisar POP, IT ou Regimento (documentos de texto — ver `revisor-pop-gadens` e
  `revisor-regimento-gadens`), e NÃO use para revisar a própria metodologia/template BPMN do
  Grupo Gadens em si — isso é conversa de governança, não auditoria de um fluxograma específico.
license: Uso pessoal — Bruno Kawasaki, Grupo Gadens / Projeto Next
---

# Revisor de Fluxogramas — Grupo Gadens

Audita um fluxograma/diagrama BPMN do Grupo Gadens já elaborado, em duas frentes:

1. **Notação** — contra a metodologia BPMN oficial do Grupo Gadens (elementos corretos, boas
   práticas, erros comuns de modelagem).
2. **Leitura analítica** — usando um framework de heurísticas por elemento (raias, gateways,
   tarefas, eventos, etc.) para levantar perguntas sobre possíveis gargalos, desperdícios e
   oportunidades de melhoria — nunca afirmações de que o processo está errado.

Produz uma lista de apontamentos classificados por natureza, e **sempre** um documento Word em
formato de checklist para trabalhar as pendências — não só quando pedido.

Esta skill é irmã de `revisor-pop-gadens` e `revisor-regimento-gadens` (mesma metodologia de
classificação e mesmo formato de saída), adaptada para o objeto ser um diagrama, não um texto
estruturado por seções.

## Antes de começar

1. **Não presuma que o fluxograma já está no contexto.** Se o Bruno mencionar um fluxo sem
   anexá-lo (imagem, `.docx`/`.pptx` com o desenho, Mermaid, export do Bizagi), pergunte por ele.
   Nunca revise de memória — use o artefato real.
2. **Identifique o formato de entrada**:
   - **Imagem/print** — ler visualmente (Claude é multimodal, basta abrir a imagem). Descrever
     mentalmente pools/raias/elementos antes de apontar, já que não há texto para grep.
   - **Mermaid/texto estruturado** — ler o código do diagrama diretamente; mapear a sintaxe
     Mermaid para os elementos equivalentes de BPMN (decisão losango ≈ gateway, etc.) antes de
     aplicar os critérios abaixo.
   - Se vier dentro de um `.docx`/`.pptx`, extrair a imagem/objeto primeiro.
3. Carregue `references/metodologia-bpmn-gadens.md` (notação oficial, boas práticas, erros
   comuns) e `references/gargalos-heuristicas.md` (framework de leitura analítica) antes de
   revisar.
4. Se vier mais de um fluxograma na mesma mensagem, revise cada um separadamente — sem
   comparação cruzada entre eles por padrão, a menos que o Bruno peça explicitamente.

## Fluxo de revisão

1. **Mapear o diagrama por inteiro** antes de apontar qualquer coisa: quantas pools/raias,
   quantos gateways, onde estão os eventos de início/fim, que artefatos aparecem. Isso evita
   apontamento fragmentado que ignora o desenho como um todo.
2. **Rodar a checagem de notação** de `references/metodologia-bpmn-gadens.md`: símbolos corretos
   (cores dos eventos, tipo certo de gateway, ícone certo de tarefa), nomes no padrão verbo +
   complemento, raia sem dono, mistura de AS-IS/TO-BE sem marcação, sistema/documento usado sem
   objeto de dados ou armazenamento de dados correspondente.
3. **Rodar a leitura analítica** de `references/gargalos-heuristicas.md`: aplicar os gatilhos por
   elemento (raias, gateways, tarefas manuais, eventos de borda, fluxos de mensagem, objetos de
   dados, subprocessos, paralelismo, anotações, extensão do fluxo) — só quando o padrão for
   notável, não para toda ocorrência isolada (ver "Como aplicar sem virar ruído" no arquivo).
4. **Classificar cada achado:**
   - **[E]** erro objetivo de notação — símbolo errado, cor errada, gateway sem os caminhos
     rotulados, nome de atividade que não é verbo + complemento, raia sem responsável nenhum.
   - **[C]** conteúdo — precisa de confirmação da área/dono do processo (ex.: um SLA citado numa
     anotação, um critério de decisão de um gateway).
   - **[D]** decisão — é escopo/padrão de modelagem do projeto (nível de detalhe, se vira
     subprocesso ou não), não erro de quem desenhou; cabe ao Bruno ou à governança do Projeto
     Next decidir.
   - **[O]** oportunidade/gargalo — leitura analítica das heurísticas acima, sempre formulada
     como pergunta específica ancorada no fluxo observado, nunca como afirmação de erro.
   - Se genuinamente não der para saber se é [C] ou [D], marcar **[C/D]** e explicar a hesitação
     em uma frase curta. Não travar a revisão por causa disso.
5. **Escrever os apontamentos** no formato da seção "Formato de saída (chat)" abaixo.
6. **Sempre também gerar o checklist de trabalho em Word** cobrindo todo item [C]/[D]/[C/D]/[O]
   — ver seção "Checklist de trabalho (Word)" abaixo. Não é opcional nem depende do Bruno pedir
   de novo.

## A regra mais importante desta skill — não afrouxar

Separar três coisas distintas, sem misturá-las:

- **Erro de notação** ([E]) — o desenho não segue a metodologia BPMN do Grupo Gadens. Isso é
  objetivo e se aponta direto.
- **Conteúdo de processo que existe mas precisa confirmação** ([C]/[D]) — um valor, regra ou
  responsável que está no diagrama mas parece incompleto ou ambíguo. Nunca afirmar que está
  "errado no mérito" — é pergunta para quem executa o processo.
- **Leitura analítica de gargalo** ([O]) — nunca é erro nem pendência de notação. É a pergunta
  que o desenho provoca sobre por que o processo funciona daquele jeito. Ver o princípio-guia em
  `references/gargalos-heuristicas.md`: "nenhum elemento representa automaticamente um
  problema, mas cada um deve provocar uma pergunta".

Teste rápido antes de escrever qualquer apontamento: **"isso é notação errada (aponto [E]), é
conteúdo do processo que preciso confirmar ([C]/[D]), ou é um padrão que me faz querer perguntar
por que o processo é assim ([O])?"**

## O que esta skill não faz (por escopo deliberado, não esquecimento)

- **Não desenha nem redesenha o fluxograma.** Propor um TO-BE completo é escopo de
  `anthropic-skills:analista-processos-bpmn-lean` ou `process-mapping`, não desta skill — aqui só
  se aponta e pergunta, não se resolve o desenho.
- **Não compara fluxogramas "irmãos" entre si por padrão.** Só se o Bruno pedir explicitamente e
  fornecer os diagramas a comparar na mesma tarefa.
- **Não revisa a própria metodologia BPMN do Grupo Gadens** (o documento de referência em si).
  Isso é conversa de governança com o Bruno e o Projeto Next.
- **Não valida com a área/especialista do processo.** Quando um apontamento depender de saber se
  o fluxo reflete a realidade operacional, isso vira [C] para a área confirmar — a skill nunca
  afirma isso sozinha.
- **Não cobre POP, IT nem Regimento.** Documentos de texto têm skills próprias
  (`revisor-pop-gadens`, `revisor-regimento-gadens`).

## Formato de saída (chat)

Texto corrido, agrupado por fluxograma — sem tabela nem artifact, a menos que o Bruno peça.

```
### [Nome/identificação do fluxograma]

1. [E] Descrição objetiva do erro de notação e onde está. Ação: o que corrigir.
2. [C] Descrição do que precisa confirmação. Pergunta específica para a área.
3. [D] Descrição da lacuna de escopo/decisão de modelagem. Quem decide.
4. [O] Pergunta analítica ancorada no elemento observado (ex.: "a raia Suprimentos recebe o
   fluxo de volta 3 vezes por retrabalho de aprovação — isso é esperado ou vale revisar o
   critério de aprovação?").
```

Fechar com uma linha de resumo quando houver mais de um fluxograma: quantos [E], [C], [D], [O],
e uma sugestão de sequência de ataque (ex.: "[E] você ajusta direto na ferramenta, [C]/[O] viram
pauta com a área, [D] é seu").

## Checklist de trabalho (Word) — sempre gerar

Todo item [C]/[D]/[C/D]/[O] vira uma linha no checklist Word, além de aparecer no chat. Use
`scripts/gen_checklist.py` (python-docx, funciona neste ambiente) em vez de escrever o XML na
mão — ele já implementa o formato certo (ver docstring do script: caixa de seleção + linha em
branco com borda para responder). Prefixe cada item do JSON com a etiqueta (`[C]`, `[D]`, `[O]`
etc.) para o Bruno saber a natureza sem abrir o chat de novo. Chame assim:

```bash
python3 scripts/gen_checklist.py --output "<caminho>.docx" --title "Checklist de Correções — <fluxograma>" --subtitle "<descrição curta do lote>" --data '<json com heading+items por fluxograma>'
```

Ou importe `build_checklist()` diretamente se estiver gerando o conteúdo dentro de outro script
Python. Salve o resultado na mesma pasta de saída que o Bruno já usa para entregáveis (ver
memória `feedback_output_folder` — pasta "Projeto teste", nunca Downloads).

## Ambiente técnico

- **Sem Node.js/npm** — não use `docx`-js.
- **Word COM não é confiável** (`New-Object -ComObject Word.Application` costuma falhar com
  `TYPE_E_CANTLOADLIBRARY`) — não dependa dele para abrir/validar arquivos.
- **`python3`/`python` com `python-docx` funcionam bem** — use para o checklist e para extrair
  imagens/texto de um `.docx`/`.pptx` existente que contenha o fluxograma.
- **Imagens**: ler diretamente com a ferramenta de leitura de arquivo (Claude é multimodal) —
  não precisa de OCR à parte para descrever o que está no desenho.
- **Validação**: depois de gerar o Word, confirme integridade fazendo o parse do
  `word/document.xml` extraído do pacote (checagem de XML bem formado), já que abrir no Word de
  verdade pode não estar disponível. Avise o Bruno quando isso acontecer e recomende que ele
  abra o arquivo uma vez antes de circular.

## Referências

- `references/metodologia-bpmn-gadens.md` — notação oficial do Grupo Gadens (eventos,
  atividades, gateways, artefatos, pools/raias), boas práticas e erros mais comuns, extraída do
  documento interno "MÉTODOLOGIA BPMN PARA MAPEAMENTO". Se o Bruno avisar que esse documento foi
  revisado, atualizar este arquivo antes de continuar revisando fluxogramas.
- `references/gargalos-heuristicas.md` — framework de leitura analítica por elemento (raias,
  gateways, tarefas manuais, eventos de borda, fluxos de mensagem, objetos de dados,
  subprocessos, paralelismo, anotações, extensão do fluxo), com o princípio-guia de nunca tratar
  um elemento como erro automático.

## Origem

Nasceu de uma conversa em que o Bruno trouxe (1) a metodologia BPMN oficial do Grupo Gadens e (2)
um framework de leitura analítica de um infográfico externo (@mapeandonapratica, elementos do
Bizagi) sobre como cada elemento do diagrama pode sinalizar risco/gargalo/oportunidade. A skill
junta as duas frentes — notação correta e leitura analítica — em vez de tratar só uma delas,
porque o Bruno explicitamente rejeitou reduzir a revisão a "o diagrama está correto na BPMN?".
