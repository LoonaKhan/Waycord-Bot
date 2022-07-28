# Waycord

An discord bot archiver.

# dependancies
- mariadb:10.8.3 docker image

# Deployment:
- create the mariadb container:
```shell
docker run --detach --name mariadb_dev --env MYSQL_ROOT_PASSWORD=1234 -e MYSQL_USER=dev_user -e MYSQL_PASSWORD=1234 -p 10.0.0.186:3306:3306  mariadb
```
- log into the db and configure the db
```shell
mysql -u [user] -h [ip] -p
```
- copy the contents of src/db/db_setup.sql and paste into the db shell.
- build the docker image in src/server and run the container.
```shell
docker build -t monemperor/server
docker run -p 3000:4000 monemperor/server
```

## todo:
- api calls
- docs + README
- discord bot
- host it somewhere.
