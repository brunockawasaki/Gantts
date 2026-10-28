param(
    [Parameter(Mandatory=$true)][string]$PdfPath,
    [string]$OutDir = (Split-Path (Resolve-Path $PdfPath).Path -Parent),
    [int]$Width = 1000
)
# Renderiza cada página de um PDF em PNG (page-01.png, ...) usando a API WinRT
# do Windows (Windows.Data.Pdf) — não requer poppler/LibreOffice. Jul/2026.
$ErrorActionPreference = 'Stop'
$PdfPath = (Resolve-Path $PdfPath).Path

Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime]
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.RandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
})[0]

function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}
function AwaitAction($WinRtAction) {
    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction'
    })[0]
    $netTask = $asTask.Invoke($null, @($WinRtAction))
    $netTask.Wait(-1) | Out-Null
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($PdfPath)) ([Windows.Storage.StorageFile])
$pdfDoc = Await ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
"Paginas: $($pdfDoc.PageCount)"

for ($i = 0; $i -lt $pdfDoc.PageCount; $i++) {
    $page = $pdfDoc.GetPage($i)
    $outPath = Join-Path $OutDir ("page-{0:d2}.png" -f ($i + 1))
    $outFileStream = [System.IO.File]::Create($outPath)
    $winStream = [System.IO.WindowsRuntimeStreamExtensions]::AsRandomAccessStream($outFileStream)
    $opts = New-Object Windows.Data.Pdf.PdfPageRenderOptions
    $opts.DestinationWidth = $Width
    AwaitAction ($page.RenderToStreamAsync($winStream, $opts))
    $outFileStream.Flush(); $outFileStream.Dispose()
    $page.Dispose()
    "OK $outPath"
}
