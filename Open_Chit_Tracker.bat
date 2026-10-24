@echo off
title Chit Fund Payment Tracker App
setlocal enabledelayedexpansion

set "APP_DIR=%~dp0MAIN"
set "RAW_PATH=%~dp0MAIN\index.html"
set "NORMALIZED_PATH=%RAW_PATH:\=/%"
set "APP_URL=file:///%NORMALIZED_PATH%"

echo ============================================================
echo   Opening Chit Fund Tracker App (Fresh Offline Version)...
echo ============================================================

:: 1. Try Microsoft Edge in dedicated Standalone App window (no URL bar, clean desktop app)
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --app="%APP_URL%"
    exit /b 0
)

if exist "C:\Program Files\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files\Microsoft\Edge\Application\msedge.exe" --app="%APP_URL%"
    exit /b 0
)

:: 2. Try Google Chrome in dedicated Standalone App window
if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --app="%APP_URL%"
    exit /b 0
)

if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="%APP_URL%"
    exit /b 0
)

:: 3. Fallback to default browser
start "" "%RAW_PATH%"
exit /b 0
