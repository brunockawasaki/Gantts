---
name: feedback-launch-json-ler-antes
description: Em Projeto teste já existe .claude/launch.json com painel-local e levantamento-local; ler antes de editar e nunca sobrescrever
metadata:
  node_type: memory
  type: feedback
  originSessionId: 62ad9d04-0a4a-4020-9d0d-bc82214cbf0f
  modified: 2026-10-20T13:31:53.750Z
---

`Projeto teste\.claude\launch.json` é compartilhado por vários projetos (painel-local porta 8765, levantamento-local porta 8766). Em 20/10/2026 eu o sobrescrevi sem ler para testar um HTML; tive de reconstruir o conteúdo pelo histórico das sessões.

**Why:** perder as configurações quebra o preview de outros projetos do Bruno.

**How to apply:** antes de criar ou mudar o launch.json, **ler o arquivo** e só **acrescentar** uma entrada (porta nova, ex.: 8769); depois remover a entrada de teste. Não usar `cat >` para sobrescrever. Alternativa: testar HTML via servidor em outra pasta.
