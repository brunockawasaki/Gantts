---
name: project-formulario-regimento
description: Formulário interativo de Levantamento de Regimento (gera Word no RE.GG.PRO.001) em Projeto teste/Levantamento de Regimento; como refazer e o que foi testado
metadata:
  node_type: memory
  type: project
  originSessionId: 6b831697-41c0-4ca9-bef9-9676cf65e9c3
  modified: 2026-10-08T15:54:27.118Z
---

Criado em 2026-10-08 a pedido do Bruno ("fazer parecido com o de POP, para regimentos, base no template e no modelo RE.GG.NNG.001"). Pasta: `Projeto teste/Levantamento de Regimento/` com o HTML, o modelo docx com marcadores, `montar_modelo_regimento.py`, `montar_formulario_regimento.py` e LEIA-ME.txt. Mesmo padrão do formulário de IT ([[project_formulario_it]]): deriva do formulário de POP (autosave, "?" com exemplos, modo por voz, progresso).

17 perguntas ligadas às 9 seções do template (mapa no LEIA-ME). Quórum, consequência de reunião não feita e prazos de ata/pendências entram como perguntas dentro de Convocação, Periodicidade e Registro/Ata (sem criar título novo — ver [[feedback_transposicao_estrita_template]]). Reunião com etapas (V0/V1/V2): a pessoa escreve a etapa no começo da linha; o template tem só uma tabela por seção.

Detalhes técnicos: texto com várias linhas vira um parágrafo por linha (`fillToken`), porque `<w:br/>` em texto justificado estica as palavras; listas usam bullet numId=2 com `contextualSpacing=0` e os títulos 4 e 9 também, senão o Word cola o título no último item da lista.

Testado: gerou Word no navegador (servidor local `levantamento-local`, porta 8766), abriu no Word real, 3 páginas, sem marcador sobrando, "?" abre. NÃO testado: modo por voz com as novas perguntas, publicação no GitHub Pages, inclusão no painel G-Docs ("Elaborar Regimento"). Só publicar/commitar (`git add -- "Levantamento de Regimento"`) quando o Bruno pedir.
