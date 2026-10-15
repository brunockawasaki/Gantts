# Ferramentas

| Arquivo | O que faz |
|---|---|
| `gerar.py` | Lê `../dados/*.json` e escreve os cronogramas e os menus. |
| `conferir_planilha.py` | Compara uma planilha com `../dados/*.json`. Só lê. |
| `modelo_gantt.html` | Modelo do cronograma. Tem `__TITULO__`, `__EMPRESA__`, `__EMPRESA_SLUG__` e `__DADOS__`. |
| `modelo_menu.html` | Modelo do menu principal. Tem `__CARTOES__` e `__POSICAO__`. |
| `modelo_empresa.html` | Modelo do menu de cada empresa. Tem `__EMPRESA__`, `__CARTOES__` e `__POSICAO__`. |

## Uso

Na raiz do repositório:

```
python ferramentas/gerar.py
python ferramentas/conferir_planilha.py "caminho\PLANILHA.xlsx"
```

`gerar.py` só precisa do Python. `conferir_planilha.py` precisa de `pip install openpyxl`.

## Regra de ouro

Os arquivos em `cronogramas/`, `make-it/` e `index.html` são **gerados**. Se mudar algum à mão, a próxima geração apaga a mudança. Para mudar conteúdo, edite `dados/`. Para mudar o visual, edite os `modelo_*.html`.

## Se o gráfico mudar

O desenho e o cálculo do gráfico estão no `<script>` de `modelo_gantt.html`. O mesmo cálculo existe em `gerar.py` (função `calcular`), usado só para os números dos menus. **Se mudar a regra num lugar, mude no outro.**
