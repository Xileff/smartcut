FROM python:3.10

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn","--bind=0.0.0.0:8080","app:app"]