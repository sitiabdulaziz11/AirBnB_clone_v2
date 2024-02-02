#!/usr/bin/env bash
# A Bash script that sets up my web servers for the deployment of web_static project.

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "Holberton School for the win!" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
NEW_STRING="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "38i $NEW_STRING" /etc/nginx/sites-available/default
sudo service nginx restart