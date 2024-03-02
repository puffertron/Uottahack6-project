from linked_list import LinkedList
import pygame as pg

class Player():
    """Holds information unique t o each player; in particular, e.g., stance history, audio clips"""
    def __init__(self):
        self.history = LinkedList()


        # Sounds specific to player
        self.player_note:list[pg.mixer.Sound] = []
        self.player_chord:pg.mixer.Sound = None
        self.miss_sound:pg.mixer.Sound = None
        self.dodge_sound:pg.mixer.Sound = None
        self.hit_sound:pg.mixer.Sound = None
        self.parry_sound:pg.mixer.Sound = None
        self.fumble_sound:pg.mixer.Sound = None