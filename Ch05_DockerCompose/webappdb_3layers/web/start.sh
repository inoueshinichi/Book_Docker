#!/bin/sh

# NginxのWebサーバ設定からリバースプロキシーサーバ設定への変更
sed -e "s/{{NAIVE_HTTP_PORT}}/$NAIVE_HTTP_PORT/g" /etc/nginx/nginx.conf.tmp > /etc/nginx/nginx.conf
sed -i -e "s^{{APP_SERVER}}^$APP_SERVER^g" /etc/nginx/nginx.conf

# PID1としてNginxを起動する
exec nginx -g "daemon off;"