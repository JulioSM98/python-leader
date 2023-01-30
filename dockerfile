FROM python:3.10.9-alpine3.17

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app