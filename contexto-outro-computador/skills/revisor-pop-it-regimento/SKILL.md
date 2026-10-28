---
name: revisor-pop-it-regimento
description: >
  Revisa e audita POPs, Instruções de Trabalho (IT) e Regimentos (RE) do Grupo Gadens já
  elaborados contra o padrão documental oficial PO.GG.QLD.002 e contra a estrutura de completude
  esperada de cada tipo (12 seções para POP, 6 para IT, 9 para Regimento), produzindo apontamentos
  classificados [E]/[C]/[D] e sempre um checklist Word para o Bruno preencher junto. Use sempre que
  o Bruno pedir para revisar, auditar, conferir ou apontar erros/pendências em um POP, IT ou
  Regimento, mesmo que ele não use essas palavras exatas — por exemplo "dá uma olhada nesse
  documento", "tá certo isso?", "compara com o QLD.002", ou anexar um arquivo PO.xx.xxx.xxx /
  IT.xx.xxx.xxx / RE.xx.xxx.xxx pedindo para conferir. Também use quando ele quiser comparar um
  documento contra o template oficial do tipo (PO.GG.QLD.001, IT.GG.PRO.001, RE.GG.PRO.001) ou
  contra as regras do QLD.002. NÃO use para gerar um documento novo a partir de texto bruto (isso
  é o workflow de elaboração — ver memórias pop_template_workflow / pop_it_template_workflow /
  regimento_template_workflow), e NÃO use para revisar os próprios templates/modelos padrão ou o
  QLD.002 em si — isso é conversa de governança, não auditoria de documento de processo.
license: Uso pessoal — Bruno Kawasaki, Grupo Gadens / Projeto Next
---

# Revisor de POPs, ITs e Regimentos — Grupo Gadens

Audita um documento de processo (POP, IT ou Regimento) do Grupo Gadens já elaborado contra o
padrão documental oficial e contra a estrutura esperada do tipo. Produz uma lista de apontamentos
classificados por natureza, e **sempre** um documento Word em formato de checklist para trabalhar
as pendências — não só quando pedido.

Esta skill nasceu de uma ideia de um colega do Bruno no Projeto Next (Fabrício), que tinha uma
skill genérica para POP/IT/Regimento em um único arquivo, escrita para o fluxo de trabalho dele.
Esta versão unifica os três tipos como a original, mas adaptada ao ambiente e aos hábitos de
trabalho do Bruno — ver "O que foi adaptado da ideia original" no fim deste arquivo. Ela consolida
o que antes eram duas skills separadas (`revisor-pop-gadens`, `revisor-regimento-gadens`) mais a
cobertura de IT que ainda não existia.

## Antes de começar

1. **Não presuma que o arquivo já está no contexto.** Se o Bruno mencionar um documento sem
   anexá-lo, pergunte por ele ou procure no diretório de trabalho recente. Nunca revise de
   memória — use o arquivo real.
2. **Carregue sempre `references/qld-002.md` e `references/templates.md`.** O primeiro são as
   regras oficiais, extraídas do PDF real (Rev. 02); o segundo é a estrutura exata dos três
   modelos padrão, com os textos de fábrica de cada seção. Valem para os três tipos.
3. **Identifique o tipo pelo código do documento** (prefixo `PO.` / `IT.` / `RE.`) ou pelo
   conteúdo, e carregue o checklist de completude correspondente:
   - **POP** → `references/pop-checklist.md` (12 seções)
   - **IT** → `references/it-checklist.md` (6 seções)
   - **Regimento** → `references/regimento-checklist.md` (9 seções)
4. Se não conseguir identificar o tipo com confiança, pergunte ao Bruno em vez de adivinhar.
5. Se vier mais de um documento na mesma mensagem, revise cada um separadamente — **sem
   comparação cruzada entre eles por padrão** (ver "O que esta skill não faz").

## Fluxo de revisão

1. **Ler o documento por inteiro.** Para `.docx`, extrair também cabeçalho e rodapé — eles
   guardam código, revisão e data que costumam divergir da capa ou do corpo. Sem Word COM
   confiável neste ambiente (ver "Ambiente técnico" abaixo), extraia via unzip + parse do
   `word/document.xml`, ou com `python-docx` iterando parágrafos/tabelas.
