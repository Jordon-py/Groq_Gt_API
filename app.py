from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv


# ---------------------------------> Load API key from .env file
load_dotenv('.env')
GROQ_API_KEY = os.getenv("GROQ_API_KEY")



# -------------------------------> Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Groq GT API is running!"})



# -------------------------- Runs API
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use Heroku's port
    app.run(debug=True, host="0.0.0.0", port=port)

