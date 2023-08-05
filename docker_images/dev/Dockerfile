FROM python:3.10.11

# Install system level dependencies
RUN python -m pip install gunicorn flask

# Install pypoetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

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
