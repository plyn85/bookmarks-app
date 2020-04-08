# Imports
import os
import math
from flask import Flask, render_template, redirect, request, url_for, session, flash, abort, json
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
# setting global date variable
date = datetime.utcnow()
# ---------------- #
# APP ROUTES  #
# ---------------- #

# ----- index, index page search,  login, register, and log out routes ----- #


@app.route('/index')
@app.route('/')
def index():
    """ Pagintion with thanks to Miroslav Svec, DCD Channel lead.
        altered from https://github.com/MiroslavSvec/DCD_lead/tree/pagination
        paginated results to be displayed on index page  by upvotes and Id"""
    #  getting categorys collection from database
    categories = categories_collection.find()
    #  setting args varibales
    num_results = bookmarks_collection.count()
    users = users_collection.find()
    p_limit = int(request.args.get('limit', 6))
    p_offset = int(request.args.get('offset', 0))
    # getting bookmarks collection orderding by votes and adding pagination
    bookmarks = bookmarks_collection.find().sort(
        "upvotes", -1).limit(p_limit).skip(p_offset)
    # args added here to be used on pagintion page
    args = {
        "p_limit": p_limit,
        "p_offset": p_offset,
        "num_results": num_results,
        "next_url": f"/index?limit={str(p_limit)}&offset={str(p_offset + p_limit)}",
        "prev_url": f"/index?limit={str(p_limit)}&offset={str(p_offset - p_limit)}",

    }

    return render_template('index.html', categories=categories,
                           bookmarks=bookmarks, users=users, args=args)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """ First we find the logged in user in the data base
    If it the user exists In the database we compare the
    encncipted password from the form and the database
    password with the database password. The username is added to the session
    and from a tutorial found at www.youtube.com/watchv=vVx1737auSE """

    if request.method == 'POST':
        # getting username and password from register form
        username = request.form['username']
        password = request.form['password']
        # finding user in the database
        login_user = users_collection.find_one(
            {'name': username})
        # If the user exists
        if login_user:
            #  if the password from the form and database match
            if bcrypt.hashpw(password.encode('utf-8'), login_user['password']) == login_user['password']:
                # If the session username and form username match
                session['username'] = username
                # If any user is logged in
                session['logged_in'] = True
                # alert flashed on user is redirect to the home page
                flash(f'You are logged in!', 'success')
                return redirect(url_for('index'))
                # If login Is unsuccesful warning flashed an user stays on login page
        if not login_user:
            flash(
                f'Login  Unsuccessful. Please check username!', 'danger')
        else:
            flash(
                f'Login  Unsuccessful. Please check password!', 'danger')

    return render_template('login.html', title="Login")


@app.route('/register', methods=['POST', 'GET'])
def register():
    """First we find the existing user in user in the data base
    If it the user does not exist In the database we insert the user to the
    database along with there encripted password. If the session username
    Is the same as the username enetered to the form the user is redirect to the
    login page taken an altered from a tutorial found at https://www.youtube.com/watch?v=vVx1737auSE"""

    if request.method == 'POST':
        # getting username,password an comfrim-password from register form
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # getting existing user from the database
        existing_user = users_collection.find_one(
            {'name': username})
        # If the users name is not In database and passwords match
        if existing_user is None and password == confirm_password:
            # getting users password from register form an encrypting It
            hashpass = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())
            # Inserting the data to the users collection In the database
            users_collection.insert(
                {'name': username, 'password': hashpass})
            session['username'] = username
            flash(f'You are now regsitered please login!', 'success')
            return redirect(url_for('login'))
        # If username already exists and passwords do not match
        if existing_user and password != confirm_password:
            flash(
                f'Username Is In use and and passwords do not match!', 'danger')
        # If username is not in use an passwords do not match
        if existing_user is None and password != confirm_password:
            flash(
                f'Your passwords do not match!', 'danger')
        # If username Is In use but passwords match
        elif existing_user:
            flash(
                f'Username In use! Please try another username', 'danger')

    return render_template('register.html', title="Regsiter")


@app.route('/logout')
def logout():
    session.clear()
    flash(f'You are now  logged out!', 'danger')
    return redirect(url_for('index'))

# -----  end of index, login, register, and log out routes ----- #

# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #

# ----- CREATE ----- #


@app.route('/add_bookmark')
def add_bookmark():
    """ add bookmark page render when add category link In navbar clicked"""
    # find categories collection In database
    categories = categories_collection.find()
    return render_template('add_bookmark.html',
                           categories=categories, title="Add bookmark")


