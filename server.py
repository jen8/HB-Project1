import os

import random
from jinja2 import StrictUndefined

from flask import Flask, send_from_directory, Request, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename
import datetime

# UPLOAD_FOLDER = '/path/to/the/uploads'

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


from model import connect_to_db, db, Post, User


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True




@app.route('/', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/log_in', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No such user")
        return redirect("/")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/")

    session["user_id"] = user.user_id

    flash("Logged in")
    # return redirect("/users/%s" % user.user_id)
    return redirect("make_post")
    # create route for this

#### FIX ME...log in allows non-users to post


@app.route('/registration_form', methods=['GET'])
def registration_form():
    """Show user registration form."""

    return render_template("registration_form.html")


@app.route('/process_registration', methods=['POST'])
def process_registration():
    """Takes user info from website and adds them to crime database."""

    # take the user info
    username = request.form["username"]
    password = request.form["password"]
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    zipcode = request.form["zipcode"]
    # take all of the user input and put all user info into database
    new_user = User(username=username, password=password, first_name=firstname, 
    last_name=lastname, zipcode=zipcode)

    db.session.add(new_user)

    # db.session.add(new_post)
    db.session.commit()


    ## IN ORDER FOR FLASH MSG TO APPEAR, ADD THE APPROPRIATE HTML FOR FLASH 
    flash("User %s added." % username)

    ### DECIDE WHICH PAGE TO SHOW AFTER USER IS SUCCESSFULLY ADDED?
    return render_template("make_post.html")

#### FINISH ME!



@app.route('/make_post')
def make_post():
    """Shows form to make text post or photo post."""
    # if "user_id" not in session:  #force user to be logged-in
    #     return redirect("/")

    # greet user when arriving to their post page
    # get the user id from session then, use id to get firstname of user
    user = User.query.filter_by(user_id=session["user_id"]).first()


    return render_template("make_post.html", first_name=user.first_name)


@app.route('/submit_post', methods=['POST'])
def show_post():
    """Takes posts from website and adds them to crime database."""
    filename = None
  
    # check if the post request has the file part
    if 'file' not in request.files:
        print "one"
        flash('No file part')
        ### TO DO : FIX flash and redirect, or else it doesnt get saved to db
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print "two"
    if file and allowed_file(file.filename):
        print "three"
        filename = secure_filename(file.filename)
        # add unique hash id for photos to avoid photo name collision
        # Split file into 3 parts: filename, ".", extenstion
        parts = filename.split(".")
        # access the extension part of the file
        extension = parts[len(parts)-1]
        # get a random, relatively unique hash id from 100000-999999
        hash_num = random.randrange(100000, 999999)
        # create new file name based on new hash id
        filename = str(hash_num) + "." + extension
        # save file to disk wih new filename, joining folder to filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    # take the user text post
    post = request.form["post"]
    # take the category of post user has selected on makepost.html page
    category = request.form["category"]

    # get current date
    right_now = datetime.datetime.utcnow()


    # get user id from session, then put it into new Post object
    # add new post to database and commit
    new_post = Post(post=post, photo_id=filename, category=category, date=right_now, user_id=session["user_id"])

    db.session.add(new_post)
    db.session.commit()

 
    # flash("Post %s added." % post)
    post = Post.query.all()
    return redirect("/display_post")

#### FIXME   /r+ symbol added to some posts in database


@app.route('/display_post', methods=['GET'])
def display_post():
    """Display Post from crime database to website."""
    # takes posts from database to website
    post = Post.query.all()

    # get the option user has selected from the sort menu on display_post.html
    sort_type = request.args.get("type")
    
    # get zipcode from zipcode form on display_post.html
    zipcode_area = request.form.get("zipcode")
    print "Sort Type" + str(sort_type)
    # if zipcode:
        # sorts by newest posts on top
    if sort_type == "Most Recent" or sort_type == None:
        sorted_posts = post[::-1]

     # sorts by oldest posts on top
    elif sort_type == "Least Recent":
        # REMEMBER TO CHANGE 8 since first 8 db entries do not have datetime
        # key=lambda post, create a new variable called post
        sorted_posts = sorted(post[8:], key=lambda post: post.date)

    # sorts by crime alerts
    elif sort_type == "Crime Alert":
        sorted_posts = Post.query.filter_by(category='crime').all()

    # sorts by community events
    elif sort_type == "Community Event":
        sorted_posts = Post.query.filter_by(category='community').all()

    # # if users chooses not to sort, just display all posts
    # else:
    #     sorted_posts = Post.query.all()


    # query date from database
    raw_date = db.session.query(Post.date).all()
    print raw_date

    # take current date into a better looking format (August 16, 2016)
    # strftime turns datetime object into string 
    neater_date = raw_date[10][0].strftime("%B %d, %Y")

    
    return render_template("display_post.html", post=sorted_posts, neater_date=neater_date)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # add unique hash id for photos to avoid photo name collision
            # Split file into 3 parts: filename, ".", extenstion
            parts = filename.split(".")
            # access the extension part of the file
            extension = parts[len(parts)-1]
            # get a random, relatively unique hash id from 100000-999999
            hash_num = random.randrange(100000, 999999)
            # create new file name based on new hash id
            filename = str(hash_num) + "." + extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
             # find me route for uploaded file function and get filename
            return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    "Show photo"
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/police_district', methods=['GET'])
def show_police_station():
    """Shows police station map"""

    return render_template("police_district.html")


# TO DO: CONNECT THIS ROUTE TO SERVE
@app.route('/safety_tips', methods=['GET'])
def show_safety_tips():
    """Shows personal safety tips"""

    return render_template("safety_tips.html")

@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


if __name__ == "__main__":
    # app.run(debug=True)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

    