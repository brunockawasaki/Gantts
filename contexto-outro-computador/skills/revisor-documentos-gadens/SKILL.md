---
name: revisor-documentos-gadens
description: >
  Revisa POPs, Instruções de Trabalho (IT) e Regimentos do Grupo Gadens já elaborados, contra o
  padrão documental oficial PO.GG.QLD.002 e contra a estrutura esperada de cada tipo (12 seções
  para POP, 6 para IT, 9 para Regimento). Entende o processo antes de conferir requisito, produz
  apontamentos classificados [E]/[C]/[D], aplica sozinho as correções que não dependem de
  resposta de ninguém, e gera um checklist Word com o que sobra. Use sempre que alguém pedir para
  revisar, auditar, conferir ou apontar erros em um POP, IT ou Regimento — mesmo sem essas
  palavras exatas ("dá uma olhada nesse documento", "tá certo isso?", "compara com o QLD.002"),
  ou ao anexar um arquivo PO.xx.xxx.xxx / IT.xx.xxx.xxx / RE.xx.xxx.xxx. Também para comparar um
  documento contra o modelo do tipo. NÃO use para escrever um documento novo a partir de texto
  bruto, nem para revisar os próprios modelos padrão ou o QLD.002 — isso é conversa de governança.
license: Uso interno Grupo Gadens — Projeto Next
---

# Revisor de documentos — Grupo Gadens

Audita POP, IT e Regimento contra o padrão oficial e contra o que se espera de cada tipo. Faz três
coisas, nesta ordem de importância:

1. **Entende o processo** e aponta o que quebraria na vida real.
2. **Corrige sozinho** o que não depende de resposta de ninguém — erro de digitação, vírgula,
   grafia de papel, sobra de texto do modelo, campo da capa.
3. **Gera um checklist Word** só com o que precisa de decisão humana.

---

## Antes do primeiro uso — configuração

Três coisas para ajustar na sua máquina:

**1. Instalar a biblioteca de leitura de Word:**

```bash
pip install python-docx
```

**2. Apontar os caminhos.** Os programas em `scripts/` precisam saber onde estão os documentos e
o modelo padrão. Você pode passar por argumento a cada uso (`--pasta`, `--modelo`) ou preencher as
duas constantes no topo de `scripts/aplicar_correcoes.py`.

**3. Conferir se as referências estão atualizadas.** Os arquivos em `references/` foram extraídos
dos documentos oficiais em **26/08/2026**:

| Arquivo | Fonte | Versão capturada |
|---|---|---|
| `qld-002.md` | `PO.GG.QLD.002 - Regras de elaboração de documento` (**.docx**, não o PDF) | Revisão 03, 14/08/2026 |
| `templates.md` | `PO.GG.QLD.001`, `IT.GG.PRO.001`, `RE.GG.PRO.001` | 26/08/2026 |

**Sempre extrair do `.docx`, nunca do `.pdf`.** Já aconteceu de o PDF na pasta estar uma revisão
atrás e não conter a Matriz de Aprovação inteira, o que levou a conclusões erradas.

---

## O método — entender antes de conferir

**Esta é a parte que mais importa, e a mais fácil de pular.**

Depois de ler o documento e **antes** de escrever qualquer apontamento, responder para si mesmo:

- **O que este processo entrega, e para quem?**
- **Quem faz o quê, em que ordem?** Seguir o fluxo como se fosse executá-lo.
- **Se alguém seguisse este documento ao pé da letra, o que daria errado?**
- **Onde isso quebra na vida real?**

Todo apontamento tem que se conectar a esse entendimento. Teste antes de escrever cada um:
**se eu mostrar isso a quem executa o processo, ele reconhece como problema?** Se a resposta for
"não, mas está diferente do checklist", o apontamento não existe — apagar.

### Por que isso importa: exemplos reais

**O que só aparece entendendo, e nenhum checklist pega:**

- Um POP existe para padronizar a descrição dos itens, e o padrão de descrição não está em lugar
  nenhum do documento. Cada seção, olhada sozinha, parecia completa.