2. **ENTENDER O PROCESSO — antes de conferir qualquer coisa.** Instrução direta do Bruno em
   2026-08-26: *"quero que além de checagem de requisitos, você realmente analise o texto e
   entenda"*. Este passo não é opcional e não é retórica; é o que separa uma revisão útil de uma
   conferência de formulário.

   Depois de ler o documento e antes de escrever qualquer apontamento, responder para si mesmo,
   em texto corrido (não vai para a saída):

   - **O que este processo entrega, e para quem?**
   - **Quem faz o quê, em que ordem?** Seguir o fluxo como se fosse executá-lo.
   - **Se alguém seguisse este documento ao pé da letra, o que daria errado?**
   - **Onde isso quebra na vida real?** Material que chega errado, ferramenta que não volta, nota
     que chega depois do fechamento.

   Só depois disso rodar as checagens. **Todo apontamento tem que se conectar a esse
   entendimento.** Teste antes de escrever cada um: *se eu mostrar isso a quem executa o processo,
   ele reconhece como problema?* Se a resposta for "não, mas está diferente do checklist", o
   apontamento não existe — apagar.

   **O que só aparece entendendo, e nenhum checklist pega** (todos achados reais deste lote):

   - O SUP.010 existe para padronizar a descrição dos itens, e o padrão de descrição não está em
     lugar nenhum do documento. Cada seção, isolada, parecia completa.
   - O SUP.013 prevê o desvio "divergência entre pedido e nota fiscal", mas nenhum passo compara
     os dois. O documento monitora um problema que ele mesmo não consegue enxergar.
   - O SUP.011 promete reduzir extravios e não define prazo de devolução. Sem prazo, não existe o
     momento em que a ferramenta passa a ser considerada extraviada.
   - O SUP.008 manda confirmar a data com o fornecedor antes de verificar se há espaço para
     receber.

   **E o inverso: entender evita o apontamento burro.** Os sete erros do `nao-apontar.md` saíram
   todos de eu conferir campo em vez de entender processo — ferramenta fica no almoxarifado,
   cadastrar implica manter, e-mail é ferramenta e produto ao mesmo tempo. Nenhum deles teria sido
   escrito se eu tivesse lido o processo como processo.

3. **Rodar `scripts/checagem_mecanica.py`.** Ele faz as
   conferências que não exigem julgamento e que a leitura à mão erra de vez em quando:
   pontuação final dos passos, célula sem ponto, vírgula depois de "contendo"/"após", formas
   verbais misturadas, voz passiva, parêntese aberto, sobras do modelo, capa × rodapé, matriz de
   papéis (onde cada um aparece e onde falta), grafias divergentes, desvio circular, coluna sem
   variação, contradição em Indicadores, definições quase idênticas, estilo de lista divergente.

   ```bash
   python3 scripts/checagem_mecanica.py --pasta "<pasta>"
   python3 scripts/checagem_mecanica.py "<arquivo.docx>" ["<outro.docx>" ...]
   ```

   Ele só lê, nunca altera. **Motivo de existir:** em duas rodadas seguidas a revisão à mão
   falhou exatamente nessas conferências — regra escrita e não aplicada, ou aplicada num
   documento e não no seguinte (ver "Segunda rodada de absorção" no fim deste arquivo). O que o
   programa entrega pronto libera a leitura para o que exige pensar: ordem dos passos, desvios
   que faltam, definição que não combina com o termo. **Ele não substitui nada disso** — os
   passos 4 a 9 continuam obrigatórios.
4. **Rodar a checagem formal** de `references/qld-002.md`: estrutura do código,
   esteira/matriz de aprovação, capa × cabeçalho × rodapé, placeholders não preenchidos,
   formatação (Tabela 5).
5. **Rodar o checklist de completude** do tipo (`pop-checklist.md`, `it-checklist.md` ou
   `regimento-checklist.md`): as seções esperadas, e o que cada uma precisa conter para estar
   completa.
