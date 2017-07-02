from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Your mom'

