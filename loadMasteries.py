import requests
from bs4 import BeautifulSoup
from interfaces import buildmastery


def loadmastery(ok_server, player, headers):
	try:
		mastery = "https://lol.estiah.com/?region=" + (ok_server if ok_server!= 'www' else 'kr') + '&name=' + player
		result3= requests.get(mastery, headers=headers).text
		document3 = BeautifulSoup(result3,'html.parser')

		firstchamp = document3.find('div', class_='row dataview-content').findChild('div')

		champs_m =  firstchamp.find_next_siblings('div',limit=6)
		
		name_m = firstchamp.find('div', class_='name').text.split('\n')[1].replace('  ', '')
		image_m = firstchamp.find('img', class_='champion')['src']
		nivel = int(firstchamp['class'][2].split('-')[-1])
		puntos = int(firstchamp.findChild('div',class_='avatar')['title'].split(' ')[1])

		masteries = []

		masteries.append(buildmastery(name=name_m, image='https:'+ image_m, level=nivel, points=puntos))

		for champ_m in champs_m:
			name_m = champ_m.find('div', class_='name').text.split('\n')[1].replace('  ', '')
			image_m = champ_m.find('img', class_='champion')['src']
			nivel = int(champ_m['class'][2].split('-')[-1])
			puntos = int(champ_m.findChild('div',class_='avatar')['title'].split(' ')[1])

			masteries.append(buildmastery(name=name_m, image='https:'+ image_m, level=nivel, points=puntos))
	except:
		masteries = []
	return masteries
