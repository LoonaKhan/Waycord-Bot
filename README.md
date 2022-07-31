# Waycord

An discord bot archiver.

# dependancies
- mariadb:10.8.3 docker image

# Deployment:
- create the mariadb container:
```shell
docker run --detach --name mariadb_dev --env MYSQL_ROOT_PASSWORD=[password] -p [ip]:3306:3306  mariadb
```
- log into the db and configure the db
```shell
mysql -u [user] -h [ip] -p
```
- copy the contents of src/db/db_setup.sql and paste into the db shell.
- build the docker image in src/server and run the container.
```shell
cd Waycord/src/server
docker build -t server .
docker run --detach --name app -e PASSWORD=[password] -e USERNAME=[username] -e HOST=[ip] -e KEY=[key] -p [ip]:3000:4000 server
```

## todo:
- api calls
- docs + README
- discord bot
- host it somewhere.
