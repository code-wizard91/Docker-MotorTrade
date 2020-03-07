from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SECRET_KEY'] = 'fee323f72238c94ce34302364eb0b21a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ali:password@localhost/flaskapp'

db = SQLAlchemy(app)

from application import routes
