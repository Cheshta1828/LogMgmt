#!/bin/bash

# Change to the working directory
cd /app

# Install Python dependencies using pip
pip install -r requirements.txt

# Run the Django application
python manage.py runserver 0.0.0.0:8000
