FROM python:3.12-slim

RUN pip install flask requests

WORKDIR /app

# Kopiere den Code und das Skript
COPY app.py .
COPY entrypoint.sh .

# Macht das Skript innerhalb des Containers ausführbar
RUN chmod +x entrypoint.sh

# Definiert das Skript als Einstiegspunkt
ENTRYPOINT ["./entrypoint.sh"]