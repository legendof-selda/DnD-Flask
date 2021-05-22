from flask import Blueprint, render_template


home = Blueprint('home', __name__)


@home.get('/')
def index():
    return render_template('index.html')


@home.get('/setup')
def setup():
    return render_template('setup/setup.html')
