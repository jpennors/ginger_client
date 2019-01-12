import configparser
import requests


class GingerClient():
	"""docstring for GingerClient"""
	def __init__(self):
		config = configparser.ConfigParser()
		config.read("config/env.ini")
		self.key = config['GINGER KEY']['APP_GINGER_KEY']
		self.url = config['GINGER KEY']['APP_GINGER_URL']
		
	
   # Récupérer un utilisateur à partir d'un id de badge
   # (si la clé l'autorise).
   
   # @param string $badge Identifiant de badge
   # @return object Utilisateur
   
	def getInfoByBadge(self, badge):

		return self.apiCall("badge/" + badge);


	def apiCall(self, path):

		uri = self.url + path
		key = self.key

		response = requests.get(uri + "?key=" + key)

		if response.status_code == 200:
			print(response.json())
			return response.json()
	