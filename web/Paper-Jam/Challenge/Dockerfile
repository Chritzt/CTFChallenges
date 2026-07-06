# --- STAGE 1: Die App im Container bauen ---
FROM maven:3.8.5-openjdk-17 AS builder
WORKDIR /build

# Nur die für den Build wichtigen Dateien kopieren
COPY pom.xml .
COPY src ./src

# Die JAR-Datei direkt im Docker-Container bauen
RUN mvn clean package -DskipTests

# --- STAGE 2: Die schlanke Laufzeitumgebung ---
FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app

# Wir kopieren die frisch gebaute JAR aus der ersten Stage
COPY --from=builder /build/target/Challenge-0.0.1-SNAPSHOT.jar app.jar

# Skript und Flagge kopieren
COPY entrypoint.sh /app/entrypoint.sh

RUN sed -i 's/\r$//' /app/entrypoint.sh && chmod +x /app/entrypoint.sh

EXPOSE 3000
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]