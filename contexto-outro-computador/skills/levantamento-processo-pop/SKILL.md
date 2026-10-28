---
name: levantamento-processo-pop
description: >-
  Gera formulários de levantamento de processo em linguagem leiga para embasar a
  elaboração de POPs (Procedimentos Operacionais Padrão) do Grupo Gadens, em dois
  formatos: Word com identidade visual da marca (logo, vermelho/cinza) e/ou
  Microsoft Forms montado via automação do Chrome — sempre com cada pergunta
  mapeada à seção do POP em que a resposta será usada. Use sempre que o usuário
  pedir formulário ou questionário de levantamento/coleta de processo, quiser
  transformar um modelo de POP em perguntas para quem não conhece POPs, pedir a
  versão Forms de um formulário de processo, ou precisar coletar informações de
  executores para escrever/padronizar um procedimento — mesmo que não use a
  palavra "POP" (ex.: "formulário para o time descrever a rotina", "coletar como
  o setor faz X para documentar").
---

# Formulário de Levantamento de Processo (base para POP)

## Objetivo

O analista de processos precisa que executores leigos descrevam como uma rotina
funciona hoje, para depois transcrever as respostas para o POP oficial. Esta
skill gera o instrumento de coleta em dois formatos:

| Formato | Quando usar | Resultado |
|---|---|---|
| **Word + PDF** (padrão) | Preenchimento à mão, por e-mail ou impresso | Docx A4 ~6 páginas com identidade visual, salvo na pasta do projeto |
| **Microsoft Forms** | Coleta digital com respostas caindo no Excel | Formulário na conta M365 do usuário, montado via Chrome |
| **HTML interativo** | Preenchimento digital sem tocar na conta M365 (offline, por e-mail/OneDrive) | Arquivo único .html com autosave, salvo na pasta do projeto |

Se o usuário não disser o formato, pergunte. Na dúvida ou sem acesso ao Chrome
logado, gere o Word — é rápido e não toca na conta Microsoft.

## Estrutura de POP de referência

Modelo padrão Grupo Gadens (PO.GG.QLD.001), 12 seções: 1 Objetivo · 2 Aplicação ·
3 Referências · 4 Definições (tabela de siglas) · 5 Recursos necessários (5.1
Sistemas, 5.2 Documentos/entradas, 5.3 Papéis-chave) · 6 Principais passos ·
7 Papéis, responsabilidades e autonomia · 8 Indicadores · 9 Pontos críticos ·
10 Desvios/ações · 11 Registro do processo · 12 Controle de emissão.

**Controle de emissão, código do documento, aprovações e fluxo Bizagi ficam FORA
do formulário** — são preenchidos pela equipe de Processos/Qualidade. Avise isso
no fechamento do formulário para o leigo não travar nessas partes.

Se o usuário fornecer **outro modelo** de POP (.docx), extraia a estrutura antes
de gerar: descompacte (`unzip`) e leia os textos de `word/document.xml` com
Python (`xml.etree`; capture parágrafos, estilos e células de tabela). O pandoc
normalmente NÃO está instalado nessas máquinas. Depois adapte o banco de
perguntas seguindo a mesma lógica de tradução (seção técnica → pergunta leiga).

## Princípios das perguntas (valem para os dois formatos)

- Tom de "explique a um colega novo no setor"; zero jargão de qualidade.
- Toda pergunta tem **exemplo concreto** de resposta na dica/subtítulo.
- Convenção anti-trava: "se não souber, escreva 'não sei'; se não se aplicar,
  'não se aplica'" — dita nas instruções iniciais.
- **Etiqueta de transcrição** `[POP · Seção X — Nome]` em cada pergunta: quase
  invisível para o leigo, mas vira o mapa do analista na hora de escrever o POP.
- Obrigatórias mínimas: identificação, objetivo (seção 1) e passo a passo
  (seção 6). O resto é opcional de propósito.
- Tabelas do Word viram "um item por linha" no Forms (Forms não tem tabela).

O banco completo de perguntas, textos de abertura e configurações está em
[references/banco-de-perguntas.md](references/banco-de-perguntas.md) — **leia
antes de gerar qualquer versão**.

## Versão Word

1. Dependência: `python-docx` (`python -m pip install python-docx` se faltar).
2. Rode o gerador pronto:
   ```
   python scripts/gera_formulario_word.py --saida "<pasta do projeto>\Formulário de Levantamento de Processo - Base para POP - Grupo Gadens.docx"
   ```
   Logo em `assets/logo_gadens.png` (usado por padrão); cores da marca já
   embutidas: vermelho `C0272D`, cinza `58595B`. Só edite o script se o usuário
   pedir mudança de conteúdo/layout.
3. **Verifique visualmente antes de entregar**: converta em PDF e renderize as
   páginas em PNG (LibreOffice e pdftoppm normalmente não existem; use os
   scripts prontos que usam Word COM e WinRT):
   ```
   powershell -File scripts/docx_para_pdf.ps1 -DocxPath <docx> -PdfPath <pdf>
   powershell -File scripts/render_pdf.ps1 -PdfPath <pdf> -OutDir <pasta>
   ```
   Leia os PNGs e confira: barras de seção com etiqueta, linhas de exemplo em
   cinza, tabelas com cabeçalho repetido, rodapé com paginação.
4. Entregue `.docx` (editável) + `.pdf` (impressão) na pasta do projeto.

## Versão HTML interativa

Use quando o preenchedor não tem acesso ao Word (ou prefere digital) e não se quer
mexer na conta M365 do usuário — por exemplo, distribuição em massa por e-mail/
OneDrive/celular sem depender de Forms.

- Modelo pronto (já com o conteúdo do banco de perguntas, cores da marca e logo
  embutido em base64) em `assets/formulario_interativo.html`. Copie esse arquivo
  para a pasta do projeto e renomeie; normalmente não é preciso editar nada.
- 100% autossuficiente e offline: um único arquivo, sem CDN/servidor, abre com
  duplo clique em qualquer navegador (inclusive celular), responsivo.
- Autosave em `localStorage` (restaura ao reabrir o mesmo arquivo no mesmo
  navegador/computador), barra de progresso, tabelas dinâmicas com "+ adicionar
  linha", botão "Baixar respostas (.txt)" organizado por seção do POP com as
  etiquetas, botão "Salvar em PDF" (`window.print()`) e botão "Limpar tudo".
- Obrigatórias (destacadas ao exportar, sem travar navegação): nome, e-mail,
  área dona do processo, empresa do grupo, data, nome da tarefa (bloco de
  identificação), pergunta 1 (objetivo) e ao menos 1 linha do passo a passo.
- Se o usuário pedir mudança de conteúdo/layout, edite o array `QUESTIONS` no
  `<script>` do HTML (mesma lógica de tradução do banco de perguntas) — não
  reescreva do zero.
- **Botão "Enviar Respostas (gerar Word)"**: gera, 100% no navegador (sem
  internet, sem IA, sem servidor), um `.docx` já no modelo oficial
  PO.GG.QLD.001, preenchido com as respostas. Funciona substituindo
  `{{marcadores}}` dentro de uma cópia do template embutida em base64 no
  próprio HTML — o `.docx` original em "1. Padrões" nunca é tocado. Usa a
  biblioteca `fflate` (MIT, embutida inline, sem CDN) para ler/escrever o zip
  do docx.
  - Template marcado: `assets/template_pop_marcadores.docx` (gerado por
    `scripts/tag_template_docx.py` a partir do original). Se o padrão oficial
    do POP mudar de layout, rode o script de novo e reembuta o resultado no
    HTML (ver `scripts/gera_formulario_word.py` como referência de como este
    tipo de embed em base64 é feito).
  - Mapeamento pergunta → marcador está direto no código, na função
    `buildFilledDocumentXml` do HTML: perguntas de texto único (objetivo,
    aplicação, referências) substituem um marcador simples; perguntas de
    tabela/lista (siglas, sistemas, entradas, papéis-chave, passos macro,
    indicadores, pontos críticos, papéis/autonomia, desvios, registro) clonam
    a linha/item de exemplo do template uma vez por resposta preenchida.
  - A seção "Principais passos do processo" do Word é alimentada pela
    pergunta extra "etapas macro" (não pela tabela detalhada de passo a
    passo) — foi adicionada especificamente para isso, porque resumir a
    tabela detalhada em etapas macro exigiria julgamento humano/IA, e a ideia
    é que esse botão funcione sem depender de IA.
  - Código do documento, revisão, aprovadores e a tabela "Controle de
    emissão" nunca são tocados — ficam para a equipe de Qualidade, como
    sempre.
- Verifique sempre antes de entregar: abra no navegador, preencha dados de
  teste, recarregue para confirmar o autosave, baixe o .txt e confira o
  conteúdo por seção, confira a visualização de impressão.

## Versão Microsoft Forms

Automação real na conta corporativa do usuário — **leia antes o roteiro testado
em [references/forms-automation.md](references/forms-automation.md)**, que traz
o ciclo de criação de perguntas, as regras de herança de configurações e as
armadilhas conhecidas (com correções).

Regras que não mudam:
- Use o Claude in Chrome (sessão logada). Permaneça em `forms.office.com` — o
  domínio `office.com` costuma estar fora da permissão da extensão.
- Nome, e-mail e data de quem responde o Forms registra sozinho em formulário
  interno — não crie perguntas para isso.
- Tema da marca: Estilo → Personalizado → "+" → Hex `C0272D` (criar o swatch
  não aplica; é preciso clicar nele depois).
- **Nunca clique em "Coletar respostas" nem compartilhe o link** — escolher quem
  responde é decisão do usuário. Diga onde fica o botão e pare aí.

## Entrega final (sempre)

- Resumo com o mapeamento pergunta → seção do POP (tabela curta).
- O que ficou de fora de propósito (controle de emissão, código, aprovações).
- No Forms: oriente "Exibir respostas → Abrir no Excel" (cada coluna já carrega
  a etiqueta da seção) e o passo manual de "Coletar respostas".
- Ofereça ajustes (mais linhas no passo a passo, versão enxuta, outra pergunta).
