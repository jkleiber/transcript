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

# Install the pypoetry dependencies globally
RUN poetry export -f requirements.txt --output requirements.txt
RUN python3 -m pip install -r requirements.txt

# Expose the port
EXPOSE 5001

# Install developer dependencies
RUN apt-get install -y htop

# Run the container until it is explicitly stopped
CMD tail -f /dev/null
