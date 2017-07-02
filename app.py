from flask import Flask, jsonify, send_from_directory
from emojis import emojis
import random

app = Flask(__name__, static_url_path='')

@app.route('/')
def serve():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def send_assets(path):
    return send_from_directory('static', path)

@app.route('/rand')
def rand():
    return jsonify({ 'emoji': random.choice(emojis) })

