#!/bin/sh

# Falls keine FLAG-Umgebungsvariable gesetzt ist, setzen wir eine Standard-Flagge
if [ -z "$FLAG" ]; then
    export FLAG="FLAG{dummy_flag_docker_forgot_to_set_it}"
fi

echo "[*] Starte Five-Finger Discount Web Challenge..."
echo "[*] Aktuelle Flagge ist geladen."

# Flask-App im Produktionsmodus (oder mit gunicorn, hier reicht python) starten
exec python app.py