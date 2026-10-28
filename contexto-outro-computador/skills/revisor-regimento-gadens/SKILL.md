---
name: revisor-regimento-gadens
description: >
  Revisa e audita Regimentos (RE) do Grupo Gadens já elaborados contra o padrão documental
  oficial PO.GG.QLD.002 e contra a estrutura de 9 seções esperada de um Regimento, produzindo
  apontamentos classificados [E]/[C]/[D] e sempre um checklist Word para o Bruno preencher junto.
  Use sempre que o Bruno pedir para revisar, auditar, conferir ou apontar erros/pendências em um
  Regimento, mesmo que ele não use essas palavras exatas — por exemplo "dá uma olhada nesse
  Regimento", "tá certo isso?", "compara com o QLD.002", ou anexar um arquivo RE.xx.xxx.xxx
  pedindo para conferir. Também use quando ele quiser comparar um Regimento contra o template
  RE.GG.PRO.001 ou contra as regras do QLD.002. NÃO use para gerar um Regimento novo a partir de
  texto bruto (isso é o workflow de elaboração — ver memória pop_template_workflow / regimento
  do Bruno), NÃO use para POP ou IT (fora de escopo desta skill), e NÃO use para revisar os
  próprios templates/modelos padrão (RE.GG.PRO.001, PO.GG.QLD.001, IT.GG.PRO.001) ou o QLD.002
  em si — isso é conversa de governança, não auditoria de documento de processo.
license: Uso pessoal — Bruno Kawasaki, Grupo Gadens / Projeto Next
---

# Revisor de Regimentos — Grupo Gadens

Audita um Regimento (RE) do Grupo Gadens já elaborado contra o padrão documental oficial e
contra a estrutura esperada do tipo. Produz uma lista de apontamentos classificados por
prioridade/natureza, e **sempre** um documento Word em formato de checklist para trabalhar as
pendências — não só quando pedido.

Esta skill nasceu de uma ideia de um colega do Bruno no Projeto Next (Fabrício), que tinha uma
skill parecida mas genérica para POP/IT/Regimento. Esta versão é focada só em Regimento, e
adiciona um guarda-corpo importante que a original não tinha (ver seção "Guarda-corpo" abaixo).

## Antes de começar

1. **Não presuma que o arquivo já está no contexto.** Se o Bruno mencionar um Regimento sem
   anexá-lo, pergunte por ele ou procure no diretório de trabalho recente. Nunca revise de
   memória — use o arquivo real.
2. **Confirme que é mesmo um Regimento** pelo código (prefixo `RE.`) ou pelo conteúdo (pauta de
   reunião deliberativa, envolvidos/entradas/saídas). Se for um POP ou uma IT, avise o Bruno que
   esta skill está escopada só para Regimento e pergunte se ele quer seguir mesmo assim sem o
   apoio da skill, ou se prefere que você aplique o mesmo raciocínio manualmente.
3. Carregue `references/qld-002.md` (checagens formais, valem para o código/capa/formatação de
   qualquer documento) e `references/regimento-checklist.md` (completude estrutural específica
   de Regimento) antes de revisar.
4. Se vier mais de um Regimento na mesma mensagem, revise cada um separadamente — **sem
   comparação cruzada entre eles por padrão** (ver "O que esta skill não faz").

## Fluxo de revisão

1. **Ler o documento por inteiro.** Para `.docx`, extrair também cabeçalho e rodapé — eles
   guardam código, revisão e data que costumam divergir da capa ou do corpo. Sem Word COM
   confiável neste ambiente (ver "Ambiente técnico" abaixo), extraia via unzip + parse do
   `word/document.xml`, ou com `python-docx` iterando parágrafos/tabelas.
2. **Rodar a checagem formal** de `references/qld-002.md`: estrutura do código, esteira/matriz
   de aprovação, capa × cabeçalho × rodapé, placeholders não preenchidos, formatação (Tabela 5).
3. **Rodar o checklist de completude de Regimento** de `references/regimento-checklist.md`: as
   9 seções esperadas, e o que cada uma precisa conter para estar completa.
4. **Classificar cada achado:**
   - **[E]** erro objetivo — corrige direto, não depende de decisão de ninguém.
   - **[C]** conteúdo — precisa de confirmação da área responsável pelo processo/comitê.
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
técnica** (um valor de negócio que existe, mas parece questionável). O Bruno e esta skill são de
processos, não especialistas no mérito de cada comitê — então:

