# Imports
import os
import math
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import bcrypt
from datetime import datetime
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

# global collection varibales set here
users_collection = mongo.db.users
bookmarks_collection = mongo.db.bookmarks
categories_collection = mongo.db.categories

# index,  login, register, and log out section -----------------------------------------
@app.route('/index', methods=['GET'])
@app.route('/')
# User authentication with thanks to Miroslav Svec, DCD Channel lead.
# altered from https://github.com/MiroslavSvec/DCD_lead/tree/pagination
def index():

    num_results = bookmarks_collection.count()
    users = users_collection.find()
    categories = categories_collection.find()
    if request.method == "GET":
        p_limit = int(request.args.get('limit', 6))
        p_offset = int(request.args.get('offset', 0))
        bookmarks = bookmarks_collection.find().sort([
            ("upvotes", -1), ("_id", -1)]).limit(p_limit).skip(p_offset)
        args = {
            "p_limit": p_limit,
            "p_offset": p_offset,
            "num_results": num_results,
            "next_url": f"/index?limit={str(p_limit)}&offset={str(p_offset + p_limit)}",
            "prev_url": f"/index?limit={str(p_limit)}&offset={str(p_offset - p_limit)}",

        }

    return render_template('index.html', categories=categories, bookmarks=bookmarks, users=users, args=args)


