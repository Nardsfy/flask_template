import psycopg2
from flask import Flask
from flask_login import LoginManager

# Create Flask app
app = Flask(__name__)
app.config.from_pyfile("settings.py")

# Initialize session login
login_manager = LoginManager()
login_manager.init_app(app)

# Handle session login redirect and message
login_manager.login_view                = "login"
login_manager.login_message             = "Please log in to access this page."
login_manager.login_message_category    = "danger"

def connectionDB():
    conn = psycopg2.connect(
        host        = app.config['HOST_DB'],
        database    = app.config['DATABASE_DB'],
        user        = app.config['USER_DB'],
        password    = app.config['PASSWORD_DB']
    )
    return conn

# Declare route controller application
from flask_template.controllers import (routes, validate, user)