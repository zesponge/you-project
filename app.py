from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<p>lebron the goat</p>"