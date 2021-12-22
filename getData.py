import requests
import json
from bs4 import BeautifulSoup
from interfaces import buildChamp, buildPlayer
from whitelist import players_whitelist
	

# Headers to avoid bot protection
headers = requests.utils.default_headers()
headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


# Function to extract the data from the page to the dictionary
def getData(players_get):

	# Data returned
	data = []

	# Players
	for player in players_whitelist:
		
		if player['name'] in players_get:
			
			# Fetch OPGG data for a player
			opgg = "https://euw.op.gg/summoner/userName=" + player['alias']
			result = requests.get(opgg, headers=headers).text
			document = BeautifulSoup(result, 'html.parser')

			# Fetch player data
			name = player['name']
			alias = player['alias']
			image = 'https:' + document.find(class_='ProfileImage')['src']
			rank = document.find(class_='TierRank').string

			# Exception for unranked players
			if len(rank) >= 15:
				rank = 'Unranked'

			champs = []
		
			# Fetch champions data
			champs_data = document.find_all(class_='ChampionBox Ranked')
			for champ_data in champs_data:
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
				champs.append(buildChamp(name=name_champ, image=image_champ, games=games, winrate=winrate, kda=kda, kills=kills, deaths=deaths, assists=assists, cs=cs, csmedian=csmedian))

			# Append data to data object
			data.append(buildPlayer(name=name, alias=alias, image=image, rank=rank, champs=champs))
		
	return json.dumps(data)
