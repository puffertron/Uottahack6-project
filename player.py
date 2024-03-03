from linked_list import LinkedList
import pygame as pg

class Player():
    """Holds information unique t o each player; in particular, e.g., stance history, audio clips"""
    def __init__(self):
        self.history = LinkedList()


        # Sounds specific to player, updated in 'setup.py'
        self.player_note:list[pg.mixer.Sound] = [] #NOTE - currently only use first index of these lists of sounds, can add later ability to randomly choose one
        self.player_chord:list[pg.mixer.Sound] = []
        self.dodge_sound:pg.mixer.Sound = None # Played when successful dodge as defender
        self.hit_sound:pg.mixer.Sound = None # Played when hit by attacker
        self.parry_sound:pg.mixer.Sound = None # Played when do successful parry against attacker
        self.fumble_sound:pg.mixer.Sound = None # Played when failed to attack
