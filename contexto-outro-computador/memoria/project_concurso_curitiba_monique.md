---
name: project-concurso-curitiba-monique
description: "Material de estudos do concurso de Agente Administrativo da Prefeitura de Curitiba (FAFIPA, prova 13/12/2026) para a Monique; onde estão os arquivos e como refazer"
metadata:
  node_type: memory
  type: project
  originSessionId: 62ad9d04-0a4a-4020-9d0d-bc82214cbf0f
  modified: 2026-10-20T14:21:10.310Z
---

Bruno pediu material de estudo para a **Monique** (quem faz a prova): Edital Normativo 4/2026 da Prefeitura de Curitiba, banca Fundação FAFIPA, cargo Agente Administrativo, prova objetiva em 13/12/2026 (40 questões, 2,5 pontos cada, nota mínima 60 = 24 acertos, **erro não anula acerto**, 4 horas).

Tudo em `Projeto teste\Concurso Curitiba 2026\`: edital (PDF), subpasta `Leis` (14 leis em .html; **falta a Lei Orgânica de Curitiba**), plano de estudos (.xlsx e .docx), 6 simulados (.docx), `Caderno de Estudos` (.docx e .pdf, 135 páginas A4, margem interna para espiral), `Sistema de Estudos - Curitiba 2026.html` (sistema offline com leitura, treino, simulados cronometrados, caderno de erros, plano, progresso, backup) e `_fontes\` (scripts Python e template para regerar tudo; ver LEIA-ME.txt).

**Publicado (20/10/2026):** o sistema HTML está no repositório público https://github.com/brunockawasaki/FAFIPA (criado pelo Bruno, vazio), com GitHub Pages em https://brunockawasaki.github.io/FAFIPA/ (branch main, raiz; arquivos `index.html`, `README.md`, `.nojekyll`). Clone local: `...\1. Bruno Kawasaki\Estudos-Curitiba-2026` (separado de `Projeto teste`, que é outro repo). Commits com identidade local "Bruno Kawasaki" + e-mail noreply do GitHub (não expor o e-mail do Grupo). `gh` CLI não está instalado; push funciona com `git` pelo HTTPS. Para atualizar: regerar o HTML (`_fontes\export_data.py` e `build_sistema.py`), copiar para `index.html` do clone e **só commitar/pushar com pedido claro do Bruno** (ver [[feedback-github-perguntar-antes]]).

**Why:** o questionário e os arquivos foram feitos em várias etapas; as questões são elaboradas por mim (não oficiais), e as leis municipais (Estatuto 1.656/1958, Lei 7.671/1991) baixadas mostram a redação antiga, então o caderno traz só roteiro delas.

**How to apply:** para alterar conteúdo, editar os módulos em `_fontes` e rodar os builders; o Excel só recalcula via automação com `win32com.client.dynamic.Dispatch` (o PowerShell COM tipado falha). Conferir sempre datas e prazos no edital atual da FAFIPA. Ver também [[reference-render-word-pdf-windows]].
