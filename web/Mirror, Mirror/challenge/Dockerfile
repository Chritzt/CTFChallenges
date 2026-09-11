FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir grpcio grpcio-tools grpcio-reflection

COPY server.py challenge.proto ./

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. challenge.proto

EXPOSE 50051

CMD ["python", "server.py"]