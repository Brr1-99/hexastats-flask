League of Legends stats visualization tool backend. 

<h1 align="center">Hexastats</h1>

<div align="center">
  </span><img src="https://img.shields.io/badge/made%20with-python-blue" /><span> <img src="https://img.shields.io/badge/made%20with-flask-white" /><span> </span><img src="https://img.shields.io/badge/made%20with-beautifulsoup4-green" />
</div>

Flask app. Scrapes [op.gg](https://www.op.gg/) and [lol.estiah](https://lol.estiah.com/) with BS4 to fetch stats and data about League of Legends players and serves it as a JSON through a web API. 





<h2 align="center">More info</h2>

This is a backend made for our [Dawichi/hexastats](https://github.com/Dawichi/hexastats) frontend project, a React + D3.js website to visualize all this data.

🎉🎉🎉 Check it on [hexastats.vercel.app](https://hexastats.vercel.app)





<h2 align="center">API Documentation</h2>

#### GET: One player data 

````python
?players=<name>

# Example: ?players=Bruno
# returns JSON:
[
    {player.data}
]
````




#### GET: Multiple player data 

````python
# NOTE: trailing commas and spaces between names in GET param allowed
?players=<name1>,<name2>
?players=<name1>,<name2>,
?players=<name1>, <name2>

# Example: ?players=David ,Alex, Cristian,
# returns JSON: 
[
    {player1.data},
    {player2.data},
    {player3.data}
]
````




#### GET: Specific server

If you want to search for a player in a specific server (euw, kr, etc...) just add a `server=` param 

````python
?players=<name1>&server=euw
?players=<name1>,<name2>,&server=euw

# Example: ?players=David ,Alex, Cristian,&server=euw
# returns JSON: 
[
    {player1.data},
    {player2.data},
    {player3.data}
]
````



![showcase](./showcase.png)





