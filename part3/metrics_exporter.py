from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    # Get system metrics
    cpu_load = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    # Define Prometheus-style metrics
    prom_metrics = [
        f'# HELP cpu_load CPU Load in percentage',
        f'# TYPE cpu_load gauge',
        f'cpu_load {cpu_load}',
        f'# HELP memory_usage Memory Usage in percentage',
        f'# TYPE memory_usage gauge',
        f'memory_usage {memory_usage}'
    ]

    return '\n'.join(prom_metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
