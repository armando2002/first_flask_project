# file runs on initiation, generates Flask app function for main.py

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cats'

    from .views import views
    from .auth import auth

    # register the blueprints to the homepage
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

