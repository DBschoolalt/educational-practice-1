import json
class CharacterData:
	__data_location = 'characters.json'
	@staticmethod
	def get():
		try:
			with open(CharacterData.__data_location, 'r') as file:
				return json.load(file)
		except FileNotFoundError:
			return []
	def set(data):
		with open(CharacterData.__data_location, 'w') as file:
			json.dump(data, file)

class GameData:
	__data_location = 'gamestate.json'
	@staticmethod
	def get():
		try:
			with open(GameData.__data_location, 'r') as file:
				return json.load(file)
		except FileNotFoundError:
			return {'turn': 0, 'alive':[], 'dead':[]}
	def set(data):
		with open(GameData.__data_location, 'w') as file:
			json.dump(data, file)