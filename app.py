from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import bcrypt
import os
from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']

            return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')

    if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
                port=int(os.environ.get('PORT')),
                debug=False)
