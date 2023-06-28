From golang:1.13.4-alpine3.10 as builder
WORKDIR /src
COPY ./main.go /src
RUN go build -o start_appserver main.go

From alpine:3.10.3
COPY --from=builder /src/start_appserver /bin/start_appserver
CMD ["/bin/start_appserver"]