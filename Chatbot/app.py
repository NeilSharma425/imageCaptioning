from chatbot import callModel
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "hello"
@app.route('/chatbot', methods=['POST'])

def handle_prompt():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt required"})
    
    response = callModel(prompt)
    return jsonify({"response": response})
if __name__ == '__main__':
    app.run()