# Dockerfile for Nginx

# Image
From nginx:1.17.5-alpine

Label author="inoue.shinichi.1800@gmail.com"

COPY ./nginx.conf.tmp /etc/nginx/
COPY ./start.sh /usr/local/bin

ENV NAIVE_HTTP_PORT=${HTTP_PORT}
EXPOSE ${HTTP_PORT}

RUN chmod +x /usr/local/bin/start.sh
CMD ["/usr/local/bin/start.sh"]