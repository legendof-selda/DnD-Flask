from flask import Flask, render_template, request, url_for, redirect, Markup, flash
from flask_sqlalchemy import SQLAlchemy
from setttings import SECRET_KEY, CONNECTION_STRING
from app import db
from app import model
from app import controller


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)

app.register_blueprint(controller.index)
app.register_blueprint(controller.team, url_prefix='/setup/teams')
