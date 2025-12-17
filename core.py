import random

# the Character class, has the ability to attack other instances of the same class
# name 		- string representing characters name
# base_hp 	- maximum hp character can have, can be any integer value
# hp 		- current health of character, can be any integer value
# dmg 		- damage output of character, can be any integer value
# crit 		- chance of critical damage specified as an int ranging from 0 to 100, critical damage is always twice the normal damage
class Character:
	def __init__(self, character):
		self.set(character)

	def set(self, character):
		self.__name = character['name']
		self.__base_hp = character['base_hp']
		self.__hp = character['hp']
		self.__dmg = character['dmg']
		self.__crit = character['crit']

	def get(self):
		return {
			'name': self.__name, 
			'base_hp': self.__base_hp,
			'hp': self.__hp,
			'dmg': self.__dmg,
			'crit': self.__crit,
			}

	def info(self):
		return f"{self.__name} hp:({self.__hp}/{self.__base_hp}) dmg:[{self.__dmg}] crit_chance:|{self.__crit}%|"
	def is_dead(self):
		if self.__hp <= 0: return True
		return False

	def get_hurt(self, dmg):
		self.__hp = self.__hp-dmg
		if self.__hp < 0: self.__hp = 0

	def attack(self, target):
		if random.randint(1, 100) <= self.__crit:
			string = f"{self.name()} hits {target.name()} dealing [{self.__dmg*2}] critical damage!"
			target.get_hurt(self.__dmg*2)
			return string
		string = f"{self.name()} hits {target.name()} dealing [{self.__dmg}] damage!"
		target.get_hurt(self.__dmg)
		return string

	def name(self):
		return f"{self.__name} ({self.__hp}/{self.__base_hp})"

	def reset(self):
		self.__hp = self.__base_hp

# a simple class for loggin the game process
class SimpleLogger:
    def __init__(self):
        self.__log = ''
    def reset(self):
        self.__log = ''
    def log(self, text):
        self.__log += text+'\n'
    def get(self):
        return self.__log[:-1]


class Game:
	def __init__(self):
		self.__alive = []
		self.__dead = []
		self.__turn = 0
		self.__done = False
		self.__logger = SimpleLogger()

	def reset_game(self):
		self.__alive.extend(self.__dead)
		self.__dead.clear()
		for i in self.__alive:
			i.reset()
		self.__turn = 0
		self.__done = False

	def get_state(self):
		state = {'turn': self.__turn, 'alive': [], 'dead': []}
		for i in self.__alive:
			state['alive'].append(i.get())
		for i in self.__dead:
			state['dead'].append(i.get())
		return state

	def set_state(self, state):
		self.__turn = state['turn']
		for i in state['alive']:
			self.__alive.append(Character(i))
		for i in state['dead']:
			self.__alive.append(Character(i))

	def turn(self):
		if len(self.__alive) <= 1:
			return ''
		self.__logger.reset()
		self.__turn += 1
		self.__logger.log(f' - TURN {self.__turn}')

		for character in self.__alive:
			if character.is_dead():
				self.__alive.remove(character)
				self.__dead.append(character)
		# attacking characters
		for character in self.__alive:
			if character.is_dead():
				self.__alive.remove(character)
				self.__dead.append(character)
				break
			target = self.__alive.copy()
			target.remove(character)
			if len(target) <= 0:
				continue
			self.__logger.log(character.attack(random.choice(target)))

			if character.is_dead():
				self.__alive.remove(character)
				self.__dead.append(character)

		if len(self.__alive) <= 1:
			self.__logger.log(f'{self.__alive[0].get()['name']} wins!')
			self.__done = True

		self.__logger.log('')
		return self.__logger.get()


	def add_character(self, character):
		self.__alive.append(Character(character))

	def clear_characters(self):
		self.__alive.clear()
		self.__dead.clear()

	def get_turn(self): 
		return self.__turn

	def info(self):
		self.__logger.reset()
		self.__logger.log(f'turn {self.__turn}')
		self.__logger.log(f' - ALIVE')
		for i in self.__alive:
			self.__logger.log(i.info())
		self.__logger.log(f' - DEAD')
		for i in self.__dead:
			self.__logger.log(i.info())
		self.__logger.log('')
		return self.__logger.get()

	def is_done(self):
		return self.__done







# game = Game()
# game.add_character({'name': 'Nester', 'base_hp': 20, 'hp': 20, 'dmg': 4,'crit': 30})
# game.add_character({'name': 'Gabriel', 'base_hp': 30, 'hp': 30, 'dmg': 2,'crit': 50})
# game.add_character({'name': 'Lampman', 'base_hp': 10, 'hp': 10, 'dmg': 7,'crit': 60})

# while True:
# 	while not game.is_done():
# 		print(game.turn())
# 		if game.get_turn() == 4:
# 			print(game.get_state())
# 			game.set_state(game.get_state())
# 	print(game.info())
# 	input('press any key to reset')
# 	game.reset_game()