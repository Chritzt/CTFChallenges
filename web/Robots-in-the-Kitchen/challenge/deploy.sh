#!/bin/bash

BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Prüfen, ob Docker läuft
if ! command -v docker &> /dev/null || ! docker ps &> /dev/null; then
    echo -e "${RED}[+] Docker ist nicht installiert oder läuft nicht!${NC}"
    exit 1
fi

echo -e "${BLUE}[+] Baue Robots-Challenge Container...${NC}"
docker build -t localhost/robots-kitchen --platform linux/amd64 .

echo -e "${BLUE}[+] Starte Robots-Challenge auf http://127.0.0.1:81${NC}"
docker run --name robots_in_the_kitchen --rm -p 127.0.0.1:81:80 -t -i --platform linux/amd64 localhost/robots-kitchen