---
name: reference_clickup_5w2h
description: "ClickUp \"Implantação de Melhorias (5W2H)\" — IDs de lista/campos, regras de preenchimento (Área, Diretoria, Demandante, etiquetas) e armadilhas ao cadastrar tarefas"
metadata:
  node_type: memory
  type: reference
  originSessionId: 3dcd900f-5a53-4521-bc57-5c0c7e95418d
  modified: 2026-10-20T21:01:59.148Z
---

Lista: "Implantação de Melhorias (5W2H)" (id 901321384887, pasta Projeto Next, workspace 9013344143). Bruno user id 118051003.

Campos (ids): Área (texto) a27aee2f-f293-4c31-bd1c-22ab50e42f34; Área/Departamento (dropdown, valor = UUID da opção) 632e082a-874d-4286-9647-98e9683c599f; Diretoria (texto) 878d75a6-9494-4cdb-9cd8-2385f0c243f5; Demandante (users, valor `{"add":[id]}`) cabfc237-2ba0-41f4-99b7-f62f4f4e9493; Processo c2eebdfb-4d18-4380-8bae-bbd2b9e332d1; Tipo de Ação 7972ebf5-090a-474f-9276-05f684862d99; Data de reprogramação 07743692-7ea0-4a95-9c4d-a26f1e22e97f; Causa do desvio e5f58cef-a874-4b05-ae06-741e5ae76f8a; Ação corretiva 17dd80e4-ac06-47d6-b3dd-5391a608cf2d.

Regras que o Bruno definiu ao cadastrar itens das planilhas "Comercial - Dores" e "GMO - DORES" (Projeto Next / 2. Processos):
- Área e Área/Departamento = área do responsável (Alexandre → Projetos e Sistemas; Hellen → Planejamento e Controle; Edgard → Jurídico; Paulo → Contabilidade; Lizandra → GMO; Fernando de Souza → Obras; Bruna → Administrativo; Roberto Dias → TI).
- Diretoria por área: Marcelo Cerqueira (Projetos e Sistemas, Jurídico, Contabilidade, Administrativo, TI, Controladoria), William Raphalski (GMO, Planejamento e Controle, Obras), Lincoln Gadens (Marketing, Comercial Gadens), Thiago Gadens (Incorporação Gadens, Secretaria de Vendas).
- Processo (texto livre, mas a checagem diária só aceita: Novos Negócios, Incorporação Make It, Incorporação Gadens, Engenharia e GMO, Engenharia, GMO, Suprimentos, Financeiro, Comercial Gadens, Comercial Make It) = igual à etiqueta: "Comercial Gadens" / "Comercial Make It" / "GMO" — nunca só "Comercial" nem "Incorporação"; Tipo de Ação = "Ação de melhoria"; status "sem prazo definido"; prioridade normal; etiqueta "comercial gadens" / "comercial make it" (cada ação do Comercial existe em 2 versões) ou "gmo".
- Itens com demandado = Bruno ou "Processos" NÃO se cadastram (são do Bruno).
- Demandante da planilha "Processos"/em branco fica vazio.

**Why:** evitar retrabalho; o Bruno pediu essas regras explicitamente.
**How to apply:** ao cadastrar tarefas novas dessa lista, reaplicar as regras e mostrar um exemplo antes; sempre conferir duplicidade lendo a lista inteira (filter_tasks pagina de 100; a busca por palavra do ClickUp não é confiável — volta vazia).

Armadilhas: usuário sem acesso à lista (ex.: Tamires Goes) não pode ser responsável (erro "All assignees must have access"); uma tarefa ganhou sozinha a etiqueta "comercial make it" (conferir etiquetas depois de criar).

- Tipo de Ação por prefixo do nome: "Implementar indicador..." → "Indicador"; "Elaborar POP"/"Elaborar IT"/"Elaborar Política" → "Documento Normativo"; demais → "Ação de melhoria". Combinado em 20/10/2026 (Bruno confirmou).
