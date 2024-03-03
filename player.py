from linked_list import LinkedList
import pygame as pg

class Player():
    """Holds information unique t o each player; in particular, e.g., stance history, audio clips"""
    def __init__(self):
        self.history = LinkedList()

        self.note_ind = 0 # Which note was just played, cycles through notes


        # Sounds specific to player, updated in 'setup.py'
        self.player_note:list[pg.mixer.Sound] = [] # Has ability to cycle through notes
        self.player_chord:list[pg.mixer.Sound] = [] # NOTE: Currently only use first index
        self.dodge_sound:pg.mixer.Sound = None # Played when successful dodge as defender
        self.hit_sound:pg.mixer.Sound = None # Played when hit by attacker
        self.parry_sound:pg.mixer.Sound = None # Played when do successful parry against attacker
        self.fumble_sound:pg.mixer.Sound = None # Played when failed to attack
        self.advantage_sound = None
        self.win_sound = None

    def getNote(self):
        if self.note_ind == len(self.player_note)-1: #Cycle through notes
            self.note_ind = 0
        else:
            self.note_ind += 1
        return self.player_note[self.note_ind]