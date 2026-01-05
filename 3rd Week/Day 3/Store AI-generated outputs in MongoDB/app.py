from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from ollama_model import generate_text

app = Flask(__name__)

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ai_database"]
collection = db["ollama_outputs"]

@app.route("/generate", methods=["POST"])
def generate_and_store():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Generate response from Ollama
    ai_output = generate_text(prompt)

    document = {
        "prompt": prompt,
        "ai_output": ai_output,
        "model": "llama3",
        "created_at": datetime.utcnow()
    }

    result = collection.insert_one(document)

    return jsonify({
        "message": "Ollama output stored successfully",
        "id": str(result.inserted_id),
        "output": ai_output
    }), 201


@app.route("/outputs", methods=["GET"])
def get_outputs():
    results = []
    for doc in collection.find():
        doc["_id"] = str(doc["_id"])
        results.append(doc)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
