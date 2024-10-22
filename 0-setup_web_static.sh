#!/usr/bin/env bash
# A Bash script that sets up my web servers for the deployment of web_static.

# Install Nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx
service nginx start

# Create directories if they don't exist
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Alx (Holberton) School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
