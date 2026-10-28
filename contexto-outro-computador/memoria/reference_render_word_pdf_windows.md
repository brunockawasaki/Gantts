---
name: reference-render-word-pdf-windows
description: "Como ver (renderizar) um .docx/PDF como imagem neste PC Windows, já que não há LibreOffice, pandoc nem pdftoppm"
metadata:
  node_type: memory
  type: reference
  originSessionId: 0b51ec10-09dd-45f3-99ef-321f9e69ee3a
  modified: 2026-10-21T21:49:11.099Z
---

Neste computador NÃO há LibreOffice, pandoc, pdftoppm nem pypdf, e o `pip install` não funciona (sem internet). Mesmo assim dá para conferir visualmente um Word gerado:

1. **Word real via COM, pelo PowerShell, com late binding** (o jeito normal `New-Object -ComObject` + `.Visible = $false` dá erro TYPE_E_CANTLOADLIBRARY). Usar reflection: `$wt=[Type]::GetTypeFromProgID("Word.Application"); $word=[Activator]::CreateInstance($wt); $wt.InvokeMember("Visible",[Reflection.BindingFlags]::SetProperty,$null,$word,@($false))` e depois `Documents.Open(path, $false, $true)`, `ComputeStatistics(2)` (nº de páginas), `Range.Information(3)` (página de um trecho achado com `Content.Find`), `SaveAs2(pdf, 17)` (exporta PDF). Sempre `Close($false)` e `Quit()`.
2. **PDF -> PNG** pelo leitor do Windows (WinRT) no PowerShell 5.1: carregar `Windows.Storage.StorageFile` e `Windows.Data.Pdf.PdfDocument`, aguardar os IAsyncOperation via `System.WindowsRuntimeSystemExtensions.AsTask`, `PdfDocument.GetPage(i).RenderToStreamAsync(stream, opts)` com `PdfPageRenderOptions.DestinationWidth=900`, copiar o stream para um .png e abrir o PNG com a ferramenta Read.
3. O painel de navegador embutido NÃO mostra PDF (ele baixa e abre diálogo de salvar) — não tentar.
4. Para tirar um arquivo gerado dentro do navegador (blob), subir um receptor POST temporário em Python (127.0.0.1, porta livre, com cabeçalhos CORS) e fazer `fetch(..., {method:"POST", body: blob})`; encerrar o processo depois.

**Excel (2026-10-21):** o `recalc.py` da skill xlsx NÃO roda aqui (erro `socket.AF_UNIX`). Para calcular as fórmulas de uma planilha feita com openpyxl: Excel por reflection, mesmo padrão do Word (`GetTypeFromProgID("Excel.Application")`, `Visible`/`DisplayAlerts` falso, `Workbooks.Open` com UM argumento `[object[]]@($caminho)`, `CalculateFull`, `Save`, `Close($false)`, `Quit` em `finally`). Depois ler os valores gravados com `openpyxl data_only=True` e contar erros `#`. Funcionou com 3.710 fórmulas, 0 erros.

Acentos no caminho: no Bash do Windows, caminhos com acento (ex.: "Padrões") às vezes não casam; usar Python (`os.listdir`/`glob`/`shutil`) para achar e copiar arquivos.

Detalhe importante (2026-10-07): `Documents.Open` por reflection só funcionou passando UM argumento (`[object[]]@($caminho)`); com 3 argumentos (ReadOnly etc.) deu DISP_E_TYPEMISMATCH. Sempre encerrar o Word em `finally` (um WINWORD órfão atrapalha a próxima chamada) e converter as strings com `[string]`.
