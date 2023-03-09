import psycopg2
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('../settings.py')
app.secret_key = app.config['SECRET_KEY']

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def dbConnect():
    conn = psycopg2.connect(
        host=app.config['HOST_DB'],
        database=app.config['DATABASE_DB'],
        user=app.config['USER_DB'],
        password=app.config['PASSWORD_DB']
    )
    return conn

from flask_template.controllers.flaskController import *
from flask_template.controllers.login import *