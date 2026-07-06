#!/bin/sh
set -e

# Falls im docker-compose KEINE Flagge definiert wurde, greift dieser Fallback:
if [ -z "$FLAG" ]; then
    export FLAG="FLAG{dummy_flag_docker_forgot_to_set_it}"
fi

echo "[INFO] Starting Flask Application..."

# Startet Python und nimmt die exportierte FLAG-Variable mit
exec python app.py