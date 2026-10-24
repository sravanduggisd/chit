@echo off
title Chit Fund Tracker Mobile Server
echo ==============================================================
echo       CHIT FUND TRACKER - MOBILE WIFI SERVER
echo ==============================================================
echo.
echo 1. Keep this window OPEN.
echo 2. Open browser on your MOBILE PHONE (connected to same Wi-Fi).
echo 3. Check your computer IP below and open:
echo.
ipconfig | findstr /i "IPv4"
echo.
echo For example, if your IPv4 is 192.168.1.15, type in mobile browser:
echo        http://192.168.1.15:8080
echo.
echo ==============================================================
python "%~dp0server.py"
pause
