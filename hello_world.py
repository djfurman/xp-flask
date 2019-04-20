"""
A basic hello world example for flask web pages
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"
