@echo off

:: Define variables
set docker-img="transcript-alpha-img"
set container="transcript-alpha-container"
set dev-container="transcript-dev-container"

:: Stop and remove conflicting containers
docker stop %container%
docker rm %container%
docker stop %dev-container%
docker rm %dev-container%

:: Build the image
docker build . -f docker_images/alpha/Dockerfile -t %docker-img%

:: Run a docker image for development on static dependencies.
:: This is closer to a production environment than normal dev.
docker run --name %container%^
 -d^
 -v %cd%/../transcript:/transcript^
 -p 5001:5001^
 %docker-img%
 