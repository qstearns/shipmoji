from flask import Flask, url_for

app = Flask(__name__)

url_for('public', filename='styles.css')
url_for('public', filename='index.html')

@app.route('/')
def hello_world():
    return 'Your mom'

