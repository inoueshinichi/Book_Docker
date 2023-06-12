##########################
#  WordPress and MySql   #
##########################
#!/bin/bash

# Make wordpress container network
echo "[[[Make docker network]]]"
docker network create -d bridge wp-net

# Start mysql container
echo "[[[Start mysql container]]]"
docker container run -d --rm --network wp-net \
  --mount source=mysqlvolume,target=/var/lib/mysql \
  --mount type=bind,source=$HOME/Desktop/MyGithub/Book_Docker/Ch03_WordPressMySql/MySqlBackup,target=/mysqlbackup \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wordpress \
  -e MYSQL_PASSWORD=password \
  --name mysql-container \
  mysql:5.7.28

# Start wordpress container
echo "[[[Start wordpress container]]]"
docker container run -d --rm --network wp-net \
  -p 8080:80 \
  -e WORDPRESS_DB_HOST=mysql-container:3306 \
  -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=wordpress \
  -e WORDPRESS_DB_PASSWORD=password \
  --name wordpress-container \
  wordpress:5.2.3-php7.3-apache

echo "Finish container building."


