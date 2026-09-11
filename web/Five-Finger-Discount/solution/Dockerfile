FROM python:3.12-slim
RUN apt-get update && apt-get install -y iputils-ping curl && rm -rf /var/lib/apt/lists/*
RUN pip install requests
COPY exploit /app/exploit
RUN chmod +x /app/exploit
WORKDIR /app
CMD ["./exploit"]