- Um POP prevê o desvio "divergência entre pedido e nota fiscal", mas nenhum passo compara os
  dois. O documento monitora um problema que ele mesmo não consegue enxergar.
- Um POP promete reduzir extravio de ferramenta e não define prazo de devolução. Sem prazo, não
  existe o momento em que a ferramenta passa a ser considerada extraviada.
- Um POP manda confirmar a data de entrega com o fornecedor **antes** de verificar se há espaço
  físico para receber.

**E o inverso — entender evita o apontamento inútil.** Ferramenta fica no almoxarifado, então
definir o almoxarife como "responsável pelo estoque" cobre ferramenta. Cadastrar item implica
mantê-lo. O e-mail é ferramenta e produto ao mesmo tempo. Ver `references/nao-apontar.md`.

---

## Fluxo de revisão

1. **Ler o documento por inteiro**, incluindo cabeçalho e rodapé — eles guardam código, revisão e
   data que costumam divergir da capa. A capa fica dentro de uma caixa de texto e não aparece na
   leitura simples; extrair de `<w:txbxContent>` no `word/document.xml`.

2. **Entender o processo** (seção acima). Não é opcional.

3. **Rodar `scripts/checagem_mecanica.py`.** Faz as conferências que não exigem julgamento e que a
   leitura à mão erra de vez em quando: pontuação dos passos, célula sem ponto, vírgula indevida,
   verbo misturado, voz passiva, parêntese aberto, sobras do modelo, capa × rodapé, matriz de
   papéis, grafias divergentes, desvio circular, coluna sem variação, maiúscula no meio da frase,
   sistema listado e não usado, entregável que nenhum passo produz.

   ```bash
   python3 scripts/checagem_mecanica.py --pasta "<pasta>"
   python3 scripts/checagem_mecanica.py "<arquivo.docx>" ["<outro.docx>" ...]
   ```

   Só lê, nunca altera.

4. **Checagem formal** contra `references/qld-002.md`: código, esteira de aprovação, capa ×
   cabeçalho × rodapé, placeholder não preenchido, formatação.

5. **Completude estrutural** conforme o tipo: `pop-checklist.md` (12 seções), `it-checklist.md`
   (6) ou `regimento-checklist.md` (9).

6. **Coerência interna** — `references/coerencia-interna.md`.

7. **Ler os passos como fluxo** — `references/fluxo-e-desvios.md`. A ordem faz sentido? Todo ramo
   condicional chega a algum lugar? O fluxo tem saída? O desvio previsto é detectável pelo fluxo
   descrito? Existe prazo em algum lugar?

8. **Filtrar por `references/nao-apontar.md`.** Decisões já tomadas sobre o que **não** é
   apontamento. Item que cair numa dessas regras se **apaga**, não se rebaixa de [E] para [C].

9. **Separar em três montes** — é o que evita entregar 200 itens para alguém tratar:

   | Monte | O que é | Quem resolve |
   |---|---|---|
   | **A** | Erro que não depende de resposta | O revisor executa, com `aplicar_correcoes.py` |
   | **B** | Falta conteúdo, mas dá para propor o texto | O revisor escreve a proposta; a área aprova ou ajusta |
   | **C** | Precisa de decisão real | A área dona do processo, ou a governança |

   **Entregar proposta, não pergunta.** Em quase todo item onde se pergunta "o que falta aqui?",
   dá para escrever a sugestão. Escrever é trabalho do revisor.

10. **Classificar o que sobrou:**
    - **[E]** erro objetivo — corrige direto.
    - **[C]** conteúdo — precisa de confirmação da área dona do processo.
    - **[D]** decisão de escopo/padrão — cabe à governança do Projeto Next.

