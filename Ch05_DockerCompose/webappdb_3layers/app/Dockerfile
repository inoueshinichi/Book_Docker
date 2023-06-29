# Dockerfile for flask

# Image
From python:3.9.17-slim

Label author="inoue.shinichi.1800@gmail.com"

# Flask 2.3.2 (Python >= 3.8)
# Redis 3.3.8
RUN pip install flask==2.3.2 redis==3.3.8

WORKDIR /flask_app
COPY ./bind_src/flask_server.py /flask_app

ENV APP_PORT 80

# Default db conf
ENV REDIS_HOST 127.0.0.1
ENV REDIS_PORT 6379
ENV REDIS_DB 0

CMD ["python", "-u", "/flask_app/flask_server.py"]