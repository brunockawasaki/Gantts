# Gantts — Cronogramas do Grupo Gadens (Crédito Imobiliário)

Repositório de cronogramas (Gantt) em HTML, com prazo ideal x prazo real, análise do projeto e menu por empresa (Gadens e Make It). Hoje tem Horizon e Now (Make It, financiamento CEF). Dono: Bruno Kawasaki (Processos e Melhoria Contínua). A planilha de origem é preenchida pela Danielle.

## Como falar com o Bruno
- Português simples e direto: frases curtas, palavras comuns, sem jargão sem explicar. Ele não é desenvolvedor.
- Nunca invente data, prazo, percentual, responsável ou motivo. Tudo vem da planilha ou dele. Falta dado: diga que falta e pergunte. Inferência vai escrita como inferência ("confirmar com o setor").
- Se houver mais de uma leitura possível, pergunte antes de construir ou publicar. Já houve caso de publicar uma opção sem confirmar e ter de desfazer.
- Pergunta do tipo "é possível?" ou "não execute" pede só a resposta: o que sugere e o principal ponto de atenção, sem mexer em arquivo.
- "Grupo Gadens" já inclui Gadens Incorporadora e Make It. Não escreva "Grupo Gadens e Make It".

## Regra principal: GitHub só com sim
- Trabalhe **só no HTML local**. **Nunca faça `git commit` nem `git push` sem perguntar "Posso subir para o GitHub?" e receber um "sim" claro.** Pedido de ajuste no HTML não é pedido para publicar. Um "sim" vale só para aquela publicação.
- O repositório é **privado** (privado desde 28/10/2026) e o site (Pages) está **desligado**: os links públicos pararam. Ele guarda memórias e skills em `contexto-outro-computador\`. **Não torne público de novo sem avisar**: o histórico inteiro ficaria visível. Não suba planilhas de origem sem ele pedir.
- Antes de subir, mostre `git status` (só os arquivos esperados). Depois do push, confira com `git status -sb` e `git log origin/main -1`. Não há site para conferir.
- Resposta final curta: o que mudou, o que foi testado, o que **não** foi testado e se algo foi publicado.

## Onde está cada coisa
- **Pasta local (clone):** `...\1. Bruno Kawasaki\Gantts\` (fora da pasta `Projeto teste`, para não ficar um repositório dentro do outro).
- **GitHub (privado):** https://github.com/brunockawasaki/Gantts. O site antigo (`brunockawasaki.github.io/Gantts`) está desligado. Para ver, abra os arquivos `index.html`, `make-it\index.html` e `cronogramas\<Projeto>.html` da pasta local.
- **Fonte da verdade:** `dados\*.json` (tarefas, durações, progresso, motivos e texto da análise; `_meta` com empresa, posição e aba).
- **Gerador:** `ferramentas\gerar.py` (só biblioteca padrão). Escreve `cronogramas\`, `make-it\` e `index.html`. **Esses arquivos são gerados: nunca edite à mão.** Visual = `ferramentas\modelo_gantt.html`, `modelo_empresa.html`, `modelo_menu.html`.
- **Conferir planilha:** `ferramentas\conferir_planilha.py "<planilha.xlsx>"` (só lê; precisa de `openpyxl`). Logo novo: `ferramentas\preparar_logo.py`.
- **Agente:** `agents\gantt-cronogramas.md` (cópia em `Projeto teste\.claude\agents\`). Descreve o passo a passo e já manda perguntar antes de subir.
- **Planilha de origem atual:** `Downloads\PLANILHA DANIELLE 1.xlsx` (16/10/2026). Abas HORIZON, NOW, ESSENCE, Palácio, Silva Jardim. Colunas: Solicitante, Atividade, Responsável, Protocolo, Prazo Ideal, Prazo Real, Motivo do Desvio.
- **Checklist enviado à Danielle:** `Projeto teste\Checklist de Correções - Planilha Danielle (Essence, Now, Horizon).docx`.
- O Gantt do Comercial (`fluxo-lancamentos-comercial\`) é independente e **fica fora do menu**.

## Fluxo de trabalho (seguir sempre)
1. Conferir a planilha: `python ferramentas\conferir_planilha.py "<planilha>"`. Ler as diferenças.
2. Atualizar `dados\<projeto>.json`. Campos: `id`, `nome`, `fase`, `etapa`, `responsavel`, `duracao`, `inicio` (protocolo), `depende`, `progresso`, `marco`, `referencia` (prazo ideal), `aberta` (em andamento sem previsão), `solicitante`, `motivo`, `prazoIdealPlan`, `prazoRealPlan`. **O andamento (%) não vem da planilha: pergunte ao Bruno.**
3. Atualizar `_meta.posicao`, rodar `python ferramentas\gerar.py` e ler os números antes de escrever a `analise`.
4. Reescrever a `analise` (críticos, atenção, observações; no máximo 5 itens cada; cada item diz o quê, onde e quanto). Rodar o gerador de novo.
5. **Testar localmente** (ver abaixo). Parar. Perguntar se pode subir.

## Como testar
- Copie `cronogramas`, `assets`, `make-it` e `index.html` para `Projeto teste\_preview_gantts\` e sirva com a entrada `levantamento-local` (porta 8766) do `.claude\launch.json`. **Ao terminar, pare o servidor e apague a pasta `_preview_gantts`.** O `launch.json` é compartilhado: leia antes e só acrescente entrada, nunca sobrescreva.
- O painel embutido não mostra arquivo local (`file://`) nem o endereço `localhost` de outra porta. Use a prévia acima.
- Confira: sem rolagem lateral em tela larga; nenhum texto cortado ou sobreposto; números do menu iguais aos do cronograma; em tamanho de celular, **arraste o gráfico para o lado** e veja se marco, % e barras passam por baixo da coluna do nome (nunca por cima).
- Não declare que algo está certo sem medir na página montada (cor, posição, sobreposição). Já houve cor trocada sem conferir e o resultado saiu errado.

