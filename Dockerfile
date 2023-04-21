# syntax=docker/dockerfile:1.4
#FROM python:3.10-alpine AS builder
FROM python:3.9-slim AS builder
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
#RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install --upgrade pip
#RUN pip install numpy cython
COPY requirements.txt .
RUN pip install -r requirements.txt

#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
#EXPOSE 80
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=main.py

#CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
# This is working but probably i dont need this becasue i already define it in 
# the .yaml file
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:create_app()"]
