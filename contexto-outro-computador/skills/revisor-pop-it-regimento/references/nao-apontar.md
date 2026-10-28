# O que NÃO apontar — decisões do Bruno

Cada regra aqui saiu de uma devolutiva real: eu apontei, o Bruno explicou por que não era
apontamento, e a explicação vale para os próximos documentos. **Ler antes de escrever
apontamento** — várias destas anulam checagens que os outros arquivos de referência mandam fazer.

Origem: devolutiva do checklist dos 9 POPs de Suprimentos, 2026-08-26.

---

## 1. A tabela de Definições é de siglas e termos, não de cargos

**Não apontar** "papel X não está na Tabela 1". A Tabela 1 (Siglas e definições) existe para termos
técnicos, siglas e abreviaturas — não para catalogar quem é quem.

Palavras do Bruno: *"Tabela de definições sem necessidade de complementar com esses cargos, visto
que estão explícitos no documento suas funções"* e *"Sem necessidade, tendo em vista ser tabela de
termos e siglas"*.

Um papel pode estar definido ali quando o autor achou útil, mas a **ausência nunca é erro**. Isso
anula a regra 4 do `pop-checklist.md` quando o termo faltante é um cargo — continua valendo para
sigla de sistema, material ou documento.

## 2. Aplicação em formato aberto pode ser intencional

**Não apontar como erro** a seção 2 escrita como "Todos os colaboradores do Grupo Gadens
autorizados a X" em vez de "Empresa: X. Setores envolvidos: Y."

Palavras do Bruno: *"A intenção do autor foi deixar aberta a aplicação, tendo em vista poder variar
quem tem essa autorização."*

Quando quem executa varia por autorização e não por setor fixo, a redação aberta é escolha
deliberada. Cabe no máximo uma observação, nunca um [E].

## 3. O mesmo recurso pode ser sistema e entrada ao mesmo tempo

**Não apontar** "o e-mail está em Sistemas (5.1) mas também aparece como entrada e como
armazenamento — defina o que ele é".

Palavras do Bruno: *"o e-mail pode ser tanto a ferramenta, quanto o produto da ferramenta. Absorva
esse entendimento lógico para as próximas revisões."*

Vale para qualquer recurso com essa natureza dupla: e-mail, SharePoint, planilha. Estar em duas
seções não é contradição — é a mesma coisa cumprindo dois papéis.

## 4. A definição pode cobrir a atividade vizinha

**Não apontar** que uma definição "extrapola o escopo do documento".

Dois casos reais em que eu errei:

- SUP.014 (Manutenção de cadastro) define o Supervisor como responsável pelo cadastro **e** pela
  manutenção. Bruno: *"Não tem como falar de cadastro de itens, sem se referir à manutenção dos
  itens já cadastrados. Cadastro sem verificação é retrabalho, insegurança e instabilidade."*
- SUP.011 (Retirada de ferramentas) define Almoxarife como "responsável pelo estoque do local".
  Bruno: *"As ferramentas estão localizadas no almoxarifado, refine mais seu raciocínio."*

**Esta regra cancela a seção 6 de `coerencia-interna.md`**, que eu tinha escrito de manhã dizendo o
contrário. Antes de apontar escopo de definição, perguntar: as duas coisas acontecem no mesmo
lugar, ou uma é consequência natural da outra? Se sim, não é apontamento.

## 5. Não exigir por escrito o que a sequência já implica

**Não apontar** que um passo precisa repetir o que os passos anteriores já estabeleceram.

Caso real: no SUP.010 eu apontei que o passo 6 diz "Após ser feito o cadastro do material", o que
apontaria para o passo 4 e não para o 5. Bruno: *"Isso está explicitamente escrito que o cadastro
envolve as duas etapas anteriores, não é necessário deixar o texto redundante para adaptação do
Claude, guarde essa instrução e aprenda para os próximos documentos, utilizar o 'raciocínio
lógico'."*

Se a leitura na ordem já deixa claro, o documento está certo. Só apontar quando a sequência
**contradiz** de fato — não quando ela apenas não repete.

