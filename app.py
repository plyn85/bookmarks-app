from os import path
from flask import Flask render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import os
app = Flask(__name__)

app.config["MONGO_DBNAME"] = ""
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
if path.exists("env.py"):
    import env


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
