from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from ollama_model import generate_text

app = Flask(__name__)

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ai_database"]
collection = db["ollama_outputs"]

# --------------------------------------------------
# Generate AI Output
# --------------------------------------------------
@app.route("/generate", methods=["POST"])
def generate_and_store():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    ai_output = generate_text(prompt)

    document = {
    "prompt": prompt,
    "ai_output": ai_output,
    "model": "llama3",
    "status": "Open",
    "priority": "Medium",
    "assignee": None,
    "tags": [],
    "due_date": None,
    "version": 1,
    "last_modified_by": "system",
    "created_at": datetime.utcnow(),
    "updated_at": datetime.utcnow()
}


    result = collection.insert_one(document)

    return jsonify({
        "message": "Ollama output stored successfully",
        "id": str(result.inserted_id),
        "ai_output": ai_output
    })

# --------------------------------------------------
# View Outputs (Table / HTML)
# --------------------------------------------------
@app.route("/outputs", methods=["GET"])
def get_outputs():
    outputs = []
    for doc in collection.find().sort("created_at", -1):
        doc["_id"] = str(doc["_id"])
        outputs.append(doc)

    return render_template("outputs.html", outputs=outputs)

# --------------------------------------------------
# Update Task Metadata
# --------------------------------------------------
@app.route("/update-task/<task_id>", methods=["PUT"])
def update_task_metadata(task_id):
    data = request.json

    set_fields = {}

    allowed_fields = [
        "status",
        "priority",
        "assignee",
        "tags",
        "due_date",
        "last_modified_by",
        "prompt"
    ]

    for field in allowed_fields:
        if field in data:
            set_fields[field] = data[field]

    if not set_fields:
        return jsonify({"error": "No valid fields to update"}), 400

    # Always update timestamp
    set_fields["updated_at"] = datetime.utcnow()

    result = collection.update_one(
        {"_id": ObjectId(task_id)},
        {
            "$set": set_fields,
            "$inc": {"version": 1}
        }
    )

    if result.matched_count == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "message": "Task updated successfully",
        "updated_fields": set_fields,
        "version_incremented": True
    })

# --------------------------------------------------
# Run App (MUST BE LAST)
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
