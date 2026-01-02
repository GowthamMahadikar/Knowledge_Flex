from flask import Flask, render_template_string, request
from textblob import TextBlob

app = Flask(__name__)

# Simple HTML template as a string
TEMPLATE = """
<!doctype html>
<html>
  <head><title>Sentiment App</title></head>
  <body>
    <h1>Sentiment Analysis</h1>
    <form method="POST">
      <textarea name="text" rows="5" cols="40"
        placeholder="Type some text here..."></textarea><br>
      <button type="submit">Analyze</button>
    </form>

    {% if result is not none %}
      <h2>Result</h2>
      <p><b>Polarity</b>: {{ result.polarity }}</p>
      <p><b>Subjectivity</b>: {{ result.subjectivity }}</p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        blob = TextBlob(text)
        result = {
            "polarity": blob.sentiment.polarity,       # -1 (negative) to 1 (positive)
            "subjectivity": blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
        }
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
