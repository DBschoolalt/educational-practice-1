# Usage

`turn` - proceed to next turn in the game (you can also just press enter)

`info` - show current status of the game

`reset` - restart the game

`savegame` - save current game turn

`loadgame` - load last saved game turn

`addchr [name] [health] [damage] [critical chance]` - add a character to the game, `critical chance` attribute goes from 0 to 100

`savechr` - save all current game characters

`loadchr`  -  load last saved characters (resets the game)

`clearchr`  -  remove all characters from the game

`help` - list all available commands

# Using the unit-tests

Install `pytest`

```
pip install pytest
```

Open terminal in project folder and run `test_core.py` with pytest

```
pytest test_core.py
```

# Build instructions

Install `pyinstaller`

```
pip install pyinstaller
```

Open terminal in project folder and build the app

```
pyinstaller ui.py --onefile
```

Your compiled app should be locked in `dist` folder of the project
