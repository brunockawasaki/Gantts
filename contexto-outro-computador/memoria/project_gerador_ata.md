---
name: project-gerador-ata
description: "Formulário \"Elaborar Ata\" (gera Word no padrão ATA.docx) em Projeto teste/Levantamento de Ata e incorporado ao painel G-Docs; padrão da Ata sem código/revisão"
metadata:
  node_type: memory
  type: project
  originSessionId: 79e3e099-0e4c-492f-b36b-2b589f7f173e
  modified: 2026-10-14T21:27:41.927Z
---

Criado em 2026-10-14 a pedido do Bruno ("projeto de gerador de atas dentro do Organizador-de-documentos, no formato dos demais"). O padrão da Ata é o arquivo `...\1. Bruno Kawasaki\1. Padrões\1. Padrões\ATA.docx`: uma página, sem capa, "ATA DE REUNIÃO" + logo no topo, 4 seções (Pauta, Decisão, Outputs, PARTICIPANTES), rodapé Tipo de documento | Elaborador | Data. **Sem código e sem controle de revisão** (Bruno: "só para formalização de decisões de reuniões"). Outputs levam responsável e data de entrega ("Output – Responsável – DD/MM/AAAA;"). Assinatura não faz parte (só se a ata for impressa e Bruno pedir). Meu primeiro modelo (com capa e tabelas, derivado do Regimento) foi descartado por ele.

Pasta `Projeto teste/Levantamento de Ata/`: `montar_modelo_ata.py` (ATA.docx -> MODELO ATA com marcadores), `montar_formulario_ata.py` (POP html + modelo -> formulário), LEIA-ME. Mesmo padrão de [[project_formulario_regimento]]. Diferença técnica: o clique de gerar também preenche `word/footer1.xml` (Elaborador = nome de quem preenche, Data = data da reunião).

Painel: `organizador de documentos/atualizar_formularios.py` agora recebe 5 argumentos (POP, IT, Regimento, Ata, painel) e também cria o item "Ata" no menu Elaborar (root `#elat-root`, view `elaborar-ata`, ids `at_id_*`). Testado em servidor local (gerou Word com pauta, decisão, outputs, participantes e rodapé). Copiado para o clone `Projeto teste/org-docs-repo` com backup `.backup-2026-10-14-pre-elaborar-ata.html`, SEM commit/push — só subir ao GitHub quando Bruno pedir (ver [[gdocs_elaborar_pop_merge]]).
