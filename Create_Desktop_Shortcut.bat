@echo off
title Create Desktop App Shortcut
color 0A
echo ===========================================================================
echo       CREATING FRESH CHIT FUND TRACKER DESKTOP APP SHORTCUT
echo ===========================================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0TOOLS\create_shortcut.ps1"

echo.
echo ===========================================================================
echo   Look at your Desktop for the 'Chit Fund Tracker' icon!
echo   Double-clicking it opens the latest app directly (no old cache).
echo ===========================================================================
echo.
pause
