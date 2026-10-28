# Roteiro testado — montar o formulário no Microsoft Forms via Chrome

Roteiro validado em produção (jul/2026, Forms em pt-BR, viewport ~1568px de
largura). Coordenadas citadas são referência daquela sessão: **use-as como
expectativa, não como verdade** — confirme cada alvo na captura de tela mais
recente antes de clicar. Se a janela do usuário tiver outro tamanho, recalibre
tudo pelas capturas.

## Preparação

1. Carregue as ferramentas do Claude in Chrome em UM ToolSearch só
   (tabs_context_mcp, navigate, computer, read_page, find, form_input,
   get_page_text, browser_batch, list_connected_browsers).
2. `list_connected_browsers` — confirme extensão conectada; senão, peça ao
   usuário para conectar e pare.
3. Navegue para `https://forms.office.com/Pages/DesignPageV2.aspx`.
   - **Fique em forms.office.com.** `office.com` e outros domínios costumam ser
     negados pela permissão da extensão.
   - Conta sem formulários mostra tela de boas-vindas com 4 cartões de cenário
     (Feedback/Registro/Pesquisa/Teste) e nenhum botão "em branco". Clicar num
     cartão (ex.: Registro) **abre NOVA ABA** com rascunho "Formulário sem
     título" já em modo edição — use essa aba (pegue o tabId novo no retorno) e
     feche o painel lateral de modelos no X.

## Título e descrição

Clique no título → campo entra em edição com texto selecionado → digite por
cima. Clique na descrição → digite. Depois de digitar qualquer campo, a página
reflui: **screenshot antes do próximo clique**.

## Ciclo por pergunta (o coração da automação)

Estado estável após criar pergunta + rolar: card selecionado com título em
y≈387, campo de subtítulo em y≈429, rodapé de toggles em y≈520 (Resposta longa
x≈943, Obrigatória x≈1082, menu "..." x≈1206), botão "Adicionar nova pergunta"
~50px abaixo do rodapé.

Para cada pergunta, DOIS lotes (browser_batch):

**Lote A — abrir o menu (nunca encadear às cegas):**
1. Clicar "Adicionar nova pergunta" (posição lida da última captura).
2. wait 1s → **screenshot**. O menu de tipos (Opção/Texto/Classificação/...)
   pode abrir mais acima ou mais abaixo; pegue a posição real de "Texto".

**Lote B — criar e configurar:**
1. Clicar "Texto" → wait 1s → o foco cai no título da nova pergunta → digitar o
   título.
2. `scroll down 4` (normaliza o layout para o estado estável acima).
3. Toggles ANTES do subtítulo (o subtítulo de 2 linhas desloca tudo):
   - "Resposta longa" em (943,520). Ao ligar, o rodapé desce ~21px (vai a ~541).
   - "Obrigatória" em (1082, 520 ou 541 conforme o passo anterior).
4. Clicar o campo "Insira um subtítulo" (795,429) → digitar a dica com a
   etiqueta `[POP · Seção X — Nome]` no final.
5. **screenshot** de fechamento (vira a calibração do próximo Lote A).

### Regras de herança (economizam cliques)

- **Obrigatória HERDA** da pergunta anterior. Sequência otimizada: perguntas
  1–5 obrigatórias em cadeia; desligue na 6; religue só no passo a passo (e
  desligue de novo na seguinte).
- **Resposta longa NÃO herda** — ligue em cada pergunta de conteúdo.
- O campo de subtítulo visível herda depois que a primeira pergunta o usa (via
  menu "..." → "Subtítulo" na primeira vez; depois já aparece).

### Armadilhas conhecidas (todas já aconteceram)

- **Encadear "Adicionar → Texto → digitar" sem screenshot no meio** pode clicar
  no vazio: o texto se perde e os cliques de toggle caem na PERGUNTA ANTERIOR,
  invertendo configurações dela. Se um lote falhar assim, confira a pergunta
  anterior (zoom no rodapé) e corrija antes de seguir.
- **Subtítulo de 2 linhas** empurra o botão "Adicionar" ~24px para baixo — não
  reutilize a posição da rodada anterior sem conferir.
- **Toggle é confirmado com zoom**, não com fé: `zoom` na região do rodapé
  mostra o estado real (vermelho = ligado). Verifique sempre as obrigatórias e
  qualquer clique de toggle feito após o subtítulo.
- Cliques logo após digitação podem "gastar o clique" fechando a edição do
  campo. O screenshot do Lote A já dá o tempo de assentar.

## Verificação final

1. Botão "Visualização" → `get_page_text`: confira todas as perguntas, ordem,
   subtítulos e etiquetas.
2. Na captura da visualização, confira os asteriscos `*` das obrigatórias.
3. Volte com "Voltar".

## Tema da marca

Estilo → aba "Personalizado" → botão "+" → ícone do balde → campo "Hex #" →
digitar `C0272D` → Enter. **Criar o swatch NÃO aplica o tema**: é preciso
clicar no swatch vermelho recém-criado na lista e confirmar que o fundo do
canvas ficou vermelho.

## Limites (não negociáveis)

- **Não clicar "Coletar respostas"**, não gerar/copiar link, não compartilhar —
  quem decide o público do formulário é o usuário. Apenas informe onde fica.
- Não criar perguntas de nome/e-mail/data — o Forms interno registra sozinho.
- O formulário fica salvo automaticamente ("Salvo" no topo) em Meus formulários.
