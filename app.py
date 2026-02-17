from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify(status="ok", env=os.getenv("WEBSITE_SITE_NAME", "local"))

if __name__ == "__main__":
    # Local run only. Azure uses Gunicorn from startup command.
    app.run(host="0.0.0.0", port=8000, debug=True)
