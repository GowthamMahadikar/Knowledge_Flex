from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/chat", methods=["POST"])
def chat():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json(silent=True)
    if not data or "prompt" not in data:
        return jsonify({"error": "Invalid JSON or missing 'prompt'"}), 400

    prompt = data["prompt"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
