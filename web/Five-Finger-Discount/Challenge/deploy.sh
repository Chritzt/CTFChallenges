#!/bin/bash

# Farben für die Ausgabe definieren
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 1. Voraussetzungen prüfen
if ! command -v docker &> /dev/null; then
    echo -e "${RED}[+] docker command not found. Is docker installed?${NC}"
    exit 1
fi

if ! docker ps &> /dev/null; then
    echo -e "${RED}[+] \"docker ps\" failed. Is docker running?${NC}"
    exit 1
fi

# 2. Container bauen
echo -e "${BLUE}[+] Building Challenge Container: five-finger-discount${NC}"
docker build -t localhost/five-finger-discount --platform linux/amd64 .

# 3. Container ausführen
echo -e "${BLUE}[+] Running Challenge Container on 127.0.0.1:80${NC}"
docker run --name five-finger-discount-store \
    --rm \
    -p 127.0.0.1:80:5000 \
    -t -i \
    -e HOST=127.0.0.1 \
    -e PORT=5000 \
    -e FLAG="FLAG{7h15_15_wh47_1_c4ll_4_f1v3_f1ng3r_d15c0un7}" \
    --platform linux/amd64 \
    localhost/five-finger-discount