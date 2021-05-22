from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, HiddenField


team = Blueprint('team', __name__)


class NewTeam(FlaskForm):
    id_field = HiddenField()
    name = StringField('Team Name')
    submit = SubmitField('Join')


@team.get('/')
def index():
    return render_template('setup/teams.html')
