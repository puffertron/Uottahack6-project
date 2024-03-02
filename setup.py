# setup called at start of main to set up players and audio clips
from state import State
from player import Player
import pygame as pg
import config

def setup():
    print("setup players")
    State.player0 = Player()
    State.player1 = Player()
    State.players = [State.player0,State.player1]


    # Add sounds to players
    State.player0.player_note = [pg.mixer.Sound(config.ATTACK_SOUND_FILE)]
    State.player1.player_note = [pg.mixer.Sound(config.ATTACK_SOUND_FILE)]
    State.player0.player_chord = pg.mixer.Sound(config.P0CHORD_FILE)
    State.player1.player_chord = pg.mixer.Sound(config.P1CHORD_FILE)
    State.player0.miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)
    State.player1.miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)
    State.player0.dodge_sound = pg.mixer.Sound(config.DODGE_SOUND_FILE)
    State.player1.dodge_sound = pg.mixer.Sound(config.DODGE_SOUND_FILE)
    State.player0.hit_sound = pg.mixer.Sound(config.HIT_SOUND_FILE)
    State.player1.hit_sound = pg.mixer.Sound(config.HIT_SOUND_FILE)
    State.player0.parry_sound = pg.mixer.Sound(config.PARRY_SOUND_FILE)
    State.player1.parry_sound = pg.mixer.Sound(config.PARRY_SOUND_FILE)
    State.player0.fumble_sound = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)
    State.player1.fumble_sound = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)
