import os
from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyDzT4_j3YgnXY-Tcj0u9Ggp-iVFYzeb--A"))

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
  <head><title>Flask Gemini Chat</title></head>
  <body>
    <h1>Chat with Gemini</h1>
    <form method="POST">
      <textarea name="message" rows="4" cols="50"
        placeholder="Type your question..."></textarea><br>
      <button type="submit">Send</button>
    </form>

    {% if reply %}
      <h2>Reply</h2>
      <p>{{ reply }}</p>
    {% endif %}
  </body>
</html>
"""

# Use a text model (change name if needed, e.g. "gemini-2.0-flash" or "gemini-1.5-flash")
model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(user_message: str) -> str:
    resp = model.generate_content(user_message)
    return resp.text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    reply = None
    if request.method == "POST":
        msg = request.form.get("message", "")
        if msg:
            reply = ask_gemini(msg)
    return render_template_string(HTML, reply=reply)

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(force=True)
    msg = data.get("message", "")
    if not msg:
        return jsonify({"error": "message is required"}), 400
    return jsonify({"reply": ask_gemini(msg)})

if __name__ == "__main__":
    app.run(debug=True)
