# --- Stage 1: Build-Umgebung ---
FROM golang:1.22-alpine AS builder

# Installiert GCC und Build-Tools (zwingend nötig für den C-Code von go-sqlite3)
RUN apk add --no-cache build-base

WORKDIR /app

# Initialisiert das Go-Modul und lädt den SQLite-Treiber herunter
RUN go mod init coffeebot && go get github.com/mattn/go-sqlite3

# Kopiert den Go-Quellcode (main.go) in den Container
COPY /main/main.go .

# Kompiliere das Go-Projekt explizit für linux/amd64 (passend zu eurem deploy-Skript)
RUN CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -o coffee-bot .


# --- Stage 2: Finale Laufzeit-Umgebung ---
FROM alpine:3.19
RUN apk add --no-cache libc6-compat

WORKDIR /app

# 1. Kopiere das fertige Go-Binary und das Entrypoint-Skript aus Stage 1
COPY --from=builder /app/coffee-bot .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# 2. HIER WIRD DEINE LOKALE DATA-BASE IN DEN CONTAINER KOPIERT
# Stelle sicher, dass die Datei "coffee.db" im selben Ordner wie dieses Dockerfile liegt!
COPY coffee.db /app/coffee.db

# Wichtig: Schreibrechte für die DB öffnen, damit der Go-Code beim Start
# die Flagge dynamisch hineinschreiben kann.
RUN chmod 666 /app/coffee.db

EXPOSE 80

ENTRYPOINT ["./entrypoint.sh"]