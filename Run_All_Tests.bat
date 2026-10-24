@echo off
title Chit Fund Tracker - Automated Test Suite Runner
color 0A
echo ===========================================================================
echo       RUNNING ALL CHIT FUND SYSTEM AND EDGE-CASE TEST SUITES
echo ===========================================================================
echo.

python d:\CHIT\TOOLS\test_edge_cases_comprehensive.py
if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo [ERROR] test_edge_cases_comprehensive.py failed!
    pause
    exit /b 1
)

echo.
python d:\CHIT\TOOLS\test_math_and_logic_simulation.py
if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo [ERROR] test_math_and_logic_simulation.py failed!
    pause
    exit /b 1
)

echo.
echo ===========================================================================
echo     ALL 83 TESTS AND EDGE-CASES PASSED WITH 100%% SUCCESS! (0 ERRORS)
echo ===========================================================================
echo.
pause
