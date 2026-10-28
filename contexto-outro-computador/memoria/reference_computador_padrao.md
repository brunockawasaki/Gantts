---
name: reference-computador-padrao
description: Computador padrão do Bruno desde 2026-10-26 (DESKTOP-IS1HAB3) e diferenças de ferramentas em relação ao outro (DESKTOP-D1V5L3V)
metadata:
  node_type: memory
  type: reference
  originSessionId: b3f3cea1-f242-4fed-9cfc-7187c96cb2ce
  modified: 2026-10-26T21:32:20.316Z
---

Em 2026-10-26 o Bruno disse que **este computador é o padrão agora, não o outro**. Padrão: `DESKTOP-IS1HAB3`, usuário `bruno.kawasaki`. O outro: `DESKTOP-D1V5L3V` (aparece no sufixo de arquivos de versão no OneDrive).

Neste computador funcionam `openpyxl`, `python-docx` e o Word e o Excel por COM com reflection. O `CLAUDE.md` da pasta `Claude\Assistente ClickUp` (escrito no outro computador) diz que não há openpyxl e que o Excel COM não funciona; **não herdar essa limitação sem testar**. O que não há aqui: LibreOffice, pdftoppm e o `recalc.py` da skill de planilha (ver [[reference_render_word_pdf_windows]]).

Em 2026-10-26 o Bruno disse também que está **aposentando o outro computador** (`DESKTOP-D1V5L3V`). Ele citou o IP 172.29.3.12 como o oficial, mas esta máquina (`DESKTOP-IS1HAB3`) respondeu 172.29.2.64; a divergência não foi esclarecida. IP de rede interna muda; guiar-se pelo nome (`hostname`), não pelo IP.

Depois o Bruno mandou só "NT2610261", sem explicar. Provável nome (hostname) ou patrimônio do computador oficial novo; não confirmado. Esta sessão rodou em `DESKTOP-IS1HAB3`, então se `NT2610261` for outra máquina, as ferramentas dela precisam ser testadas antes de herdar o que está aqui.

**Why:** o OneDrive sincroniza as pastas entre os dois computadores, então instruções escritas num podem descrever limites que não valem no outro.

**How to apply:** ao ler instruções de outro projeto, conferir se a limitação de ferramenta vale para a máquina atual (`hostname`). Pastas de projeto ficam em `...\1. Bruno Kawasaki\Projeto teste\Claude\` (ver também [[project_matriz_prioridades_clickup]]).
