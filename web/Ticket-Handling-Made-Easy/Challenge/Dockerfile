FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask

# Einzeln und explizit kopieren, damit nichts verloren geht:
COPY app.py .
COPY entrypoint.sh .
COPY templates/ ./templates/

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]