6. **Rodar as checagens de coerência interna** de `references/coerencia-interna.md` — resíduo de
   instrução de preenchimento, contradição interna dentro de uma seção, consistência de termos/
   papéis nas duas direções (inclusive grafias divergentes do mesmo papel), colunas que não
   discriminam nada, e redação/gramática básica. **Não são opcionais** — nasceram de uma lacuna
   real desta skill detectada numa revisão paralela (ver arquivo para o histórico). Também vale
   ser mais generoso com perguntas [C] de aprofundamento de processo (ver nota no fim daquele
   arquivo). Inclui os cruzamentos de capa × rodapé e da cadeia de aprovação (seção 6).
7. **Ler os passos como fluxo**, não como lista — `references/fluxo-e-desvios.md`: a ordem dos
   passos faz sentido? todo ramo condicional chega a algum lugar? o fluxo tem saída? o executor
   nomeado em cada passo é quem realmente faz aquilo? quais desvios prováveis derivam dos passos e
   não estão na tabela de Desvios? o Registro bate com o que os passos produzem? **Também não é
   opcional** — é a categoria que produz os achados mais caros e a que faltava inteira até
   2026-08-25.
8. **Filtrar por `references/nao-apontar.md`.** São as decisões do Bruno sobre o que **não** é
   apontamento, tiradas de devolutivas reais dele. Várias anulam checagens dos arquivos
   anteriores — por exemplo, papel ausente da tabela de Definições não é erro, porque aquela
   tabela é de siglas e termos, não de cargos. Item que cair numa dessas regras se **apaga**, não
   se rebaixa de [E] para [C]. Quando o Bruno explicar numa devolutiva por que algo não é
   apontamento, **acrescentar a regra nesse arquivo**.
9. **Classificar cada achado:**
   - **[E]** erro objetivo — corrige direto, não depende de decisão de ninguém.
   - **[C]** conteúdo — precisa de confirmação da área responsável pelo processo/comitê.
   - **[D]** decisão — é escopo/padrão do projeto, não erro de quem escreveu; cabe ao Bruno ou
     à governança do Projeto Next decidir.
   - Se genuinamente não der para saber se é [C] ou [D], marcar **[C/D]** e escrever uma frase
     curta explicando a hesitação. Não travar a revisão por causa disso.
10. **GERAR O CHECKLIST WORD — antes de escrever a resposta no chat.** Cobrindo todo item
    [C]/[D]/[C/D], mais um bloco final registrando o que foi corrigido e o que o programa acusou
    mas foi descartado de propósito. Ver "Checklist de trabalho (Word)" abaixo.

    **A ordem importa e é o conserto de um erro real.** A regra "sempre gerar o checklist" já
    existia aqui como último passo, e mesmo assim foi esquecida — o Bruno teve que cobrar
    (2026-08-31). O motivo: depois de escrever um resumo longo no chat, a resposta já parece
    entregue, e o checklist vira apêndice que se perde. **Gerando primeiro, o texto do chat vira
    o resumo de um entregável que já existe, em vez de substituto dele.**

    Se a revisão não produziu nenhum item [C]/[D], dizer isso explicitamente no chat em vez de
    simplesmente não gerar nada.
11. **Escrever a resposta no chat**, no formato da seção "Formato de saída (chat)" abaixo,
    fechando com o caminho do checklist gerado.

## As duas regras que não se afrouxam

**A primeira é entender antes de conferir** (passo 2 do fluxo). Checklist é rede de segurança,
não é o trabalho. Apontamento que só existe porque um campo não bate com uma lista, e que não
significa nada para quem executa o processo, não é apontamento.

**A segunda** separa **apontamento** (algo objetivamente ausente ou quebrado na estrutura) de **opinião
técnica** (um valor de negócio/processo que existe, mas parece questionável). O Bruno e esta
skill são de processos, não especialistas na área fim de cada documento (obra, suprimentos,
orçamento, comitês etc.) — então:

- **Sempre aponte**: ausência de estrutura esperada — seção do template sem conteúdo nenhum,
  indicador que não mede o que o próprio documento declara monitorar, ação de desvio que não
  corrige o desvio descrito, papel citado no texto e ausente da tabela de Papéis/Responsabilidades
  ou de Definições, contradição interna (duas seções descrevendo o mesmo passo/fluxo de forma
  diferente), referência citada e não listada, placeholder não preenchido, numeração de passo/
  seção com lacuna, sistema/recurso citado no corpo mas ausente da seção correspondente.
