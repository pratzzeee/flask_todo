from re import template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder = 'template')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


from flasktodo import routes