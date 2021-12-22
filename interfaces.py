# ┌────────────────────────
# │       INTERFACES
# └────────────────────────


# Function to create the champ data
def buildChamp(name, image, games, winrate, kda, kills, deaths, assists, cs, csmedian, gold, max_kills, max_deaths, avg_damage_dealt, avg_damage_taken):
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
		'gold': gold,
		'max_kills': max_kills,
		'max_deaths': max_deaths,
		'avg_damage_dealt': avg_damage_dealt,
		'avg_damage_taken' : avg_damage_taken
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
