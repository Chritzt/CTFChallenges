#!/bin/bash

BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Prüfen, ob Docker läuft
if ! command -v docker &> /dev/null || ! docker ps &> /dev/null; then
    echo -e "${RED}[+] Docker ist nicht installiert oder läuft nicht!${NC}"
    exit 1
fi

echo -e "${BLUE}[+] Baue Challenge Container...${NC}"
docker build -t localhost/prisoners-crypt --platform linux/amd64 .

echo -e "${BLUE}[+] Starte -Challenge auf http://127.0.0.1:3000${NC}"
docker run --name prisoners-crypt --rm -p 127.0.0.1:3000:3000 -t -i --platform linux/amd64 localhost/prisoners-crypt