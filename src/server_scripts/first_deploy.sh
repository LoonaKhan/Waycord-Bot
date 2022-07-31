#!/bin/sh
# runs the first deployment
# todo:
#   install npm and run npm init before running the api image
#   do the same with python once the bot is ready

# installs docker
sudo apt remove docker docker-engine docker.io # removes any existing docker packages

# setup requirements for docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# installs docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# starts and enables docker on startup
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl enable containerd

# gets the mariadb docker image
sudo docker pull mariadb

# runs the mariadb image
# you need to put the root password
docker run --detach --name mariadb_dev --env MYSQL_ROOT_PASSWORD= -p 3306:3306  mariadb

# builds and runs the api image
cd /root/Waycord/src/api
docker build -t server .
docker run --detach --name server -e PASSWORD= -e USERNAME= -e HOST= -e KEY= -p 3000:4000 server
#node /root/Waycord/src/api/app.js # make this use the docker image instead

# runs the bot
cd /root/Waycord/src
python3 waycord_bot/bot.py # change this to a dsocker container