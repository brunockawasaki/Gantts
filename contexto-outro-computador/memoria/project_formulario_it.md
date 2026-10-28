---
name: project-formulario-it
description: "Formulário interativo de Levantamento de IT (versão por blocos, baseada na IT de Cadastro de CNO) — onde está, como funciona, como refazer e o que foi verificado"
metadata:
  node_type: memory
  type: project
  originSessionId: 0b51ec10-09dd-45f3-99ef-321f9e69ee3a
  modified: 2026-10-07T21:55:13.595Z
---

Em 2026-10-07 Bruno pediu "algo parecido com o formulário do repo Levantamento-de-Processos, mas para elaboração de IT". Decisões: arquivo HTML separado (não dentro do G-Docs ainda). **A 1ª versão (perguntas de obra: ferramentas, materiais, segurança, tabela de passos com coluna de imagem) foi REJEITADA** ("não gostei"). Ele mandou como modelo a IT.GG.CON.001 (Cadastro de CNO — IT de passo a passo em portal da Receita, com prints e tabelas Campo/Descrição) e pediu: perguntas e exemplos baseados nessa IT, e, na seção ETAPAS, a pessoa escreve e logo abaixo anexa/cola o print; "o mais fácil de preencher possível".

**Onde está:** `Projeto teste/Levantamento de IT/`. **Publicado em 2026-10-08** no repo público brunockawasaki/Levantamento-de-Processos (commit 74745a7, pasta `Levantamento de IT/`, só essa pasta foi adicionada — o repo local tem dezenas de arquivos pendentes que NÃO devem ir junto; usar sempre `git add -- "pasta"`, nunca `git add .`). Link: https://brunockawasaki.github.io/Levantamento-de-Processos/Levantamento%20de%20IT/Formul%C3%A1rio%20de%20Levantamento%20de%20IT%20-%20Interativo%20-%20Grupo%20Gadens.html (Pages leva ~1 min para atualizar após o push). Para atualizar: regenerar, copiar para a pasta, commitar só ela e dar push em main. `gh` não está instalado; git push funciona. Contém o HTML, `IT.GG.PRO.001 - MODELO IT com marcadores.docx`, `montar_modelo_it.py`, `montar_formulario_it.py`, LEIA-ME.txt.

**Como é (versão 2, por blocos):** perguntas 1–4 curtas (Objetivo, Aplicação, Referências, Definições) com "?" mostrando trechos reais da IT de CNO; pergunta 5 = Etapas montada em blocos na ordem: "+ Título" (Etapa/Subetapa/Item → 5.1, 5.1.1, numerados no Word pelo multinível), "+ Texto com imagem" (texto e, logo abaixo, "+ Imagem ou print": clicar, Ctrl+V ou arrastar), "+ Lista de opções" (marcadores), "+ Tabela Campo / Descrição". Blocos têm ↑ ↓ ×; cada caixa de texto tem microfone. Imagens: reduzidas a JPEG 1400 px, guardadas em localStorage (chave gadens_levantamento_it_v2), no Word com 13 cm de largura (máx. 12 cm de altura), centralizadas. Capa/cabeçalho/código/aprovações/Controle de Emissão ficam como no template (Processos preenche); só o título da capa recebe o nome da atividade. Objetivo/Aplicação ganham ponto final automático.

**Como refazer:** rodar `montar_modelo_it.py` (usa o template oficial de IT mais novo) e depois `montar_formulario_it.py <form POP.html> <modelo com marcadores.docx> <saida.html>` (comandos no LEIA-ME). O script falha de propósito se o formulário de POP mudou num trecho que ele altera.

**Verificado (2026-10-07):** gerei Word de teste no navegador, abri no Word real e conferi visualmente: numeração 5.x, tabela CAMPO/DESCRIÇÃO, lista, prints logo abaixo de cada texto, 4 páginas; reabrir a página restaura blocos e imagens. NÃO testado: modo por voz (cobre só perguntas 1–4 + identificação), celular, colar print real do clipboard (testado só anexar arquivo).

**Pendências possíveis:** Bruno validar o texto das perguntas; levar para o G-Docs como "Elaborar IT" (ver [[gdocs_elaborar_pop_merge]]); incluir o link do formulário de IT no G-Docs/Organizador.

Relacionado: [[pop_it_template_workflow]], [[reference_po_gg_qld_002]], [[reference_render_word_pdf_windows]].
