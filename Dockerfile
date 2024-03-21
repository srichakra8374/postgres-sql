# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# install required packages for system
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install app dependencies
RUN pip install  psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .
#set envirment variable
ENV DB_USER=flaskdevl
ENV DB_USER_PWD=flaskdevl01
ENV DB_HOST=dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com
# Specify the command to run your application
CMD ["python", "app.py"]

