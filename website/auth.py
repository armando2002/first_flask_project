# file used to setup authentication routes

from flask import Blueprint, render_template, request, flash
# set up an auth blueprint for flask app
auth = Blueprint('auth', __name__)


# define login and accept get/post requests
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=False)


# define logout
@auth.route('/logout')
def logout():
    return "<p>logout</p>"


# define signup and accept get/post requests
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # use flash to show messages
        if len(email) < 4:
            flash('Email must be longer than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be longer than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            flash('Account created.', category='success')


    return render_template("signup.html")
