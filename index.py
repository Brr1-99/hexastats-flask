from flask import Flask, request
from getData import getData

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
    return gamers