From nginx:1.17.5-alpine
COPY ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
ENV PORT=80
ENV DEBUG=False
CMD ["/usr/local/bin/start.sh"]

