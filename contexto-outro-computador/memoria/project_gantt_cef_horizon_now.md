---
name: project-gantt-cef-horizon-now
description: "Repositório PRIVADO Gantts (desde 28/10/2026, Pages desligado) com os Gantts Make It (Horizon, Now; Essence pendente), menu Gadens/Make It com logos, gerador em ferramentas/gerar.py, planilha de origem e decisões já tomadas/pendentes"
metadata:
  node_type: memory
  type: project
  originSessionId: 97e90818-3850-44fb-820a-5bed6ef2cec6
  modified: 2026-10-16T12:12:41.207Z
---

**Repositório:** https://github.com/brunockawasaki/Gantts, **privado desde 28/10/2026** (o Bruno pediu; o site do Pages caiu e os links públicos pararam). Guarda também a pasta `contexto-outro-computador/` (memórias e skills). Clone local: `...\1. Bruno Kawasaki\Gantts`. Menu principal: **Gadens** ("em breve", logo em cinza) e **Make It** (Horizon e Now). A logo ganha cor sozinha quando a empresa tem projeto (Bruno pediu para manter cinza até lá). Gantt do Comercial fica fora do menu (link direto).

**Como atualizar:** `dados/*.json` é a fonte da verdade (inclui análise e `_meta.posicao`); `python ferramentas/gerar.py` regera cronogramas e menus; `ferramentas/conferir_planilha.py` compara a planilha; fluxo completo no README e em `agents/gantt-cronogramas.md`. Páginas geradas não se editam à mão. Etapa em andamento sem previsão = `aberta: true` (barra até a posição; seguintes ficam "sem data").

**Planilha de origem:** versão mais recente `PLANILHA DANIELLE 1.xlsx` (Downloads, 16/10/2026): abas HORIZON, NOW, ESSENCE, Palácio, Silva Jardim. Colunas: Solicitante, Atividade, Responsável, Protocolo, Prazo Ideal, Prazo Real, Motivo do Desvio. **Linhas do Gantt seguem a ordem da planilha** (nunca ordenar por data). O andamento (%) não vem da planilha.

**Decisões do Bruno:** prazo ideal = uma passada de 58 dias (10+21+8+8+8+3), não a soma linha a linha. Palácio e Silva Jardim são **Gadens** (só têm prazos ideais, sem datas/real) — ainda não criados. Essence: Bruno escolheu "usar datas como estão (2026)", mas isso quebra o gráfico (assinatura 05/01/2026 antes do R.I 22/07/2026; várias datas em dez/2026 já marcadas como concluídas) — **ficou pendente confirmar** antes de criar.

**Preferências visuais:** formato do primeiro HTML (uma linha por tarefa, parte escura = % feito, linha de hoje), sem painel lateral, sem esmaecer, sem popups sobre informação; % sempre dentro da barra; sem notas de rodapé explicativas; menu centralizado na vertical; estilo do Comercial foi tentado e **rejeitado**. Quando houver mais de uma leitura, perguntar antes de publicar (publiquei "opção A" sem confirmar uma vez e tive de desfazer).

**Números em 16/10/2026:** Horizon termina 15/11 (ideal 24/09, +52). Now: Risco em andamento desde 26/08 (52 dias, ideal 8), sem previsão de término; ideal terminava 19/09.

**Pendente também:** (o repositório público expunha frases como "Jurídico não atendeu o prazo"; resolvido ao tornar privado em 28/10/2026); logo Make It é JPG pequeno; etiquetas "hoje" e "término ideal" se sobrepõem quando as datas são próximas em tela estreita.

**Why:** Bruno pediu "analisar, melhorar, não criar informações inexistentes".
**How to apply:** análise só com o que os dados mostram; marcar inferência como "confirmar". Ver [[feedback_no_fabricated_content]].
