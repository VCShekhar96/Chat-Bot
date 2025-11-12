""" 
AI ChatBot using Gemini API (Google Generative AI)
Author: V Chandrashekhar
Description: Flask-based chatbot integrating Gemini API for intelligent responses.
"""
import os
from flask import Flask, render_template, request, jsonify
from api_handler import get_gemini_response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form.get("msg", "")
    if not user_input:
        return jsonify({"response": "Please send a non-empty message."})
    bot_response = get_gemini_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    # Use 0.0.0.0 for deployment environments
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
