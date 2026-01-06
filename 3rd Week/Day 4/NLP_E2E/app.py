
from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_classifier(text):
    if "bug" in text.lower() or "crash" in text.lower():
        return "Bug", 0.95
    return "Feature", 0.80

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    label, confidence = simple_classifier(text)
    return jsonify({"label": label, "confidence": confidence})

if __name__ == "__main__":
    app.run(debug=True)
