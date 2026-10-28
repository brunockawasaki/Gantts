---
name: revisor-pop-gadens
description: >
  Revisa e audita POPs (Procedimento Operacional Padrão) do Grupo Gadens já elaborados contra o
  padrão documental oficial PO.GG.QLD.002 e contra a estrutura de 12 seções esperada de um POP,
  produzindo apontamentos classificados [E]/[C]/[D] e sempre um checklist Word para o Bruno
  preencher junto. Use sempre que o Bruno pedir para revisar, auditar, conferir ou apontar
  erros/pendências em um POP, mesmo que ele não use essas palavras exatas — por exemplo "dá uma
  olhada nesse POP", "tá certo isso?", "compara com o QLD.002", ou anexar um arquivo PO.xx.xxx.xxx
  pedindo para conferir. Também use quando ele quiser comparar um POP contra o template
  PO.GG.QLD.001 ou contra as regras do QLD.002. NÃO use para gerar um POP novo a partir de texto
  bruto (isso é o workflow de elaboração — ver memória pop_template_workflow), NÃO use para IT ou
  Regimento (fora de escopo desta skill — ver revisor-regimento-gadens para Regimento), e NÃO use
  para revisar os próprios templates/modelos padrão (PO.GG.QLD.001, IT.GG.PRO.001, RE.GG.PRO.001)
  ou o QLD.002 em si — isso é conversa de governança, não auditoria de documento de processo.
license: Uso pessoal — Bruno Kawasaki, Grupo Gadens / Projeto Next
---

# Revisor de POPs — Grupo Gadens

Audita um POP (Procedimento Operacional Padrão) do Grupo Gadens já elaborado contra o padrão
documental oficial e contra a estrutura esperada do tipo. Produz uma lista de apontamentos
classificados por natureza, e **sempre** um documento Word em formato de checklist para trabalhar
as pendências — não só quando pedido.

