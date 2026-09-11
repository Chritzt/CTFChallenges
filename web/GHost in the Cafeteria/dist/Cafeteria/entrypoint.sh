#!/bin/sh
# Erzwingt, dass das Skript sofort abbricht, wenn ein Fehler auftritt
set -e

echo "[INFO] Starting Flask Application..."

# Startet die Python-Anwendung und übergibt alle zusätzlichen Argumente, 
# die eventuell über das Dockerfile oder docker-compose übergeben werden.
exec python app.py