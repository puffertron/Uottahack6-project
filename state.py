# Holds state of game. Is imported by most other files, does not import other
from player import Player


class State:
    """State holds the changing state of the game, it is set up in setup then used and changed by other files"""
    player0: Player = None
    player1: Player = None
    players: list[Player] = []
    winner = 2

    # Pause is used when hit or fumble happens and attacker is swapped
    pause_for_beats = 0 # If this is non-zero, counts down by one every beat, for whole beat ignores input and stops metronome (onBeat())

    #TODO - add combo things

