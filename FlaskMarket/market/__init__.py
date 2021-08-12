from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#URI = Unifrom Resource Identifier

app.config['SECRET_KEY'] = 'f254277eeb141537535b12bc'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from market import routes




# @app.route('/about/<username>')
# def about_page(username):
#   return f'<h1>This is the about page of {username}</h1>'