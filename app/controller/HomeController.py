from flask import Blueprint, render_template


api = Blueprint('home', __name__)


@api.get('/')
def index():
    return render_template('index.html')


@api.get('/setup')
def setup():
    return render_template('setup/setup.html')