- **Nunca afirme como erro** que um valor técnico/operacional existente está errado no mérito —
  um prazo de execução, uma regra de alçada, um critério de tolerância de engenharia/estoque/
  qualidade, uma técnica de execução descrita numa IT. Se um valor existe mas parece
  questionável, isso vira **pergunta [C]** para a área confirmar, nunca uma afirmação de erro.
- Teste rápido antes de escrever qualquer apontamento: **"isso é ausência de estrutura (aponto)
  ou é o conteúdo técnico de uma estrutura que já existe (pergunto, não afirmo)?"**
- **Cuidado especial com IT**: não apontar como [E] a ausência de seções que uma IT genuinamente
  não tem (Recursos Necessários, Papéis e Responsabilidades, Indicadores, Pontos Críticos,
  Desvios/Ações, Registro do Processo — essas são seções de POP). A estrutura de 6 seções da IT é
  mais enxuta por desenho, não por lacuna — ver `references/it-checklist.md`.

## Guarda-corpo — não confundir o template em branco com uma revisão real

Ao revisar POPs de Orçamento em sessão anterior, um apontamento quase afirmou "capa desatualizada,
revisão vigente é 01 por Bruno / Carlos Vargas" — mas esses nomes são só o placeholder de fábrica
dos modelos, não uma revisão anterior real.

**Valores de fábrica conferidos nos modelos reais em 2026-08-26** (lista completa em
`references/templates.md`): Elaborador `Bruno Kawasaki`, Aprovador `Carlos Vargas`,
Revisão `00`, Status `Aprovado`, Empresas abrangidas `GRUPO GADENS`, título
`TÍTULO DE ...`. Nada disso é evidência de revisão anterior.

Duas correções à versão antiga desta seção, que trazia valores errados de memória:
o Aprovador de fábrica é **`Carlos Vargas` sozinho** (`Alessandro Braz, Carlos Vargas` é o
aprovador do próprio QLD.002, não dos modelos), e a Revisão de fábrica é **`00`**, não `02`.
E o campo "Tipo de documento" de fábrica no modelo de POP é **`Procedimento Operacional Padrão`**,
com "Padrão" — logo, um POP cuja capa traga só "Procedimento Operacional" **não** herdou isso do
modelo, e a divergência com o rodapé é [E] real.

**Antes de apontar "capa desatualizada", "revisão anterior diverge" ou qualquer inconsistência
que dependa de comparar contra uma versão prévia do documento**: confirmar que os valores
"diferentes" não são simplesmente os defaults de fábrica do template em branco correspondente ao
tipo. Se não houver como confirmar isso com certeza, virar pergunta [C]/[D] em vez de afirmação [E].

### Limite de escopo deste guarda-corpo — não aplicar largo demais

Ele vale **só** para comparações contra uma suposta versão anterior do documento. **Não** vale
para inconsistência interna entre dois lugares do mesmo arquivo. Se a capa diz "Procedimento
Operacional" e o rodapé diz "Procedimento Operacional Padrão", isso é divergência capa × rodapé —
apontamento **[E]** normal, por documento, exatamente como manda o checklist formal do
`qld-002-<tipo>.md`. Não importa se o valor divergente veio do template: o documento que vai
circular está internamente incoerente, e quem lê vê os dois.

Erro real já cometido (2026-08-25, lote SUP): a divergência capa × rodapé de "Tipo de documento"
foi rebaixada de [E] para uma nota [D] de lote com a justificativa "parece texto de fábrica do
template". O dado estava na mão e foi desclassificado por aplicar este guarda-corpo fora do
escopo dele. **Na dúvida sobre qual dos dois valores é o certo**, o apontamento continua [E]
(a incoerência é objetiva) e a pergunta sobre qual valor prevalece vira um [C]/[D] separado.

## Guarda-corpo — fusão de colunas não é perda de conteúdo

Quando um documento-fonte (pré-transposição) tinha mais colunas do que o template oficial suporta
numa tabela (ex.: "Escalonamento" na tabela de Desvios de um POP, ou "Proteção/Retenção/Descarte"
na tabela de Registro), o conteúdo pode ter sido fundido dentro de uma célula vizinha como frase
adicional, em vez de descartado — ver `reference_ooxml_toolkit` na memória do projeto para o
padrão exato usado. **Isso não é um erro de completude** ([E]) por si só; é uma adaptação
esperada. Só apontar como [E]/[C] se a fusão tiver corrompido o texto (frase truncada, dado
sumido de verdade) — comparar com o texto-fonte original quando disponível antes de afirmar.

