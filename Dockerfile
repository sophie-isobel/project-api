FROM python:3

WORKDIR /app
COPY . .
RUN pip install flask fastapi uvicorn python-multipart

ENV api_url="http://127.0.0.1:8000"

ENTRYPOINT uvicorn main:app --host 0.0.0.0