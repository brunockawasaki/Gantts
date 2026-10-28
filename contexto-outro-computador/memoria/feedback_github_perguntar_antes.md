---
name: feedback-github-perguntar-antes
description: Nos Gantts (repo brunockawasaki/Gantts) trabalhar só no HTML local; nunca fazer commit/push sem perguntar antes e esperar o sim do Bruno
metadata:
  node_type: memory
  type: feedback
  originSessionId: 97e90818-3850-44fb-820a-5bed6ef2cec6
  modified: 2026-10-20T14:08:24.349Z
---

A partir de 20/10/2026, o trabalho nos Gantts (clone local `...\1. Bruno Kawasaki\Gantts`, repositório https://github.com/brunockawasaki/Gantts, privado desde 28/10/2026) fica **só no HTML local**. **Nunca fazer `git commit` nem `git push` sem perguntar antes e receber um "sim" claro.** Pedido de ajuste no HTML não é pedido de publicar.

**Why:** até então eu publicava a cada ajuste (e o repositório era público, com dados do Grupo; hoje é privado). O Bruno quer revisar localmente e decidir quando vai ao ar. Já houve caso em que publiquei uma opção sem confirmação e tive de desfazer.

**How to apply:** editar `dados/*.json` / `ferramentas/modelo_*.html`, rodar `python ferramentas/gerar.py` e conferir no navegador local (copiar a pasta para `Projeto teste/_preview_gantts` e servir com `levantamento-local`, apagando a cópia depois). Ao terminar, dizer o que mudou, que **nada foi publicado**, e perguntar "posso subir para o GitHub?". Só então commit + push + conferir o envio (`git status -sb`; não há site, o Pages está desligado). O arquivo do agente (`agents/gantt-cronogramas.md`, passo 7) já foi ajustado para perguntar antes. Ver [[project-gantt-cef-horizon-now]].
