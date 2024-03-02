# Holds state of game. Is imported by most other files, does not import other
from player import Player


class State:
    """State holds the changing state of the game, it is set up in setup then used and changed by other files"""
    
    player1:Player = None
    player2:Player = None