## Regras do gráfico (iguais no `modelo_gantt.html` e em `gerar.py`)
- Uma linha por tarefa, **na ordem da planilha** (nunca ordenar por data).
- Em cada linha: barra **verde** = prazo ideal da etapa (início e fim); marco **◆** = início real (o popup traz o motivo do desvio); barra real logo abaixo.
- Cores do real: **azul** = dentro do prazo; **amarelo `#FFD600`** = começou depois do início ideal, ainda dentro do prazo ideal; **laranja `#E8662A`** = tudo o que passa do fim do ideal (ou que começa depois dele). Concluída fica na cor pura; só a tarefa em andamento escurece a parte feita (% feito). Previsão = tracejada. Contorno vermelho = caminho crítico. Linha de "hoje" roxa.
- Prazo ideal = cadeia de **uma passada, 58 dias** (10+21+8+8+8+3), decisão do Bruno. Cada linha usa a janela ideal da sua **etapa**; rodadas repetidas e retrabalho caem fora da janela e ficam laranja. Não troque pela soma linha a linha da planilha sem perguntar.
- Tarefa já iniciada com `inicio`: vale a data informada. A iniciar: `inicio` é "não antes de" e a dependência pode empurrar.
- `aberta: true`: barra até a data da posição; as etapas seguintes ficam **sem data** e o término aparece como "sem previsão".
- Barra curta ganha largura mínima (40 px) para caber o %. Coluna do nome sempre acima do gráfico (z-index). Navegação aponta para `index.html` (funciona também ao abrir o arquivo do computador).

## Já tentado e recusado (não repetir)
- Visual do Gantt do Comercial nos projetos da CEF; painel lateral de detalhes; esmaecer as outras linhas; popup flutuante cobrindo as linhas.
- Notas de rodapé explicativas nas páginas ("largura mínima", "agrupamento é nosso", "Análise feita em...").
- Logo da Gadens colorida enquanto o botão está "Em breve" (fica cinza; ganha cor sozinha quando houver projeto da Gadens).

## Em aberto (em 26/10/2026)
- **Essence:** aguardando a planilha corrigida. A aba mistura anos (R.I 22/07/2025, protocolos 2026, datas de dezembro/2026 já com prazo real, assinatura em 05/01/2026) e a Conformidade está contraditória. O Bruno chegou a escolher "usar como está", mas isso quebra o gráfico. Não criar o Essence sem os anos confirmados.
- **Now:** Risco do empreendimento em andamento desde 26/08, sem previsão de término. Falta a previsão e o andamento.
- **Horizon:** falta a data de início e o andamento (%) da Risco P03 (hoje 30%, valor antigo) e confirmar se o "ideal 17" é o prazo novo da CEF.
- **Palácio e Silva Jardim** (são Gadens): só têm prazos ideais. Não criar sem dados reais.
- Posição dos dados: 16/10/2026. Para atualizar, regerar.
- Logo da Make It é JPG pequeno (447 px).

## Ambiente técnico (Windows)
- Sem Node.js. Python tem `openpyxl`, `python-docx` e `pillow`. Rode `python` **sem** `-I` quando precisar de `openpyxl` (o modo isolado não enxerga os pacotes do usuário).
- `git` pelo PowerShell: o `git push` mostra um "erro" vermelho (`NativeCommandError`) mesmo com sucesso; a linha `a..b main -> main` confirma. Avisos de CRLF são normais.
- Caminho curto `BRUNO~1.KAW` (8.3) engana o Git e o Bash; para clonar ou testar, use o caminho longo ou copie para pasta com nome normal.
- Para ver Word/PDF como imagem: ver memória `reference_render_word_pdf_windows` (Word COM por reflection + leitor de PDF do Windows).
- Checklist Word: formato fixo (título centralizado, subtítulo cinza em itálico, cabeçalho azul-marinho, `☐` + linha de resposta, Arial 10). Ver memória `feedback_checklist_trabalho_format`. Os números de linha no Word são os do Excel (linha da planilha), não a posição na lista.

## Memória
Detalhes ficam em `C:\Users\bruno.kawasaki\.claude\projects\C--Users-bruno-kawasaki-OneDrive---Grupo-Gadens-1--Bruno-Kawasaki-Projeto-teste\memory\` (índice em `MEMORY.md`). Principais: `project_gantt_cef_horizon_now`, `feedback_github_perguntar_antes`.
