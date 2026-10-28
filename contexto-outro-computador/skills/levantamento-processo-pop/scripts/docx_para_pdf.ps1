param(
    [Parameter(Mandatory=$true)][string]$DocxPath,
    [Parameter(Mandatory=$true)][string]$PdfPath
)
# Converte .docx em PDF usando o Word instalado (COM). Validado em jul/2026.
$ErrorActionPreference = 'Stop'
$w = New-Object -ComObject Word.Application
$w.Visible = $false
try {
    $d = $w.Documents.Open((Resolve-Path $DocxPath).Path, $false, $true)
    $d.ExportAsFixedFormat($PdfPath, 17)  # 17 = wdExportFormatPDF
    $pages = $d.ComputeStatistics(2)      # 2 = wdStatisticPages
    $d.Close(0)
    "PDF gerado com $pages paginas: $PdfPath"
} finally {
    $w.Quit()
}
