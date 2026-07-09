#!/bin/bash

# 1. Den Ciphertext aus den EXIF-Metadaten extrahieren
CIPHER=$(exiftool "./vigenere.jpg" 2>/dev/null | grep -i "Title" | awk -F': ' '{print $2}' | tr -d '\r\n')
echo "[+] Gefundener Ciphertext: $CIPHER"

# 2. Den Key aus den Binärdaten extrahieren
# Wir suchen nach "Geheimschluessel" und nehmen ALLES dahinter, egal welches Encoding
KEY=$(strings "./vigenere.jpg" | grep -i "Key" | cut -d':' -f2- | tr -d ' \r\n')

# Falls "Geheimschluessel:" nicht exakt matched, suchen wir nach dem Wort "coffee" am Dateiende
if [ -z "$KEY" ]; then
    KEY=$(strings "./vigenere.jpg" | tail -n 10 | grep -oE '[a-zA-Z]{4,}' | grep -v "Geheimschluessel" | head -n 1)
fi

echo "[+] Gefundener Key: $KEY"

# Falls immer noch kein Key da ist, brechen wir sauber ab, statt zu crashen
if [ -z "$KEY" ] || [ -z "$CIPHER" ]; then
    echo "[-] Fehler: Cipher oder Key konnte nicht aus der Datei gelesen werden!"
    exit 1
fi

# 3. Automatische Entschlüsselung via Python
echo -n "[*] Entschlüsselte Flagge: "
python3 -c "
import sys
cipher = '$CIPHER'
key = '$KEY'.lower()
flag = []
key_idx = 0

for char in cipher:
    if char.isalpha():
        shift = ord(key[key_idx % len(key)]) - 97
        base = 65 if char.isupper() else 97
        flag.append(chr((ord(char) - base - shift) % 26 + base))
        key_idx += 1
    else:
        flag.append(char)
print(''.join(flag))
"