### Limite de escopo deste guarda-corpo — protege a forma, não o conteúdo

"A fusão não é defeito estrutural" **não** significa "não preciso ler o texto fundido". O texto
que foi fundido dentro da célula vizinha é conteúdo do documento como qualquer outro e passa por
todas as checagens normais: vaguidade, referência não resolvida, contradição, redação.

Erro real já cometido (2026-08-25, lote SUP): a célula de Armazenamento traz "Retenção: Conforme
política interna. Descarte: Conforme política interna." — **qual** política interna? É uma
referência a um documento que não é nomeado nem consta em Referências, ou seja, um [C] legítimo.
Ele passou batido porque este guarda-corpo foi lido como permissão para pular a leitura daquele
texto. Sempre ler o conteúdo fundido; o guarda-corpo só impede de apontar a *fusão em si* como
perda de conteúdo.

## O que esta skill não faz (por escopo deliberado, não esquecimento)

- **Não compara documentos "irmãos" entre si por padrão** (ex.: os 5 Regimentos de comitê de
  fase, os POPs de Orçamento/Suprimentos, ITs do mesmo POP-mãe). Isso pega inconsistências reais
  entre documentos da mesma família, mas só deve ser feito se o Bruno pedir explicitamente e
  fornecer os documentos a comparar na mesma tarefa.

  **Exceção (2026-08-26): contradição de controle sobre o mesmo evento sempre vale.** Quando dois
  documentos do lote descrevem **o mesmo momento físico** e exigem **controles diferentes**, isso
  é apontamento [C] mesmo sem pedido de comparação. A regra acima existe para evitar ruído de
  estilo ("um escreve 'Objetivo:' e outro 'Objetivo –'"), não para calar risco operacional.

  Exemplo real: o SUP.007 manda "coletar assinatura do responsável pela retirada" na saída de
  material; o SUP.009 descreve a mesma entrega como "o material é entregue ao solicitante", sem
  assinatura nenhuma. O mesmo almoxarife, no mesmo balcão, colhe ou não colhe assinatura conforme
  o POP que ler. O documento irmão aqui é **evidência** da lacuna, não o objeto da comparação.

  Teste para separar os dois casos: a diferença muda **o que alguém tem que fazer ou provar**?
  Se sim, aponta. Se só muda a forma de escrever, cala (ou vira [D] de padronização).
- **Não revisa os templates/modelos padrão em si** (`PO.GG.QLD.001`, `IT.GG.PRO.001`,
  `RE.GG.PRO.001`, ou o próprio QLD.002). Revisão de template é conversa separada com o Bruno e a
  governança do Projeto Next — apontar o problema e perguntar antes de qualquer edição no modelo
  compartilhado.
- **Não decide se um documento espelhado entre Gadens e Make It é duplicidade.** Documentos
  espelhados entre as duas empresas são intencionais por padrão — nunca sinalizar como
  redundância sem confirmar antes.
- **Não gera documentos novos.** Elaboração a partir de texto bruto é um fluxo diferente
  (`pop_template_workflow` / `pop_it_template_workflow` / `regimento_template_workflow`).

## Granularidade — um achado por lacuna, nunca agregado

Um apontamento que junta várias lacunas numa frase vira uma correção vaga; separado, vira várias
correções executáveis. **Sempre desdobrar por item concreto**, mesmo que a causa-raiz seja a mesma.

Errado (agregado): "Papéis-chave lista 4 papéis, mas a Tabela 2 só tem 1."
Certo (desdobrado, um por papel órfão, cada um com a sua lacuna específica):
- "Solicitante" está definido na Tabela 1 e listado em Papéis-chave, mas não aparece em nenhum
  passo da seção 6 nem tem linha na Tabela 2.
- "Comprador" é acionado no passo 2, mas não tem linha na Tabela 2 **nem consta nas Definições**.
- "Supervisor de Almoxarife" é declarado como decisão final, aprova no passo 2 e valida o desvio
  da Tabela 3, mas não tem linha na Tabela 2, não está nas Definições, e aparece em três grafias.

