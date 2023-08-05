@echo off

:: Define variables
set docker-img="transcript-dev-img"
set container="transcript-dev-container"

:: Stop and remove conflicting containers
docker stop %container%
docker rm %container%

:: Build the image
docker build . -f docker_images/dev/Dockerfile -t %docker-img%

:: Run the docker image for the development
docker run --name %container%^
 -d^
 -v %cd%/../transcript:/transcript^
 -p 5001:5001^
 %docker-img%
 