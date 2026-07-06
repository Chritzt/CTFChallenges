@echo off
setlocal
call :setESC

:req
    echo %ESC%[34m[+] Note: This script has only been tested for docker using WSL2. It might work with Hyper-V, but it was not tested.%ESC%[0m
    where docker > NUL 2>&1
    if %ERRORLEVEL% NEQ 0 (
        ECHO %ESC%[31m[+] docker command not found. Is docker installed?%ESC%[0m
        exit /B 1
    )
    docker ps >NUL 2>&1
    if %ERRORLEVEL% NEQ 0 (
        ECHO %ESC%[31m[+] "docker ps" failed. Is docker running?%ESC%[0m
        exit /B 1
    )

:build
    echo %ESC%[34m[+] Building Challenge Container: Ticket-Handling-Made-Easy%ESC%[0m
    docker build -t localhost/ticket-handling-made-easy --platform linux/amd64 .

:run
    echo %ESC%[34m[+] Running Challenge Container on 127.0.0.1:80%ESC%[0m
    docker run --name ticket-handling-made-easy --rm -p 127.0.0.1:80:5000 -t -i -e HOST=127.0.0.1 -e PORT=5000 -e FLAG=FLAG{7h15_71ck37_h45_b33n_d31373d_5ucc355fu11y} --platform linux/amd64 localhost/ticket-handling-made-easy

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #${H}#${E}# & echo on & for %%b in (1) do rem"') do (
    set ESC=%%b
    exit /B 0
)
exit /B 0