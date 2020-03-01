import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt


from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # taken an altered from a tutorial found at https://www.youtube.com/watch?v=vVx1737auSE
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form.get('password').encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form.get('username')
                session['logged_in'] = True
                flash(f'You are logged in!', 'success')
                return redirect(url_for('index'))
            else:
                flash(
                    f'Login  Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    '''taken an altered from a tutorial found at https://www.youtube.com/watch?v=vVx1737auSE'''
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            flash(f'You are now regsitered please login!', 'success')
            return redirect(url_for('login'))
        else:
            flash(
                f'Registraion Unsuccessful. Please check username and password', 'danger')
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(f'You are now  logged out!', 'danger')
    return redirect(url_for('index'))


@app.route('/user_bookmarks')
def user_bookmarks():
    return render_template('bookmarks.html', bookmark=mongo.db.bookmarks.find())


@app.route('/add_bookmark')
def add_bookmark():
    return render_template('add_bookmark.html')


@app.route('/insert_bookmark',  methods=["GET", "POST"])
def insert_bookmark():
    bookmarks = mongo.db.bookmarks
    bookmarks.insert_one(request.form.to_dict())
    return redirect(url_for('user_bookmarks'))


@app.route('/edit_bookmark')
def edit_bookmark():
    return render_template('edit_bookmark.html')


@app.route("/remove/<bookmark_id>")
def remove(bookmark_id):
    mongo.db.bookmarks.remove({"_id": ObjectId(bookmark_id)})
    return redirect(url_for('user_bookmarks'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',  categories=mongo.db.categories.find())


@app.route('/insert_category',  methods=["GET", "POST"])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('add_category.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
