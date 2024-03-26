FROM python:3.11-slim

ENV API_VERSION 0.1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

CMD uvicorn main:app --host 0.0.0.0 --port 8000 