11. **GERAR O CHECKLIST WORD — antes de escrever a resposta no chat.** Com os montes B e C, mais
    um bloco final registrando o que foi corrigido e o que o programa acusou mas foi descartado
    de propósito.

    **A ordem importa.** Depois de escrever um resumo longo no chat, a resposta já parece
    entregue e o checklist vira apêndice que se perde — foi o que aconteceu numa revisão real.
    Gerando primeiro, o texto do chat vira o resumo de um entregável que já existe.

12. **Escrever a resposta no chat**, fechando com o caminho do checklist gerado.

---

## As duas regras que não se afrouxam

**Primeira: entender antes de conferir.** Checklist é rede de segurança, não é o trabalho.
Apontamento que só existe porque um campo não bate com uma lista, e que não significa nada para
quem executa o processo, não é apontamento.

**Segunda: separar apontamento de opinião técnica.** Quem revisa é de processos, não especialista
na área fim (obra, suprimentos, orçamento).

- **Sempre aponte:** ausência de estrutura esperada — seção vazia, indicador que não mede o que o
  documento declara monitorar, ação de desvio que não corrige o desvio, papel citado e ausente da
  tabela de responsabilidades, contradição interna, referência citada e não listada, placeholder,
  numeração com lacuna.
- **Nunca afirme como erro** que um valor técnico existente está errado no mérito — um prazo de
  execução, uma regra de alçada, um critério de tolerância. Se parece questionável, vira
  **pergunta [C]**, nunca afirmação.
- Teste: *isso é ausência de estrutura (aponto) ou é o conteúdo técnico de uma estrutura que já
  existe (pergunto)?*

---

## Guarda-corpos

**Não confundir o modelo em branco com uma revisão anterior.** Os modelos vêm com Elaborador,
Aprovador, Revisão `00` e Status `Aprovado` preenchidos de fábrica. Antes de apontar "capa
desatualizada", confirmar que os valores não são simplesmente o padrão do modelo. Ver
`references/templates.md`.

*Limite:* isso vale só para comparação com uma suposta versão anterior. **Não** vale para
divergência interna dentro do mesmo arquivo — capa dizendo uma coisa e rodapé outra é [E] normal,
mesmo que o valor tenha vindo do modelo.

**Fusão de colunas não é perda de conteúdo.** Quando o texto-fonte tinha mais colunas do que o
modelo suporta, o conteúdo pode ter sido fundido numa célula vizinha. Isso é adaptação esperada.

*Limite:* protege a forma, não o conteúdo. O texto fundido passa por todas as checagens normais —
vaguidade, referência não resolvida, contradição.

**Documento espelhado entre empresas do Grupo é intencional.** Nunca sinalizar como duplicidade.

*Exceção:* quando dois documentos descrevem **o mesmo momento físico** e exigem **controles
diferentes**, isso é apontamento [C] mesmo sem pedido de comparação. Exemplo real: um POP manda
colher assinatura na entrega de material, o POP irmão descreve a mesma entrega sem assinatura
nenhuma. Teste: a diferença muda **o que alguém tem que fazer ou provar**? Se sim, aponta. Se só
muda a forma de escrever, vira [D] de padronização.

---

## O que esta skill não faz

- **Não escreve documento novo** a partir de texto bruto. Isso é o fluxo de elaboração.
- **Não revisa os modelos padrão** (`PO.GG.QLD.001`, `IT.GG.PRO.001`, `RE.GG.PRO.001`) nem o
  próprio QLD.002. Apontar o problema e levar à governança, sem editar o modelo compartilhado.
- **Não preenche seção vazia nem inventa conteúdo.** Onde estiver "Não especificado no texto de
  origem", o texto que entra ali depende da área dona do processo.

---

## Formato de saída

Texto corrido no chat, agrupado por documento:

```
### [Código] - [Título curto]

1. [E] Descrição objetiva do erro e onde está. Ação: o que corrigir.
2. [C] O que precisa de confirmação. Pergunta específica para a área.
3. [D] Lacuna de escopo/decisão. Quem decide.
```

