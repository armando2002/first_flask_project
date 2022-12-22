# file used to setup homepage view

from flask import Blueprint, render_template
# set up a blueprint for flask app
views = Blueprint('views', __name__)


# define homepage route
@views.route('/')
# show Test text when route accessed, render home.html
def home():
    return render_template("home.html")