O caso acima é real (SUP.008, 2026-08-25): a versão agregada virou 1 achado; a desdobrada virou 3,
e ao desdobrar apareceram duas lacunas que a agregação tinha escondido (Comprador ausente também
das Definições; terceira grafia do Supervisor). **Agregar não é resumir, é perder achado.**

Vale para tudo, não só papéis: uma grafia inconsistente e uma ausência de tabela são dois defeitos
distintos do mesmo papel e rendem dois itens.

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

## Corrigir os documentos — `scripts/aplicar_correcoes.py`

Quando o Bruno pedir para **corrigir** (não só apontar), usar este script em vez de editar à mão.
Ele faz só o que não depende de resposta de ninguém: erro de digitação, vírgula, concordância,
voz passiva, grafia de papel, sobra de texto do modelo, campo da capa, pontuação dos passos,
ponto final em célula de tabela, estilo de lista.

```bash
python3 scripts/aplicar_correcoes.py --simular          # mostra sem gravar
python3 scripts/aplicar_correcoes.py --aplicar
python3 scripts/aplicar_correcoes.py --aplicar --so "SUP.009"
```

Trabalha numa cópia, valida o XML e só então substitui o original; se algo falhar, o original
fica intacto. **Sempre rodar `--simular` primeiro** e fazer backup dos originais antes.

Duas coisas que ele **não** faz, de propósito: não mexe em "Não especificado no texto de origem"
(o texto que entra ali depende da área) e não preenche seção vazia.

A tabela `CORRECOES` no topo do arquivo é por documento — ao corrigir um lote novo, acrescentar
as entradas dele ali. Cuidado conhecido: texto que o Word quebrou em vários pedaços não é achado
por busca literal; use `troca_no_xml()` para cabeçalho/rodapé, que já trata isso (foi assim que o
`9001:20/15` do SUP.013 escapou na primeira rodada).

## Acrescentar itens a um checklist em uso — `scripts/acrescentar_itens.py`

**Nunca regerar do zero um checklist que o Bruno já começou a preencher** — isso apaga as
respostas que ele escreveu nas linhas em branco. Para incluir itens novos:

```bash
python3 scripts/acrescentar_itens.py --arquivo "<checklist.docx>" --novos novos.json --simular
python3 scripts/acrescentar_itens.py --arquivo "<checklist.docx>" --novos novos.json
```

`novos.json` é `{"PO.GG.SUP.006": ["item novo", ...], ...}`. O script descobre o que já existe,
insere só o que falta no fim do bloco de cada documento, copia a formatação de um item existente
e guarda uma cópia do arquivo anterior.

Se o arquivo estiver aberto no Word, a gravação falha com `PermissionError` — pedir para o Bruno
fechar. Para apenas **ler** um arquivo aberto, copiar para uma pasta temporária antes.

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
  pacote. Ver `reference_ooxml_toolkit` na memória do projeto.

## Referências

- `references/qld-002.md` — as regras oficiais do PO.GG.QLD.002, extraídas do PDF real em
  2026-08-26 (Rev. 02). Traz uma seção **"O que o QLD.002 NÃO define"** — ler antes de apontar
  qualquer coisa como violação da norma, porque as versões anteriores desta skill apresentavam
  como regra oficial várias coisas que não estão lá. Se o Bruno avisar que o QLD.002 foi
  revisado, reextrair do PDF.
- `references/templates.md` — estrutura exata dos três modelos padrão e os textos de fábrica de
  cada seção, mais as divergências conhecidas entre modelo e QLD.002 e os defeitos dos próprios
  modelos.
- `references/pop-checklist.md` — completude estrutural de POP, 12 seções.
- `references/it-checklist.md` — completude estrutural de IT, 6 seções.
- `references/regimento-checklist.md` — completude estrutural de Regimento, 9 seções.
- `references/coerencia-interna.md` — checagens de coerência interna válidas para os três tipos
  (resíduo de instrução de preenchimento, contradição interna de seção, consistência de termos/
  papéis nas duas direções, colunas que não discriminam nada, redação básica, cruzamentos de
  capa × rodapé e da cadeia de aprovação). Sempre rodar, não é opcional — ver o arquivo para o
  histórico de por que foi criado.
