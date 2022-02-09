import requests
from interfaces import buildChamp,buildPlayer
from loadMasteries import loadmastery
from bs4 import BeautifulSoup

# Function to factor the extraction of multiple kills data
def get_multiple_kills(doc,x):
	try:
		result = int(doc[x+5].text)
	except:
		result = 0
	return result

def loadData(ok_server, headers, player):
	data = []
	# Fetch OPGG data for a player
	opgg = "https://"+ ok_server + '.op.gg/summoner/userName=' + player
	result = requests.get(opgg, headers=headers).text
	document = BeautifulSoup(result, 'html.parser')


	champions = "https://"+ ok_server + ".op.gg/summoner/champions/userName=" + player
	result2 = requests.get(champions, headers=headers).text
	document2 = BeautifulSoup(result2, 'html.parser')

	# Fetch profile data
	# name = realName(player)
	alias = player

	image = document.find('div', class_='profile-icon').findChild('img')['src']
	level = int(document.find('div', class_='profile-icon').findChild('span').text)

	# Fetch recent games stats
	# record = document.find(class_='WinRatioTitle').findChildren('span')
	# matches = record[0].text
	# wins = record[1].text
	# loses = record[2].text


	# Fetch solo/duo data 
	image_s = document.find_all('div', class_='medal')[0].findChild('img')['src']
	try :
		rank_s = document.find_all('div', class_='tier-rank')[0].text
	except IndexError:
		rank_s = 'Unranked'

	if rank_s != 'Unranked':
		lp_s = int(document.find_all('div', class_='tier-info')[0].findChild('span').text.split(' ')[0])
		win_s = int(document.find_all('span', class_='win-lose')[0].text.split(' ')[0][:-1])
		lose_s = int(document.find_all('span', class_='win-lose')[0].text.split(' ')[1][:-4])
		winrate_s = int(document.find_all('span', class_='win-lose')[0].text.split(' ')[-1][:-1])
	else:
		rank_s = 'Unranked'
		lp_s = 0
		win_s = 0
		lose_s = 0
		winrate_s = 0

	# Fetch flex data 
	image_f = document.find_all('div', class_='medal')[1].findChild('img')['src']
	try:
		rank_f = document.find_all('div', class_='tier-rank')[1].text
	except IndexError:
		rank_f = 'Unranked'

	if rank_f != 'Unranked':
		lp_f = int(document.find_all('div', class_='tier-info')[-1].findChild('span').text.split(' ')[0])
		win_f= int(document.find_all('span', class_='win-lose')[-1].text.split(' ')[0][:-1])
		lose_f = int(document.find_all('span', class_='win-lose')[-1].text.split(' ')[1][:-4])
		winrate_f = int(document.find_all('span', class_='win-lose')[-1].text.split(' ')[-1][:-1])

	else:
		lp_f = 0
		win_f = 0
		lose_f = 0
		winrate_f = 0

	try:
		global_ranking = int(document.find('span', class_='ranking').string.replace(',',''))
		percent_better_players = float(document.find('div', class_='rank').findChild('a').text.split('(')[1].split('%')[0])

	except AttributeError:
		global_ranking = 0
		percent_better_players = 0
	
	champs_more_data = document2.find_all('tr')[1:]

	champs = []

	# Fetch champions data
	champs_data = document.find_all('div', class_='champion-box')
	for index,champ_data in enumerate(champs_data):
		name_champ = champ_data.find('div', class_='face').findChild('img')['alt']
		image_champ = str(champ_data.find('img')['src'])
		games = int(champ_data.find('div', class_='played').findChildren('div')[-1].text.split(' ')[0])
		winrate = int(champ_data.find('div', class_='played').findChildren('div')[-2].text.split(' ')[0][:-1])
		try:
			kda = float(champ_data.find('div', class_='kda').findChildren('div')[0].findChildren('div')[-1].text.split(':')[0])
		except ValueError:
			kda = 100
		kills = float(champ_data.find('div', class_='detail').text.split('/')[0])
		deaths = float(champ_data.find('div', class_='detail').text.split('/')[1])
		assists = float(champ_data.find('div', class_='detail').text.split('/')[2])

		cs = float(champ_data.find('div', class_='cs').text.split(' ')[1])
		csmin = float(champ_data.find('div', class_='cs').text.split('(')[-1].split(')')[0])

		cells = champs_more_data[index].find_all('td', class_='value')
		
		gold = int(cells[1].text.replace(',',''))
		max_kills = int(cells[3].text)
		max_deaths = int(cells[4].text)
		avg_damage_dealt = int(cells[5].text.replace(',',''))
		avg_damage_taken = int(cells[6].text.replace(',',''))

		
		double_kills = get_multiple_kills(cells, 2)
		triple_kills = get_multiple_kills(cells, 3)
		quadra_kills = get_multiple_kills(cells, 4)
		penta_kills = get_multiple_kills(cells, 5)

		champs.append(buildChamp(name=name_champ, image=image_champ, games=games, winrate=winrate,
		kda=kda, kills=kills, deaths=deaths, assists=assists, cs=cs, csmin=csmin, gold=gold,
		max_kills=max_kills, max_deaths=max_deaths, avg_damage_dealt=avg_damage_dealt, avg_damage_taken=avg_damage_taken,
		double_kills=double_kills, triple_kills=triple_kills, quadra_kills=quadra_kills, penta_kills=penta_kills))

	masteries=loadmastery(ok_server, player, headers) 

	data=(buildPlayer(#name=name, 
	alias=alias, image=image, level=level, rank_n=global_ranking, rank_p=percent_better_players,
	rank_s=rank_s, image_s=image_s, lp_s=lp_s, win_s=win_s, lose_s=lose_s, winrate_s=winrate_s,
	rank_f=rank_f, image_f=image_f, lp_f=lp_f, win_f=win_f, lose_f=lose_f, winrate_f=winrate_f, champs=champs, masteries=masteries))

	return data