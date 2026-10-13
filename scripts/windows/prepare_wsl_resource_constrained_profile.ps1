# FUTURE MANUAL EXECUTION FROM WINDOWS POWERSHELL ONLY.
# This script intentionally does not shut down/restart WSL or start Docker.
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
if ($env:OS -ne "Windows_NT") {
    throw "WINDOWS_HOST_REQUIRED"
}

Write-Host "USERPROFILE=$env:USERPROFILE"
$computer = Get-CimInstance Win32_ComputerSystem
$hostGiB = [math]::Round($computer.TotalPhysicalMemory / 1GB, 2)
Write-Host "HOST_RAM_GIB=$hostGiB"
if ($hostGiB -lt 14.5 -or $hostGiB -gt 16.0) {
    throw "HOST_RAM_MATERIALLY_DIFFERS_FROM_15_19_GIB"
}

$cDrive = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
if ($null -eq $cDrive) {
    throw "WINDOWS_C_DRIVE_QUERY_FAILED"
}
$cFreeGiB = [math]::Round($cDrive.FreeSpace / 1GB, 2)
Write-Host "WINDOWS_C_FREE_GIB=$cFreeGiB"
if ($cFreeGiB -lt 2.0) {
    throw "WINDOWS_C_FREE_SPACE_CRITICAL"
}

$wslRows = & wsl.exe --list --verbose
if ($LASTEXITCODE -ne 0) {
    throw "WSL_LIST_FAILED"
}
$wslRows | ForEach-Object { Write-Host $_ }
$ubuntuWsl2 = @($wslRows | Where-Object {
    ($_ -match "(?i)Ubuntu") -and ($_ -match "\s2\s*$")
})
if ($ubuntuWsl2.Count -lt 1) {
    throw "NO_UBUNTU_LIKE_WSL2_DISTRIBUTION"
}

$path = Join-Path $env:USERPROFILE ".wslconfig"
$timestamp = Get-Date -Format "yyyyMMddTHHmmss"
$backup = $null
if (Test-Path -LiteralPath $path) {
    $backup = "$path.backup-$timestamp"
    Copy-Item -LiteralPath $path -Destination $backup -ErrorAction Stop
    $backupHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $backup).Hash.ToLower()
    Write-Host "BACKUP_PATH=$backup"
    Write-Host "BACKUP_SHA256=$backupHash"
    $lines = [System.Collections.Generic.List[string]](Get-Content -LiteralPath $path)
} else {
    $lines = [System.Collections.Generic.List[string]]::new()
}

$sectionStart = -1
$sectionEnd = $lines.Count
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "^\s*\[wsl2\]\s*$") {
        $sectionStart = $i
        for ($j = $i + 1; $j -lt $lines.Count; $j++) {
            if ($lines[$j] -match "^\s*\[[^\]]+\]\s*$") {
                $sectionEnd = $j
                break
            }
        }
        break
    }
}

if ($sectionStart -lt 0) {
    if ($lines.Count -gt 0 -and $lines[$lines.Count - 1] -ne "") {
        $lines.Add("")
    }
    $lines.Add("[wsl2]")
    $lines.Add("memory=10GB")
    $lines.Add("swap=2GB")
} else {
    for ($i = $sectionEnd - 1; $i -gt $sectionStart; $i--) {
        if ($lines[$i] -match "^\s*(memory|swap)\s*=") {
            $lines.RemoveAt($i)
        }
    }
    $lines.Insert($sectionStart + 1, "swap=2GB")
    $lines.Insert($sectionStart + 1, "memory=10GB")
}

$encoding = New-Object System.Text.UTF8Encoding($false)
$finalText = ($lines -join "`r`n") + "`r`n"
[System.IO.File]::WriteAllText($path, $finalText, $encoding)
$newHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLower()
Write-Host "NEW_SHA256=$newHash"
Write-Host "FINAL_FILE_BEGIN"
Get-Content -LiteralPath $path
Write-Host "FINAL_FILE_END"
Write-Host "CONFIG_WRITTEN_RESTART_NOT_YET_PERFORMED"
