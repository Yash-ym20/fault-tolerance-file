from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

file_table = {}
NODES = ["http://localhost:5001", "http://localhost:5002"]

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.json['filename']
    file_table[filename] = NODES
    return jsonify({"nodes": NODES})

@app.route('/get/<filename>', methods=['GET'])
def get_file(filename):
    return jsonify({"nodes": file_table.get(filename, [])})

@app.route('/nodes', methods=['GET'])
def nodes():
    return jsonify({"nodes": NODES})

app.run(port=5000)