@app.route('/login', methods=['POST', 'GET'])
# First we find the logged in user in the data base
#    If it the user exists In the database we compare the
#    encncipted password from the form and the database
#    password with the database password. The username is added to the session
def login():
    # taken an altered from a tutorial found at https://www.youtube.com/watch?v=vVx1737auSE
    if request.method == 'POST':
        login_user = users_collection.find_one(
            {'name': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form.get('password').encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form.get('username')
                session['logged_in'] = True
                flash(f'You are logged in!', 'success')
                return redirect(url_for('index'))
        flash(
            f'Login  Unsuccessful. Please check username/password combination', 'danger')

    return render_template('login.html', title="Login")


@app.route('/register', methods=['POST', 'GET'])
def register():
    '''taken an altered from a tutorial found at https://www.youtube.com/watch?v=vVx1737auSE'''
    if request.method == 'POST':
        existing_user = users_collection.find_one(
            {'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users_collection.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            flash(f'You are now regsitered please login!', 'success')
            return redirect(url_for('login'))
        else:
            flash(
                f'Username Is in Use. Please Try a different username', 'danger')
    return render_template('register.html', title="Regsiter")


@app.route('/logout')
def logout():
    session.clear()
    flash(f'You are now  logged out!', 'danger')
    return redirect(url_for('index'))
# search bar section

# search bar
@app.route('/search_results', methods=['POST', 'GET'])
def search_results():
    if request.method == "POST":
        bookmarks = bookmarks_collection.find()
        query = request.form.get('search_bar')
        results = bookmarks_collection.find({'$text': {'$search': query}})
        if query == "":
            flash(
                f'This those not match any Bookmarks! please return to home page change your search text and try again', 'danger')

        return render_template('search_results.html', results=results, title="Search result", bookmarks=bookmarks)


# user search page only the bookmarks unique to each user will ne returned on this page

@app.route('/user_search_results', methods=['POST', 'GET'])
def user_search_results():
    if request.method == "POST":
        query = request.form.get('user_search_bar')
        results = bookmarks_collection.find({'$text': {'$search': query}})
        if query == "":
            flash(
                f'This those not match any Bookmarks! please return tomy bookmarks change your search text and try again', 'danger')
        return render_template('user_search_results.html', results=results, title="User Search result")

# user section
@app.route('/users')
# if a user has not yet added a bookmark the newuser page will be render
# and if the user has bookmarks already added the user page will render
def users():
    username = session.get('username')
    users = users_collection.find()
    categories = categories_collection.find()
    p_limit = int(request.args.get('limit', 6))
    p_offset = int(request.args.get('offset', 0))
    num_results = bookmarks_collection.count(
        {'username': username})
    bookmarks = bookmarks_collection.find({'username': username}).sort(
        "_id", -1).limit(p_limit).skip(p_offset)
    book_name = bookmarks_collection.find_one(
        {'username': username})
    args = {
        "p_limit": p_limit,
        "p_offset": p_offset,
        "book_name": book_name,
        "num_results": num_results,
        "next_url": f"/users?limit={str(p_limit)}&offset={str(p_offset + p_limit)}",
        "prev_url": f"/users?limit={str(p_limit)}&offset={str(p_offset - p_limit)}",

    }
    if book_name is None:
        return render_template('newuser.html')

    return render_template('users.html', users=users, bookmarks=bookmarks, categories=categories, args=args, title=username)

    # bookmarks section ---------------------------------------------------------------------


@app.route('/add_bookmark')
def add_bookmark():
    categories = categories_collection.find()
    return render_template('add_bookmark.html', categories=categories, title="Add bookmark")


@app.route('/insert_bookmark',  methods=["GET", "POST"])
def insert_bookmark():
    date = datetime.utcnow()
    format_date = date.strftime("%a %B %d")
    bookmarks_collection.insert_one({
        "last_modified":  format_date,
        'username': session['username'],
        'category_name': request.form.get('category_name'),
        'add_bookmark_url': request.form.get('add_bookmark_url'),
        'bookmark_description': request.form.get('bookmark_description'),
        'upvotes': int(0)
    })
    flash(f'You have added a new bookmark!', 'success')
    return redirect(url_for('users'))


@app.route("/edit_bookmark/<book_id>")
def edit_bookmark(book_id):
    user = users_collection.find()
    all_categories = categories_collection.find()
    the_bookmark = bookmarks_collection.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_bookmark.html", book=the_bookmark, categories=all_categories, user=user, title="edit bookmark")


@app.route('/update_bookmark/<book_id>', methods=["POST"])
def update_bookmark(book_id):
    date = datetime.utcnow()
    format_date = date.strftime("%a %B %d")
    bookmarks_collection.update({'_id': ObjectId(book_id)},
                                {
        "last_modified": format_date,
        'username': session['username'],
        'category_name': request.form.get('category_name'),
        'add_bookmark_url': request.form.get('add_bookmark_url'),
        'bookmark_description': request.form.get('bookmark_description')

    })
    return redirect(url_for('users'))


@app.route('/delete_bookmark/<book_id>', methods=["POST", "GET"])
def delete_bookmark(book_id):
    all_categories = categories_collection.find()
    the_bookmark = bookmarks_collection.find_one({"_id": ObjectId(book_id)})
    return render_template('delete_bookmark.html', book=the_bookmark,  categories=all_categories, title="edit bookmark")


@app.route('/remove_bookmark/<book_id>', methods=["POST", "GET"])
def remove_bookmark(book_id):
    flash(f'Your bookmark has been removed!', 'success')
    bookmarks_collection.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('users'))

# up voting route
@app.route('/upvote/<book_id>')
def upvote(book_id):
    bookmarks_collection.find_one_and_update(
        {'_id': ObjectId(book_id)},
        {'$inc': {'upvotes': 1}}
    )
    return redirect(url_for('index', book_id=book_id))
# end bookmarks section ------------------------------------------------------------------

#  categories section -----------------------------------------------------------------------
@app.route('/user_categories')
def user_categories():
    # if a user has not yet added a category the newuser_cat  page will be rendered
    # and if the user has categories already added the categories page will render
    categories = categories_collection.find().sort("_id", -1)
    bookmarks = bookmarks_collection.find()
    user = users_collection.find()
    cat_name = categories_collection.find_one(
        {'username': session.get('username')})
    if cat_name is None:
        return render_template('newuser_cat.html')
    return render_template('categories.html', categories=categories, bookmarks=bookmarks, user=user, title="Categories")


@app.route('/add_category')
def add_category():
    return render_template('add_category.html', title="Add category")


@app.route('/insert_category', methods=["POST"])
def insert_category():
    flash(f'Your category has been added! It will be now be available in the add bookmarks section In the dropdown menu', 'success')
    categories_collection.insert_one({
        'username': session['username'],
        'category_name': request.form.get('category_name')


    })
    return redirect(url_for('user_categories'))


@app.route('/edit_category/<cat_id>')
def edit_category(cat_id):
    category = categories_collection.find_one(
        {'_id': ObjectId(cat_id)})
    return render_template('edit_category.html', cat=category, title="Edit category"
                           )


@app.route('/update_category/<cat_id>', methods=['POST'])
def update_category(cat_id):
    categories_collection.update(
        {'_id': ObjectId(cat_id)},
        {'category_name': request.form.get('category_name'),
         'username': session['username']
         })
    return redirect(url_for('user_categories'))


@app.route('/delete_category/<cat_id>', methods=["POST", "GET"])
def delete_category(cat_id):
    category = categories_collection.find_one({"_id": ObjectId(cat_id)})
    return render_template('delete_category.html', cat=category, title="Delete category")


@app.route('/remove_category/<cat_id>', methods=["POST", "GET"])
def remove_category(cat_id):
    flash(f'Your category has been deleted!', 'success')
    categories_collection.remove({'_id': ObjectId(cat_id)})
    return redirect(url_for('user_categories'))


#  end categories section ---------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
