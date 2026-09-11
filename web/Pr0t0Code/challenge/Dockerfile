FROM docker.io/library/node:20-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY package.json /app/
RUN npm install express

# Source Code kopieren
COPY server.js index.html /app/

# Sicherheitsaspekt: Als unprivilegierter User ausführen
USER node

EXPOSE 1337

# Startbefehl
CMD ["node", "server.js"]