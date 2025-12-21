from core import *

def test_character_get():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	assert c.get() == {"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30}

def test_character_info():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	assert c.info() == "Nester hp:(9/20) dmg:[4] crit_chance:|30%|"

def test_character_is_dead():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 0, "dmg": 4, "crit": 30})
	assert c.is_dead() == True
	c = Character({"name": "Nester", "base_hp": 20, "hp": 3153, "dmg": 4, "crit": 30})
	assert c.is_dead() == False

def test_character_attack():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 5, "dmg": 4, "crit": 0})
	b = Character({"name": "Jester", "base_hp": 20, "hp": 5, "dmg": 4, "crit": 0})
	assert c.attack(b) == "Nester (5/20) hits Jester (5/20) dealing [4] damage!"
	c = Character({"name": "Nester", "base_hp": 20, "hp": 5, "dmg": 4, "crit": 100})
	b = Character({"name": "Jester", "base_hp": 20, "hp": 5, "dmg": 4, "crit": 100})
	assert c.attack(b) == "Nester (5/20) hits Jester (5/20) dealing [8] critical damage!"

def test_character_get_name():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	assert c.name() == "Nester (9/20)"

def test_character_reset():
	c = Character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	c.reset()
	assert c.name() == "Nester (20/20)"

def test_simplelogger_get():
	a = SimpleLogger()
	a.log('a')
	a.log('b')
	a.log('c')
	assert a.get() == "a\nb\nc"

def test_simplelogger_reset():
	a = SimpleLogger()
	a.log('a')
	a.log('b')
	a.log('c')
	a.reset()
	assert a.get() == ""

def test_game_reset():
	a = Game()
	a.add_character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.add_character({"name": "Jester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	for _ in range(50):
		a.turn()

	a.reset_game()
	assert a.get_turn() == 0
	assert a.get_state()['dead'] == []

def test_game_clear_characters():
	a = Game()
	a.add_character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.add_character({"name": "Jester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	for _ in range(50):
		a.turn()
	a.clear_characters()
	assert a.get_characters() == []

def test_game_get_turn():
	a = Game()
	a.add_character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.add_character({"name": "Jester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.turn()
	a.turn()
	assert a.get_turn() == 2

def test_game_is_done():
	a = Game()
	a.add_character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.add_character({"name": "Jester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	for _ in range(50):
		a.turn()
	assert a.is_done() == True

def test_game_info():
	a = Game()
	a.add_character({"name": "Nester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	a.add_character({"name": "Jester", "base_hp": 20, "hp": 9, "dmg": 4, "crit": 30})
	assert a.info() == 'turn 0\n - ALIVE\nNester hp:(9/20) dmg:[4] crit_chance:|30%|\nJester hp:(9/20) dmg:[4] crit_chance:|30%|\n - DEAD\n'