---
name: feedback-transposicao-estrita-template
description: "Bruno's standing rule for transposing raw/source documents into Grupo Gadens templates (Regimento, IT, POP): never invent new structural elements or formatting"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6b831697-41c0-4ca9-bef9-9676cf65e9c3
  modified: 2026-08-05T12:56:22.182Z
---

Quando um documento fonte tem conteúdo que não corresponde a nenhum título do template padrão (ex.: uma seção "Definições" no PO original, sem equivalente no template de Regimento), a única ação permitida é **encaixar esse conteúdo dentro de um título que já existe no template**, desde que faça sentido — nunca descartar o conteúdo, e nunca criar um título novo fora dos que já existem no template.

Dentro de um título/tabela existente, é proibido inventar formatação ou estrutura que não está presente no template em branco: nada de negrito novo (ex.: "Responsabilidade:" em negrito), nada de listas com marcadores (bullets) se o template não usa bullets, e nunca mover conteúdo para fora de uma tabela/célula do template para "resolver" um problema visual. Use exatamente o estilo de parágrafo que a célula/título já tem.

**Por quê:** Bruno corrigiu isso duas vezes seguidas no Regimento CERP (PO.GG.PJC.004) — eu (1) descartei a seção "Definições" do PO original por não ter título correspondente no Regimento, e (2) movi a pauta detalhada dos comitês para fora da tabela de Governança e usei negrito/bullets inventados, justificando por um bug visual (célula de tabela muito extensa quebra em várias páginas com coluna em branco ao lado). Bruno deixou claro: a missão é transpor para o template, com permissão apenas para reencaixar conteúdo sem título correspondente dentro de um título existente — nunca criar estrutura nova nem reformatar além do que o template já define. Mesmo que o resultado visual de uma célula de tabela muito longa (coluna vazia ao lado, quebra de página no meio do texto) pareça ruim, isso é aceitável e não deve ser "corrigido" inventando uma estrutura fora do template.

**Como aplicar:**
- Antes de mover qualquer conteúdo para fora de uma tabela/célula do template, ou de adicionar negrito/bullets que não existem no estilo original daquela célula, PARAR e não fazer — encaixar o texto como parágrafo(s) simples dentro da célula/título já existente, mesmo que fique denso.
- Se o conteúdo fonte tiver uma seção sem título correspondente no template (ex. Definições, um Fluxo BPMN, etc.), decidir em qual título existente ele melhor se encaixa (ex.: Definições coube dentro do título "1. OBJETIVO", como texto corrido) e perguntar ao Bruno apenas se a escolha não for óbvia — nunca simplesmente omitir o conteúdo.
- Isso vale para todos os templates de transposição: Regimento (RE.GG.PRO.001), IT (IT.GG.PRO.001), POP. Ver [[regimento_template_workflow]] e [[pop_it_template_workflow]].
