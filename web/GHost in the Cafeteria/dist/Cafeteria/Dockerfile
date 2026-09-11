FROM python:3.12-slim

# 1. Module installieren (Muss vor dem COPY stehen!)
RUN pip install flask requests

WORKDIR /app

# 2. Dateien kopieren
COPY app.py .
COPY entrypoint.sh .

# 3. Rechte vergeben und starten
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]