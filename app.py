from flask import Flask, jsonify
from emojis import emojis
import random
import yaml

app = Flask(__name__)

@app.route('/rand')
def rand():
    return jsonify({ 'emoji': random.choice(emojis) })

