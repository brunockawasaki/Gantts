---
name: gdocs-elaborar-pop-merge
description: G-Docs (painel do Organizador) incorpora os formularios Elaborar POP, IT e Regimento (repo Levantamento-de-Processos) como telas do menu; como atualizar quando os formularios mudarem
metadata:
  node_type: memory
  type: project
  originSessionId: 07b58c78-1214-4327-b49a-05bcb057e688
  modified: 2026-10-08T12:22:45.694Z
---

O painel G-Docs (`organizador de documentos/painel-organizacao-documentos.html`, publicado em brunockawasaki.github.io/Organizador-de-documentos/) tem menu lateral com telas (Resumo, Documentos, Favoritos, grupo "Elaborar" com POP/IT/Regimento, Fale comigo, Modelos e ajuda). "Elaborar POP/IT/Regimento" NAO sao iframe nem atalho: o codigo dos formularios do repo `brunockawasaki/Levantamento-de-Processos` e copiado para dentro do painel. Cada um fica em `#elab-root` (POP), `#elit-root` (IT) e `#elrg-root` (Regimento), com CSS escopado, JS em IIFE com um "document" falso que so enxerga o proprio root (ids repetidos como q1/btn-enviar nao colidem; ids id_* do IT/Regimento viram it_id_*/rg_id_*). Cada formulario guarda seus dados no localStorage com chave propria.

**Fontes:** POP = `Projeto teste/Formulário de Levantamento de Processo - Interativo - Grupo Gadens.html`; IT = `Projeto teste/Levantamento de IT/Formulário de Levantamento de IT - Interativo - Grupo Gadens.html` (gerado a partir do de POP por `montar_formulario_it.py`; ver [[project_formulario_it]]); Regimento = `Projeto teste/Levantamento de Regimento/Formulário de Levantamento de Regimento - Interativo - Grupo Gadens.html` (gerado por `montar_formulario_regimento.py`, com exemplos de 4 regimentos publicados). O repo local `Projeto teste` E o repo Levantamento-de-Processos (remote origin) — commitar so o arquivo desejado (`git add -- "arquivo"`), nunca `git add .`.

**Why:** Bruno quis "um sistema so", nao um atalho. Iframe nao serve porque o Artifact do Claude bloqueia sites embutidos.

**How to apply:** quando Bruno pedir para atualizar Elaborar POP/IT com o codigo do GitHub, fazer `git pull` no repo e rodar `python atualizar_formularios.py <POP.html> <IT.html> <Regimento.html> <painel-organizacao-documentos.html>` (script na pasta `organizador de documentos`). Ele regera CSS, marcacao e JS dos DOIS formularios e reaplica os ajustes (aviso na tela no lugar de alert, copia alternativa, erros do microfone, sem botao de tema/balao proprios). Falha de proposito se algum trecho esperado mudou. Depois: testar em servidor local (.claude/launch.json "painel-local", porta 8765), publicar no Artifact, so subir ao GitHub (clone `Projeto teste/org-docs-repo`, com backup `.backup-AAAA-MM-DD-...html` quando for mudanca grande) quando Bruno pedir. Artifact bloqueia download, microfone, area de transferencia, alert e confirm: testar isso so no GitHub Pages. Exemplos reais dos botoes "?" do POP vem de 8 POPs publicados (conferidos palavra por palavra); a pergunta 17 ficou sem exemplo.
