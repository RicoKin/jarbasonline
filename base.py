from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_text():
    text = request.json["text"]
    text = text.lower()
    text = " ".join(text.splitlines())
    result = ""

    openai.api_key = "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"

    def generate_text(prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.6,
        )
        message = completions.choices[0].text
        return message.strip()
    prompt = text
    result = generate_text(prompt)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


