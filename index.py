from flask import Flask, render_template, request
from lib.getData import getData
import json

app = Flask(__name__)


@app.route("/")
def home():
    try:
        # ?players=Bruno
        players = request.args.get('players')
        players = players.split(',')
    except AttributeError:
        players = []
    gamers = getData(players)
    # return render_template('home.html', data=gamers)
    return gamers