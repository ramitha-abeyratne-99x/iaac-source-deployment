from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Python 7 - Flask app running!'