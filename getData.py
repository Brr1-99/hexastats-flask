import requests
import json
from bs4 import BeautifulSoup
from interfaces import buildChamp, buildPlayer
from whitelist import realName
	

# Headers to avoid bot protection
headers = requests.utils.default_headers()
headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# Function to factor the extraction of multiple kills data
def get_multiple_kills(doc,x):
	try:
		result = int(doc[x+4].string.split('\t')[13][:-1])
	except:
		result = 0
	return result

# Function to extract the data from the page to the dictionary
def getData(players_get, singleMode):
	base_url = {
		'home': "https://euw.op.gg/summoner/userName=",
		'champions': "https://euw.op.gg/summoner/champions/userName="
	}
	# Data returned
	data = []

	# Players
	for player in players_get:
		
		# TODO try catch por si te pasan un jugador que no existe

		# Fetch OPGG data for a player
		opgg = base_url['home'] + player
		result = requests.get(opgg, headers=headers).text
		document = BeautifulSoup(result, 'html.parser')

		champions = base_url['champions'] + player
		result2 = requests.get(champions, headers=headers).text
		document2 = BeautifulSoup(result2, 'html.parser')

		# Fetch player data
		name = realName(player)
		alias = player
		image = 'https:' + document.find(class_='ProfileImage')['src']

		try:
			global_ranking = int(document.find(class_='ranking').string.replace(',',''))
			percent_better_players = float(document.find(class_='LadderRank').findChild('a').text.split('\t')[6].split('(')[1].split('%')[0])
		except AttributeError:
			global_ranking = -1
			percent_better_players = -1

		rank = document.find(class_='TierRank').string

		# Exception for unranked players
		if len(rank) >= 15:
			rank = 'Unranked'
		
		champs_more_data = document2.find_all(class_='Row TopRanker')
	
		champs = []
		

		# Fetch champions data
		champs_data = document.find_all(class_='ChampionBox Ranked')
		for index,champ_data in enumerate(champs_data):
			name_champ = champ_data.find(class_='Face')['title']
			image_champ = 'https:' + str(champ_data.find('img')['src'])
			games = int(champ_data.find(class_='Played').findChildren('div')[-1].string.split(' ')[0])
			winrate = int(champ_data.find(class_='Played').findChildren('div')[0].string.split('\t')[5][:-2])
			kda = float(champ_data.find(class_='PersonalKDA').findChildren('span')[0].string.split(':')[0])
			kills = float(champ_data.find(class_='KDAEach').findChildren('span')[0].string)
			deaths = float(champ_data.find(class_='KDAEach').findChildren('span')[2].string)
			assists = float(champ_data.find(class_='KDAEach').findChildren('span')[4].string)
			cs = float(champ_data.find(class_='ChampionInfo').findChildren('div')[-1].string.split(' ')[1])
			csmedian = float(champ_data.find(class_='ChampionInfo').findChildren('div')[-1].string.split('\t')[9].split('(')[1].split(')')[0])

			cells = champs_more_data[index].find_all(class_='Value Cell')
			
			gold = int(cells[0].string.split('\t')[5][:-1].replace(',',''))
			max_kills = int(cells[2].string.split('\t')[6][:-1])
			max_deaths = int(cells[3].string.split('\t')[6][:-1])
			avg_damage_dealt = int(cells[4].string.split('\t')[6][:-1].replace(',',''))
			avg_damage_taken = int(cells[5].string.split('\t')[6][:-1].replace(',',''))

			
			double_kills = get_multiple_kills(cells, 2)
			triple_kills = get_multiple_kills(cells, 3)
			quadra_kills = get_multiple_kills(cells, 4)
			penta_kills = get_multiple_kills(cells, 5)

			champs.append(buildChamp(name=name_champ, image=image_champ, games=games, winrate=winrate,
			kda=kda, kills=kills, deaths=deaths, assists=assists, cs=cs, csmedian=csmedian, gold=gold,
			max_kills=max_kills, max_deaths=max_deaths, avg_damage_dealt=avg_damage_dealt, avg_damage_taken=avg_damage_taken,
			double_kills=double_kills, triple_kills=triple_kills, quadra_kills=quadra_kills, penta_kills=penta_kills))

		# Append data to data object
		data.append(buildPlayer(name=name, alias=alias, image=image, rank_n=global_ranking, rank_p=percent_better_players, rank=rank, champs=champs))
	
	if singleMode:
		return json.dumps(data)
	else:
		return json.dumps(data[0])
