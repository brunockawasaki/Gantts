---
name: reference-ooxml-toolkit
description: Reusable Perl OOXML fill toolkit + known PO.GG.QLD.001 template anchors + environment/validation notes for building Grupo Gadens docx documents without Node/Word COM
metadata: 
  node_type: memory
  type: reference
  originSessionId: a472d24e-e52e-49e1-a2a2-249ab3afa8e2
  modified: 2026-08-20T14:10:28.042Z
---

This environment has no Node.js (`docx`-js unavailable), and Word COM automation frequently fails with `TYPE_E_CANTLOADLIBRARY` (observed repeatedly from 2026-07-31 onward — treat as generally unreliable, not a one-off). `python3`/`python` ARE available with `python-docx` importable — use that only for **fresh** documents built from scratch (e.g. the "checklist de trabalho" format, see [[feedback_checklist_trabalho_format]]). For **filling an existing template** (POP/IT/Regimento), use the Perl + PowerShell pipeline below instead — rewriting it from scratch each session is what caused real bugs (missing `sz=20` on one rPr constant, "Aprovado" left uncorrected, a stray leading space, an accented-character typo) — copy this library instead of retyping it.

## Perl fill-script skeleton

Save as `fill_<code>.pl`, called as `perl fill_<code>.pl <src_document.xml> <out_document.xml>`:

```perl
#!/usr/bin/perl
use strict; use warnings; use utf8;
binmode(STDOUT, ":utf8");
my ($infile,$outfile)=@ARGV; die "usage\n" unless $outfile;
open(my $fh, "<:encoding(UTF-8)", $infile) or die $!;
local $/; my $xml = <$fh>; close($fh);
my $edits = 0;
sub esc { my $t = shift; $t =~ s/&/&amp;/g; $t =~ s/</&lt;/g; $t =~ s/>/&gt;/g; return $t; }
sub replace_exact {
    my ($old, $new, $expect) = @_;
    my $count = () = $xml =~ /\Q$old\E/g;
    die "Expected $expect occurrences, found $count, for: [" . substr($old,0,100) . "]\n" if $count != $expect;
    $xml =~ s/\Q$old\E/$new/g;
    $edits++;
}
sub fill_bullets {
    my ($anchor_paraid, $numid, $items, $rpr) = @_;
    my $re = qr/<w:p w14:paraId="\Q$anchor_paraid\E"[^>]*><w:pPr><w:pStyle w:val="PargrafodaLista"\/><w:numPr><w:ilvl w:val="0"\/><w:numId w:val="\Q$numid\E"\/><\/w:numPr><w:spacing[^>]*\/>(?:<w:rPr>.*?<\/w:rPr>)?<\/w:pPr><\/w:p>/;
    die "bullet template $anchor_paraid not found\n" unless $xml =~ $re;
    my $tpl = $&;
    my ($open) = $tpl =~ /^(.*<\/w:pPr>)<\/w:p>$/s;
    my $filled = "";
    for my $it (@$items) { $filled .= $open . "<w:r><w:rPr>$rpr</w:rPr><w:t xml:space=\"preserve\">" . esc($it) . "</w:t></w:r></w:p>"; }
    my $n = ($xml =~ s/\Q$tpl\E/$filled/);
    die "bullet replace failed for $anchor_paraid\n" unless $n == 1;
    $edits++;
}
sub fill_numbered {
    my ($paraid, $numid, $items, $rpr) = @_;
    my $re = qr/<w:p w14:paraId="\Q$paraid\E"[^>]*><w:pPr><w:pStyle w:val="PargrafodaLista"\/><w:numPr><w:ilvl w:val="0"\/><w:numId w:val="\Q$numid\E"\/><\/w:numPr><w:spacing[^>]*\/><w:rPr>.*?<\/w:rPr><\/w:pPr><\/w:p>/;
    die "numbered template $paraid not found\n" unless $xml =~ $re;
    my $tpl = $&;
    my ($open) = $tpl =~ /^(.*<\/w:pPr>)<\/w:p>$/s;
    my $filled = "";
    for my $it (@$items) { $filled .= $open . "<w:r><w:rPr>$rpr</w:rPr><w:t xml:space=\"preserve\">" . esc($it) . "</w:t></w:r></w:p>"; }
    my $n = ($xml =~ s/\Q$tpl\E/$filled/);
    die "numbered replace failed $paraid\n" unless $n == 1;
    $edits++;
}
sub fill_table_row_multi {
    my ($row_re, $col_paraids, $rows, $rpr) = @_;
    die "table row not found\n" unless $xml =~ $row_re;
    my $tpl = $&;
    my $filled = "";
    for my $r (@$rows) {
        my $row = $tpl;
        for my $i (0..$#$col_paraids) {
            my $pid = $col_paraids->[$i];
            my $val = $r->[$i];
            $row =~ s{(<w:p w14:paraId="\Q$pid\E".*?)</w:p>}{$1<w:r><w:rPr>$rpr</w:rPr><w:t xml:space="preserve">${\esc($val)}</w:t></w:r></w:p>}s;
        }
        $filled .= $row;
    }
    my $n = ($xml =~ s/\Q$tpl\E/$filled/);
    die "table replace failed\n" unless $n == 1;
    $edits++;
}

# Standard rPr constants — Arial 10pt (sz=20/szCs=20) EXPLICIT on every one. Never omit sz.
my $R_RECURSOS = '<w:rFonts w:ascii="Arial" w:eastAsia="Times New Roman" w:hAnsi="Arial" w:cs="Arial"/><w:color w:val="000000" w:themeColor="text1"/><w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:eastAsia="pt-BR"/>';
my $R_PASSOS = '<w:rFonts w:ascii="Arial" w:eastAsia="Times New Roman" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:eastAsia="pt-BR"/>';
my $R_PONTOS = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/>';
my $R_DEFTBL = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:color w:val="000000" w:themeColor="text1"/><w:sz w:val="20"/><w:szCs w:val="20"/>';
my $R_TBL_PLAIN = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/>';

# ... cover/section replace_exact + fill_* calls go here (see below for known anchors) ...

print "Total edit groups applied: $edits\n";
open(my $out, ">:encoding(UTF-8)", $outfile) or die $!;
print $out $xml; close($out);
```

