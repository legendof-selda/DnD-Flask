from flask import Blueprint, render_template, flash, request
from flask_wtf import Form
from wtforms import SubmitField, StringField, HiddenField, validators
from app import db
from app.model import Team


api = Blueprint('team', __name__)


class NewTeam(Form):
    id_field = HiddenField()
    name = StringField('Team Name', validators=[validators.InputRequired()], id='name')
    submit = SubmitField('Join')


@api.get('/')
def index():
    return render_template('setup/teams.html')


@api.route('/add_team', methods=['GET', 'POST'])
def add_team():
    form = NewTeam(request.form)
    if form.validate_on_submit():
        record = Team.Team(request.form['name'])
        db.session.add(record)
        db.session.commit()
        return render_template('setup/teams.html', message=f"Team {request.form['name']} added!")
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ), 'error')
        return render_template('setup/teams.html', form=form)