**Granularidade: um achado por lacuna, nunca agregado.** "Papéis-chave lista 4 papéis e a tabela
só tem 1" vira uma correção vaga. Desdobrado em um item por papel órfão, com a lacuna específica
de cada um, vira várias correções executáveis — e aparecem lacunas que a agregação escondia.

---

## Programas

| Programa | O que faz |
|---|---|
| `checagem_mecanica.py` | Só lê. Faz as conferências que não exigem julgamento. |
| `aplicar_correcoes.py` | Corrige o Monte A. Trabalha em cópia, valida o XML e só então substitui. `--simular` mostra sem gravar. |
| `gen_checklist.py` | Gera o checklist Word (☐ + item + linha para resposta). |
| `acrescentar_itens.py` | Acrescenta itens a um checklist **já em uso**, sem apagar as respostas escritas. |

**Nunca regerar do zero um checklist que alguém já começou a preencher** — usar
`acrescentar_itens.py`.

### Cuidados técnicos

- **Sempre `--simular` antes de `--aplicar`**, e sempre backup dos originais.
- **Um documento por vez** ao corrigir, conferindo cada um.
- **Texto quebrado em pedaços:** o Word divide uma frase em vários `<w:t>`. Busca literal não
  acha. Um erro no cabeçalho (`9001:20/15`) escapou de uma rodada inteira por isso — usar as
  funções que juntam os pedaços antes de trocar.
- **Arquivo aberto no Word** não pode ser gravado (`PermissionError`). Para apenas ler, copiar
  para uma pasta temporária antes.
- **Validar depois de gravar:** parse do XML de todas as partes + abrir com `python-docx`. Isso
  não substitui abrir no Word — avisar quem recebe para abrir uma vez antes de circular.
- **Nunca deixar arquivo de rascunho** na pasta usada para reempacotar um `.docx`: corrompe o
  pacote.

---

## Arquivos de referência

| Arquivo | Conteúdo |
|---|---|
| `qld-002.md` | Regras oficiais do PO.GG.QLD.002. Traz uma seção **"O que o QLD.002 NÃO define"** — ler antes de apontar algo como violação da norma. |
| `templates.md` | Estrutura exata dos três modelos, textos de fábrica de cada seção, e os defeitos conhecidos dos próprios modelos. |
| `pop-checklist.md` | Completude de POP, 12 seções. |
| `it-checklist.md` | Completude de IT, 6 seções. |
| `regimento-checklist.md` | Completude de Regimento, 9 seções. |
| `coerencia-interna.md` | Resíduo de texto do modelo, contradição interna, consistência de termos e papéis, coluna que não discrimina, redação. |
| `fluxo-e-desvios.md` | Leitura dos passos como cadeia causal: ordem, ramos que morrem, executor real, desvios deriváveis, prazo, registro. |
| `nao-apontar.md` | O que já se decidiu que **não** é apontamento. Cancela regras dos outros arquivos quando houver conflito. |

**Manutenção:** quando alguém explicar numa devolutiva por que algo não é apontamento,
**acrescentar a regra em `nao-apontar.md`**, com as palavras da pessoa e o caso concreto. É o
arquivo que impede a skill de repetir o mesmo apontamento inútil em todo lote.

---

## Como esta skill foi construída

Nasceu de uma ideia de revisão estruturada de POP/IT/Regimento no Projeto Next, e foi refinada em
agosto de 2026 revisando 11 documentos reais (9 POPs de Suprimentos e 2 de Projetos
Complementares).

O que mais melhorou a qualidade não foi escrever mais regra — foi **comparar contra outra revisão
independente do mesmo documento**. Cada rodada de comparação expôs uma categoria inteira de
checagem que faltava. Vale repetir isso quem for usar: revisar em dupla, comparar, e escrever no
`nao-apontar.md` o que a comparação ensinar.

A segunda coisa que mais ajudou foi **parar de medir sucesso por quantidade de achado**. Uma
revisão que entrega 10 pontos que importam vale mais que 200 que incluem tudo — achado que
ninguém vai tratar não é resultado, é ruído.
