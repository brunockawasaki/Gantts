---
name: project-dashboard-next-bumblebee
description: Como o dashboard do Projeto Next (http://bumblebee/relatorios/projetonext/) é gerado; onde estão os scripts, template e histórico
metadata:
  type: project
---

Dashboard "Gestão de Processos — Projeto Next" = 1 HTML autossuficiente (dados embutidos, Chart.js). Gerado por Python, não editado à mão.

**Pasta de origem:** `C:\Users\bruno.kawasaki\OneDrive - Grupo Gadens\Processos - Documentos\Processos Grupo Gadens\1. Projetos\1. Projeto Next\3. ProjetoNext_Dashboard` (tem repo git próprio).

**Fluxo:** `atualizar_tudo_v2.py` -> `gerar_dashboard_v3.py` (ClickUp API lista 901321384887 + contagem Bizagi .bpm + Colaboradores xlsx) injeta placeholders (`__TASKS__`, `__HM_DATA__`, `__FLUXOS__`...) em `dashboard_template_v2.html` -> grava `ProjetoNext_Dashboard_v2_LATEST.html` + versão com data -> copia p/ `\BUMBLEBEE\ProjetoNext` e `\BUMBLEBEE\relatorios\projetonext\index.html`. Depois capturar_dashboard*.py (prints) e gerar_apresentacoes.py (slides). Histórico semanal em `historico_snapshots.json`; checagem diária em `Validação ClickUp/Checagem_ClickUp_*.xlsx` (checar_erros_clickup.py).

**Regras-chave:** melhoria = tarefa que NÃO começa com "elaborar pop/regimento/it/pol" nem "implementar indicador" (ou é subtarefa); status EM ATRASO/SEM PRAZO são derivados da data; Engenharia+GMO = um processo; nunca inventar histórico filtrado.

**Pontos de cuidado (ver 2026-10-20):** token ClickUp tem fallback hardcoded no .py (usar env CLICKUP_TOKEN); rodapé fixo "Jun/2026"; lista de processos do filtro é hardcoded no template; `dashboard_template_v2_teste.html`/`_TESTE.html` são testes em andamento de 20/10/2026; script antigo v2 tem caminho fixo do OneDrive do Carlos (v3 corrige).

**Why:** Bruno pediu para aprender o código p/ criar/manter dashboards no futuro; não executar nada nele sem pedido. **How to apply:** só ler; para mudar, editar o template/script e regenerar, nunca o HTML final.

**Template (dashboard_template_v2.html):** HTML+CSS+JS únicos (~1.670 linhas; 616KB são o logo base64 na linha 291). Placeholders: `__DATE__ __TASKS__ __DONE_*__ __SP_*__ __ATR_*__ __HM_DATA__ __COLABORADORES__ __FLUXOS__ __ATIVIDADES__ __SOL_RUPT__ __MELHORIAS__ __POPS__ __INDICADORES__`. Tema: CSS vars `--tk-cXXXXXX` (escuro) + `THEME_PALETTE_LIGHT` JS + função `C('#hex')` (cores no JS devem passar por C()); localStorage `projetonext_theme`. Seções por id (`sectionHeatmap`, `sectionTabelaAtraso`...). Entrada: `render()` -> `renderV2()` + `buildHeatmap()`. Teste de 20/10: heatmap em 3 faixas fixas (pouco/médio/alto = terços do máximo) no `_teste`.

**checar_erros_clickup.py:** importa `gerar_dashboard_v2` (não o v3!) p/ token/fetch. Roda 08:00 (Tarefa Agendada Windows), ignora concluídas, gera `Validação ClickUp/Checagem_ClickUp_AAAA-MM-DD.xlsx` (Erro/Atenção). Regras: campos obrigatórios (Processo, Prioridade, Diretoria, Área, Tipo de Ação, responsável); Em Progresso exige prazo e não pode estar vencido; Em Atraso exige Causa do desvio + Ação corretiva (+ reprogramação = atenção); reprogramações sucessivas contadas em `historico_reprogramacoes.json`; ortografia pt-BR (pyspellchecker + dicionario_projeto.txt); Tipo de Ação x prefixo do nome; responsável inativo; responsável x área/diretoria conforme planilha Colaboradores (mapas de apelidos no topo do script).
