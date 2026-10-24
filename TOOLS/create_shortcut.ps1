$ws = New-Object -ComObject WScript.Shell
$desktop = [Environment]::GetFolderPath('Desktop')
$lnkPath = Join-Path $desktop 'Chit Fund Tracker.lnk'

# 1. Remove old or stale shortcut from Desktop
if (Test-Path $lnkPath) {
    Remove-Item -Force $lnkPath
    Write-Host "[OK] Old desktop shortcut removed." -ForegroundColor Yellow
}

# 2. Find Edge or Chrome browser executable
$browser = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if (-not (Test-Path $browser)) {
    $browser = 'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
}
if (-not (Test-Path $browser)) {
    $browser = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
}
if (-not (Test-Path $browser)) {
    $browser = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
}

# 3. Target local index.html with normalized file URI
$appPath = 'file:///D:/CHIT/MAIN/index.html'

# 4. Create fresh shortcut
$shortcut = $ws.CreateShortcut($lnkPath)
$shortcut.TargetPath = $browser
$shortcut.Arguments = "--app=`"$appPath`""
$shortcut.IconLocation = 'd:\CHIT\MAIN\app_icon.ico,0'
$shortcut.Description = 'Chit Fund Payment Tracker & Settlement App'
$shortcut.WorkingDirectory = 'd:\CHIT\MAIN'
$shortcut.Save()

if (Test-Path $lnkPath) {
    Write-Host "[SUCCESS] Fresh Desktop Shortcut Created at: $lnkPath" -ForegroundColor Green
    Write-Host "[INFO] Opens latest local app directly in dedicated standalone window with zero cache delay."
} else {
    Write-Host "[ERROR] Could not create shortcut." -ForegroundColor Red
}
