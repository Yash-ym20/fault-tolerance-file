from flask import Flask, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

STORAGE = "storage_node2"
os.makedirs(STORAGE, exist_ok=True)

@app.route('/store', methods=['POST'])
def store():
    file = request.files['file']
    path = os.path.join(STORAGE, file.filename)
    file.save(path)
    return "Stored"

@app.route('/get/<filename>', methods=['GET'])
def get_file(filename):
    path = os.path.join(STORAGE, filename)
    if os.path.exists(path):
        return send_file(path)
    return "Not Found", 404

@app.route('/')
def home():
    return "Node2 Running"

app.run(port=5002)