#!/bin/pwsh

function New-TemporaryDirectory {
    $parent = [System.IO.Path]::GetTempPath()
    $name = [System.IO.Path]::GetRandomFileName()
    New-Item -ItemType Directory -Path (Join-Path $parent $name)
}

$Dir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Definition)
$Temp = New-TemporaryDirectory

$Build = "$Dir\build"
New-Item -ItemType Directory -Force -Path $Build | Out-Null

$Name = Get-Content $Dir\mod\aa_header.rpy | Select-String '^\s*name="([^"]+)"' | ForEach-Object { $_.Matches[0].Groups[1].Value }
$Version = Get-Content $Dir\mod\aa_header.rpy | Select-String '^\s*version="([^"]+)"' | ForEach-Object { $_.Matches[0].Groups[1].Value }
$Package = $Name.ToLower() -Replace "\s", "-"

$Mod = "$Temp\game\Submods"
New-Item -ItemType Directory -Force -Path $Mod | Out-Null
$Mod = "$Mod\$Name"

Copy-Item -Recurse $Dir\mod $Mod
Remove-Item $Mod\README.md
Remove-Item $Mod\aa_source_dist_trap.rpy
Copy-Item -Recurse $Dir\res\* $Mod

Compress-Archive -Update -Path $Temp\game -DestinationPath $Build\$Package-$Version.zip
Remove-Item -Recurse $Temp

Compress-Archive -Update -Path $Dir\spritepacks -DestinationPath $Build\spritepacks-$Version.zip