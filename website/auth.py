# file used to setup authentication routes

from flask import Blueprint, render_template
# set up an auth blueprint for flask app
auth = Blueprint('auth', __name__)


# define login
@auth.route('/login')
def login():
    return render_template("login.html", boolean=False)


# define logout
@auth.route('/logout')
def logout():
    return "<p>logout</p>"


# define signup
@auth.route('/signup')
def signup():
    return render_template("signup.html")
