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
    echo %ESC%[34m[+] Building Challenge Container: five-finger-discount%ESC%[0m
    docker build -t localhost/five-finger-discount --platform linux/amd64 .

:run
    echo %ESC%[34m[+] Running Challenge Container on 127.0.0.1:80%ESC%[0m
    docker run --name five-finger-discount-store --rm -p 127.0.0.1:80:5000 -t -i -e HOST=127.0.0.1 -e PORT=5000 -e FLAG=FLAG{7h15_15_wh47_1_c4ll_4_f1v3_f1ng3r_d15c0un7} --platform linux/amd64 localhost/five-finger-discount

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #${H}#${E}# & echo on & for %%b in (1) do rem"') do (
    set ESC=%%b
    exit /B 0
)
exit /B 0