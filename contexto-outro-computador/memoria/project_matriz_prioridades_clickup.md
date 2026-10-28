---
name: project-matriz-prioridades-clickup
description: "Matriz de prioridades 1-4 das atividades do ClickUp (Projeto Next): lógica, números, arquivos, o que o Bruno decidiu, o que está em aberto e como buscar os dados"
metadata:
  node_type: memory
  type: project
  originSessionId: b3f3cea1-f242-4fed-9cfc-7187c96cb2ce
  modified: 2026-10-27T20:47:46.840Z
---

**Pedido (21/10/2026):** Bruno, analista de Processos, pediu uma matriz **simples e racional** para dar prioridade 1 Baixa, 2 Normal, 3 Alta, 4 Urgente às atividades da lista "Implantação de Melhorias (5W2H)" (id 901321384887), **ignorando as prioridades que já estão no ClickUp**. Os 4 níveis casam com as bandeiras nativas do campo Prioridade (cinza, azul, amarela, vermelha). Ele leva a proposta ao **chefe** para validar; **nada foi aplicado no ClickUp**.

## Arquivos (pasta `...\1. Bruno Kawasaki\Projeto teste`)
- `Matriz de Prioridades - ClickUp Projeto Next.xlsx`: matriz com 401 abertas (21/10), 12 âncoras pontuadas por mim, resto em branco.
- `Matriz de Prioridades - Material para Analise.docx`: 9 págs. que explicam a lógica; tabelas espelham a planilha (não é objeto embutido; ofereci embutir, sem resposta).
- `Sugestao de Prioridades - Urgente e Alta.xlsx` (27/10): **todas as 979 atividades, todos os status** (398 abertas, 502 concluídas, 79 canceladas). Abas Leia-me, Resumo, Urgente (56), Alta (166), Todas (fórmulas vivas) e Parametros. 515 pontuadas à mão por mim (nome da atividade + contexto lido); as outras 464 pela regra base limitada a nota 3. Verificado: 9.028 fórmulas, 0 erros, notas batendo com Python; não vista renderizada.
- `Claude\CLAUDE.md`: instruções do projeto. Checklist antigo em Word: superado (Bruno não aprovou).

## Lógica (tudo proposta minha, sem validação do chefe)
Nota = média ponderada de 5 critérios (1-5, com régua escrita): risco de fraude e erro 30, impacto financeiro 20, obra e entrega 20, legal/CEF/compliance 15, dependência 15 → × fator do processo (0,9 a 1,1; média de 3 notas: dinheiro, dependência, irreversibilidade) → + ajuste da natureza (controle +0,3; documento/automação/definição 0; treinamento -0,2; indicador -0,3). Cortes: Normal ≥2,5, Alta ≥3,3, Urgente ≥**3,9**. Vetos: risco 5 vira no mínimo Alta; "para obra ou repasse CEF" vira Urgente. **Esforço fica fora da nota**, só ordena dentro da categoria.
**Why:** misturar importância, prazo e esforço esconde tarefa importante e difícil (ex.: Plano de Alçadas); processo de apoio (Financeiro) pode ter risco alto, por isso o fator é pequeno.

## Resultado de 27/10
Urgente 56 (5,7%), Alta 166 (17,0%), dentro das faixas de referência (5-10% e 15-25%); Urgente+Alta 22,7% do total. Corte de Urgente baixado de 4,0 para 3,9 (com 4,0 dava 4,2%, abaixo do mínimo de 5%). **Nas 398 abertas, Urgente 32 + Alta 108 = 35,2%, acima da trava de capacidade de 30%.** Acima do limite de 3 Urgentes abertas por pessoa: Bruna 8, Alexandre 6, Alessandro 5; o Alexandre tem 103 das 398 abertas (26%). Comercial: quase tudo em Alta (39 das 119 abertas), só 4 Urgentes. Topo: alçadas, controles de dados bancários/acesso/pagamento, medição, segurança do trabalho, repasse ao terreneiro.

## O que o Bruno decidiu
- Ignorar prioridades atuais do ClickUp; analisar o **total, todos os status**; gostou da ideia e vai discutir com o chefe; computador padrão = DESKTOP-IS1HAB3 ([[reference_computador_padrao]]); criar o CLAUDE.md na pasta Claude; escolheu a **opção 1 de memória** (arquivos de memória + CLAUDE.md, não o plugin claude-mem; plugin só com aval da TI).
- Esclarecido a pedido dele: "erro grave" não é campo; o critério chama "Risco de fraude e erro". Sugeri renomear para "Risco de desvio ou erro grave" (ou só "Risco de fraude"); **ele ainda não escolheu**.

## Em aberto
1. Chefe validar pesos, cortes, vetos, fatores dos processos. 2. Nome do critério de risco. 3. Aprovar corte de Urgente 3,9. 4. A matriz ordena a entrega ou mede exposição? 5. Quem pontua, quem confirma, quem decide pesos finais. 6. Gadens e Make It: nota única ou separada. 7. Gravar no campo Prioridade ou só na planilha. 8. Campo numérico "Nota final" no piloto. 9. Faixas reais de R$ (Financeiro). 10. Significado das bolinhas/caixas vermelhas do macro FL.GG.PRO.01 e onde fica o GMO. 11. Qual consultoria fez o quê (apresentações citam União Consultoria; Bruno citou Falconi). 12. Embutir a planilha no Word?

## Integração com o assistente de cadastro (não feita)
Assistente em `Claude\Assistente ClickUp` (tem CLAUDE.md próprio) cadastra tarefas a partir das planilhas de dores, com acesso total à lista. Plano proposto: caminho A (piloto) = assistente sugere as 5 notas + esforço com motivo e confiança e escreve **comentário** com a categoria; prioridade segue "normal" (regra dele) até alguém confirmar; só tarefas novas; baixa confiança = "a pontuar". Caminho B = campos novos. As regras do CLAUDE.md do assistente continuam valendo.

## Como buscar dados do ClickUp
O conector (MCP) devolve tudo inline, não grava em arquivo e **não traz campos personalizados** (Processo, Tipo de Ação). Em 21/10 e 27/10 usei a API (GET, só leitura) com o token que o Bruno colou na conversa, por variável de ambiente; **nunca gravar o token**; ele foi orientado a revogar. Pedir autorização e token novo antes de usar de novo. Tarefas "cancelado" não vêm como fechadas na API (filtrar). Scripts ficaram só no scratchpad; as notas estão na aba Todas.

Ver também [[reference_clickup_5w2h]], [[project_next]], [[reference_projeto_next_pasta_leitura]], [[feedback_material_para_chefe]].
