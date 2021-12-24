from flask import Flask, request
from getData import getData
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
	try:
		# singleMode: ?players=Bruno&server=euw
		# multiMode: ?players=Bruno,Alex&server=euw
		players = request.args.get('players')
		server = request.args.get('server')

		# Probably not correct data
		if len(players) < 3:
			players = []
		# Remove end comma if exists
		elif players[-1] == ',':
			players = players[:-1]

		# Now everything is ok, split the players
		players = players.split(',')

		# There is 1 or multiple players?
		singleMode = len(players) == 1
	except (AttributeError , IndexError , TypeError):
		return json.dumps([])
	# Everything went ok: process the data
	gamers = getData(players, server, singleMode)
	return gamers
