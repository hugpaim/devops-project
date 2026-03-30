from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter('app_requests_total', 'Total requests')

@app.route("/")
def home():
    REQUESTS.inc()
    return "DevOps Lab Running 🚀"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
