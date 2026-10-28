# Extração de metadados e conteúdo residual de um .docx

Este é o passo que a versão original da skill citava (INF-07 "metadados e conteúdo residual") mas
nunca ensinava a fazer. Um `.docx` é um zip. Sem isso, o item nunca gera achado de verdade — vira
frase genérica de checklist.

Não use Word COM neste ambiente (não é confiável — ver "Ambiente técnico" no `SKILL.md`). Use
Python (`python-docx` já está disponível) ou extração direta do zip.

## 1. Autor real, empresa, datas — `docProps/core.xml` e `docProps/app.xml`

```bash
python3 - <<'EOF'
import zipfile
z = zipfile.ZipFile(r"CAMINHO\PARA\arquivo.docx")
print(z.read("docProps/core.xml").decode("utf-8", errors="replace"))
print("---")
try:
    print(z.read("docProps/app.xml").decode("utf-8", errors="replace"))
except KeyError:
    pass
EOF
```

O que olhar em `core.xml`: `<dc:creator>`, `<cp:lastModifiedBy>`, `<dcterms:created>`,
`<dcterms:modified>`, `<cp:revision>`. Um autor real diferente do "Elaborador" declarado na capa
não é por si só um erro — mas se o autor for de outra área ou empresa (ex.: documento de
Suprimentos criado por alguém de TI), vale registrar como observação DOC-01/DOC-02, nunca como
afirmação de fraude.

## 2. Comentários — `word/comments.xml`

```bash
python3 - <<'EOF'
import zipfile
z = zipfile.ZipFile(r"CAMINHO\PARA\arquivo.docx")
names = [n for n in z.namelist() if "comment" in n.lower()]
print(names)
for n in names:
    print(z.read(n).decode("utf-8", errors="replace")[:5000])
EOF
```

Se `word/comments.xml` não existir no zip, não há comentários — não inventar achado. Se existir,
ler o conteúdo: comentário interno esquecido no arquivo entregue ("confirmar com fulano antes de
publicar", "isso ainda não foi aprovado pelo diretor") é evidência direta de DOC-10 (aprovação
não confirmada) ou de informação que não deveria circular com o documento.

## 3. Alterações rastreadas (Track Changes) — `w:ins` / `w:del` em `word/document.xml`

```bash
python3 - <<'EOF'
import zipfile, re
z = zipfile.ZipFile(r"CAMINHO\PARA\arquivo.docx")
xml = z.read("word/document.xml").decode("utf-8", errors="replace")
ins = re.findall(r'<w:ins [^>]*w:author="([^"]*)"', xml)
dele = re.findall(r'<w:del [^>]*w:author="([^"]*)"', xml)
print("Inserções não aceitas, por autor:", ins)
print("Exclusões não aceitas, por autor:", dele)
EOF
```

Lista não vazia = o documento ainda tem edição pendente de aceitar/rejeitar. Isso é DOC-10
(documento "final" ainda em edição) e também pode revelar texto excluído que continua tecnicamente
recuperável no arquivo — relevante se o texto excluído continha algo sensível.

## 4. Texto oculto ou fora de área visível

Menos comum em .docx de processo, mas verificar:

```bash
python3 - <<'EOF'
import re, zipfile
z = zipfile.ZipFile(r"CAMINHO\PARA\arquivo.docx")
xml = z.read("word/document.xml").decode("utf-8", errors="replace")
print("w:vanish (texto oculto) encontrado:", "w:vanish" in xml)
EOF
```

## Regra de registro

Tudo que aparecer aqui e for sensível (nome de pessoa, caminho de rede interno, comentário sobre
aprovação pendente) entra no achado **mascarado** — nunca reproduzir o valor bruto no relatório.
Ex.: `<dc:creator>` mostra `joao.silva@gadens...` → registrar como "autor real do arquivo diverge
do Elaborador declarado na capa (e-mail de domínio Gadens, nome mascarado)", não colar o e-mail
inteiro.
