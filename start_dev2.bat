@echo off

:: Define variables
set docker-img="transcript-dev2-img"
set container="transcript-dev2-container"
set dev-container="transcript-dev-container"

:: Stop and remove conflicting containers
docker stop %container%
docker rm %container%
docker stop %dev-container%
docker rm %dev-container%

:: Build the image
docker build . -f docker_images/dev2/Dockerfile -t %docker-img%

:: Run a docker image for development
docker run --name %container%^
 -d^
 -v %cd%/../transcript:/transcript^
 -p 5001:5001^
 %docker-img%
 