Accented characters: prefer `\x{E7}` (ç) / `\x{E3}` (ã) style escapes over literal UTF-8 in the source over `use utf8;` literals — a past bug (`\x{ED}\x{EA}` instead of `i\x{EA}` for "Dossiê") was caught only by post-hoc grep. Either works with `use utf8;` declared, but `\x{}` escapes are easier to eyeball-verify character-by-character.

## Known PO.GG.QLD.001 template anchors (re-verify before trusting — templates drift)

**Always re-check freshness first**: `grep -c "TÍTULO" word/document.xml` on a fresh unzip must be 2, with no leftover filled content, before assuming any anchor below still applies. If a `replace_exact`/`fill_*` call dies with "not found", re-inspect the live template XML rather than assuming the anchor is stale — table structures have drifted mid-session before (CONTROLE DE EMISSÃO went from 3-column to 4-column with merged Elaboração/Aprovação cells; REGISTRO went from 3 data columns to 2).

- Cover title run: literal text `TÍTULO</w:t></w:r><w:r w:rsidR="007F04FB">...` — replace title text and the following `<w:t>001` for the code.
- Revisão dropdown default: `02</w:t></w:r></w:sdtContent>` → replace with `00` for new docs.
- Elaborador/Aprovador defaults: literal `Bruno Kawasaki` / `Alessandro Braz, Carlos Vargas` (2 occurrences each — cover shows the field twice, once per redundant sdt).
- DEFINIÇÕES table row: `<w:tr w:rsidR="00385250" w14:paraId="144F4749"...>`, cell paraIds `2BBE6342` (termo) / `41F2A275` (definição).
- RECURSOS bullets (numId=2): anchors `6746B202` (Sistemas), `007906F9` (Documentos/Entradas), `2175E7EB` (Papéis-chave).
- PRINCIPAIS PASSOS numbered list (numId=3): anchor `32281CFC`.
- RESPONSABILIDADES table row: `<w:tr w:rsidR="007F04FB" w:rsidRPr="007F04FB" w14:paraId="4854C1AF"...>`, cell paraIds `6ABCA0F2` / `617752CE` / `39B0A272`.
- INDICADORES bullet (numId=4): anchor `4C3EEB2F`. Intro sentence to fix: template default says "...diretrizes estratégicas de prospecção definidas neste POP:" — always replace with "...diretrizes deste POP:" regardless of topic (this is a template-wide leftover bug, not specific to any one POP).
- PONTOS CRÍTICOS bullets (numId=4): anchor `37085916`; spare unused bullet paragraph to delete afterward: `0B54EF9E`.
- DESVIOS table row: `<w:tr w:rsidR="00EF2D30" w14:paraId="22CA91A5"...>`, cell paraIds `2AC6A588` / `21C92C8C` / `3DBEBE0B`.
- REGISTRO table row: `<w:tr w:rsidR="00244F6C" w14:paraId="41DC4A46"...>`, cell paraIds `0DE5AEFB` / `3F768BC1`.
- CONTROLE DE EMISSÃO: three separate `replace_exact` calls — (1) the "Elaboração:/Aprovação:" combined run (has a `<w:proofErr w:type="gramStart"/>`/`gramEnd` wrapper, watch for `<w:sdtEndPr/>` self-closing vs `</w:sdtEndPr>` — a past bug used the wrong closing form), (2) the empty "Itens Revisados" cell paraId `46F38953` → fill with "Elaboração Inicial", (3) the split `DD/MM/AAAA` / `DD/MM/AA`+`AA` date runs (rsidRPr `00206192`).

