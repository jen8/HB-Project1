from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Post


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/users/%s" % user.user_id)


@app.route('/make_post', methods=['POST'])
def make_post():
    """Homepage that shows post box."""

    return render_template("homepage.html")

@app.route('/show_post', methods=['POST'])
def show_post():
    """Takes posts from website and adds them to crime database."""

    # take the user post
    post = request.form["post"]
    # add new post to database and commit
    new_post = Post(post=post)

    db.session.add(new_post)
    db.session.commit()

    flash("Post %s added." % post)
    return render_template("show_post.html", post=post)




# @app.route('/display_post')
# def display_post():
#     """Display Post."""

#     # Query post from crime database
#     post = Post.query.all()
#     return render_template("display_post.html", post=post)

# currently displaying all posts with all the junk symbols next to it
# might want to use a for loop to print out posts 

if __name__ == "__main__":
    # app.run(debug=True)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

    