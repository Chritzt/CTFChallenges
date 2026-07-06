@echo off
setlocal

rem In Windows CMD muessen wir die Parameter ganz normal in Anfuehrungszeichen setzen
curl -s -X POST -d "problem={{config}}" http://127.0.0.1:5000/check-ticket

echo.
echo ----------------------------------------
echo [+] Request abgeschlossen.
echo ----------------------------------------
pause