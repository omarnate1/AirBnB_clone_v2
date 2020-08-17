#!/usr/bin/env bash
# Create directories for the project and setup nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# update config file to redirect
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /data/web_static/current;
    index  index.html index.htm 8-index.html;

    add_header X-Served-By 1574-web-01;

    location / {
        alias /data/web_static/current/;
    }

    location /redirect_me {
        return 301 http://google.com/;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