@app.route('/insert_bookmark',  methods=["GET", "POST"])
def insert_bookmark():
    """ route activated when add bookmark submit button post request recived
    from form in add bookmark page user then redirected to users page"""
    # date formated by day, month, date
    format_date = date.strftime("%a %B %d")
    if request.method == "POST":
        # inserting data to bookmarks collection In the database
        bookmarks_collection.insert_one({
            "last_modified":  format_date,
            'username': session['username'],
            'category_name': request.form.get('category_name'),
            'add_bookmark_url': request.form.get('add_bookmark_url'),
            'bookmark_description': request.form.get('bookmark_description'),
            'upvotes': int(0)
        })
    # user alert If succesfully added bookmark
    flash(f'You have added a new bookmark!', 'success')
    return redirect(url_for('users'))


@app.route('/add_category')
def add_category():
    """ add category page render when add category link In navbar clicked"""
    return render_template('add_category.html', title="Add category")


@app.route('/insert_category', methods=["POST", "GET"])
def insert_category():
    """ route activated when add category submit button post request recived
    from form in add category page user then redirected to user categories page"""

    # date formated by day, month, date
    format_date = date.strftime("%a %B %d")
    if request.method == "POST":
        # inserting data to categories collection In the database
        categories_collection.insert_one({
            'username': session['username'],
            'category_name': request.form.get('category_name'),
            "last_modified":  format_date,


        })
    # user alert If succesfully added category
    flash(f'Your category has been added! ', 'success')
    return redirect(url_for('user_categories'))


# ----- Update ----- #


@app.route("/edit_bookmark/<book_id>")
def edit_bookmark(book_id):
    """Route activated when edit bookmark button is clicked in user bookmarks page.
        Gets the bookmarks collection  object Id from the database an displays the category In a form on the edit category page """
    # finding the categories collection from the data base
    all_categories = categories_collection.find()
    #  finding the bookmarks collection object Id in the database
    the_bookmark = bookmarks_collection.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_bookmark.html", book=the_bookmark, categories=all_categories, title="edit bookmark")


@app.route('/update_bookmark/<book_id>', methods=["POST"])
def update_bookmark(book_id):
    """Route updates bookmarks collection for the user in the database 
    after the Edit bookmark form Is submited user Is then redirect back to 
    user bookmarks page"""
    # date formated by day, month, date
    format_date = date.strftime("%a %B %d")
    if request.method == "POST":
        # updating the bookmarks collection
        bookmarks_collection.update({'_id': ObjectId(book_id)},
                                    {
            "last_modified": format_date,
            'username': session['username'],
            'category_name': request.form.get('category_name'),
            'add_bookmark_url': request.form.get('add_bookmark_url'),
            'bookmark_description': request.form.get('bookmark_description')

        })
        # alerting user after bookmark has been edited
        flash(f'Your bookmark  has been edited!', 'success')
    return redirect(url_for('users'))


@app.route('/edit_category/<cat_id>')
def edit_category(cat_id):
    """Route activated when edit button is clicked in user categories page.
        Gets the categories collection object Id from database an displays the category In a form on the edit category page """
    # finding the categories collection object Id
    category = categories_collection.find_one(
        {'_id': ObjectId(cat_id)})
    return render_template('edit_category.html', cat=category, title="Edit category"
                           )


@app.route('/update_category/<cat_id>', methods=['POST'])
def update_category(cat_id):
    """Route updates category collection for the user in the database 
    after the Edit category form Is submited user Is then redirect back to 
    user categories page"""
    # updating category_name an the categories username in the database
    if request.method == "POST":
        categories_collection.update(
            {'_id': ObjectId(cat_id)},
            {'category_name': request.form.get('category_name'),
             'username': session['username']
             })
    # alerting user after bookmark has been edited
    flash(f'Your bookmark  has been edited!', 'success')
    return redirect(url_for('user_categories'))


@app.route('/upvote/<book_id>', methods=["GET", "POST"])
def upvote(book_id):
    """ Upvote route add likes to bookmarks on index and search pages"""
    # finds upvotes In bookmarks collection and adds one when button is clicked
    if request.method == "POST":

        bookmarks_collection.find_one_and_update(
            {'_id': ObjectId(book_id)},
            {'$inc': {'upvotes': 1}}
        )

    return redirect(url_for('index',  book_id=book_id))


# ----- Delete ----- #

@app.route('/delete_bookmark/<book_id>', methods=["POST", "GET"])
def delete_bookmark(book_id):
    """ route acitvated when delete bookmark button is clicked entire 
    bookmark is sent to delete bookmark form to confirm the bookmark delete  """
    # getting categories an bookmarks Id from data base
    all_categories = categories_collection.find()
    the_bookmark = bookmarks_collection.find(
        {"_id": ObjectId(book_id)})
    return render_template('delete_bookmark.html', book=the_bookmark,  categories=all_categories, title=" delete bookmark")


