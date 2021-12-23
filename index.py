from flask import Flask, request
from getData import getData

app = Flask(__name__)


@app.route("/")
def home():
	players = []
	try:
		#?players=Bruno
		players = request.args.get('players')
		if len(players) < 3:
			players = []
		elif players[-1] == ',':
			players = players[:-1]
		players = players.split(',')
	except (AttributeError , IndexError , TypeError):
		players = []
	gamers = getData(players)
	return gamers