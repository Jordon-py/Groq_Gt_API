from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# ---------------------------------> Load API key from .env file
load_dotenv('.env')
GROQ_API_KEY = os.getenv("GROQ_API_KEY")



# -------------------------------> Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Groq GT API is running!"})



# -------------------------- Runs API

    port = int(os.environ.get("PORT", 5000))  # Use Heroku's port
    app.run(debug=True, host="0.0.0.0", port=port)