- **Sempre aponte**: ausência de estrutura esperada — quórum não definido, participantes
  obrigatórios não listados, regra de deliberação ausente, consequência de reunião não
  realizada não tratada, prazo/local de armazenamento de ata ausente, indicador/coluna que não
  cobre o que o próprio documento declara, papel citado no texto e ausente da tabela de
  responsabilidades, contradição interna (duas seções descrevendo o mesmo fluxo de forma
  diferente), referência citada e não listada, placeholder não preenchido, numeração de seção
  incoerente com o conteúdo, frase quebrada/sem sentido gramatical.
- **Nunca afirme como erro** que um valor técnico/de negócio existente está errado no mérito —
  um prazo de convocação, um formato de reunião, uma regra de periodicidade. Se um valor existe
  mas parece questionável, isso vira **pergunta [C]** para a área confirmar, nunca uma
  afirmação de erro.
- Teste rápido antes de escrever qualquer apontamento: **"isso é ausência de estrutura (aponto)
  ou é o conteúdo técnico de uma estrutura que já existe (pergunto, não afirmo)?"**

## Guarda-corpo — não confundir o template em branco com uma revisão real

Isso é o que diferencia esta skill da ideia original do Fabrício, e nasceu de um erro real: ao
revisar POPs de Orçamento nesta sessão, um apontamento afirmou "capa desatualizada, revisão
vigente é 01 por Bruno / Carlos Vargas" — mas "Bruno Kawasaki" e "Alessandro Braz, Carlos
Vargas" são só os nomes-placeholder de fábrica do template, não uma revisão anterior real. O
mesmo vale para "Revisão: 02" e "Status: Aprovado" como valores-padrão do modelo em branco.

**Antes de apontar "capa desatualizada", "revisão anterior diverge" ou qualquer inconsistência
que dependa de comparar contra uma versão prévia do documento**: confirmar que os valores
"diferentes" não são simplesmente os defaults de fábrica do template RE.GG.PRO.001 em branco.
Se não houver como confirmar isso com certeza, virar pergunta [C]/[D] em vez de afirmação [E].

## O que esta skill não faz (por escopo deliberado, não esquecimento)

- **Não compara Regimentos "irmãos" entre si por padrão** (ex.: os 5 Regimentos de comitê de
  fase — Due Diligence, Estudo Preliminar, Anteprojeto, Pré-executivo, Executivo). Isso pega
  inconsistências reais entre documentos da mesma família, mas só deve ser feito se o Bruno
  pedir explicitamente e fornecer os documentos a comparar na mesma tarefa.
- **Não revisa os templates/modelos padrão em si** (RE.GG.PRO.001, PO.GG.QLD.001,
  IT.GG.PRO.001, ou o próprio QLD.002). Revisão de template é conversa separada com o Bruno e a
  governança do Projeto Next.
- **Não decide se um Regimento espelhado entre Gadens e Make It é duplicidade.** Documentos
  espelhados entre as duas empresas são intencionais por padrão — nunca sinalizar como
  redundância sem confirmar antes.
- **Não cobre POP nem IT.** Se o Bruno quiser o mesmo tipo de revisão para esses tipos, é uma
  skill separada (fora do escopo desta).
- **Não gera Regimentos novos.** Elaboração a partir de texto bruto é um fluxo diferente.

## Formato de saída (chat)

Texto corrido, agrupado por documento — sem tabela nem artifact, a menos que o Bruno peça.

```
### [Código do documento] - [Título curto]

1. [E] Descrição objetiva do erro e onde está. Ação: o que corrigir.
2. [C] Descrição do que precisa confirmação. Pergunta específica para a área.
3. [D] Descrição da lacuna de escopo/decisão. Quem decide.
```

Fechar com uma linha de resumo quando houver mais de um documento: quantos [E], [C], [D], e uma
sugestão de sequência de ataque (ex.: "[E] você resolve direto, [C] vira pauta com o comitê,
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

## Referências

- `references/qld-002.md` — cópia das regras oficiais do PO.GG.QLD.002 relevantes para
  auditoria (código, matriz de aprovação, formatação, controle de revisão). Se o Bruno avisar
  que o QLD.002 foi revisado, atualize este arquivo antes de continuar revisando documentos —
  não confie em memória de conversas antigas sobre o que ele dizia.
- `references/regimento-checklist.md` — completude estrutural esperada de um Regimento, seção
  por seção, com os pontos específicos a verificar dentro de cada uma.
