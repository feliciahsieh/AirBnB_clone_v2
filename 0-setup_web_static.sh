#!/usr/bin/env bash
# Deploy webservers (web01, web02) in web_static using Fabric
# 142.44.167.237 214-web-01 144.217.246.206 214-web-02

# install nginx
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# create folders
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create basic HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create new symbolic link
if [ -L /data/web_static/current ]
then sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# change owner & group of /data/ to ubuntu
sudo chown -R ubuntu /data
sudo chown -R ubuntu:ubuntu /data

# update nginx to serve content of /data/web_static/current to hbnb_static
sudo sed -i '17i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart

exit 0