## Packing and validating (PowerShell)

```powershell
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$fs = [System.IO.File]::Open($outDocx, [System.IO.FileMode]::CreateNew)
$archive = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)
$baseLen = $srcDir.Length + 1
Get-ChildItem -Path $srcDir -Recurse -File | ForEach-Object {
    $relPath = $_.FullName.Substring($baseLen) -replace '\\', '/'   # MUST normalize to forward slashes — Compress-Archive and raw ZipFile.CreateFromDirectory both emit backslash paths on Windows, which corrupts the OOXML package
    $entry = $archive.CreateEntry($relPath, [System.IO.Compression.CompressionLevel]::Optimal)
    $entryStream = $entry.Open()
    $fileBytes = [System.IO.File]::ReadAllBytes($_.FullName)
    $entryStream.Write($fileBytes, 0, $fileBytes.Length)
    $entryStream.Close()
}
$archive.Dispose(); $fs.Close()
```

Validate: try Word COM open first (`New-Object -ComObject Word.Application`), but expect it to fail with `TYPE_E_CANTLOADLIBRARY` — when it does, fall back to (a) well-formed-XML check via `[xml]$x = $xmlText` on the packed `word/document.xml`, and (b) structural sanity via `grep -c "<w:tbl>"` / `<w:tr>` matching expected table/row counts. Always tell Bruno explicitly when Word-open validation wasn't possible and recommend he open the file once before circulating.

`$srcDir` must be derived via `(Get-Item <path>).FullName`, never a literal typed path — mismatched 8.3-short-name vs. long-name forms between the literal string and what `Get-ChildItem` returns has caused wrong `.Substring()` offsets before.

## Critical bug class: stray scratch files corrupting the package (2026-08-20)

When **editing an existing docx in place** (not filling a blank template — e.g. a formatting/typo fix pass), the workflow is: unzip the real docx into a temp folder → edit `word/document.xml` there → repack that whole folder. The packing step (`Get-ChildItem -Path $srcDir -Recurse -File`) grabs **every file sitting in that folder**, not just legitimate OOXML parts.

This caused two real corrupted deliveries (PO.CM.PJC.001 and PO.IG.PJC.001, 2026-08-19/20): a `text.txt` I wrote into that same folder for my own review (extracting plain text to read before delivering) got swept into the repacked `.docx`. `[Content_Types].xml` has no declaration for `.txt`, so Word treats the whole package as corrupted and refuses to open it — even though the zip container itself passes integrity checks and `python-docx` opens it without complaint (python-docx is lenient; real Word is strict about undeclared parts). This is why it can look "fine" in every automated check and still fail for Bruno.

**How to apply, every time an existing docx is edited in place (not just filled from a blank template):**
- Never write review/scratch artifacts (extracted `text.txt`, notes, intermediate dumps) into the same directory that holds the unzipped docx parts. Use a sibling directory instead.
- Before packing, verify the source folder contains only recognized OOXML top-level entries (`word/`, `docProps/`, `customXml/`, `_rels/`, `[Content_Types].xml`) — no stray files at the root. Print the full entry list after packing and check it, exactly like the `$hasStray` check added to the Pack-Docx helper in this session — keep that check as a standard step going forward, not a one-off.
- If a batch touches multiple sibling files (e.g. a CM/IG pair, or all 5 PJC Regimentos), re-verify **every file in the batch** for this bug, not just the ones the user explicitly reports as broken — one file failing silently doesn't mean the others are clean; they likely share the same contamination if built with the same script pattern in the same pass.