@app.route('/remove_bookmark/<book_id>', methods=["POST", "GET"])
def remove_bookmark(book_id):
    """ Route confirms delete an redirect user to there user bookmarks page  """
    if request.method == "POST":
        bookmarks_collection.remove({'_id': ObjectId(book_id)})
        flash(f'Your bookmark has been removed!', 'success')
    return redirect(url_for('users'))


@app.route('/delete_category/<cat_id>', methods=["POST", "GET"])
def delete_category(cat_id):
    """ route acitvated when delete category  button is clicked entire bookmark is sent to
    delete bookmark from to confirm the categoy
    delete """
    # getting  category id from the data base
    category = categories_collection.find_one({"_id": ObjectId(cat_id)})
    return render_template('delete_category.html', cat=category, title="Delete category")


@app.route('/remove_category/<cat_id>', methods=["POST", "GET"])
def remove_category(cat_id):
    """ Route confirms delete an redirect user to there user categorys page  """
    if request.method == "POST":
        categories_collection.remove({'_id': ObjectId(cat_id)})
        flash(f'Your category has been deleted!', 'success')
    return redirect(url_for('user_categories'))


# ----- Read ----- #


@app.route('/users')
def users():
    """ Here thu users search results are paginated and displayed on the users page
          only there unique results will be shown. if a user has not yet added a bookmark the newuser page will be render and if the user has bookmarks already added the user page will render """
    # getting the session username
    username = session.get('username')
    # getting  users and  categories collections from database
    users = users_collection.find()
    categories = categories_collection.find()
    # setting args variables page limit and offset here
    p_limit = int(request.args.get('limit', 6))
    p_offset = int(request.args.get('offset', 0))
    # getting the number of bookmarks for each user
    num_results = bookmarks_collection.count(
        {'username': username})
    # getting bookmarks by username and reversing order
    bookmarks = bookmarks_collection.find({'username': username}).sort(
        "_id", -1).limit(p_limit).skip(p_offset)
    args = {
        "p_limit": p_limit,
        "p_offset": p_offset,
        "num_results": num_results,
        "next_url": f"/users?limit={str(p_limit)}&offset={str(p_offset + p_limit)}",
        "prev_url": f"/users?limit={str(p_limit)}&offset={str(p_offset - p_limit)}",

    }
    # getting username for each bookmark
    book_name = bookmarks_collection.find_one(
        {'username': username})
    # if user has no bookmarks new user page rendered
    if book_name is None:
        return render_template('newuser.html')
    # if the user has bookmarks added users page rendered
    return render_template('users.html', users=users, bookmarks=bookmarks, categories=categories, args=args, title=username)


@app.route('/user_search_results', methods=['POST', 'GET'])
def user_search_results():
    """ Query from the search bar on the users page taken here an matched 
    with the results of the text search qurey from the data base if the qurey 
    is empty user is redirected back to users page"""

    if request.method == "POST":
        # get search bar post
        query = request.form.get('user_search_bar')
        # text search on the bookmarks collection
        results = bookmarks_collection.find({'$text': {'$search': query}})
        return render_template('user_search_results.html', results=results, title="User Search result")


@app.route('/search_results', methods=['POST', 'GET'])
def search_results():
    """ Query from the search bar on the index  page taken here an matched 
    with the results of the text search qurey from the data base if the qurey is empty user is redirected back to index page"""
    if request.method == "POST":
        # get search bar post
        query = request.form.get('search_bar')
        # text search on the bookmarks collection
        results = bookmarks_collection.find({'$text': {'$search': query}})
        return render_template('search_results.html', results=results, title="User Search result")


@app.route('/user_categories')
def user_categories():
    """ if a user has not yet added a category the newuser_cat  page will be rendered
         and if the user has categories already added the categories page will render """
    # getting  categories collection and reversing order
    categories = categories_collection.find().sort("_id", -1)
    # finding all categories for the user
    cat_name = categories_collection.find_one(
        {'username': session.get('username')})
    # if the user has no categories
    if cat_name is None:
        return render_template('newuser_cat.html')
    return render_template('categories.html',
                           categories=categories, title="Categories")

# ----- Error handlers ----- #


@app.errorhandler(404)
def not_found(e):
    """ displays custom 404 html page """
    return render_template("404.html", title="Page not found")


@app.errorhandler(500)
def response_500(e):
    """ displays custom 500 html page """
    return render_template("500.html", title="Server error")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