- `references/nao-apontar.md` — o que o Bruno já decidiu que **não** é apontamento, com as
  palavras dele e o caso concreto. Ler antes de fechar a lista; cancela regras dos outros
  arquivos quando houver conflito, porque é decisão dele e não inferência minha.
- `references/fluxo-e-desvios.md` — leitura dos passos como cadeia causal, válida para os três
  tipos (ordem dos passos, ramos que morrem, fluxo sem saída, executor nomeado × executor real,
  desvios derivados dos passos, Registro × saídas dos passos). Sempre rodar, não é opcional.

## O que foi adaptado da ideia original (Fabrício)

A ideia original era uma única skill genérica para POP/IT/Regimento, escrita para o Fabrício,
com output só em texto para colar no Teams e um único `qld-002.md` compartilhado entre os três
tipos. Diferenças desta versão:

- **Sempre** gera checklist Word além do chat (decisão do Bruno anterior a esta skill — não é
  opcional aqui como seria numa versão genérica).
- `qld-002.md` foi desdobrado em três arquivos adaptados por tipo (`-pop`, `-it`, `-regimento`)
  em vez de um único genérico — cada tipo tem observações e exemplos próprios (ex.: formato da
  coluna "Etapa" no Controle de Emissão diverge entre POP e IT) que ficariam confusos misturados.
- Adiciona os guarda-corpos de "template em branco × revisão real" e "fusão de colunas × perda de
  conteúdo" — vieram de erros reais cometidos em sessões anteriores, a ideia original não tinha.
- Adiciona o cuidado explícito de não tratar a estrutura mais enxuta da IT (6 seções) como lacuna
  em relação à estrutura do POP (12 seções) — são tipos de documento diferentes por desenho.
- Sem dependência de `/mnt/user-data/uploads` (convenção do Claude.ai web) — neste ambiente os
  arquivos vêm por caminho local do Windows.

**Atualização 2026-08-25:** uma revisão paralela feita por um colega do Bruno (usando uma versão
mais completa/manual do mesmo tipo de auditoria) sobre o mesmo lote de POPs de Suprimentos
encontrou muito mais apontamentos do que esta skill — a comparação revelou 5 categorias de defeito
que o checklist original não cobria (resíduo de instrução de preenchimento, contradição interna de
seção, consistência de termos/papéis nas duas direções, colunas que não discriminam nada, redação
básica). Essas 5 categorias foram formalizadas em `references/coerencia-interna.md` e são agora
parte obrigatória do fluxo de revisão (ver "Fluxo de revisão" acima). Um dos apontamentos da outra
revisão (código "FL" não constar na tipologia do QLD.002) parecia incorreto contra a cópia de
QLD.002 desta skill (que já lista "FL | Fluxogramas" na Tabela 2) — vale confirmar qual versão do
QLD.002 foi usada do outro lado antes de tratar isso como pendência real.

**Segunda rodada de absorção (2026-08-25, mesmo dia):** uma terceira revisão paralela, desta vez
de um único documento a fundo (SUP.008), expôs mais cinco causas de falha — duas delas
autoinfligidas, que são as mais graves porque faziam esta skill **descartar achado que já tinha na
mão**:

1. **Guarda-corpo de "template em branco" aplicado largo demais** — rebaixava divergência interna
   capa × rodapé de [E] para nota [D], com a justificativa de que o valor vinha do template. Ver o
   limite de escopo agora escrito na seção daquele guarda-corpo.
2. **Guarda-corpo de "fusão de colunas" aplicado largo demais** — virava permissão para não ler o
   texto fundido, perdendo lacunas de conteúdo dentro dele. Idem.
3. **Faltava a leitura do processo como cadeia causal** → `references/fluxo-e-desvios.md` (novo).
4. **Faltavam dois cruzamentos** (capa × rodapé campo a campo; Aprovador da capa × último evento
   datado do Controle de Emissão) → seção 6 de `references/coerencia-interna.md`.
5. **Achados agregados em vez de desdobrados por lacuna** → seção "Granularidade" acima.

Lição transversal das duas rodadas: quando uma revisão paralela encontra mais, o motivo raramente
é "olhou com mais atenção" — é uma categoria de checagem ausente ou uma regra própria aplicada
fora do escopo. Vale sempre mapear a causa antes de reescrever o checklist.
