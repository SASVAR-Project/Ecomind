# Proyecto

## Correr con Python

1. Clona este repositorio en tu computador.

2. Ejecuta el siguiente comando `python manage.py runserver`

## Correr con Docker

1. Clona este repositorio en tu computador.

2. Ejecuta el siguiente comando para construir la imagen, ubicado en la raíz del proyecto.

`sudo docker build -t ecomind-app .`

3. Ejecuta el siguiente comando correr el proyecto en localhost.

`sudo docker container run -d --name ecomind-docker -p 80:80 ecomind-app`

## Correr con Docker Hub

1. Ejecuta el siguiente comando correr el proyecto en localhost.

`sudo docker run -d -p 80:80 --name ecomind-docker danielgara/ecomind`