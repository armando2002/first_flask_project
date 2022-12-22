# file used to setup authentication routes

from flask import Blueprint
# set up an auth blueprint for flask app
auth = Blueprint('auth', __name__)


# define login
@auth.route('/login')
def login():
    return "<p>Login</>"


# define logout
@auth.route('/logout')
def logout():
    return "<p>logout</p>"


# define signup
@auth.route('/signup')
def signup():
    return "<p>signup</p>"
