# Gantts — Grupo Gadens

Cronogramas (Gantt) do Grupo Gadens, com comparativo contra o prazo ideal e análise do projeto (pontos críticos, pontos de atenção e observações).

Cada Gantt é **um único arquivo HTML**. Abre direto no navegador, sem instalar nada, e o botão "Imprimir" salva em PDF.

## Gantts

| Arquivo | Projeto | Posição | Término previsto | Prazo ideal |
|---|---|---|---|---|
| [Horizon · Financiamento CEF](cronogramas/Horizon%20%C2%B7%20Financiamento%20CEF.html) | Horizon | 15/10/2026 | 15/11/2026 | 24/09/2026 |
| [Now · Financiamento CEF](cronogramas/Now%20%C2%B7%20Financiamento%20CEF.html) | Now | 15/10/2026 | 07/11/2026 | 19/09/2026 |
| [Fluxo de lançamentos (Comercial)](fluxo-lancamentos-comercial/cronograma.html) | Projeto Next | 02/10/2026 | dia 190 (dia 0 = entrada do PL) | não se aplica |

## Como usar os Gantts da CEF

- **Passe o mouse** (ou use Tab) sobre uma tarefa: aparece o detalhe com datas, responsável, situação, folga, do que ela depende e o que ela libera. A tarefa fica em foco com as ligadas a ela; as demais ficam esmaecidas.
- **Clique numa etapa** da tabela de comparativo: as tarefas dela, no previsto e no ideal, ficam destacadas no gráfico. Clique de novo para soltar.
- **Botões:** Dia, Semana e Mês mudam a escala; Só caminho crítico filtra as tarefas sem folga; Ocultar prazo ideal esconde a referência.

## Como cada arquivo é feito

- Os dados ficam em um bloco `<script type="application/json" id="dados">` dentro do próprio HTML: tarefas, durações, dependências, responsável, progresso e o texto da análise.
- O resto do arquivo é o desenho e o cálculo (caminho crítico, folga, comparativo). Para atualizar um Gantt, altere só o bloco de dados.
- Tarefas do prazo ideal têm `"referencia": true`. Cada tarefa tem `"etapa"`, usada para comparar com o ideal.

## Regras do cálculo

- Tarefa já iniciada, com `inicio` informado: vale a data informada (é o realizado).
- Tarefa ainda não iniciada: `inicio` é "não antes de"; a dependência pode empurrá-la.
- Previsto e prazo ideal são duas cadeias separadas, cada uma com o seu fim.
- A análise só usa o que está nos dados. O que depende de confirmação está escrito como tal.

## Pasta `fluxo-lancamentos-comercial/`

Gantt das cinco frentes do fluxo de lançamentos do Comercial (Documentação, Imagens, Orçamento, Maquete e Takes), em dias relativos, dia 0 = entrada do PL. Tem a página (`cronograma.html`), o gerador da planilha (`gera_gantt_excel.py`), a planilha pronta, as duas versões da planilha de origem e um `LEIA-ME.txt` com o passo a passo.

## Pasta `agents/`

`gantt-cronogramas.md` é o agente do Claude Code que monta Gantts a partir de planilhas. Copie para `.claude/agents/` do projeto, ou para `~/.claude/agents/` para usar em todos.

## Como adicionar um Gantt

1. Salve o HTML em `cronogramas/` com o nome `<Projeto> · <Assunto>.html`.
2. Inclua uma linha na tabela acima.
3. Se já existir versão anterior, substitua o arquivo. O histórico fica no Git.


