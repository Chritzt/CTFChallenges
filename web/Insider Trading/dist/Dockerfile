# Dockerfile
FROM node:20-alpine

# Arbeitsverzeichnis im Container
WORKDIR /app

# Paketdateien kopieren und Abhängigkeiten installieren
COPY package*.json ./
RUN npm ci --only=production

# Quellcode kopieren
COPY server.js schema.js admin_bot.js ./
COPY public ./public
# Standard-Port für das GraphQL-Interface
EXPOSE 4000

# Standard-Startbefehl (kann in docker-compose überschrieben werden)
CMD ["node", "server.js"]