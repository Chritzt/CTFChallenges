#!/bin/sh

# 1. Startet den Redis-Server im Hintergrund (ohne protected-mode, damit wir via SSRF draufkommen)
redis-server --protected-mode no &

# 2. Wartet kurz, bis der Server hochgefahren und empfangsbereit ist
sleep 1.5

# 3. Schreibt die vom Framework dynamisch injizierte Flagge in den Key 'flag'
if [ -n "$FLAG" ]; then
    redis-cli set flag "$FLAG"
    echo "[*] Flagge erfolgreich in Redis geladen!"
else
    redis-cli set flag "CLA{fallback_local_testing_flag}"
    echo "[!] Keine dynamische Flagge gefunden, Fallback-Flagge gesetzt."
fi

# 4. Hält den Container am Leben und reicht Signale weiter
wait