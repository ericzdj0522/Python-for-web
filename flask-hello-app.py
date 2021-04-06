from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'A quick test1111111111'