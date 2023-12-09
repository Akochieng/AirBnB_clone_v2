#!/usr/bin/env bash
#simple script to set up servers
sudo apt update
sudo apt install nginx -y
/usr/sbin/nginx
mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo "Holberton School" | tee -a /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test
chown -R ubuntu:ubuntu /data
sed '/ pass PHP scripts to FastCGI server/i \
	\tlocation /hbnb_static {\
	\t\talias /data/web_static/current/ \
	\t}' /etc/nginx/sites-enabled/default
nginx -s reload
