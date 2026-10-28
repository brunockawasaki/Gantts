# Matriz de controles — genérica, qualquer área

Esta matriz substitui a ideia de "lista de riscos específicos de Suprimentos" da versão original
da skill. Ela é a parte que faz a auditoria achar coisa de verdade, e funciona em qualquer
processo operacional (Suprimentos, Fiscal, Orçamento, Obra, RH, Comitês) porque descreve
**famílias de controle**, não regras de uma área.

Para cada família, o teste é sempre o mesmo: **o documento descreve um controle real, ou só
descreve uma atividade?** Uma atividade diz o que fazer. Um controle diz o que impede, detecta ou
limita que a atividade dê errado, seja abusada ou seja feita por quem não devia.

## 1. Segregação de funções

Quem **solicita/pede** um processo não deveria também **aprovar**, **executar** e **conferir** o
mesmo evento sozinho. Ler o fluxo e listar, para cada decisão relevante, quem pede, quem aprova,
quem executa e quem confere. Se a mesma pessoa (ou o mesmo papel, não só o mesmo nome) aparece em
duas ou mais dessas quatro colunas para o mesmo evento, é um achado de PRC-03.

Perguntas de apoio:
- Quem pede o item/serviço/material é a mesma pessoa que aprova a compra ou a liberação?
- Quem recebe fisicamente é a mesma pessoa que confere contra a nota fiscal/pedido?
- Quem cadastra um fornecedor/item/parceiro é a mesma pessoa que depois usa esse cadastro sem
  segunda validação?
- Existe uma etapa de conferência **independente** de quem executou a etapa anterior, ou o
  documento presume boa-fé o tempo todo?

**Não é achado**: papéis diferentes que pertencem à mesma área/gerência quando a estrutura
organizacional real da empresa é pequena e não comporta mais segregação — nesse caso vira
**observação**, não risco, e citar o porte como limitação do achado.

## 2. Alçada e limite de valor/quantidade

Todo processo que envolve dinheiro, quantidade ou compromisso deveria ter um limite explícito a
partir do qual a decisão sobe de nível (valor de compra, quantidade retirada, prazo de exceção).

- O documento define algum limite numérico, ou usa linguagem vaga ("valores relevantes",
  "quantidade significativa") sem número, tabela ou remissão a política que tenha o número?
- Se define, o limite está no próprio documento ou remete a "política vigente" sem nomear qual?
  Remissão sem nome é DOC-06 (referência não resolvida).
- Existe um caminho para quando o valor/quantidade ultrapassa o limite normal, ou o processo só
  descreve o caminho padrão e nunca o caminho de exceção?

## 3. Evidência e registro

Todo controle que existe só na cabeça de alguém não é controle — precisa deixar rastro.

- Cada aprovação, conferência ou decisão do fluxo gera um registro (assinatura, sistema, e-mail,
  ata)? Ou o documento diz "o responsável aprova" sem dizer como isso fica provado depois?
- O registro permite reconstruir **quem** fez **o quê** e **quando**, ou só confirma que "foi
  feito"?
- Quando o documento promete rastreabilidade ("garantir controle", "assegurar rastreabilidade")
  mas a etapa que geraria esse rastro está ausente, isso é PRC-05 — a lacuna clássica de "o
  documento monitora um problema que ele mesmo não consegue enxergar" (mesmo padrão já visto em
  revisões de conteúdo da `revisor-pop-it-regimento`).

## 4. Exceção, urgência e desvio da rotina

Todo processo tem um caminho feliz e, mais cedo ou mais tarde, uma situação fora da rotina.

- O documento prevê algum tipo de exceção/urgência, ou só descreve o fluxo ideal?
- Se prevê, quem autoriza a exceção? É alguém com alçada real, ou o próprio executor pode se
  autoexcepcionalizar?
- A exceção tem algum controle a posteriori (revisão, relatório, regularização), ou uma vez
  aberta a exceção o processo nunca mais "fecha o ciclo" com controle normal?

## 5. Conflito de interesse

Aplica-se sempre que o processo envolve escolha de fornecedor, prestador, parceiro, ou qualquer
decisão em que a pessoa que decide poderia se beneficiar da própria decisão.

- O documento pede declaração de conflito de interesse antes de uma escolha relevante, ou é
  silencioso sobre isso?
- Existe alguma regra sobre parentesco, sociedade ou vínculo prévio com quem está sendo
  escolhido/cadastrado?
- Isso só vira achado quando o processo **de fato envolve escolha entre opções** (fornecedor,
  prestador). Processo puramente mecânico (ex.: devolver ferramenta ao almoxarifado) não precisa
  disso — não forçar o item aqui.

## 6. Continuidade e dependência de pessoa

- O processo depende de uma pessoa específica sem substituto previsto (ex.: só um aprovador
  citado por nome, sem cargo/papel substituto)?
- Existe algum SPOF (ponto único de falha) claro: um sistema, uma planilha pessoal, um e-mail que,
  se a pessoa sair de férias ou desligar, trava o processo inteiro?

## 7. Exposição de informação (INF-xx)

Ver `references/taxonomia-riscos.md` para os códigos completos. Resumo do que procurar:

- credencial, senha, chave de acesso, token — nunca reproduzir, só sinalizar a existência e a
  localização, mascarado;
- dado pessoal (CPF, RG, endereço, dado bancário de pessoa física) documentado sem necessidade
  clara para o processo;
- informação comercial estratégica (preço negociado, margem, condição especial de fornecedor)
  num documento com público amplo demais para o que ele contém;
- metadados residuais do arquivo (autor real, caminho de rede, comentários, alterações
  rastreadas) que revelam algo que o texto visível não revela — ver
  `references/extracao-metadados.md` para como olhar isso de verdade, não de memória.

## 8. Ciclo de vida documental (DOC-xx)

Isto é o que a `revisor-pop-it-regimento` já confere bem (estrutura, seções, template QLD.002) —
**não duplicar**. Aqui o foco é só: o documento está em uso real sem status de vigência claro?
Alguém pode estar seguindo uma minuta como se fosse norma aprovada? Isso é DOC-10 e é sempre
relevante, mesmo que a estrutura do documento esteja perfeita.

## Como transformar a matriz em achado

Para cada família acima que gerar um "sim, isso falta", escrever o achado no formato da seção
"Registro obrigatório de cada constatação" do `SKILL.md` — nunca como afirmação solta. E sempre
perguntar antes de escrever: **"se eu mostrar isso a quem executa o processo, ele reconhece como
risco real, ou é só uma lacuna de formulário?"** Se for só formulário, não é achado desta skill —
pode ser achado da `revisor-pop-it-regimento`, que audita estrutura.
