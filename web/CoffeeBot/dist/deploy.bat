@echo off
chcp 65001 >nul

if "%~1"=="" goto default
if "%~1"=="check" goto check
if "%~1"=="build" goto build
if "%~1"=="run" goto run
if "%~1"=="kill" goto kill

:check
echo [+] Verifying Challenge Integrity
:: Nutzt Windows certutil für den Check, falls sha256sum nicht installiert ist
powershell -Command "if (Test-Path sha256sum) { Get-Content sha256sum | ForEach-Object { \$p = \$_ -split '  '; \$h = (Get-FileHash \$p[1] -Algorithm SHA256).Hash.ToLower(); if (\$h -eq \$p[0]) { write-host \"\$(\$p[1]): OK\" -ForegroundColor Green } else { write-host \"\$(\$p[1]): FAILED\"; exit 1 } } } else { write-host \"sha256sum missing\" -ForegroundColor Red; exit 1 }"
goto :eof

:build
echo [+] Building Challenge Docker Container
docker build -t localhost/coffeebot --platform linux/amd64 .
goto :eof

:run
echo [+] Running Challenge Docker Container on 127.0.0.1:8080
docker run --name coffeebot-chall --rm -p 127.0.0.1:8080:8080 -t -i -e HOST=127.0.0.1 -e PORT=80 -e TIMEOUT=30  --read-only --privileged --platform linux/amd64 localhost/coffeebot
goto :eof

:kill
echo [-] Stopping Challenge Container
docker stop coffeebot-chall >nul 2>&1
goto :eof

:default
call :check
if %errorlevel% equ 0 (
    call :build
    if %errorlevel% equ 0 call :run
)
goto :eof