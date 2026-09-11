FROM python:3.11-alpine
WORKDIR /app
RUN pip install flask
COPY app.py /app/
COPY templates/ /app/templates/

RUN touch /app/data.db && chmod 666 /app/data.db

ENV FLAG="CLA{DEFAULT_FLAG_FOR_LOCAL_TESTING}"

CMD ["python", "app.py"]