echo off
for /f "delims=" %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
echo [93m
@echo off
title Autojoiner

python main.py

pause
echo [0m