---
name: feedback-executar-substitui-arquivo
description: "Quando Bruno pede para 'executar' um relatório/planilha já gerado, sempre sobrescrever o arquivo existente no mesmo caminho, nunca criar um novo arquivo/versão"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f8c0254b-98ac-4ea2-9e3a-d154330633e2
  modified: 2026-08-21T13:29:32.565Z
---

Quando Bruno pede para "executar" (reexecutar/rodar de novo) um relatório ou planilha que já foi gerado anteriormente, o resultado deve **sobrescrever o arquivo antigo no mesmo caminho/nome**, não criar um arquivo novo ou uma cópia com sufixo de versão/data.

**Why:** Instrução explícita de Bruno após pedir para reexecutar o levantamento de documentos prontos do Projeto Next — ele quer manter um único arquivo de referência sempre atualizado, não acumular versões.

**How to apply:** Ao reexecutar qualquer script/pipeline que gera um arquivo de saída (planilha, docx etc.) a pedido do Bruno, usar o mesmo `out_path`/nome de arquivo da execução anterior e salvar por cima. Vale para qualquer relatório/planilha reexecutável, não só o levantamento de documentos do [[project_next]].
