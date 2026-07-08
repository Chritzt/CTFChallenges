FROM node:18-alpine

WORKDIR /app

# Installiere Abhängigkeiten (Express)
RUN npm install express

# Kopiere den Server und die HTML-Datei
COPY ./web/server.js .
COPY ./web/index.html .

EXPOSE 3000

CMD ["node", "server.js"]