import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost/blogposts'
db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

from flaskblog import routes