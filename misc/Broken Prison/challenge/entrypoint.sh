#!/bin/sh
# Aktiviere die Venv falls nötig
. /.venv/bin/activate 2>/dev/null
# Starte einfach nur das Python Skript, kein socat hier
python3 -u /app/challenge