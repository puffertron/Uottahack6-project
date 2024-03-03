# setup called at start of main to set up players and audio clips
from state import State
from player import Player
import pygame as pg
import config
import audio

def setup():
    print("setup players")
    State.player0 = Player()
    State.player1 = Player()
    State.players = [State.player0,State.player1]

    # Add sounds to players
    State.player0.player_note = [
        pg.mixer.Sound(config.P0NOTE_FILE0),
        pg.mixer.Sound(config.P0NOTE_FILE1),
        pg.mixer.Sound(config.P0NOTE_FILE2),
        pg.mixer.Sound(config.P0NOTE_FILE3)
        ]
    State.player1.player_note = [pg.mixer.Sound(config.P1NOTE_FILE)]
    State.player0.player_chord = [pg.mixer.Sound(config.P0CHORD_FILE)]
    State.player1.player_chord = [pg.mixer.Sound(config.P1CHORD_FILE)]
    State.player0.dodge_sound = pg.mixer.Sound(config.P0DODGE_SOUND_FILE)
    State.player1.dodge_sound = pg.mixer.Sound(config.P1DODGE_SOUND_FILE)
    State.player0.hit_sound = pg.mixer.Sound(config.P0HIT_SOUND_FILE)
    State.player1.hit_sound = pg.mixer.Sound(config.P1HIT_SOUND_FILE)
    State.player0.parry_sound = pg.mixer.Sound(config.P0PARRY_SOUND_FILE)
    State.player1.parry_sound = pg.mixer.Sound(config.P1PARRY_SOUND_FILE)
    State.player0.fumble_sound = pg.mixer.Sound(config.P0FUMBLE_SOUND_FILE)
    State.player1.fumble_sound = pg.mixer.Sound(config.P1FUMBLE_SOUND_FILE)
    State.player0.advantage_sound = pg.mixer.Sound(config.P0ADVANTAGE_SOUND_FILE)
    State.player1.advantage_sound = pg.mixer.Sound(config.P1ADVANTAGE_SOUND_FILE)
    State.player0.win_sound = pg.mixer.Sound(config.P0WIN_SOUND_FILE)
    State.player1.win_sound = pg.mixer.Sound(config.P1WIN_SOUND_FILE)


    # Set channel volumes
    audio.player0_voice.set_volume(0.4)
    audio.player1_voice.set_volume(0.4)
    audio.SFX.set_volume(1)
    audio.metronome.set_volume(0.2)
    audio.buzzer.set_volume(0.1)
    audio.background.set_volume(0.3)
