from flask import Flask, request
from getData import getData

app = Flask(__name__)


@app.route("/")
def home():
	try:
		# singleMode: ?players=Bruno
		# multiMode: ?players=Bruno,Alex
		players = request.args.get('players')
		
		# Probably not correct data
		if len(players) < 3:
			players = []
		# Remove end comma if exists
		elif players[-1] == ',':
			players = players[:-1]

		# Now everything is ok, split the players
		players = players.split(',')

		# There is 1 or multiple players?
		singleMode = len(players == 1)

		# Everything went ok: process the data
		gamers = getData(players, singleMode)
		return gamers

	except (AttributeError , IndexError , TypeError):
		return []