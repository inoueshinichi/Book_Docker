# Staging Build

# 踏み台イメージ
From golang:1.13.4-alpine3.10 as builder
WORKDIR /src
COPY ./go_server.go /src
RUN go build -o start_appserver ./go_server.go

# 本命イメージ
From alpine:3.10.3
COPY --from=builder /src/start_appserver /bin/start_appserver
CMD ["/bin/start_appserver"]


