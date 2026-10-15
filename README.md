# Gantts — Grupo Gadens

Cronogramas (Gantt) do Grupo Gadens, com comparativo contra o prazo ideal e análise do projeto (pontos críticos, pontos de atenção e observações).

Cada Gantt é **um único arquivo HTML**. Abre direto no navegador, sem instalar nada, e o botão "Imprimir / salvar PDF" gera a versão em paisagem.

Publicado em: https://brunockawasaki.github.io/Gantts/

## Menu

A página inicial tem dois caminhos: **Gadens** (ainda sem cronogramas) e **Make It**, que abre Horizon e Now (financiamento CEF). O Gantt do Comercial não entra no menu e continua acessível pelo link direto.

| Caminho | Arquivo |
|---|---|
| Menu principal | [index.html](index.html) |
| Make It | [make-it/index.html](make-it/index.html) |
| Horizon · Financiamento CEF | [cronogramas/Horizon...html](cronogramas/Horizon%20%C2%B7%20Financiamento%20CEF.html) |
| Now · Financiamento CEF | [cronogramas/Now...html](cronogramas/Now%20%C2%B7%20Financiamento%20CEF.html) |
| Fluxo de lançamentos (Comercial), fora do menu | [fluxo-lancamentos-comercial/cronograma.html](fluxo-lancamentos-comercial/cronograma.html) |

## Como ler os Gantts da CEF

Pensado para apresentar à diretoria: uma tela só, sem rolagem, com a mensagem principal no topo.

- **Faixa de resumo:** diz quando o contrato está previsto e quantos dias depois do prazo ideal isso é.
- **Uma linha por tarefa**, na ordem da planilha. A parte escura da barra é o que já foi feito; barra toda escura é concluída; barra clara tracejada é a iniciar (previsão).
- **Prazo ideal:** grupo em verde, logo abaixo, na mesma escala. Uma linha tracejada cinza marca o término ideal e uma laranja marca hoje.
- **Contrato assinado:** a listra vermelha mostra o atraso sobre o ideal.
- **Contorno vermelho:** caminho crítico (folga zero).
- **Ao parar o mouse numa linha:** datas, responsável, situação, folga, solicitante, prazos da planilha e motivo do desvio.
- **Abaixo do gráfico:** comparativo com o prazo ideal e a análise do projeto.
- **Botões:** Ajustar à tela (padrão), Dia, Semana, Mês, Só caminho crítico, Ocultar prazo ideal e Imprimir / salvar PDF.

## Estrutura do repositório

| Pasta ou arquivo | Para que serve |
|---|---|
| `dados/*.json` | **Fonte da verdade** de cada cronograma: tarefas, durações, progresso, motivos e texto da análise. |
| `ferramentas/gerar.py` | Gera os cronogramas e os dois níveis de menu. Só usa a biblioteca padrão do Python. |
| `ferramentas/modelo_gantt.html`, `modelo_menu.html`, `modelo_empresa.html` | Modelos das páginas. Mudar o visual é mexer aqui. |
| `ferramentas/conferir_planilha.py` | Compara a planilha com os dados e aponta diferenças. Não altera nada. |
| `ferramentas/preparar_logo.py` | Corta a margem e deixa transparente o fundo de uma logo nova. |
| `cronogramas/`, `make-it/`, `index.html` | **Saída gerada.** Não editar à mão. |
| `assets/` | Logo do Grupo Gadens, logos das marcas (Gadens e Make It) e foto de fundo. |
| `fluxo-lancamentos-comercial/` | Gantt do Comercial (independente): página, gerador da planilha, planilha pronta, planilhas de origem e `LEIA-ME.txt`. |
| `agents/gantt-cronogramas.md` | Agente do Claude Code que faz o passo a passo abaixo. Copie para `.claude/agents/` do projeto, ou para `~/.claude/agents/` para usar em todos. |

## Como atualizar um cronograma

Peça ao Claude Code, com o agente `gantt-cronogramas`, algo como: *"atualize o Horizon com a planilha nova"*. Ou faça à mão:

1. Conferir a planilha:
   ```
   python ferramentas/conferir_planilha.py "caminho\PLANILHA.xlsx"
   ```
   (precisa de `pip install openpyxl`)
2. Atualizar `dados/<projeto>.json` com o que mudou: durações, `inicio`, `progresso`, `motivo` e a posição em `_meta.posicao`.
3. Reescrever o texto da `analise` no mesmo arquivo, só com o que os números mostram.
4. Regerar tudo:
   ```
   python ferramentas/gerar.py
   ```
5. Abrir `cronogramas/<projeto>.html` e conferir.
6. Publicar: `git add -A`, `git commit` e `git push`. O GitHub Pages atualiza em 1 a 2 minutos.

## Como criar um projeto novo

1. Copie um arquivo de `dados/` e ajuste. Em `_meta`, preencha `empresa` ("Gadens" ou "Make It"), `posicao` e `aba` (nome da aba da planilha).
2. Use `"projeto": "Nome · Assunto"`. O nome do arquivo HTML sai dele.
3. Rode `python ferramentas/gerar.py`. O menu da empresa e o principal se atualizam sozinhos.

## Regras do cálculo

- Tarefa já iniciada, com `inicio` informado: vale a data informada (é o realizado).
- Tarefa ainda não iniciada: `inicio` é "não antes de"; a dependência pode empurrá-la.
- Previsto e prazo ideal são duas cadeias separadas, cada uma com o seu fim.
- O andamento (`progresso`) não vem da planilha; é informado à parte.
- A análise só usa o que está nos dados. O que depende de confirmação está escrito como tal.

## Atenção

- **O repositório é público.** Qualquer pessoa com o link vê as páginas, os motivos de desvio e as planilhas de origem do Comercial. Não suba nada que não possa ser visto por qualquer pessoa.
- Os números dos menus e o texto da análise refletem a posição de `_meta.posicao`. Para atualizar, regere.
