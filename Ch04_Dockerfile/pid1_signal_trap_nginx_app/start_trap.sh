#!/bin/sh

handle() {
    echo 'handle sigterm/sigint'
    exit 0
}

# trapコマンドで sigterm/sigintをフックする
trap handle TERM INT

nginx -g "daemon off;" & 
wait

