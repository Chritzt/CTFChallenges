FROM docker.io/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY exploit .
COPY challenge.proto .

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. challenge.proto

RUN chmod +x exploit

CMD ["./exploit"]