# Imports
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from flask_moment import Moment
# Importing path from env.py
from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)
#  configuring enviroment variables which are set in env.py
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)
moment = Moment(app)
# index,  login, register, and log out section -----------------------------------------
@app.route('/index')
@app.route('/')
def index():
    users = mongo.db.users.find()
    categories = mongo.db.categories.find()
    bookmarks = mongo.db.bookmarks.find()
    return render_template('index.html', categories=categories, bookmarks=bookmarks, users=users)


@app.route('/login', methods=['POST', 'GET'])
# First we find the logged in user in the data base
#    If it the user exists In the database we compare the
#    encncipted password from the form and the database
#    password with the database password. The username is added to the session
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
        flash(
            f'Login  Unsuccessful. Please check username/password conbination', 'danger')

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
    session.clear()
    flash(f'You are now  logged out!', 'danger')
    return redirect(url_for('index'))

# user section
@app.route('/users')
def users():
    users = mongo.db.users.find()
    categories = mongo.db.categories.find()
    bookmarks = mongo.db.bookmarks.find()
    return render_template('users.html', users=users, bookmarks=bookmarks, categories=categories)
# bookmarks section ---------------------------------------------------------------------
@app.route('/add_bookmark')
def add_bookmark():
    categories = mongo.db.categories.find()
    return render_template('add_bookmark.html', categories=categories)


@app.route('/insert_bookmark',  methods=["GET", "POST"])
def insert_bookmark():
    bookmarks = mongo.db.bookmarks
    bookmarks.insert_one({
        'username': session['username'],
        'category_name': request.form.get('category_name'),
        'add_bookmark_url': request.form.get('add_bookmark_url'),
        'bookmark_description': request.form.get('bookmark_description'),
    })
    return redirect(url_for('users'))


@app.route("/edit_bookmark/<book_id>")
def edit_bookmark(book_id):
    all_categories = mongo.db.categories.find()
    the_bookmark = mongo.db.bookmarks.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_bookmark.html", book=the_bookmark, categories=all_categories)


@app.route('/update_bookmark/<book_id>', methods=["POST"])
def update_bookmark(book_id):
    bookmarks = mongo.db.bookmarks
    bookmarks.update({'_id': ObjectId(book_id)},
                     {
        'username': session['username'],
        'category_name': request.form.get('category_name'),
        'add_bookmark_url': request.form.get('add_bookmark_url'),
        'bookmark_description': request.form.get('bookmark_description')

    })
    return redirect(url_for('users'))


@app.route('/remove_bookmark/<book_id>')
def remove_bookmark(book_id):
    mongo.db.bookmarks.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('users'))
# end bookmarks section ------------------------------------------------------------------

#  categories section -----------------------------------------------------------------------
@app.route('/user_categories')
def user_categories():
    categories = mongo.db.categories.find()
    return render_template('categories.html', categories=categories)


@app.route('/add_category')
def add_category():
    return render_template('add_category.html')


@app.route('/insert_category', methods=["POST"])
def insert_category():
    category = mongo.db.categories
    category.insert_one({
        'username': session['username'],
        'category_name': request.form.get('category_name')


    })
    return redirect(url_for('user_categories'))


@app.route('/edit_category/<cat_id>')
def edit_category(cat_id):
    category = mongo.db.categories.find_one(
        {'_id': ObjectId(cat_id)})
    return render_template('edit_category.html', cat=category
                           )


@app.route('/update_category/<cat_id>', methods=['POST'])
def update_category(cat_id):
    mongo.db.categories.update(
        {'_id': ObjectId(cat_id)},
        {'category_name': request.form.get('category_name'),
         'username': session['username']
         })
    return redirect(url_for('user_categories'))


@app.route('/delete_category/<cat_id>')
def delete_category(cat_id):
    mongo.db.categories.remove({'_id': ObjectId(cat_id)})
    return redirect(url_for('user_categories'))


#  end categories section ---------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
