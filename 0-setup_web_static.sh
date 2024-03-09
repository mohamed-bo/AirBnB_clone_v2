#!/usr/bin/env bash
# install config edit index strat ngix
SERVER_NGIX="server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;

	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}

	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://intranet.alxswe.com/projects/288 permanent;
	}

	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"
INDEX_PAGE="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
    apt-get update
    apt-get -y install nginx
fi
sudo mkdir -p /var/www/html /var/www/error
sudo chmod -R 755 /var/www
sudo echo 'Hello World!' > /var/www/html/index.html
sudo echo -e "Ceci n\x27est pas une page" > /var/www/error/404.html
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo -e "$INDEX_PAGE" > /data/web_static/releases/test/index.html
[ -d /data/web_static/current ] && sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo bash -c "echo -e '$SERVER_NGIX' > /etc/nginx/sites-available/default"
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
if [ "$(pgrep -c nginx)" -le 0 ]; then
	sudo service nginx start
else
	sudo service nginx restart
fi
