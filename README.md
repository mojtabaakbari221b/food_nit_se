# resturant_nit_se

### RUN THIS COMMANDS ON ROOT DIRECTRORY OF PROJECT

## START PROJECT :
```
$ docker volume create resturant_static_volume
$ docker volume create resturant_media_volume
$ docker volume create resturant_postgresql_volume
```
```
$ docker network create resturant_network
```
```
$ docker-compose build
$ docker-compose up -d
```
```
$ docker exec -it resturant python manage.py createsuperuser
```
## UPDATE PROJECT :
```
$ docker-compose down
$ docker-compose build (IF IMAGES ARE CHANGED)
$ docker-compose up -d
```

## UPDATE DATABASE IF MODELS ARE CHANGED
```
$ docker exec -it resturant python manage.py makemigrations
$ docker exec -it resturant python manage.py migrate
```