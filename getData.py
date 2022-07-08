import requests
import json
from bs4 import BeautifulSoup
from requests.models import LocationParseError
from interfaces import buildPlayer
from whitelist import realName, validate_server
from loadDatas import loadData

	

# Headers to avoid bot protection
headers = requests.utils.default_headers()
headers.update({
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
})

# Function to extract the data from the pages to the dictionary
def getData(players_get: list[str], server: str, singleMode: bool) -> json:
	# Data returned
	data = []
	ok_server = validate_server(server)
	# Players
	for player in players_get:

		data.append(loadData(ok_server,headers, player))

	if singleMode:
		return json.dumps(data[0])
	else:
		return json.dumps(data)
