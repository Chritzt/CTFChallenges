# --- Stage 1: Build-Umgebung ---
FROM golang:1.22-alpine AS builder

# Installiert GCC und Build-Tools (zwingend nötig für den C-Code von go-sqlite3)
RUN apk add --no-cache build-base

WORKDIR /app

# Initialisiert das Go-Modul und lädt den SQLite-Treiber herunter
RUN go mod init weddingbook && go get github.com/mattn/go-sqlite3

# Kopiert den Go-Quellcode (main.go) in den Container
COPY /main/main.go .

# Kompiliere das Go-Projekt explizit für linux/amd64 (passend zu eurem deploy-Skript)
RUN CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -o weddingbook .


# --- Stage 2: Finale Laufzeit-Umgebung ---
FROM alpine:3.19

# libc6-compat für Go-CGO und dos2unix für den Windows-Zeilenenden-Fix
RUN apk add --no-cache libc6-compat sqlite-libs dos2unix

WORKDIR /app

# 1. Kopiere das fertige Go-Binary und das Entrypoint-Skript aus Stage 1
COPY --from=builder /app/weddingbook .
COPY entrypoint.sh .

# Windows-Zeilenenden fixen und ausführbar machen
RUN dos2unix entrypoint.sh && chmod +x entrypoint.sh weddingbook


EXPOSE 80

ENTRYPOINT ["./entrypoint.sh"]