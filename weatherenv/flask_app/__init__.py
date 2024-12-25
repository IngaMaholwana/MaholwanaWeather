from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_weatherapp():
    """
    Creates and configures a basic Flask web application for a weather service.

    This function sets up a Flask application with a single route ('/') that returns
    a simple message indicating that it's a weather service.

    Returns:
    Flask: A Flask application instance configured with a single route.

    Example:
    >>> app = create_weatherapp()
    >>> client = app.test_client()
    >>> response = client.get('/')
    >>> response.data.decode('utf-8')
    'This is a weather service!'
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    return app

def create_database(app):
    """
    Creates a database if it doesn't already exist.

    Args:
    app (Flask): The Flask application instance.
    """
    if not path.exists('flask_app/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')