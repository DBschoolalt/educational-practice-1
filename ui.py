import core
import data

game = core.Game()

# default characters
game.add_character({'name': 'Nester', 'base_hp': 20, 'hp': 20, 'dmg': 4,'crit': 30})
game.add_character({'name': 'Gabriel', 'base_hp': 30, 'hp': 30, 'dmg': 2,'crit': 50})
game.add_character({'name': 'Lampman', 'base_hp': 10, 'hp': 10, 'dmg': 7,'crit': 60})

def index_exists(list, index):
	return index in range(len(list))

class Parser:
	@staticmethod
	def parse(commandline):
		command = commandline[0]
		commandline.pop(0)
		args = []
		for i in commandline:
			args.append(i)
		return command, args

class Executer:
	@staticmethod
	def execute(c, a):
		match c:
			case 'help':
				return ''\
				'"turn"  -  proceed to next turn in the game (you can also just press enter)\n'\
				'"info"  -  show current status of the game\n'\
				'"reset"  -  restart the game\n'\
				'\n'\
				'"savegame"  -  save current game turn\n'\
				'"loadgame"  -  load last saved game turn\n'\
				'\n'\
				'"addchr [name] [health] [damage] [critical chance]"  -  add a character to the game\n'\
				'"savechr"  -  save all current game characters\n'\
				'"loadchr"  -  load last saved characters (resets the game)\n'\
				'"clearchr"  -  remove all characters from the game\n'\
				'\n'\
				'"help"  -  to show this message\n'\

			case 'turn':
				return game.turn()

			case 'info':
				return game.info()

			case 'reset':
				game.reset_game()
				return 'game reset'

			case 'savegame':
				data.GameData.set(game.get_state())
				return 'game saved'

			case 'loadgame':
				game.set_state(data.GameData.get())
				return 'game loaded'

			case 'savechr':
				data.CharacterData.set(game.get_characters())
				return 'characters saved'

			case 'loadchr':
				game.reset_game()
				game.set_characters(data.CharacterData.get())
				return 'characters loaded'

			case 'clearchr':
				game.clear_characters()
				return 'all characters removed'

			case 'addchr':
				if not index_exists(a, 3):
					return 'invalid arguments'
				try:
					int(a[1])
					int(a[2])
					int(a[3])
				except ValueError:
					return 'hp, dmg and crit arguments must be a number'

				character = {
					'name': a[0], 
					'base_hp': int(a[1]),
					'hp': int(a[1]),
					'dmg': int(a[2]),
					'crit': int(a[3]),
					}
				game.add_character(character)
				return f'{a[0]} added to characters'

			case _:
				return 'invalid command, type "help" for list of commands'

class Presenter:
	@staticmethod
	def present(text):
		print(text)

Presenter.present(Executer.execute('help', []))
while True:
	a = input('> ')
	if len(a) <= 0: a='turn'
	command, args = Parser.parse(a.split())
	Presenter.present(Executer.execute(command, args))