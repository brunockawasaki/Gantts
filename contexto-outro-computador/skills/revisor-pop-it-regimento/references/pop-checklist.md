# Checklist de completude estrutural — POP (Procedimento Operacional Padrão)

**Sempre rodar também `coerencia-interna.md` além deste arquivo** — cobre resíduo de instrução de
preenchimento, contradição interna de seção, consistência de termos/papéis, colunas que não
discriminam nada e redação básica; não é opcional.

Estrutura de 12 seções do template oficial `PO.GG.QLD.001`. Para cada seção, o que precisa
existir para a seção ser considerada completa.

**"Não especificado no texto de origem." são DOIS apontamentos, não um** (correção de 2026-08-25 —
a versão anterior deste arquivo mandava tratar só como [C], e isso estava errado):

- **[E]** pela frase em si. "Texto de origem" é jargão do nosso processo de elaboração (o texto
  bruto que a área nos mandou) e não significa nada para quem vai ler o POP publicado. Um
  documento que circula na empresa não pode carregar marca do processo que o produziu — a frase
  tem que sair antes da vigência, independente do que entre no lugar.
- **[C]** pelo conteúdo que entra no lugar. A skill não sabe se a seção deveria mesmo ter conteúdo
  real ou se genuinamente não se aplica a este processo — isso é pergunta para a área. Se a
  resposta for "não se aplica", o texto correto é uma frase afirmativa em linguagem de documento
  publicado (ex.: "Este POP não possui indicadores próprios."), nunca a marca de transposição.

Seção que existe mas está genuinamente vazia (sem nem essa frase) é só [C].

1. **OBJETIVO** — texto corrido explicando o propósito do processo. Apontar [E] se estiver vazio
   ou for só uma frase genérica que não diz nada específico do processo.
2. **APLICAÇÃO** — deve dizer a Empresa/setor a que se aplica ("Empresa: X. Setores envolvidos:
   Y."). Apontar [E] se citar uma empresa que não existe na Tabela 3 do QLD.002.
3. **REFERÊNCIAS** — itens separados por "; ". Apontar [C] se o corpo do documento citar um
   fluxo/sistema/norma externa que não aparece aqui.
4. **DEFINIÇÕES** — tabela Termo/Sigla | Definição. Apontar [E] se um termo usado no corpo do
   documento (ex.: um papel, uma sigla de sistema) nunca é definido aqui nem em nenhum outro
   lugar.
5. **RECURSOS NECESSÁRIOS** — 3 listas: Sistemas / Documentos-Entradas / Papéis-chave. Apontar
   [E] se um papel citado nos Principais Passos ou na tabela de Responsabilidades não aparece em
   "Papéis-chave" (ou vice-versa). Documentos-Entradas pode legitimamente estar ausente se o
   processo não depende de nenhum documento de entrada — não forçar apontamento aqui sem
   evidência de que algo foi esquecido.
6. **PRINCIPAIS PASSOS DO PROCESSO** — lista numerada. Apontar [E] se a numeração pular um
   número (ex.: passo 3 direto pro 5) **sem** que isso já esteja assim no texto-fonte original
   (se vier da fonte, é [C] perguntando à área se faltou descrever uma etapa — ver guarda-corpo
   de fusão/transposição no `SKILL.md`). Apontar [E] se um passo menciona um responsável que não
   está em "Papéis-chave" nem na tabela de Responsabilidades.
7. **PAPÉIS, RESPONSABILIDADES E AUTONOMIA** — tabela Papel Funcional | Responsabilidades |
   Limites de Autonomia. Apontar [C] se "Limites de Autonomia" estiver como "Não especificado"
   para todos os papéis — perguntar à área se isso é intencional (nem todo processo tem níveis
   de alçada) ou se ficou faltando definir.
8. **INDICADORES** — texto + lista. A frase de abertura do template ("...diretrizes estratégicas
   de prospecção definidas neste POP:") é um resíduo de fábrica que **sempre** deve ter sido
   trocado por uma frase genérica — apontar [E] se ainda aparecer "prospecção" num POP que não é
   de prospecção. Se o processo genuinamente não tem indicador próprio, a frase "Este POP não
   possui indicadores próprios" (ou equivalente) é válida — não é [E].
9. **PONTOS CRÍTICOS DO PROCESSO** — lista. Se vazio/"Não especificado", vira [C] perguntando à
   área se há algum ponto de atenção conhecido que não foi documentado — nunca inventar um ponto
   crítico.
10. **DESVIOS / AÇÕES NECESSÁRIAS** — tabela Situação de Desvio | Ação Necessária | Responsável.
    Apontar [E] se a "Ação Necessária" descrita não resolve de fato a "Situação de Desvio"
    correspondente (contradição lógica), ou se o "Responsável" citado não está definido em
    nenhum outro lugar do documento.
11. **REGISTRO DO PROCESSO** — texto + tabela Identificação | Armazenamento. Apontar [C] se o
    sistema/local de armazenamento citado aqui não bate com os sistemas listados em "Recursos
    Necessários" (pode ser uma omissão real em um dos dois lados).
12. **CONTROLE DE EMISSÃO** — tabela Revisão | Etapa | Itens Revisados | Data. Ver seção 7 do
    `qld-002.md` para as regras de Revisão/Status. Apontar [E] se "Status: Aprovado" aparecer sem
    data de aprovação preenchida.

## Perguntas de fechamento (usar só se ainda não respondidas pelos apontamentos)

- O código do documento (Tipo.Empresa.Setor.Sequência) foi confirmado com a área, ou foi inferido
  por falta de informação melhor? Se inferido, isso é sempre [C]/[D], nunca [E].
- Existe uma data de aprovação real, ou o documento ainda está "Em aprovação"?
- Há algum POP "irmão" (mesma família/área) que deveria ser comparado a este para checar
  consistência de linguagem/formato? (só investigar se o Bruno pedir explicitamente e fornecer
  os documentos).
