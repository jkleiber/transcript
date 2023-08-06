#! /bin/bash

# Ensure dependencies are set up correctly.
poetry update

# Run the server
poetry run python app/main.py
