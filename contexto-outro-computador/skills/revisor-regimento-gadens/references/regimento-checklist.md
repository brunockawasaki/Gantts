# Completude estrutural de um Regimento — Grupo Gadens

Estrutura de referência: template `RE.GG.PRO.001 - MODELO PADRÃO DE REGIMENTO`. Um Regimento
completo tem 9 seções. Ausência de qualquer uma delas é **[E]**. Presença da seção mas com
conteúdo genuinamente incompleto por dentro é o que a lista abaixo ajuda a identificar — mas
lembre-se da regra central do SKILL.md: só aponte **ausência de estrutura**, nunca o mérito de
um valor que já existe.

## 1. Objetivo
Texto corrido. Deve deixar claro qual reunião/comitê o regimento rege e por que ele existe.
- Objetivo genérico demais (copiado de outro regimento, não específico deste comitê) → [C]:
  perguntar à área se está correto.

## 2. Aplicação
Texto corrido — empresa(s) a que o regimento se aplica (Geral, Make It, Gadens, Triunfo, ULTJ).
- Se a Aplicação menciona só uma empresa mas o conteúdo (Áreas Envolvidas, Papéis) claramente
  fala de ambas → [C], perguntar se é proposital.

## 3. Áreas Envolvidas
Texto corrido listando as áreas que participam do comitê/reunião.
- Toda área citada aqui deve aparecer também na tabela de Papéis e Responsabilidades (seção 5).
  Se uma área está em Áreas Envolvidas mas não na tabela → **[E]**, papel ausente da tabela.

## 4. Governança e Operacionalização
Tabela Item/Definição com 5 linhas fixas esperadas:
- **Convocação/Agendamento** — quem convoca, com quanto tempo de antecedência.
- **Periodicidade** — de quanto em quanto tempo a reunião acontece.
- **Formato** — presencial/remoto/híbrido. **"Formato não especificado no texto de origem" é
  uma lacuna real a apontar [C]**, não um erro de transposição se a fonte realmente não dizia.
- **Pauta/Material de Apoio** — o que é discutido e o que precisa ser preparado antes.
- **Registro/Ata** — como a reunião é registrada.

Pontos específicos a verificar dentro desta seção:
- **Quórum e participantes obrigatórios**: se o regimento não define quem precisa estar
  presente para a reunião ser válida, isso é **[E]** (ausência de estrutura esperada de uma
  reunião deliberativa) — comparar com o regimento "irmão" mais completo da mesma família só se
  o Bruno pedir explicitamente (ver "O que esta skill não faz" no SKILL.md); por padrão, apontar
  a ausência sem comparar.
- **Regra de deliberação**: como a decisão é tomada (maioria, consenso, alçada de quem preside)
  — ausência é [E].
- **Consequência de reunião não realizada**: o que acontece se o comitê não se reunir (a
  atividade trava? segue com risco assumido? quem decide?) — se ausente, [E] (é uma lacuna de
  estrutura, especialmente relevante quando o comitê é gate de uma fase de processo).
- **Prazo e local de armazenamento da ata**: se a seção define prazo de entrega da ata mas não
  onde ela fica armazenada (ou vice-versa), é [E] — falta metade da estrutura esperada.
- **Frase "Prazos de devolução"** (ou similar, nos Outputs): historicamente um ponto frágil —
  conferir se a frase tem sentido gramatical completo. "De deverá e programado uma entrega aos
  participantes" é um exemplo real de frase quebrada encontrada — isso é [E], reescrever.

## 5. Papéis e Responsabilidades
Tabela Área/Responsabilidades.
- Toda área mencionada em Áreas Envolvidas (seção 3) deve estar aqui — ver acima.
- Toda área citada dentro da Pauta ou dos Inputs/Outputs (seções 6/7) como responsável por algo
  deve também aparecer nesta tabela — se não aparecer, [E].

## 6. Entradas do Processo / Inputs
Tabela Input/Descrição/Responsável.
- Cada input citado na Pauta (dentro da seção 4) deveria ter uma entrada correspondente aqui, e
  vice-versa. **Duplicação quase literal entre Pauta e Inputs** (o mesmo conteúdo escrito duas
  vezes com pequenas variações) não é exatamente um erro objetivo de estrutura, mas indica que
  um dos dois deveria remeter ao outro em vez de repetir — apontar como [C] ou [D] conforme o
  caso (ver teste da regra central: é decisão de como organizar o documento, não ausência de
  estrutura).
- Se o mesmo input (ex.: "Status de gastos") aparece com **responsáveis diferentes** na Pauta e
  nos Inputs, isso é contradição interna → **[E]**, apontar as duas menções e pedir para
  unificar.

## 7. Saídas do Processo / Outputs
Tabela Output/Descrição/Responsável.
- O rótulo do output deve ser o resultado/decisão da reunião, não o nome do comitê em si (ex.:
  output rotulado só "Comitê X" em vez de "Ata de decisão do Comitê X" ou "Aprovação/Reprovação
  de X") — [E], renomear o rótulo.
- Ver também a checagem de "Prazos de devolução" citada na seção 4 acima — a mesma frase
  costuma aparecer aqui.

## 8. Referências
Texto corrido.
- Toda referência citada no corpo do documento (ex.: "conforme o Fluxo X" ou "Ver Processo de
  Y") deve estar listada aqui. Se não estiver, [E] — referência citada e não listada.
- Se a seção diz "não há documento oficial como referência" mas o corpo cita processos/POPs
  nominalmente, isso é uma contradição interna → [E], e vale perguntar [C] se os nomes citados
  são o mesmo documento com nomes diferentes (histórico real: "POP Congelamento de Alterações de
  Fase" vs. "PO.CM.PJC.001 Controle de Alterações de Projeto" podem ser o mesmo documento).

## 9. Controle de Emissão
Tabela Revisão/Etapa/Itens Revisados/Data — ver seção 7 do `qld-002.md` para o formato exato
esperado (célula "Etapa" com Elaboração/Aprovação, não colunas separadas).
- Placeholder de data não preenchido (`XXXX/2026`, `00/00/0000`) → [E], placeholder ausente.
- Ver o guarda-corpo do SKILL.md antes de apontar qualquer divergência de revisão/data contra a
  capa como se fosse uma revisão anterior real.

## Checagem transversal (quando houver mais de um Regimento na mesma família sendo revisado
## JUNTO, só se o Bruno pediu explicitamente essa comparação)

- Convocação alternada entre áreas diferentes sem critério declarado (ex.: um comitê convocado
  pela Incorporação, outro pelos Projetos Complementares, sem explicação) → [C], perguntar se é
  intencional.
- Abrangência (Aplicação) restrita a uma empresa quando os processos relacionados (referenciados
  nas Referências) claramente envolvem as duas → [D], decisão de escopo do projeto.
