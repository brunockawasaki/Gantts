---
name: gantt-fluxo-lancamentos
description: "Gantt do fluxo de lançamentos do Comercial (Projeto Next) — onde estão os fontes, as decisões do Bruno sobre a planilha de origem, a regra de cor, e o que ficou por confirmar"
metadata:
  node_type: memory
  type: project
  originSessionId: 87663fe1-caf6-4526-9fb6-4e324de2cd03
  modified: 2026-10-02T21:04:11.150Z
---

Cronograma das cinco frentes do fluxo de lançamentos do Comercial: Documentação (prefeitura), Imagens, Orçamento, Maquete e Takes. Escala em **dias corridos relativos, dia 0 = entrada do PL**. Entregue em duas formas, que devem andar juntas.

**Fontes (permanentes):** `...\1. Bruno Kawasaki\Projeto teste\Gantt - fontes\` — `gera_gantt_excel.py`, `cronograma.html`, as duas versões da planilha de origem e um LEIA-ME com o passo a passo. Os dados ficam na lista `FRENTES`, **duplicada nos dois arquivos**; ao mudar, mexer nos dois e ajustar `DIA_MAX` / `MAX`. Os números do cabeçalho da página são calculados dos dados, não precisam de ajuste.

**Entregas:** planilha em `...\Projeto teste\Gantt - Fluxo de Lançamentos (Comercial).xlsx`; página em https://claude.ai/artifact/8pEyf9vknRwmBHDYsLYZxX (republicar o mesmo arquivo mantém a URL).

**Origem:** `resumo fluxo Gadens Next lançamentos.xlsx`, pasta do Comercial em Processos - Documentos / Projeto Next / 2. Processos / 15. Comercial. É uma grade de marcos numa régua de 5 em 5 dias — **não traz dependências**, só posições. Qualquer leitura de "X depende de Y" é inferência a partir de datas coincidirem, e precisa ser confirmada com o Comercial antes de ser afirmada.

## Decisões do Bruno que não estão em arquivo nenhum

1. **A planilha tem DUAS linhas chamadas IMAGENS.** A mais curta (termina no dia 90) é para **ignorar**; vale a outra. Dito em 29/09/2026.
2. **A escala fica em dias relativos.** Ele recusou converter para datas: *"não tem um dia específico, se refira a ele como dia 0"*.
3. **A ordem das faixas segue a ordem das linhas da planilha.** Pedido em 02/10, quando a v2 trouxe as mesmas datas em ordem diferente.

## Regra de cor (vale para as próximas alterações)

As cores são os **slots 1 a 5 da paleta de referência do dataviz, atribuídos na ordem das faixas** — não fixas por frente. Quando a ordem mudar, reatribuir e **revalidar** com `valida_paleta.py` (porte em Python do validador da skill `dataviz`; não há Node nesta máquina).

Motivo: na v2, manter a cor antiga de cada frente deixaria Maquete e Orçamento a ΔE 12,9, abaixo do piso de 15. E a paleta dessaturada que eu tinha escolhido na primeira versão **estava reprovada** e passou meses sem validação — verde e azul acinzentados a ΔE 8,4.

Na planilha, o nome da frente é **texto escuro com barra colorida à esquerda**, nunca texto branco sobre a cor: no amarelo não havia contraste.

## Por confirmar

- **"Anteprojeto" no dia 0.** Célula nova na v2, sem fim marcado. Pode ser que o dia 0 seja a entrada no Anteprojeto e todo o cronograma corra nessa fase, ou que haja outras fases depois. Desenhei como etiqueta no começo da régua. Se houver mais fases, dá para desenhar faixas.
- **1º tiro de imagens no dia 45.** Em 29/09 o Bruno pediu para movê-lo para o **110** (*"para termos um prazo de que o todo acontece"*), mas as versões da planilha de 02/10 trazem 45 nas duas. Avisei e ele não respondeu. A outra mudança daquele dia (maquete de 90 para 60 dias) foi absorvida pela planilha.

## Estado em 02/10/2026 — 190 dias

Documentação 0 / 30 / 70 / 110 / 140 (alvará) / 180 (RI) · Imagens 45 / 125 / 140 / 150 · Orçamento 80 → 120 (1ª revisão) → 140 · Maquete 125 → 185 · Takes 150 → 190.

Três convergências: **dia 125** (2º tiro + início da maquete, 15 dias antes do alvará — as duas frentes de venda arrancam antes da aprovação sair), **dia 140** (alvará + 3º tiro + orçamento final) e **dia 150** (HR de imagens e início dos takes no mesmo dia, sem folga). **O fim do cronograma sai dos takes, não da documentação** — a documentação ocupa 180 dias mas não é o caminho crítico.

Related: [[project_next]], [[feedback_output_folder]], [[feedback_reconferir_versao_atual]]
