# setup called at start of main to set up players and audio clips
from state import State
from player import Player

def setup():
    print("setup players")
    State.player0 = Player()
    State.player1 = Player()
    State.players = [State.player0,State.player1]


    #TODO - add whatever actual setup stuff needs to be done for each player like sounds