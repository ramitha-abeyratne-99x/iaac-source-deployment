from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Python xyz1 - test XX - Martin and Jon - Demo Time - Flask app running!'