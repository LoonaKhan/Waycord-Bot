# node version
FROM mariadb:10.8.3
FROM node:16.13.1

# copies the server package
COPY . /app

# working directory = src/server.
# running npm start or node app.js now works as normal
WORKDIR /app

# runs npm install
RUN npm install

# env variables
ENV PORT=4000

# actually forwards the port
EXPOSE 4000

# the command run. an array of strings
CMD [ "npm", "start" ]
