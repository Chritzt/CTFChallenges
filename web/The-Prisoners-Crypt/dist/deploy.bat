@echo off
setlocal
call :setESC

:req
    where docker > NUL 2>&1
    if %ERRORLEVEL% NEQ 0 (
        ECHO %ESC%[31m[+] Docker wurde nicht gefunden. Bitte installieren!%ESC%[0m
        exit /B 1
    )
    docker ps >NUL 2>&1
    if %ERRORLEVEL% NEQ 0 (
        ECHO %ESC%[31m[+] Docker läuft nicht. Bitte Docker Desktop starten!%ESC%[0m
        exit /B 1
    )

:build
    echo %ESC%[34m[+] Baue Challenge Container...%ESC%[0m
    docker build -t localhost/prisoners-crypt --platform linux/amd64 .

:run
    echo %ESC%[34m[+] Starte Challenge auf http://127.0.0.1:3000%ESC%[0m
    docker run --name prisoners-crypt --rm -p 127.0.0.1:3000:3000 -t -i --platform linux/amd64 localhost/prisoners-crypt

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #${H}#${E}# & echo on & for %%b in (1) do rem"') do (
    set ESC=%%b
    exit /B 0
)
exit /B 0