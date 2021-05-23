from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setttings import SECRET_KEY, CONNECTION_STRING
from app import DB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
app.config['SECRET_KEY'] = SECRET_KEY
# DB.init_app(app)
db = SQLAlchemy(app)
# db.create_all()

from app import controller


app.register_blueprint(controller.index)
app.register_blueprint(controller.team, url_prefix='/setup/teams')