Esta skill é irmã da `revisor-regimento-gadens` (mesma metodologia, escopo de documento
diferente). As duas nasceram de uma ideia de um colega do Bruno no Projeto Next (Fabrício), que
tinha uma skill genérica para POP/IT/Regimento — foram divididas por tipo de documento e
adaptadas ao ambiente e aos hábitos de trabalho do Bruno (ver "O que foi adaptado da ideia
original" no fim deste arquivo).

## Antes de começar

1. **Não presuma que o arquivo já está no contexto.** Se o Bruno mencionar um POP sem anexá-lo,
   pergunte por ele ou procure no diretório de trabalho recente. Nunca revise de memória — use o
   arquivo real.
2. **Confirme que é mesmo um POP** pelo código (prefixo `PO.`) ou pelo conteúdo (descreve etapas
   de um processo operacional). Se for uma IT ou um Regimento, avise o Bruno que esta skill está
   escopada só para POP e pergunte se ele quer seguir mesmo assim sem o apoio da skill, ou se
   prefere que você aplique o mesmo raciocínio manualmente.
3. Carregue `references/qld-002.md` (checagens formais, valem para o código/capa/formatação de
   qualquer documento) e `references/pop-checklist.md` (completude estrutural específica de POP)
   antes de revisar.
4. Se vier mais de um POP na mesma mensagem, revise cada um separadamente — **sem comparação
   cruzada entre eles por padrão** (ver "O que esta skill não faz").

## Fluxo de revisão

1. **Ler o documento por inteiro.** Para `.docx`, extrair também cabeçalho e rodapé — eles
   guardam código, revisão e data que costumam divergir da capa ou do corpo. Sem Word COM
   confiável neste ambiente (ver "Ambiente técnico" abaixo), extraia via unzip + parse do
   `word/document.xml`, ou com `python-docx` iterando parágrafos/tabelas.
2. **Rodar a checagem formal** de `references/qld-002.md`: estrutura do código, esteira/matriz
   de aprovação, capa × cabeçalho × rodapé, placeholders não preenchidos, formatação (Tabela 5).
3. **Rodar o checklist de completude de POP** de `references/pop-checklist.md`: as 12 seções
   esperadas, e o que cada uma precisa conter para estar completa.
4. **Classificar cada achado:**
   - **[E]** erro objetivo — corrige direto, não depende de decisão de ninguém.
   - **[C]** conteúdo — precisa de confirmação da área responsável pelo processo.
   - **[D]** decisão — é escopo/padrão do projeto, não erro de quem escreveu; cabe ao Bruno ou
     à governança do Projeto Next decidir.
   - Se genuinamente não der para saber se é [C] ou [D], marcar **[C/D]** e escrever uma frase
     curta explicando a hesitação. Não travar a revisão por causa disso.
5. **Escrever os apontamentos** no formato da seção "Formato de saída (chat)" abaixo.
6. **Sempre também gerar o checklist de trabalho em Word** cobrindo todo item [C]/[D]/[C/D] —
   ver seção "Checklist de trabalho (Word)" abaixo. Isso não é opcional nem depende do Bruno
   pedir de novo; é parte do fluxo padrão desta skill.

## A regra mais importante desta skill — não afrouxar

Separar **apontamento** (algo objetivamente ausente ou quebrado na estrutura) de **opinião
técnica** (um valor de negócio/processo que existe, mas parece questionável). O Bruno e esta
skill são de processos, não especialistas na área fim de cada POP (obra, suprimentos, orçamento
etc.) — então:

- **Sempre aponte**: ausência de estrutura esperada — seção do template sem conteúdo nenhum,
  indicador que não mede o que o próprio POP declara monitorar, ação de desvio que não corrige o
  desvio descrito, papel citado no texto e ausente da tabela de Papéis/Responsabilidades,
  contradição interna (duas seções descrevendo o mesmo passo de forma diferente), referência
  citada e não listada, placeholder não preenchido, numeração de passo com lacuna (ex.: pula do
  passo 3 pro 5), sistema/recurso citado no corpo mas ausente de "Recursos Necessários".
- **Nunca afirme como erro** que um valor técnico/operacional existente está errado no mérito —
  um prazo de execução, uma regra de alçada, um critério de tolerância de estoque/qualidade. Se
  um valor existe mas parece questionável, isso vira **pergunta [C]** para a área confirmar,
  nunca uma afirmação de erro.
- Teste rápido antes de escrever qualquer apontamento: **"isso é ausência de estrutura (aponto)
  ou é o conteúdo técnico de uma estrutura que já existe (pergunto, não afirmo)?"**

## Guarda-corpo — não confundir o template em branco com uma revisão real

Ao revisar POPs de Orçamento nesta sessão, um apontamento quase afirmou "capa desatualizada,
revisão vigente é 01 por Bruno / Carlos Vargas" — mas "Bruno Kawasaki" e "Alessandro Braz, Carlos
Vargas" são só os nomes-placeholder de fábrica do template `PO.GG.QLD.001`, não uma revisão
anterior real. O mesmo vale para "Revisão: 02" e "Status: Aprovado" como valores-padrão do modelo
em branco.

**Antes de apontar "capa desatualizada", "revisão anterior diverge" ou qualquer inconsistência
que dependa de comparar contra uma versão prévia do documento**: confirmar que os valores
"diferentes" não são simplesmente os defaults de fábrica do template `PO.GG.QLD.001` em branco.
Se não houver como confirmar isso com certeza, virar pergunta [C]/[D] em vez de afirmação [E].

## Guarda-corpo — fusão de colunas não é perda de conteúdo

Quando um POP-fonte (pré-transposição) tinha mais colunas do que o template oficial suporta
numa tabela (ex.: "Escalonamento" na tabela de Desvios, ou "Proteção/Retenção/Descarte" na
tabela de Registro), o conteúdo pode ter sido fundido dentro de uma célula vizinha como frase
adicional, em vez de descartado — ver `reference_ooxml_toolkit` na memória do projeto para o
padrão exato usado. **Isso não é um erro de completude** ([E]) por si só; é uma adaptação
esperada. Só apontar como [E]/[C] se a fusão tiver corrompido o texto (frase truncada, dado
sumido de verdade) — comparar com o texto-fonte original quando disponível antes de afirmar.

## O que esta skill não faz (por escopo deliberado, não esquecimento)

- **Não compara POPs "irmãos" entre si por padrão** (ex.: os POPs de Orçamento, ou os de
  Suprimentos/Almoxarifado). Isso pega inconsistências reais entre documentos da mesma família
  (ex.: um documento usando "Objetivo:" e outro "Objetivo –" para a mesma seção-padrão), mas só
  deve ser feito se o Bruno pedir explicitamente e fornecer os documentos a comparar na mesma
  tarefa.
- **Não revisa os templates/modelos padrão em si** (`PO.GG.QLD.001`, `IT.GG.PRO.001`,
  `RE.GG.PRO.001`, ou o próprio QLD.002). Revisão de template é conversa separada com o Bruno e a
  governança do Projeto Next — apontar o problema e perguntar antes de qualquer edição no modelo
  compartilhado (isso já aconteceu nesta sessão: erro de digitação em "papéis, responsabilidades
  e autonomia" só foi corrigido no template depois de confirmação explícita).
- **Não decide se um POP espelhado entre Gadens e Make It é duplicidade.** Documentos espelhados
  entre as duas empresas são intencionais por padrão — nunca sinalizar como redundância sem
  confirmar antes.
- **Não cobre IT nem Regimento.** Regimento tem skill própria (`revisor-regimento-gadens`); IT
  ainda não tem — se o Bruno pedir, é uma skill nova, não uma extensão desta.
- **Não gera POPs novos.** Elaboração a partir de texto bruto é o fluxo `pop_template_workflow`,
  documento diferente deste.

## Formato de saída (chat)

Texto corrido, agrupado por documento — sem tabela nem artifact, a menos que o Bruno peça.

```
### [Código do documento] - [Título curto]

1. [E] Descrição objetiva do erro e onde está. Ação: o que corrigir.
2. [C] Descrição do que precisa confirmação. Pergunta específica para a área.
3. [D] Descrição da lacuna de escopo/decisão. Quem decide.
```

Fechar com uma linha de resumo quando houver mais de um documento: quantos [E], [C], [D], e uma
sugestão de sequência de ataque (ex.: "[E] você resolve direto, [C] vira pauta com a área,
[D] é seu").

## Checklist de trabalho (Word) — sempre gerar

Todo item [C]/[D]/[C/D] vira uma linha no checklist Word, além de aparecer no chat. Use
`scripts/gen_checklist.py` (python-docx, funciona neste ambiente) em vez de escrever o XML na
mão — ele já implementa o formato certo (ver docstring do script para o formato exato: caixa de
seleção + linha em branco com borda para responder). Chame assim:

```bash
python3 scripts/gen_checklist.py --output "<caminho>.docx" --title "Checklist de Correções — <tópico>" --subtitle "<descrição curta do lote>" --data '<json com heading+items por documento>'
```

Ou importe `build_checklist()` diretamente se estiver gerando o conteúdo dentro de outro script
Python. Salve o resultado na mesma pasta de saída que o Bruno já usa para entregáveis (ver
memória `feedback_output_folder` — pasta "Projeto teste", nunca Downloads).

## Ambiente técnico

- **Sem Node.js/npm** — não use `docx`-js.
- **Word COM não é confiável** (`New-Object -ComObject Word.Application` costuma falhar com
  `TYPE_E_CANTLOADLIBRARY`) — não dependa dele para abrir/validar arquivos.
- **`python3`/`python` com `python-docx` funcionam bem** — use para o checklist e para extrair
  texto de um `.docx` existente.
- **Validação**: depois de gerar o Word, confirme integridade fazendo o parse do
  `word/document.xml` extraído do pacote (checagem de XML bem formado), já que abrir no Word de
  verdade pode não estar disponível. Avise o Bruno quando isso acontecer e recomende que ele
  abra o arquivo uma vez antes de circular.
- **Se for corrigir e não só apontar**: nunca deixe arquivos de rascunho (`.txt`, prints
  intermediários) na mesma pasta usada para reempacotar um `.docx` editado — isso corrompe o
  pacote (bug real, já ocorreu 2x nesta sessão). Ver `reference_ooxml_toolkit` na memória do
  projeto.

## Referências

- `references/qld-002.md` — cópia das regras oficiais do PO.GG.QLD.002 relevantes para
  auditoria (código, matriz de aprovação, formatação, controle de revisão), adaptada para POP.
  Se o Bruno avisar que o QLD.002 foi revisado, atualize este arquivo antes de continuar
  revisando documentos — não confie em memória de conversas antigas sobre o que ele dizia.
- `references/pop-checklist.md` — completude estrutural esperada de um POP, seção por seção
  (12 seções), com os pontos específicos a verificar dentro de cada uma.

## O que foi adaptado da ideia original (Fabrício)

A ideia original era uma única skill genérica para POP/IT/Regimento, escrita para o Fabrício,
com output só em texto para colar no Teams. Diferenças desta versão:

- Dividida em skills por tipo de documento (esta cobre só POP) em vez de uma genérica — mais
  fácil de manter o checklist de completude específico de cada tipo sem misturar.
- **Sempre** gera checklist Word além do chat (o Bruno já tinha decidido isso antes desta skill
  existir — não é opcional aqui como seria numa versão genérica).
- Adiciona os dois guarda-corpos acima (template em branco × revisão real; fusão de colunas ×
  perda de conteúdo) — vieram de erros reais cometidos nesta sessão, a ideia original não tinha.
- Sem dependência de `/mnt/user-data/uploads` (convenção do Claude.ai web) — neste ambiente os
  arquivos vêm por caminho local do Windows.
