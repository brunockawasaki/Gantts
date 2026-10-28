# Metodologia BPMN do Grupo Gadens

Fonte: "MÉTODOLOGIA BPMN PARA MAPEAMENTO.docx" (documento interno do Projeto Next). Se o Bruno
avisar que esse documento foi revisado, atualizar este arquivo antes de continuar revisando
fluxogramas — não confiar em memória de conversas antigas sobre o que ele dizia.

## Elementos essenciais (notação oficial usada no Grupo Gadens)

### Eventos
- **Evento Inicial** — círculo com borda fina **verde**. Início do processo. É obrigatório
  informar o que gerou a necessidade do processo (o gatilho), não só desenhar o círculo vazio.
- **Evento Intermediário** — círculo com borda fina **amarela**. Algo ocorre no meio do fluxo:
  SLA, link, condicional, mensagem, entre outros.
- **Evento Final** — círculo com borda grossa **vermelha**. Encerramento do processo — pode ser
  o fim do processo inteiro ou o fim para uma área específica dentro de um fluxo com raias.

### Atividades
- **Tarefa/Task** — retângulo de cantos arredondados. Subtipos pelo ícone:
  - **Usuário Tarefa** (ícone de humano) — atividade usando sistema/plataforma/app.
  - **Serviço Tarefa** (ícone de engrenagem) — automatizada, sem ação humana.
  - **Receber Tarefa** (carta sem preenchimento) — recebimento de demanda (e-mail, telefone,
    sistema de mensagens).
  - **Envio Tarefa** (carta com preenchimento colorido) — envio de demanda.
  - **Manual Tarefa** (ícone de mão) — atividade humana sem meio sistêmico, "manual" de verdade.
  - **Subprocesso** — retângulo de borda tracejada com "+". Agrupa outro fluxo detalhado à parte.

### Gateways (decisões) — os 3 usados no Grupo Gadens
- **Exclusivo** (losango com "X") — escolha entre caminhos alternativos, **OU** exclusivo (só um
  caminho é seguido).
- **Paralelo** (losango com "+") — caminhos executados **simultaneamente** (E).
- **Inclusivo** (losango com "O") — um **ou mais** caminhos podem ser seguidos (E/OU).

(O Grupo Gadens não usa gateway por evento como padrão — se aparecer num fluxograma, tratar como
desvio de notação a confirmar, não como elemento esperado.)

### Artefatos
- **Objeto de Dados** — informação usada ou gerada pelo processo (ex.: necessidade de elaboração
  de POP ou IT).
- **Anotação** — comentário/observação adicional para contextualizar a atividade.
- **Armazenamento de Dados** — plataformas, sistemas, sites usados para realizar as atividades.

### Piscinas e raias
- **Pool (piscina)** — representa uma organização ou processo principal.
- **Lane (raia)** — representa uma área ou papel responsável.

## Boas práticas (usar como critério de completude/qualidade)

1. **Mantenha a simplicidade** — evitar diagramas excessivamente complexos.
2. **Nomes claros** — sempre verbo + complemento (ex.: "Aprovar Contrato"). Um nome de atividade
   que é só um substantivo ("Contrato", "Aprovação") é apontamento.
3. **Valide com quem executa** — o processo desenhado deve refletir a realidade operacional, não
   uma versão idealizada.
4. **Padronize a modelagem** — usar as convenções corporativas acima, não inventar símbolo.
5. **Mantenha atualizado** — fluxo desatualizado gera retrabalho e risco.

## Erros mais comuns (checklist direto de apontamento [E])

- Diagrama gigante sem necessidade (sinal: dezenas de tarefas numa raia só, ou fluxo que dá para
  quebrar em subprocessos e não foi).
- Responsável não definido (raia sem dono claro, ou tarefa fora de qualquer raia).
- Misturar processo atual (AS-IS) e processo futuro (TO-BE) no mesmo diagrama sem marcação clara
  de qual é qual.
- Não validado com especialista do processo (não dá para checar isso só olhando o desenho — vira
  pergunta [C] ao Bruno/área, nunca uma afirmação).
- Ignorar sistemas e documentos envolvidos (atividade que claramente usa um sistema, sem
  Armazenamento de Dados/Objeto de Dados correspondente).

## Para que serve o BPMN (referência ao interpretar, não checklist de erro)

Não serve só para documentar — serve para encontrar gargalos, eliminar desperdícios, identificar
riscos, estruturar automações, melhorar indicadores, aumentar eficiência, reduzir custos e apoiar
decisões estratégicas. Isso é o pano de fundo da leitura analítica (ver
`references/gargalos-heuristicas.md`) — os apontamentos [E]/[C]/[D] de notação são só metade do
trabalho desta skill.

## Dinâmica de aprovação (contexto — não é algo que esta skill valida sozinha)

1. Fluxograma desenhado junto com as áreas mapeadas, para coletar os detalhes.
2. Fluxo editado com base nas boas práticas acima.
3. Submetido à aprovação dos gestores de cada setor envolvido.
4. Apresentado aos Diretores para esclarecimento e aprovação final.

Se o fluxograma revisado ainda não passou por uma dessas etapas, isso pode explicar lacunas
encontradas — vale mencionar no resumo final, não como erro do documento.
