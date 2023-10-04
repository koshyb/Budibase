# Using a base image with Python pre-installed
FROM python:3.8-slim

# Setting the working directory
WORKDIR /app

# Copying the Python script into the container
COPY metrics_exporter.py /app/metrics_exporter.py

# Installing Flask and psutil
RUN pip install Flask psutil

# Port to listen on
EXPOSE 8081

# Starting the exporter
CMD ["python", "metrics_exporter.py"]
