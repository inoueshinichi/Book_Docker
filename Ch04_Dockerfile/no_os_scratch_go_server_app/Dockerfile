From golang:1.13.4-alpine3.10 as builder
WORKDIR /src
COPY ./main.go /src
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o start_appserver main.go

From scratch
COPY --from=builder /src/start_appserver /start_appserver
CMD ["/start_appserver"]
