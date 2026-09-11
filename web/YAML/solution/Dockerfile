
FROM docker.io/library/python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY exploit .
RUN chmod +x exploit

CMD /usr/bin/timeout -k 5 ${TIMEOUT} ./exploit