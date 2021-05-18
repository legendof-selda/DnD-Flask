from flask import Flask, render_template, request, url_for, redirect, Markup

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setup')
def setup():
    return render_template('setup.html')


@app.route('/setup/teams', methods=['GET', 'POST'])
def setup_teams():
    return render_template('teams.html')