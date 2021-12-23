# ┌────────────────────────
# │       INTERFACES
# └────────────────────────


# Function to create the champ data
def buildChamp(
	name: str, 
	image: str,
	games: int,
	winrate: int,
	kda: int,
	kills: int,
	deaths: int,
	assists: int,
	cs: int,
	csmin: int,
	gold: int,
	max_kills: int, 
	max_deaths: int,
	avg_damage_dealt: int,
	avg_damage_taken: int,
	double_kills: int,
	triple_kills: int,
	quadra_kills: int,
	penta_kills: int
	):
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
		'csmin': csmin,
		'gold': gold,
		'max_kills': max_kills,
		'max_deaths': max_deaths,
		'avg_damage_dealt': avg_damage_dealt,
		'avg_damage_taken' : avg_damage_taken,
		'double_kills' :double_kills,
		'triple_kills' : triple_kills,
		'quadra_kills' : quadra_kills,
		'penta_kills' : penta_kills
	}


# Function to create the player data
def buildPlayer(
	name: str,
	alias: str,
	image: str,
	level: int,
	image_rank: str,
	rank_n: int,
	rank_p: int,
	rank: str,
	champs: dict
	):
	return {
		'name': name,
		'alias': alias,
		'image': image,
		'level': level,
		'image_rank': image_rank,
		'rank_n': rank_n,
		'rank_p': rank_p,
		'rank': rank,
		'champs': champs,
	}
