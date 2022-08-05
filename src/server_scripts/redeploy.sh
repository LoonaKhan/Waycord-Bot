#!/bin/sh

# redeploys the app
# rebuilds and runs the api container
# rebuilds and runs the bot container

# pulls the repo
cd /root/Waycord/
git pull

# builds and runs the api image
cd /root/Waycord/src/api
docker build -t server .
docker run --detach --name server -e PASSWORD= -e USERNAME= -e HOST= -e KEY= -p 3000:4000 server
#node /root/Waycord/src/api/app.js # make this use the docker image instead

# runs the bot
cd /root/Waycord/src
python3 waycord_bot/bot.py # change this to a dsocker container
