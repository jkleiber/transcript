# FROM python:3.10.11
FROM ubuntu:22.04

# Install system level dependencies
RUN apt-get update 
RUN apt-get install ffmpeg python3.10 python3-pip python3.10-venv -y

# Install pypoetry
ENV POETRY_HOME="/opt/poetry/"
ENV PATH="${PATH}:/opt/poetry/bin"
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry
RUN $POETRY_HOME/bin/poetry --version

# Put the app's directory in the top level of the container
COPY ./ /transcript
WORKDIR /transcript

# Expose the port
EXPOSE 5001

# Install dependencies based on requirements.txt
# RUN python -m pip install -r requirements.txt

# ENTRYPOINT [ "gunicorn" ]

# # This works when running without systemd
# CMD ["-b", "0.0.0.0:5001", "wsgi:app"]

CMD tail -f /dev/null
