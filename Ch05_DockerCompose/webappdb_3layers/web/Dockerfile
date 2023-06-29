# Dockerfile for Nginx

# Image
From nginx:1.17.5-alpine

Label author="inoue.shinichi.1800@gmail.com"

# Copy
# ここにnginx.conf.tmpを追加する.
COPY ./start.sh /usr/local/bin/start.sh

# Env
ENV PORT=80

# Open Ports
EXPOSE 80


RUN chmod +x /usr/local/bin/start.sh
CMD ["/usr/local/bin/start.sh"]