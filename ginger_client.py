import configparser
import requests



class GingerClient():
	"""Ensemble de fonctions pour interagir avce l'API Ginger, outil de gestion des cotisants"""



	def __init__(self):
		config = configparser.ConfigParser()
		config.read("config/env.ini")
		self.key = config['GINGER KEY']['APP_GINGER_KEY']
		self.url = config['GINGER KEY']['APP_GINGER_URL']


   
	def getInfoByBadge(self, badge):
		"""Fonction pour récupérer les informations d'un cotisant à partir de son numéro de badge"""

		return self._apiCall("badge/" + badge);




	def getInfoByLogin(self, login):
		"""Fonction pour récupérer les informations d'un cotisant à partir de son login"""

		return self._apiCall(login)



	def findUsers(self, characters):
		"""Fonction pour récupérer noms/prénoms/login/mail de tous les utilisateurs correpondants aux caractères entrés"""

		return self._apiCall("find/" + characters)



	def _apiCall(self, path, parameters = None):
		"""Fonction effecutant les appels API sur Ginger/v1"""

		uri = self.url + path
		key = self.key

		response = requests.get(uri + "?key=" + key, params = parameters)

		return self._buildResponse(response)

	

	def _buildResponse(self, api_response):
		"""Fonction pour construire une r^éponse à une requête API"""

		response = {
			'data' : api_response.json(),
			'status' : api_response.status_code
		}

		return response



	def setNewGingerKey(self, key):
		"""Fonction pour changer la API_GINGER_KEY dans les variables d'environnements"""

		newConfig = configparser.ConfigParser()
		newConfig['GINGER KEY'] = {
			'APP_GINGER_KEY' : key,
			'APP_GINGER_URL' : self.url
		}

		with open('config/env.ini', 'w') as configfile:
			newConfig.write(configfile)