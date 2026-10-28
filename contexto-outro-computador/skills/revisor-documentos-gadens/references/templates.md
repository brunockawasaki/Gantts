# Os três modelos padrão — estrutura real e textos de fábrica

Extraído dos arquivos reais em **2026-08-26** (releitura às 11h20, após as correções da governança do Projeto Next).

Pasta única desde 2026-08-26 — antes os modelos estavam separados em `1. POP` e `2. IT`:
`...\1. [nome do elaborador]\1. Padrões\1. Padrões\` — os três modelos, o QLD.002, e o PDF de cada um.
Os PDFs agora são gerados junto com os `.docx`; ainda assim, **extrair sempre do `.docx`**.

Serve para duas coisas: saber a estrutura exata que se espera de cada tipo, e reconhecer o texto
de fábrica que sobrou sem preencher. **Este arquivo descreve os modelos; não é para auditá-los**
(revisar template é conversa de governança — ver `SKILL.md`).

---

## Valores de fábrica da capa (iguais nos três modelos)

| Campo | Valor de fábrica |
|---|---|
| Data | 26/08/2026 (muda quando alguém abre o arquivo) |
| Revisão | `00` |
| Status | `Aprovado` |
| Elaborador | `[nome do elaborador]` |
| Aprovador | `Carlos Vargas` |
| Empresas abrangidas | `GRUPO GADENS` |
| Título | `TÍTULO DE PROCEDIMENTO OPERACIONAL PADRÃO` / `TÍTULO DE REGIMENTO` / `TÍTULO DA INSTRUÇÃO DE TRABALHO` |
| Marca d'água na capa | `Padrão de formatação para documentos.` e `procedimento operacional.` |

Nenhum desses valores é evidência de revisão anterior real — é o modelo em branco. Ver o
guarda-corpo correspondente no `SKILL.md`. **Atenção:** o `Aprovador` de fábrica é
**`Carlos Vargas` sozinho**. `Alessandro Braz, Carlos Vargas` é o aprovador do próprio QLD.002,
não o placeholder dos modelos — não confundir os dois.

Campo **"Tipo de documento" da capa**, de fábrica em cada modelo:

- POP → `Procedimento Operacional Padrão` (nome completo, com "Padrão")
- Regimento → `Regimento`
- IT → `Instrução de Trabalho` (era `Regimento` até 2026-08-26; corrigido pela governança do Projeto Next)

Consequência prática: um POP cuja capa diga apenas `Procedimento Operacional` **não** herdou isso
do modelo — o modelo traz o nome completo. Divergência entre capa e rodapé nesse campo é [E] real,
não resíduo de fábrica.

---

## POP — `PO.GG.QLD.001`, 12 seções

Cabeçalho: `PROCEDIMENTO OPERACIONAL PADRÃO | Documento: PO.GG.QLD.001 | Rev. 00 | Referência:
PBQP-H 2021 / ABNT NBR ISO 9001:2015 – 7.5`
Rodapé: `Tipo de documento: Procedimento Operacional Padrão | Revisão:00 | Data: ...`

| # | Seção | Conteúdo de fábrica / estrutura |
|---|---|---|
| 1 | OBJETIVO | "Definir o objetivo e o escopo do documento." |
| 2 | APLICAÇÃO | "Descrever a Empresa aplicável e os setores envolvidos no processo." |
| 3 | REFERÊNCIAS | "Relacionar as normas técnicas, legislações, procedimentos, especificações e demais documentos utilizados como base para a elaboração e aplicação deste documento." |
| 4 | DEFINIÇÕES | "Identificar e descrever os termos técnicos, siglas, abreviaturas e acrônimos..." + **Tabela 1 - Siglas e definições** (Termo/Sigla \| Definição) |
| 5 | RECURSOS NECESSÁRIOS | três subtítulos vazios: `Sistemas`, `Documentos/entradas`, `Papéis-chave` |
| 6 | PRINCIPAIS PASSOS DO PROCESSO | abre com "O processo é executado conforme fluxo modelado no Bizagi, contemplando as seguintes etapas macro:" e fecha com "Os detalhamentos operacionais encontram-se descritos no fluxo Bizagi correspondente." |
| 7 | PAPÉIS, RESPONSABILIDADES E AUTONOMIA | **Tabela 2 - Responsabilidades** (Papel Funcional (Área) \| Responsabilidades \| Limites de Autonomia) |
| 8 | INDICADORES | abre com "Os seguintes indicadores são utilizados para monitorar a efetividade das **diretrizes estratégicas de prospecção** definidas neste POP:" e fecha com "Os indicadores devem ser acompanhados mensalmente nos fóruns de governança." |
| 9 | PONTOS CRÍTICOS DO PROCESSO | vazio |
| 10 | DESVIOS / AÇÕES NECESSÁRIAS | **Tabela 3 - Desvios e ações necessárias** (Situação de Desvio \| Ação Necessária \| Responsável) |
| 11 | REGISTRO DO PROCESSO | "Identificar os entregáveis do processo, ou seja, o produto do processo." + **Tabela 4 - Entregáveis do processo** (Identificação \| Armazenamento) |
| 12 | CONTROLE DE EMISSÃO | **Tabela 5 - Controle de emissão** (Revisão \| Etapa \| Itens Revisados \| Data) |

**"prospecção" na seção 8 é resíduo de fábrica** e deve ter sido trocado em todo POP que não seja
de prospecção. Confirmado no modelo real.

As frases de abertura e fechamento do Bizagi (seção 6) **são do modelo** — a ausência delas num POP
é lacuna de transposição, não escolha.

---

## Regimento — `RE.GG.PRO.001`, 9 seções

Cabeçalho: `REGIMENTO | Documento: RE.GG.PRO.001 | Rev. 00`
Rodapé: `Tipo de documento: Regimento | Revisão:00 | Data: ...`

| # | Seção | Conteúdo de fábrica / estrutura |
|---|---|---|
| 1 | OBJETIVO | "Definir o objetivo e o escopo do documento." |
| 2 | APLICAÇÃO | "Descrever a Empresa aplicável e os setores envolvidos no processo." |
| 3 | ÁREAS ENVOLVIDAS | "Mencionar quais áreas estão envolvidas na reunião/comitê." |
| 4 | GOVERNANÇA E OPERACIONALIZAÇÃO | tabela **sem legenda** (ITEM \| DEFINIÇÃO), com 5 linhas fixas: `Convocação/Agendamento`, `Periodicidade`, `Formato`, `Pauta/Material de Apoio`, `Registro/Ata` |
| 5 | PAPÉIS E RESPONSABILIDADES | tabela **sem legenda** (ÁREA \| RESPONSABILIDADES) |
| 6 | ENTRADAS DO PROCESSO (INPUTS) | tabela **sem legenda** (INPUT \| DESCRIÇÃO \| RESPONSÁVEL) |
| 7 | SAÍDAS DO PROCESSO (OUTPUTS) | tabela **sem legenda** (OUTPUT \| DESCRIÇÃO \| RESPONSÁVEL) |
| 8 | REFERÊNCIAS | mesma frase do POP |
| 9 | CONTROLE DE EMISSÃO | **Tabela 1 - Controle de emissão** |

Duas particularidades que diferenciam o Regimento do POP e que **não devem virar apontamento**:

- As quatro tabelas do meio **não têm legenda "Tabela N-Nome"**. Só o Controle de Emissão tem.
- Por isso o Controle de Emissão é a **Tabela 1** num Regimento (e a Tabela 5 num POP). Numeração
  diferente é o correto para o tipo.

Textos de fábrica das tabelas: "Informar de quem é a responsabilidade de convocar os participantes
e agendar a data da reunião.", "Informar recorrência, dia da semana, horário e exceções.",
"Informar se a reunião ocorrerá presencial ou online, bem como, exceções.", "Detalhar a pauta a ser
tratada em cada reunião.", "Informar o registro/evidência/alinhamento fruto do encontro...",
"Nome da Área", "Informar as responsabilidades da área dentro da reunião",
"Input necessário para reunião", "Output necessário para reunião",
"Descrever características do input/output", "Setor responsável por entregar o input/output".

---

## IT — `IT.GG.PRO.001`, 6 seções

Cabeçalho: `INSTRUÇÃO DE TRABALHO | Documento: IT.GG.PRO.001 | Rev. 00`
Rodapé: `Tipo de documento: Instrução de Trabalho | Revisão:00 | Data: ...`

| # | Seção | Conteúdo de fábrica / estrutura |
|---|---|---|
| 1 | OBJETIVO | "Definir o objetivo e o escopo do documento." |
| 2 | APLICAÇÃO | "Descrever a Empresa aplicável e os setores envolvidos no processo." |
| 3 | REFERÊNCIAS | mesma frase do POP |
| 4 | DEFINIÇÕES | mesma frase do POP + **Tabela 1 - Siglas e definições** |
| 5 | ETAPAS DA INSTRUÇÃO DE TRABALHO | "Inserir texto explicativo da tarefa realizada." / "Inserir imagem referente ao procedimento descrito." / "Observação: Para cada passo realizado no procedimento, incluir o texto explicativo e a imagem correspondente." |
| 6 | CONTROLE DE EMISSÃO | **Tabela 2 - Controle de emissão** |

Confirma o que o `it-checklist.md` já dizia: a IT **não tem** Recursos Necessários, Papéis e
Responsabilidades, Indicadores, Pontos Críticos, Desvios nem Registro do Processo. A ausência
dessas seções numa IT é a estrutura correta e nunca é apontamento.

A seção 5 é a única do tipo que espera **texto + imagem por passo**. A tabela de Definições de uma
IT guarda **siglas técnicas**, não papéis — checagem de matriz de papéis não se aplica a IT.

---

## Controle de Emissão — formato único desde 2026-08-26

Os três modelos trazem a mesma linha de fábrica na tabela de Controle de Emissão:

| Revisão | Etapa | Itens Revisados | Data |
|---|---|---|---|
| 0 | Elaboração: <br> Revisador: <br> Validador: <br> Aprovação: | Elaboração inicial | DD/MM/AAAA <br> DD/MM/AAAA <br> DD/MM/AAAA <br> DD/MM/AAAA |

(no Regimento e na IT os campos já vêm com `Revisador: [nome do elaborador]` e
`Validador: Carlos Vargas` preenchidos de fábrica.)

### Divergências entre template e QLD.002 — citar as duas fontes ao auditar

| Ponto | QLD.002 §5.3 (Tabela 6) | Modelos |
|---|---|---|
| Etapas na célula | **duas**: `Elaboração:` + `Aprovação:` (e `Revisão:` + `Aprovação:` nas linhas seguintes) | **quatro**: `Elaboração:` + `Revisador:` + `Validador:` + `Aprovação:` |
| Datas | duas | quatro |
| Rótulo da linha de revisão | `Revisão:` | não existe linha de revisão de fábrica |

O que os dois **concordam**, e por isso é apontamento firme: **toda linha termina em
`Aprovação:`**. Uma linha de revisão que traga só `Revisador:` e `Validador:`, sem `Aprovação:`,
está incompleta pelas duas fontes ao mesmo tempo — e a aprovação é o último evento da esteira
(§5.2 do QLD.002).

Já `Revisador:` / `Validador:` **não** são desvio da área: vêm do modelo oficial. Não apontar como
erro (isto corrige uma classificação errada feita em 2026-08-25).

---

## Defeitos dos próprios modelos (levar à governança do Projeto Next, não "corrigir" em documento de área)

Achados ao ler os modelos. Não são erro de quem escreveu um POP/IT/Regimento — são do modelo, e
qualquer documento gerado a partir dele herda o problema. Conversa de governança do Projeto Next.

### Corrigidos pela governança do Projeto Next em 2026-08-26, confirmados na releitura

- ~~IT.GG.PRO.001 — capa dizia `Tipo de documento: Regimento`~~ → agora `Instrução de Trabalho`.
- ~~RE.GG.PRO.001 — `PAPÉIS E RESPONSÁBILIDADES` com acento indevido~~ → agora
  `PAPÉIS E RESPONSABILIDADES`, no título e no cabeçalho da tabela.
- ~~RE.GG.PRO.001 — `Input necessário para reunão`~~ → agora `reunião` nas duas linhas.

### Em aberto

1. **PO.GG.QLD.001 — resíduo "diretrizes estratégicas de prospecção"** na seção 8 (INDICADORES).
   É a origem do apontamento recorrente em POPs que não são de prospecção, e continua no modelo.
2. **Datas divergentes dentro do mesmo modelo** (capa × cabeçalho × rodapé), estado após as
   correções de 2026-08-26 11h:
   - POP: `26/08/2026` nos três — coerente.
   - IT: `26/08/2026` nos três — coerente (o rodapé, que dizia `08/07/2026`, foi corrigido).
   - **Regimento: continua com três datas diferentes** — capa `26/08/2026`, cabeçalho
     `15/07/2026`, rodapé `25/08/2026`. É o único dos três ainda desalinhado.
   Datas de fábrica desalinhadas ensinam a divergência para todo documento gerado a partir delas.

### Resolvido: qual formato de Controle de Emissão vale

Havia divergência entre os modelos (quatro etapas) e a Tabela 6 do QLD.002 (duas). **Em 2026-08-26
a governança do Projeto Next decidiu pelas quatro e reescreveu a Tabela 6 do QLD.002** para acompanhar. Norma e modelos
agora dizem o mesmo: `Elaboração: / Revisador: / Validador: / Aprovação:`, com quatro datas.
`Revisador:` e `Validador:` são etapas oficiais — nunca apontar como desvio.
