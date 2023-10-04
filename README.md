# Part 3

This Python script creates a Flask web application with a single /metrics endpoint. 
When you access this endpoint, it calculates CPU load and memory usage, formats them in Prometheus-style metrics

Build the Docker image from the provided Dockerfile.

docker build -t system-metrics-exporter .

Run docker-compose up -d to start all three containers, including the new system metrics exporter.

Once the Metrics Exporter is running, you can access the metrics on the terminal (recommened):

curl http://localhost:8081/metrics

you can also view it on http://localhost:8081/metrics but beware this is just outputted as txt and will depend how the web interface is rendering the metrics
