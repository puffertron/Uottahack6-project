# setup called at start of main to set up players and audio clips
from state import State
from player import Player

def setup():
    State.player1 = Player()
    State.player2 = Player()

    #TODO - add whatever actual setup stuff needs to be done for each player like sounds