from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/sample')
def sample_worky():
    return 'This is working again .. muhahaha'