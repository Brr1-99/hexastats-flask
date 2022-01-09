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

# Function to create the masteries data

def buildmastery(
	name: str,
	image: str,
	level: int,
	points: int
	):
	return {
		'name': name,
		'image': image,
		'level': level,
		'points': points,
	}

# Function to create the player data
def buildPlayer(
	# name: str,
	alias: str,
	image: str,
	level: int,
	rank_n: int,
	rank_p: int,
	rank_s: str,
	image_s : str,
	lp_s : int,
	win_s: int,
	lose_s: int,
	winrate_s: int,
	rank_f: str,
	image_f : str,
	lp_f : int,
	win_f: int,
	lose_f: int,
	winrate_f: int,
	champs: dict,
	masteries: dict
	):
	return {
		# 'name': name,
		'alias': alias,
		'image': image,
		'level': level,
		'rank':{
			'rank_n': rank_n,
			'rank_p': rank_p,
			'solo':{
				'rank': rank_s,
				'image': image_s,
				'lp': lp_s,
				'win': win_s,
				'lose': lose_s,
				'winrate': winrate_s,
			},
			'flex':{
				'rank': rank_f,
				'image': image_f,
				'lp': lp_f,
				'win': win_f,
				'lose': lose_f,
				'winrate': winrate_f
			}

		},
		
		'champs': champs,
		'masteries':masteries,
	}
