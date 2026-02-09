from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Jared's Kubernetes Lab is LIVE"

@app.route("/health")
def health():
    return "ok"

app.run(host="0.0.0.0", port=80)
