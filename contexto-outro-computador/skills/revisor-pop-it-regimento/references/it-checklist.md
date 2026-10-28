# Checklist de completude estrutural — IT (Instrução de Trabalho)

**Sempre rodar também `coerencia-interna.md` além deste arquivo** — cobre resíduo de instrução de
preenchimento, contradição interna de seção, consistência de termos/papéis, colunas que não
discriminam nada e redação básica; não é opcional.

Estrutura de **6 seções** do template oficial `IT.GG.PRO.001` — mais enxuta que POP (12 seções) e
Regimento (9 seções) de propósito: IT descreve o passo a passo de execução de uma tarefa
específica, não um processo de gestão com papéis/indicadores/desvios próprios. **Não apontar como
[E] a ausência de seções que uma IT genuinamente não tem** (Recursos Necessários, Papéis e
Responsabilidades, Indicadores, Pontos Críticos, Desvios/Ações, Registro do Processo) — essas são
seções de POP, não de IT, e sua ausência aqui é a estrutura correta do tipo, não uma lacuna.

Se uma seção existir mas estiver vazia, ou com só "Não especificado no texto de origem." herdado
da transposição, isso **não é automaticamente** um erro — só vira apontamento [C] pedindo para a
área preencher, nunca [E].

1. **OBJETIVO** — texto corrido explicando o propósito da instrução (o que a tarefa entrega/
   garante quando executada corretamente). Apontar [E] se estiver vazio ou for só uma frase
   genérica que não diz nada específico da tarefa.
2. **APLICAÇÃO** — deve dizer a Empresa/setor a que se aplica ("Empresa: X. Setores envolvidos:
   Y."). Apontar [E] se citar uma empresa que não existe na Tabela 3 do QLD.002.
3. **REFERÊNCIAS** — normas técnicas, POPs ou fluxos relacionados (ex.: PBQP-H 2021, ABNT NBR ISO
   9001:2015 – 7.5, ou um POP-mãe que a IT detalha). Apontar [C] se o corpo do documento citar uma
   norma/sistema/POP externo que não aparece aqui.
4. **DEFINIÇÕES** (Tabela 1 — Siglas e definições) — tabela Termo/Sigla | Definição. Apontar [E]
   se um termo técnico usado nas Etapas (ex.: uma sigla de material, equipamento ou sistema) nunca
   é definido aqui nem em nenhum outro lugar do documento.
5. **ETAPAS DA INSTRUÇÃO DE TRABALHO** — texto explicativo do passo + imagem por passo, quando
   aplicável. Isto é o núcleo da IT — verificar:
   - Numeração de passo sem lacuna (não pula de 3 para 5) **sem** que isso já esteja assim no
     texto-fonte original (se vier da fonte, é [C] perguntando à área se faltou descrever uma
     etapa).
   - Cada passo que menciona um EPI, ferramenta, material ou verificação de segurança/qualidade
     obrigatória mantém essa menção — não é papel desta skill julgar se a *técnica* descrita está
     certa (isso é opinião técnica de engenharia/obra, fora de escopo — ver regra de apontamento x
     opinião no `SKILL.md`), só se a estrutura do passo está completa (tem descrição + imagem
     quando o texto-fonte tinha imagem correspondente).
   - Se um passo referencia um material/ferramenta/sigla, essa referência deve estar coberta em
     "Definições" (seção 4) — apontar [E] se não estiver.
   - Imagem ausente onde o texto-fonte original claramente descrevia uma imagem/foto/diagrama para
     aquele passo é [C] (perguntar se a imagem foi perdida na transposição ou nunca existiu).
6. **CONTROLE DE EMISSÃO** (Tabela 2 — Revisão/Etapa/Itens Revisados/Data) — ver seção 7 do
   `qld-002-it.md` para as regras de Revisão/Status. Apontar [E] se "Status: Aprovado" aparecer
   sem data de aprovação preenchida.

## Perguntas de fechamento (usar só se ainda não respondidas pelos apontamentos)

- O código do documento (Tipo.Empresa.Setor.Sequência) foi confirmado com a área, ou foi inferido
  por falta de informação melhor? Se inferido, isso é sempre [C]/[D], nunca [E].
- Existe uma data de aprovação real, ou o documento ainda está "Em aprovação"?
- As imagens de cada etapa estão presentes e legíveis no arquivo final, ou só há placeholder/
  espaço reservado? (checagem de completude, não de qualidade técnica da imagem).
- Há alguma IT "irmã" (mesmo POP-mãe ou mesma família de execução de obra) que deveria ser
  comparada a esta para checar consistência de linguagem/formato? (só investigar se o Bruno pedir
  explicitamente e fornecer os documentos).
