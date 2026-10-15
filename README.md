# Gantts — Grupo Gadens

Cronogramas (Gantt) do Grupo Gadens, com comparativo contra o prazo ideal e análise do projeto (pontos críticos, pontos de atenção e observações).

Cada Gantt é **um único arquivo HTML**. Abre direto no navegador, sem instalar nada, e o botão "Imprimir" salva em PDF.

## Menu

A página inicial (`index.html`) tem dois caminhos: **Gadens** (ainda sem cronogramas) e **Make It**, que abre Horizon e Now (financiamento CEF). O Gantt do Comercial não entra no menu e continua acessível pelo link direto.

| Caminho | Arquivo |
|---|---|
| Menu principal | [index.html](index.html) |
| Make It | [make-it/index.html](make-it/index.html) |
| Horizon · Financiamento CEF | [cronogramas/Horizon...html](cronogramas/Horizon%20%C2%B7%20Financiamento%20CEF.html) |
| Now · Financiamento CEF | [cronogramas/Now...html](cronogramas/Now%20%C2%B7%20Financiamento%20CEF.html) |
| Fluxo de lançamentos (Comercial), fora do menu | [fluxo-lancamentos-comercial/cronograma.html](fluxo-lancamentos-comercial/cronograma.html) |

A pasta `assets/` guarda o logo (`logo-gg.png`) e a foto de fundo (`fachada-gadens.jpg`).

## Como ler os Gantts da CEF

Pensado para apresentar à diretoria: uma tela só, sem rolagem, com a mensagem principal no topo.

- **Faixa de resumo:** diz quando o contrato está previsto e quantos dias depois do prazo ideal isso é.
- **Uma linha por tarefa:** a barra mostra o andamento. A parte escura é o que já foi feito; barra toda escura é concluída; barra clara tracejada é a iniciar (previsão).
- **Prazo ideal:** grupo em verde, logo abaixo, para comparar na mesma escala. Uma linha tracejada cinza marca o término ideal e uma laranja marca hoje.
- **Contrato assinado:** a listra vermelha mostra o atraso sobre o ideal.
- **Contorno vermelho:** caminho crítico (folga zero).
- **Abaixo do gráfico:** comparativo com o prazo ideal (com barra do atraso acrescentado por etapa) e a análise do projeto.
- **Botões:** Ajustar à tela (padrão), Dia, Semana, Mês, Só caminho crítico, Ocultar prazo ideal e Imprimir / salvar PDF.

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