## 6. Papel citado dentro da ação participa do passo

**Não apontar** "papel X não executa nenhum passo" quando ele aparece no texto da ação, mesmo sem
estar entre parênteses como executor.

Caso real: SUP.012, passo 5 — "informar o comprador responsável... após o comprador autorizar".
Bruno: *"Comprador aparece com atribuições no ponto 5 do título 6. Refine sua revisão."*

Já corrigido em `scripts/checagem_mecanica.py` (função `coletar_papeis`), mas vale para a leitura
à mão também: ler a ação inteira, não só o parêntese.

## 7. Célula da tabela de Desvios não precisa de ponto final

**Não apontar.** Bruno: *"Padrão"* / *"Padrão do template"*. Confirmado no `PO.GG.QLD.001`: a
Tabela 3 vem com as células vazias, sem pontuação definida. Checagem já removida dos dois scripts.

---

## Como usar este arquivo

Antes de fechar a lista de apontamentos, passar cada item por aqui. Se ele cair em uma destas sete
regras, **apagar o item** — não rebaixar de [E] para [C], apagar mesmo.

Quando o Bruno der uma devolutiva nova explicando por que algo não é apontamento, **acrescentar
aqui**, com as palavras dele e o caso concreto. É o arquivo que impede a skill de repetir o mesmo
apontamento inútil em todo lote.

### 8. Indicador: não exigir meta, fonte nem frequência

O modelo de POP traz a seção Indicadores com duas frases fixas: uma de abertura e
"Os indicadores devem ser acompanhados mensalmente nos fóruns de governança." **A frequência já
está definida ali.** Não existe campo de meta nem de fonte no modelo, e o QLD.002 não os pede.

Propor "definir meta, fonte e frequência" é inventar estrutura que o padrão não tem. O Bruno
marcou isso duas vezes no checklist dos PJC (2026-09-02) como *"Claude não se atentou ao template
padrão"*.

Continua valendo apontar quando o indicador **não mede o desvio que o próprio documento declara**
— isso é incoerência interna, não exigência de campo novo.

### 9. Ponto final em célula de tabela: não é regra

O QLD.002 não diz nada sobre pontuação dentro de célula, e a Tabela 1 do modelo vem com as
células vazias. Não há padrão a cobrar. Eu tinha inventado a regra e automatizado nos dois
scripts; o Bruno desfez as alterações e anotou *"Ponto final retirado, Claude não se atentou ao
template"* (2026-09-02). As funções `corrige_celulas_sem_ponto` e `conf_celulas_sem_ponto` estão
desativadas nos dois scripts por causa disso.

O que **continua** valendo é pontuação **misturada dentro da mesma lista ou da mesma coluna** —
três células com ponto e uma sem, no mesmo lugar. Isso é inconsistência visível, não regra
inventada.

### 10. Nível de detalhe não é defeito

Um POP com muitos passos, ou com passos que descem ao "como preencher cada campo",
**não está errado**. Se o objetivo da área é esclarecer o processo para quem executa,
detalhe é o que entrega esse objetivo.

Não recomendar "separar isso numa IT", "isso é de outro nível" ou "a seção 6 deveria
ter só N passos" com base na forma. O Bruno vetou isso em 2026-10-20, no
PO.GG.CIM.001: *"Documentos com nível maior de detalhamento não são um problema.
Isso não é um erro, o objetivo é esclarecer o processo"*.

É o mesmo erro das regras 8 e 9 deste arquivo: cobrar estrutura que o padrão não
exige, em cima de um documento que está funcionando.

**O que continua valendo**, porque é incoerência interna e não questão de forma:

- Referência cruzada que aponta para o número errado. Se a lista cresceu e o
  indicador ainda diz "passo 6" para algo que virou o item 13, o que se aponta é
  **o número desencontrado**, não o tamanho da lista.
- Troca de pessoa no meio do texto ("iniciamos" entre passos em terceira pessoa).
- Marca de revisão interna que vazou para o corpo ("(OK SANDRO", "OK COMPLEMENTARES").
