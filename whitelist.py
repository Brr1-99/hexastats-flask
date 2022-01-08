# whitelist

def realName(alias) :
	players = {
		'alexwwe': 'Alex',
		'Brr1': 'Bruno',
		'BloddSword': 'Cristian',
		'Dawichii': 'Dawid',
		'Agazhord': 'Marcos',
		'Traketero': 'Rodri',
		'DryadZero': 'Samu',
		'Rhaast West': 'Diego',
		'DelemKi 26': 'Abel',
		'DAYTRESGP': 'David',
		'Telejenkem': 'Jose',
		'Ruzou': 'Ruben',
	}
	try:
		return players[alias]
	except KeyError:
		return alias

def validate_server(server):
	servers = ['euw', 'lan', 'las', 'na','eune', 'tr', 'oce', 'ru', 'jp', 'br']
	if server == 'kr':
		return 'www'
	elif server in servers:
		return server
	else:
		return servers[0]