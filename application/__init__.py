from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fee323f72238c94ce34302364eb0b21a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ali:password@localhost/flaskapp'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from application import routes
