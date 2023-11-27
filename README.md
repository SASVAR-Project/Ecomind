# EcoMind
EcoMind is a software that allows the classification and labeling of usable solid waste. Labeling categorizes waste according to specific characteristics
such as material, packaging color, and capacity. Labeling is used to identify the waste according to particular characteristics and thus create a dataset

![Linter](https://github.com/SASVAR-Project/Ecomind/actions/workflows/linter.yml/badge.svg)
![Unit tests](https://github.com/SASVAR-Project/Ecomind/actions/workflows/unit_test.yml/badge.svg)
![Docker Image](https://github.com/SASVAR-Project/Ecomind/actions/workflows/docker_image.yml/badge.svg)

# EcoMind documentation
EcoMind full documentation can be found here: [wiki](https://github.com/SASVAR-Project/Ecomind/wiki)

## Users documentation
- [Users - EcoMind manual](https://github.com/SASVAR-Project/Ecomind/wiki/Users-‐-EcoMind-manual)

## Developers documentation
- [Developers ‐ EcoMind installation](https://github.com/SASVAR-Project/Ecomind/wiki/Developers-‐-EcoMind-installation)
- [Developers ‐ EcoMind database](https://github.com/SASVAR-Project/Ecomind/wiki/Developers-‐-EcoMind-database)
- [Developers ‐ EcoMind architecture](https://github.com/SASVAR-Project/Ecomind/wiki/Developers-‐-EcoMind-architecture)
- [Developers ‐ EcoMind continuous integration and deployment](https://github.com/SASVAR-Project/Ecomind/wiki/Developers-‐-EcoMind-continuous-integration-and-deployment)

# EcoMind installation
Ecomind offers three ways to install the application. 

## Running with Python
1. Clone this repository: https://github.com/SASVAR-Project/Ecomind to your computer.
2. Located at the root of the project, move to the `src` directory with the following command: `cd src`
3. Run the following command: `pip install -r requirements.txt`
4. Run the following command: `python manage.py runserver`
5. Open **http://localhost:8000/** route in your browser.

## Running with Docker
1. Clone this repository: https://github.com/SASVAR-Project/Ecomind to your computer.
2. Run the following command to build the image, located at the root of the project: `sudo docker build -f ./src/Dockerfile ./src -t ecomind-app`
3. Run the following command to run the project on localhost: `sudo docker container run -d --name ecomind-docker -p 8000:8000 ecomind-app`
4. Open **http://localhost:8000/** route in your browser.

## Running with Docker Hub
1. Run the following command to run the project on localhost: `sudo docker run -d -p 8000:8000 --name ecomind-docker danielgara/ecomind`
2. Open **http://localhost:8000/** route in your browser.
