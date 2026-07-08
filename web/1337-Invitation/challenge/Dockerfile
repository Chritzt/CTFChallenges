# Wir nutzen ein offizielles Python-Image auf Ubuntu-Basis
FROM python:3.10-slim-bullseye

# Installiere wkhtmltopdf und benötigte System-Bibliotheken
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    xfonts-75dpi \
    xfonts-base \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# Python-Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Den App-Code in den Container kopieren
COPY app.py .

# Exponiere den Port 5000 für Flask
EXPOSE 5000

# Starte die Flask-Anwendung
CMD ["python", "app.py"]