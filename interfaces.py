# ┌────────────────────────
# │       INTERFACES
# └────────────────────────


# Function to create the champ data
def buildChamp(name, image, games, winrate, kda, kills, deaths, assists, cs, csmedian):
	return {
		'name': name,
		'image': image,
		'games': games,
		'winrate': winrate,
		'kda': kda,
		'kills': kills,
		'deaths': deaths,
		'assists': assists,
		'cs': cs,
		'csmedian': csmedian,
	}


# Function to create the player data
def buildPlayer(name, alias, image, rank, champs):
	return {
		'name': name,
		'alias': alias,
		'image': image,
		'rank': rank,
		'champs': champs,
	}
