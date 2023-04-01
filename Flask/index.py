from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)

# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=100)


app.secret_key = 'BAD_SECRET_KEY'


@app.route("/")
def hello_world():
    session['NAME'] = "Phong"
    session['NAME2'] = "Test2"
    return "<p>Hello, World!</p>"

@app.route("/app")
def hello_world2():

    return f"<p>Hello, World!</p> {session.get('NAME')}"